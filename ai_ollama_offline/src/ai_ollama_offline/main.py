#!/usr/bin/env python
import sys, warnings
from datetime import datetime
from dotenv import load_dotenv

from crew import AiOllamaOffline

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")
load_dotenv()  

def run():
    inputs = {
        'topic': 'AI Agents',                 
        'current_year': str(datetime.now().year)
    }
    try:
        AiOllamaOffline().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

# (keep train/replay/test if you want; not required)
if __name__ == "__main__":
    run()
