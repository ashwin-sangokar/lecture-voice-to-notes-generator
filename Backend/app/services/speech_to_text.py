import whisper

# Load model ONCE (important)
model = whisper.load_model("small")

def transcribe_audio(file_path: str) -> str:
    """
    Takes path of audio file
    Returns transcribed text
    """
    result = model.transcribe(file_path)
    text = result.get("text", "").strip()

    if not text:
        raise ValueError("No speech detected in audio")

    return text
