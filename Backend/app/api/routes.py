from fastapi import APIRouter, UploadFile, File, HTTPException
from app.utils.file_handler import save_audio_file
from app.services.speech_to_text import transcribe_audio
from app.services.summarizer import summarize_text
from app.services.keypoints import extract_key_points
from app.services.quiz_generator import generate_quiz_questions

router = APIRouter()

@router.post("/process-lecture")
def process_lecture(file: UploadFile = File(...)):
    try:
        file_path = save_audio_file(file)
        transcript = transcribe_audio(file_path)
        summary = summarize_text(transcript)
        key_points = extract_key_points(summary)
        quiz = generate_quiz_questions(key_points)

        return {
            "filename": file.filename,
            "transcript": transcript,
            "summary": summary,
            "key_points": key_points,
            "quiz": quiz
        }

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Internal processing error. Please try another audio file."
        )
