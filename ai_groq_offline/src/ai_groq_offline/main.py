# src/ai_groq_offline/main.py
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
# load .env from the project root
load_dotenv(dotenv_path=Path(__file__).resolve().parents[2] / ".env")

from crew import AiGroqOffline

def run():
    inputs = {"current_year": str(datetime.now().year)}
    AiGroqOffline().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()
