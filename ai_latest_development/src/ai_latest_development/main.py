from crew import AiLatestDevelopment
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

def run():
    inputs = {'topic': 'AI LLMs', 'current_year': str(datetime.now().year)}
    AiLatestDevelopment().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()
