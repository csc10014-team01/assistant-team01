import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from assistant.rules import reply


def test_greeting():
    assert "Hello" in reply("hi")


def test_help():
    assert "Available commands" in reply("help")


def test_office_lookup():
    assert "I.101" in reply("Where is the Training Office?")


def test_phone():
    assert "0808080808" in reply("what is Finance Office phone number?")


def test_health_lookup():
    assert "I.3" in reply("Where is the Health Centre?")


def test_empty():
    assert reply("   ") == "Please type a question."