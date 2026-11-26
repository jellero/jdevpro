<?php
declare(strict_types=1);

// Public contact endpoint. Only a fixed, authenticated Aruba Business SMTP destination is allowed.
const SMTP_HOST = 'out.postassl.it';
const SMTP_PORT = 465;
const MAILBOX = 'info@jdevpro.it';

header('Cache-Control: no-store');
header('X-Content-Type-Options: nosniff');
header('Referrer-Policy: no-referrer');

$en = ($_POST['lang'] ?? '') === 'en';
$json = str_contains($_SERVER['HTTP_ACCEPT'] ?? '', 'application/json');
function respond(int $code, string $it, string $english): never {
    global $en, $json;
    http_response_code($code);
    $message = $en ? $english : $it;
    if ($json) {
        header('Content-Type: application/json; charset=UTF-8');
        echo json_encode(['ok' => $code === 200, 'message' => $message], JSON_UNESCAPED_UNICODE);
    } else {
        header('Content-Type: text/html; charset=UTF-8');
        $lang = $en ? 'en' : 'it';
        $home = $en ? '/en' : '/';
        $label = $en ? 'Back to website' : 'Torna al sito';
        echo '<!doctype html><html lang="' . $lang . '"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>JDEVPRO</title><main><h1>JDEVPRO</h1><p>' . htmlspecialchars($message, ENT_QUOTES, 'UTF-8') . '</p><a href="' . $home . '">' . $label . '</a></main></html>';
    }
    exit;
}
function invalid(): never {
    respond(422, 'Controlla i campi obbligatori e riprova.', 'Check the required fields and try again.');
}
function field(string $name, int $max, bool $required = false, int $min = 0): string {
    $value = $_POST[$name] ?? '';
    if (!is_string($value) || !preg_match('//u', $value) || str_contains($value, "\0")) invalid();
    $value = trim($value);
    $length = preg_match_all('/./us', $value);
    if ($length === false || $length > $max || ($required && $length === 0) || $length < $min) invalid();
    return $value;
}
// Store only hashed client identifiers and attempt times, not submitted content.
function rate_limit(): bool {
    $dir = sys_get_temp_dir() . '/jdevpro-contact-' . hash('sha256', __DIR__);
    if (!is_dir($dir) && !@mkdir($dir, 0700) && !is_dir($dir)) throw new RuntimeException('rate directory');
    if (is_link($dir)) throw new RuntimeException('rate directory');
    $fp = @fopen($dir . '/rate.json', 'c+');
    if (!$fp) throw new RuntimeException('rate file');
    try {
        if (!flock($fp, LOCK_EX)) throw new RuntimeException('rate lock');
        $raw = stream_get_contents($fp);
        $state = $raw === '' ? [] : json_decode($raw, true, 512, JSON_THROW_ON_ERROR);
        if (!is_array($state)) throw new RuntimeException('rate state');
        $now = time();
        foreach ($state as $k => $attempts) {
            $state[$k] = array_values(array_filter($attempts, fn($t) => is_int($t) && $t > $now - 600));
            if (!$state[$k]) unset($state[$k]);
        }
        $key = hash('sha256', ($_SERVER['REMOTE_ADDR'] ?? 'unknown') . __DIR__);
        $attempts = $state[$key] ?? [];
        if (count($attempts) >= 5 || count($state) >= 5000) return false;
        $state[$key][] = $now;
        $encoded = json_encode($state, JSON_THROW_ON_ERROR);
        rewind($fp);
        if (!ftruncate($fp, 0) || fwrite($fp, $encoded) !== strlen($encoded) || !fflush($fp)) throw new RuntimeException('rate write');
        return true;
    } finally {
        fclose($fp);
    }
}
function write_all($socket, string $data): void {
    while ($data !== '') {
        $n = @fwrite($socket, $data);
        if (!$n) throw new RuntimeException('SMTP write');
        $data = substr($data, $n);
    }
}
function smtp_send(string $user, string $password, string $reply, string $subject, string $body): void {
    $ctx = stream_context_create(['ssl' => ['verify_peer' => true, 'verify_peer_name' => true, 'SNI_enabled' => true, 'peer_name' => SMTP_HOST]]);
    $socket = @stream_socket_client('ssl://' . SMTP_HOST . ':' . SMTP_PORT, $errno, $errstr, 10, STREAM_CLIENT_CONNECT, $ctx);
    if (!$socket) throw new RuntimeException('SMTP connect');
    stream_set_timeout($socket, 10);
    $read = static function (array $expected) use ($socket): string {
        $text = '';
        for ($i = 0; $i < 100; $i++) {
            $line = @fgets($socket, 2048);
            if ($line === false || !preg_match('/^([0-9]{3})([ -])/', $line, $m)) throw new RuntimeException('SMTP read');
            $text .= $line;
            if ($m[2] === ' ') {
                if (!in_array((int)$m[1], $expected, true)) throw new RuntimeException('SMTP rejected: ' . $m[1]);
                return $text;
            }
        }
        throw new RuntimeException('SMTP response limit');
    };
    $send = static function (string $command, array $expected) use ($socket, $read): string {
        write_all($socket, $command . "\r\n");
        return $read($expected);
    };
    try {
        $read([220]);
        $capabilities = $send('EHLO www.jdevpro.it', [250]);
        if (preg_match('/^250[- ]AUTH[ =][^\r\n]*\bPLAIN\b/im', $capabilities)) {
            $send('AUTH PLAIN ' . base64_encode("\0" . $user . "\0" . $password), [235]);
        } elseif (preg_match('/^250[- ]AUTH[ =][^\r\n]*\bLOGIN\b/im', $capabilities)) {
            $send('AUTH LOGIN', [334]);
            $send(base64_encode($user), [334]);
            $send(base64_encode($password), [235]);
        } else {
            throw new RuntimeException('SMTP authentication unavailable');
        }
        $send('MAIL FROM:<' . $user . '>', [250]);
        $send('RCPT TO:<' . MAILBOX . '>', [250, 251]);
        $send('DATA', [354]);
        // User content is base64 encoded; only a validated address enters Reply-To.
        $headers = [
            'Date: ' . date(DATE_RFC2822),
            'From: JDEVPRO <' . $user . '>',
            'To: ' . MAILBOX,
            'Reply-To: ' . $reply,
            'Subject: =?UTF-8?B?' . base64_encode($subject) . '?=',
            'Message-ID: <' . bin2hex(random_bytes(16)) . '@jdevpro.it>',
            'MIME-Version: 1.0',
            'Content-Type: text/plain; charset=UTF-8',
            'Content-Transfer-Encoding: base64',
        ];
        $body = str_replace(["\r\n", "\r"], "\n", $body);
        $body = str_replace("\n", "\r\n", $body);
        write_all($socket, implode("\r\n", $headers) . "\r\n\r\n" . chunk_split(base64_encode($body), 76, "\r\n") . ".\r\n");
        $read([250]); // Success only after the SMTP server accepts DATA.
        @fwrite($socket, "QUIT\r\n");
    } finally {
        fclose($socket);
    }
}

