def generate_quiz_questions(key_points, max_questions: int = 5):
    """
    Generates quiz questions from key points
    Returns a list of questions
    """

    questions = []

    templates = [
        "What is meant by {}?",
        "Why is {} important?",
        "Explain the concept of {}.",
        "How does {} work?"
    ]

    for point in key_points:
        # Extract a simple subject phrase
        subject = point.rstrip(".")
        question = templates[len(questions) % len(templates)].format(subject)
        questions.append(question)

        if len(questions) >= max_questions:
            break

    return questions
