from pathlib import Path
from html.parser import HTMLParser

ROOT = Path(__file__).resolve().parents[1]
class Forms(HTMLParser):
    def __init__(self):
        super().__init__()
        self.forms = []
    def handle_starttag(self, tag, attrs):
        if tag == "form":
            a = dict(attrs)
            assert not a.get("action", "").lower().startswith("mailto:"), "form mailto"
            if "data-interconnection-form" in a or "data-support-form" in a:
                assert a.get("action") == "/contact.php" and a.get("method") == "post", a
                self.forms.append(a)
expected = {"index.html", "en.html", "interconnessione-macchine-industria-4-0.html",
            "en-machine-interconnection.html", "assistenza.html", "en-support.html"}
found = set()
for page in ROOT.glob("*.html"):
    parser = Forms()
    parser.feed(page.read_text(encoding="utf-8"))
    if parser.forms:
        found.add(page.name)
assert expected <= found, expected - found
print("HTTPS forms OK:", sorted(found))
