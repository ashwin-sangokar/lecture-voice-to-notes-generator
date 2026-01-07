from transformers import pipeline

# Load model ONCE
summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

def summarize_text(text: str) -> str:
    """
    Takes raw transcript text
    Returns summarized text
    """
    if not text or len(text.strip()) < 50:
        return "Audio content too short to summarize."

    summary = summarizer(
        text[:3000],  # hard safety cap
        max_length=150,
        min_length=60,
        do_sample=False
    )

    return summary[0]["summary_text"]
