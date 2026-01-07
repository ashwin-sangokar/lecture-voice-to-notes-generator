# 🚀 Lecture Voice to Notes Generator

A full-stack web application that converts recorded lecture audio into structured study material. The system performs speech-to-text transcription, generates concise summaries, extracts key points, and creates quiz questions to help students revise efficiently.

This project focuses on **clean architecture, explainable NLP logic, and production-ready backend design**.

---

## 🎯 Problem Statement

Students often struggle to revise long lecture recordings efficiently.

**Manually** converting audio lectures into structured notes is time-consuming and error-prone.

This project automates that process while keeping outputs **readable, reliable, and fast**.

---

## 🧠 Solution Architecture

### Pipeline:
```mathematica
Audio File
 └─ Speech-to-Text (Whisper)
     └─ Text Summarization (BART)
         └─ Key Points Extraction (Rule-based)
             └─ Quiz Question Generation (Rule-based)
```

Each stage is modular and independently testable.

---

## ⚡ Tech Stack

### Frontend
- React (Vite)
- Tailwind CSS

### Backend
- FastAPI
- Python

### ML / NLP
- OpenAI Whisper (Speech-to-Text)
- HuggingFace Transformers (BART for summarization)

### Other
- REST APIs
- Modular service-based architecture
- Error handling & validation

---

## ⚙️ Key Features

- Audio upload with validation
- Automatic lecture transcription
- Concise summary generation
- Bullet-point key notes
- Auto-generated quiz questions
- Robust error handling for edge cases

---

## 📁 Folder Structure (Simplified)
```css
backend/
├─ app/
│  ├─ api/
│  ├─ services/
│  ├─ utils/
│  └─ main.py
frontend/
├─ components/
├─ services/
└─ App.jsx
```
---

## 🛡️ Error Handling & Edge Cases

- Invalid file formats rejected
- Large audio files blocked
- Silent / empty audio handled gracefully
- Short lectures flagged as insufficient for summarization

## Live Demo

Frontend:
https://lecture-voice-to-notes-generator.vercel.app

Backend:
Hosted on Hugging Face Spaces (FastAPI + Whisper + BART)

Note:
The first request may take longer due to model initialization on free-tier infrastructure.



