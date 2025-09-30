from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import DirectoryReadTool

from dotenv import load_dotenv
load_dotenv()


local = DirectoryReadTool(directory="knowledge")  # reads all texty files

@CrewBase
class AiGroqOffline:
    @agent
    def reader(self):
        return Agent(config=self.agents_config['reader'], verbose=True, tools=[local])

    @agent
    def reporter(self):
        return Agent(config=self.agents_config['reporter'], verbose=True)

    @task
    def ingest(self):
        return Task(config=self.tasks_config['ingest'])

    @task
    def writeup(self):
        return Task(config=self.tasks_config['writeup'], output_file="report_offline.md")

    @crew
    def crew(self):
        return Crew(agents=[self.reader(), self.reporter()],
                    tasks=[self.ingest(), self.writeup()],
                    process=Process.sequential, verbose=True)
