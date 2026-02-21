# Jarvis AI -Virtual Assistant

Jarvis AI is a Python-based voice assistant that performs automation tasks, fetches real-time news, and generates AI responses using external APIs.

## Features

- Voice command recognition
- Text-to-speech output
- Task automation via speech input
- Website launching
- Music playback
- Fetches real-time news using NewsAPI and delivers it via voice output
- AI-generated responses (Google GenAI)

## Tech Stack

- Python
- SpeechRecognition
- PyAudio
- pyttsx3
- Requests
- Google GenAI
- python-dotenv

## Installation

1. Clone the repository:

   git clone https://github.com/Piyush3462/Jarvis-AI-.git  
   cd Jarvis-AI-

2. Create and activate virtual environment:

   python -m venv .venv  
   source .venv/bin/activate  (Mac/Linux)

3. Install dependencies:

   pip install -r requirements.txt

## Environment Setup

Create a `.env` file in the project root and add:

   GOOGLE_API_KEY=your_api_key_here <br>
   NEWS_API_KEY=your_newsapi_key
## Run

   python Main.py
