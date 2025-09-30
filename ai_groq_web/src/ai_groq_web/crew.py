from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import TavilySearchTool, ScrapeWebsiteTool

from dotenv import load_dotenv
load_dotenv()


search = TavilySearchTool(max_results=3)
# Fewer results = less text to read/scrape = fewer input tokens pushed into the LLM.
scrape = ScrapeWebsiteTool()

@CrewBase
class AiGroqWeb:
    @agent
    def researcher(self):
        return Agent(config=self.agents_config['researcher'], verbose=True,
                     tools=[search, scrape])

    @agent
    def reporter(self):
        return Agent(config=self.agents_config['reporter'], verbose=True)

    @task
    def research(self):
        return Task(config=self.tasks_config['research'])

    @task
    def report(self):
        return Task(
            config=self.tasks_config['report'],
            output_file="report_web.md"  
        )


    @crew
    def crew(self):
        return Crew(agents=[self.researcher(), self.reporter()],
                    tasks=[self.research(), self.report()],
                    process=Process.sequential, verbose=True)