if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
    header('Allow: POST');
    respond(405, 'Metodo non consentito.', 'Method not allowed.');
}
if ((int)($_SERVER['CONTENT_LENGTH'] ?? 0) > 24576) respond(413, 'Richiesta troppo grande.', 'Request too large.');
if (!in_array($_SERVER['HTTP_ORIGIN'] ?? '', ['', 'https://www.jdevpro.it', 'https://jdevpro.it'], true)
    || ($_SERVER['HTTP_SEC_FETCH_SITE'] ?? '') === 'cross-site') respond(403, 'Richiesta non consentita.', 'Request not allowed.');
if (field('website', 200) !== '') invalid();
$kind = field('kind', 20, true);
$company = field('company', 120, true);
$email = field('email', 160, true);
if (preg_match('/[\r\n]/', $email) || !filter_var($email, FILTER_VALIDATE_EMAIL)) invalid();
if ($kind === 'interconnection') {
    $machine = field('machine', 160, true);
    $machines = field('machines', 3, true);
    if (!preg_match('/^[1-9][0-9]{0,2}$/D', $machines)) invalid();
    $subject = 'JDEVPRO - Richiesta verifica interconnessione';
    $body = "Azienda: $company\nEmail: $email\nMacchina: $machine\nNumero macchine: $machines\nGestionale: " . field('erp', 160) . "\nLocalità: " . field('location', 100) . "\nNote:\n" . field('notes', 1200);
} elseif ($kind === 'support') {
    if (field('consent', 3) !== 'on') invalid();
    $impact = field('impact', 20, true);
    if (!in_array($impact, ['Normale','Ridotto','Blocco','Normal','Degraded','Stopped'], true)) invalid();
    $subject = 'JDEVPRO - Richiesta assistenza tecnica';
    $body = "Azienda: $company\nEmail: $email\nSistema: " . field('system', 180, true) . "\nImpatto: $impact\nProblema:\n" . field('description', 3000, true, 15);
} else {
    invalid();
}

try {
    if (!rate_limit()) {
        header('Retry-After: 600');
        respond(429, 'Troppe richieste. Riprova tra qualche minuto.', 'Too many requests. Please try again in a few minutes.');
    }
    // Optional private configuration in the subscription directory, outside httpdocs.
    $path = dirname(__DIR__) . '/jdevpro-smtp.php';
    $config = is_readable($path) ? require $path : [];
    if (!is_array($config)) throw new RuntimeException('SMTP configuration');
    $user = $config['username'] ?? (getenv('JDEVPRO_SMTP_USER') ?: MAILBOX);
    $password = $config['password'] ?? getenv('JDEVPRO_SMTP_PASSWORD');
    if (!is_string($user) || !filter_var($user, FILTER_VALIDATE_EMAIL) || preg_match('/[\r\n]/', $user)
        || !is_string($password) || $password === '') throw new RuntimeException('SMTP not configured');
    smtp_send($user, $password, $email, $subject, $body);
    respond(200, 'Richiesta inviata correttamente. Ti risponderemo via email.', 'Request sent successfully. We will reply by email.');
} catch (Throwable $e) {
    // Never log credentials or form content.
    error_log('JDEVPRO contact: delivery or configuration failure');
    respond(503, 'Invio non disponibile. Riprova più tardi o scrivi a info@jdevpro.it.', 'Sending is unavailable. Try again later or write to info@jdevpro.it.');
}
