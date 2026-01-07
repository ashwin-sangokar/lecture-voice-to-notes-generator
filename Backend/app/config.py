import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")

ALLOWED_AUDIO_TYPES = ["audio/mpeg", "audio/wav", "audio/mp3", "audio/x-wav"]
MAX_FILE_SIZE_MB = 50
