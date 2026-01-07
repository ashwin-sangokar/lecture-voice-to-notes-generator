import os
from fastapi import UploadFile, HTTPException
from app.config import UPLOAD_DIR, ALLOWED_AUDIO_TYPES, MAX_FILE_SIZE_MB

def save_audio_file(file: UploadFile) -> str:
    if file.content_type not in ALLOWED_AUDIO_TYPES:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type. Upload WAV or MP3 audio."
        )

    # Read file to check size
    contents = file.file.read()
    size_mb = len(contents) / (1024 * 1024)

    if size_mb > MAX_FILE_SIZE_MB:
        raise HTTPException(
            status_code=413,
            detail=f"File too large. Max allowed size is {MAX_FILE_SIZE_MB} MB."
        )

    os.makedirs(UPLOAD_DIR, exist_ok=True)
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        buffer.write(contents)

    return file_path
