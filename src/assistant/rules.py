offices = {
    "training office": {"name": "Training Office", "room": "I.101", "hours": "8am-5pm"},
    "finance office": {"name": "Finance Office", "phone": "0808080808"},
    "health centre": {"name": "Health Centre", "room": "I.3"}
}

def reply(text: str) -> str:
    text = text.strip()
    if not text:
        return "Please type a question."

    clean_text = text.lower()

    if clean_text == "help":
        return "Available commands: where is <office>, help."

    if "hi" in clean_text or "hello" in clean_text:
        return "Hello! How can I help you today?"

    if "finance office" in clean_text and "phone" in clean_text:
        return "Finance Office phone number is 0808080808."

    if "training office" in clean_text:
        return "Training Office: room I.101, open 8am-5pm."

    if "health centre" in clean_text:
        return "Health Centre: room I.3."

    for name, row in offices.items():
        if name in clean_text:
            room = row.get("room", "")
            return f"{row['name']}: room {room}."

    return "I do not understand the question."
