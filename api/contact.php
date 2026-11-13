<?php
declare(strict_types=1);

// Deploy on a PHP-enabled host at https://www.jdevpro.it/api/contact.php.
// NEVER put SMTP credentials or the Turnstile secret in this public repository.
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception as MailException;

header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');

function reply(int $code, string $message, bool $ok = false): never {
    http_response_code($code);
    echo json_encode(['ok' => $ok, 'message' => $message], JSON_UNESCAPED_UNICODE);
    exit;
}

$origins = [
    'https://www.jdevpro.it',
    'https://jdevpro.it',
    'https://jellero.github.io',
];
$origin = (string) ($_SERVER['HTTP_ORIGIN'] ?? '');
if ($origin !== '' && !in_array($origin, $origins, true)) {
    reply(403, 'Origine non autorizzata.');
}
if ($origin !== '') {
    header('Access-Control-Allow-Origin: ' . $origin);
    header('Vary: Origin');
    header('Access-Control-Allow-Methods: POST, OPTIONS');
    header('Access-Control-Allow-Headers: Content-Type, Accept');
}
if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    if ($origin === '') reply(403, 'Origine richiesta.');
    http_response_code(204);
    exit;
}
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    header('Allow: POST, OPTIONS');
    reply(405, 'Metodo non supportato.');
}
if ((int) ($_SERVER['CONTENT_LENGTH'] ?? 0) > 16000) {
    reply(413, 'Richiesta troppo grande.');
}

function field(string $name, int $max, bool $required = false): string {
    $raw = $_POST[$name] ?? '';
    if (!is_string($raw)) reply(422, 'Campo non valido: ' . $name);
    $value = trim($raw);
    $value = preg_replace('/[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]/', '', $value) ?? '';
    $length = function_exists('mb_strlen') ? mb_strlen($value, 'UTF-8') : strlen($value);
    if ($length > $max || ($required && $value === '')) {
        reply(422, 'Controlla il campo: ' . $name);
    }
    return $value;
}

$company = preg_replace('/\s+/u', ' ', field('company', 120, true)) ?: '';
$email = field('email', 160, true);
$machine = preg_replace('/\s+/u', ' ', field('machine', 160, true)) ?: '';
$machinesText = field('machines', 4, true);
$machines = filter_var($machinesText, FILTER_VALIDATE_INT, [
    'options' => ['min_range' => 1, 'max_range' => 999],
]);
$erp = field('erp', 160);
$location = field('location', 100);
$notes = field('notes', 1200);
if ($machines === false || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
    reply(422, 'Controlla email e numero macchine.');
}

// Decoy field: bots that autofill hidden fields are silently discarded.
if (field('website', 500) !== '') {
    reply(200, 'Richiesta ricevuta.', true);
}

$smtpUser = getenv('JDEVPRO_SMTP_USER') ?: 'info@jdevpro.it';
$smtpPassword = getenv('JDEVPRO_SMTP_PASSWORD') ?: '';
$turnstileSecret = getenv('JDEVPRO_TURNSTILE_SECRET') ?: '';
if ($smtpPassword === '' || $turnstileSecret === '') {
    reply(503, 'Servizio temporaneamente non configurato.');
}

$token = field('cf-turnstile-response', 2048, true);
if (!extension_loaded('curl')) {
    reply(503, 'Verifica antispam non disponibile.');
}

$ip = (string) ($_SERVER['REMOTE_ADDR'] ?? '');
$ch = curl_init('https://challenges.cloudflare.com/turnstile/v0/siteverify');
if ($ch === false) reply(503, 'Verifica antispam non disponibile.');
curl_setopt_array($ch, [
    CURLOPT_POST => true,
    CURLOPT_POSTFIELDS => http_build_query([
        'secret' => $turnstileSecret,
        'response' => $token,
        'remoteip' => $ip,
    ], '', '&', PHP_QUERY_RFC3986),
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_CONNECTTIMEOUT => 5,
    CURLOPT_TIMEOUT => 12,
]);
$result = curl_exec($ch);
$verifyStatus = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);
if (!is_string($result) || $verifyStatus !== 200) {
    reply(503, 'Verifica antispam non disponibile.');
}
$verification = json_decode($result, true);
if (!is_array($verification) ||
    ($verification['success'] ?? false) !== true ||
    !in_array((string) ($verification['hostname'] ?? ''), ['www.jdevpro.it', 'jdevpro.it', 'jellero.github.io'], true) ||
    ($verification['action'] ?? '') !== 'contact') {
    reply(422, 'Verifica antispam non valida. Riprova.');
}

// Restrict to 5 accepted requests per IP in 15 minutes; store no raw IPs.
$directory = sys_get_temp_dir() . '/jdevpro-contact-limiter';
if (!is_dir($directory) && !@mkdir($directory, 0700, true) && !is_dir($directory)) {
    reply(503, 'Servizio temporaneamente non disponibile.');
}
$handle = @fopen($directory . '/' . hash('sha256', $ip) . '.json', 'c+');
if ($handle === false || !flock($handle, LOCK_EX)) {
    if ($handle !== false) fclose($handle);
    reply(503, 'Servizio temporaneamente non disponibile.');
}
$raw = stream_get_contents($handle);
$stored = json_decode(is_string($raw) ? $raw : '', true);
$now = time();
$times = array_values(array_filter(is_array($stored) ? $stored : [], static fn($t) => is_int($t) && $t > $now - 900));
if (count($times) >= 5) {
    flock($handle, LOCK_UN);
    fclose($handle);
    reply(429, 'Troppe richieste. Riprova tra qualche minuto.');
}
$times[] = $now;
rewind($handle);
ftruncate($handle, 0);
fwrite($handle, json_encode($times));
fflush($handle);
flock($handle, LOCK_UN);
fclose($handle);

$autoloader = dirname(__DIR__) . '/vendor/autoload.php';
if (!is_file($autoloader)) reply(503, 'Servizio email non disponibile.');
require_once $autoloader;

try {
    $mail = new PHPMailer(true);
    $mail->isSMTP();
    $mail->Host = 'out.postassl.it';
    $mail->Port = 465;
    $mail->SMTPSecure = PHPMailer::ENCRYPTION_SMTPS; // TLS implicito su 465 (Aruba Business).
    $mail->SMTPAuth = true;
    $mail->Username = $smtpUser;
    $mail->Password = $smtpPassword;
    $mail->Timeout = 15;
    $mail->CharSet = PHPMailer::CHARSET_UTF8;
    $mail->setFrom('info@jdevpro.it', 'JDEVPRO - sito web');
    $mail->addAddress('info@jdevpro.it', 'JDEVPRO');
    $mail->addReplyTo($email, $company);
    $mail->Subject = 'Richiesta interconnessione dal sito - ' . $company;
    $mail->isHTML(false);
    $mail->Body = implode("\n", [
        'Nuova richiesta dal sito JDEVPRO',
        '',
        'Azienda: ' . $company,
        'Email di contatto: ' . $email,
        'Macchina: ' . $machine,
        'Numero macchine: ' . (string) $machines,
        'Gestionale: ' . ($erp !== '' ? $erp : 'Non indicato'),
        'Località: ' . ($location !== '' ? $location : 'Non indicata'),
        '',
        'Dati da collegare / note:',
        $notes !== '' ? $notes : 'Nessuna nota',
    ]);
    $mail->send();
    reply(200, 'Richiesta inviata correttamente.', true);
} catch (MailException $e) {
    error_log('JDEVPRO contact SMTP failure: ' . get_class($e));
    reply(502, 'Invio non riuscito. Riprova o scrivi a info@jdevpro.it.');
}
