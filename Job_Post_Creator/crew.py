from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from typing import List
from pydantic import BaseModel, Field


@CrewBase
class JobPostingCreator():

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def job_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['job_researcher'],  # type: ignore[index]
            verbose=True,
            llm=LLM(
                model="gemini/gemini-2.0-flash",  # Use Gemini model
                temperature=0.7),
            tools=[SerperDevTool(), ScrapeWebsiteTool()]
        )

    @agent
    def job_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['job_writer'],  # type: ignore[index]
            verbose=True
            llm=LLM(
                model="gemini/gemini-2.0-flash",  # Use Gemini model
                temperature=0.7
            )
        )

    @agent
    def Hr_reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config['Hr_reviewer'],  # type: ignore[index]
            verbose=True
            llm=LLM(
                model="gemini/gemini-2.0-flash",  # Use Gemini model
                temperature=0.7
            )
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'], # type: ignore[index]
        )

    @task
    def writing_task(self) -> Task:
        return Task(
            config=self.tasks_config['writing_task'], # type: ignore[index]
            )

    @task
    def reviewing_Task(self) -> Task:
        return Task(
            config=self.tasks_config['reviewing_Task'],  # type: ignore[index]
            output_file='output/job_posting.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the JobPostingCreator crew"""

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )

