import datetime

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

now_str = datetime.datetime.now().strftime('%y%m%d_%H%M%S')

@CrewBase
class SbtProject():
    """SbtProject crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'], # type: ignore[index]
            verbose=True
        )

    @agent
    def analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['analyst'], # type: ignore[index]
            verbose=True
        )

    @agent
    def consultant(self) -> Agent:
        return Agent(
            config=self.agents_config['consultant'],  # type: ignore[index]
            verbose=True
        )

    @agent
    def translator(self) -> Agent:
        return Agent(
            config=self.agents_config['translator'],  # type: ignore[index]
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'], # type: ignore[index]
        )

    @task
    def analyze_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_task'], # type: ignore[index]
            output_file=f"analyze_task_{now_str}.md",
        )

    @task
    def consulting_task(self) -> Task:
        return Task(
            config=self.tasks_config['consulting_task'],  # type: ignore[index]
            context=[self.research_task(), self.analyze_task()],
            output_file=f"consulting_task_{now_str}.md",
        )

    @task
    def translate_task(self) -> Task:
        return Task(
            config=self.tasks_config['translate_task'],  # type: ignore[index]
            context=[self.consulting_task()],
            output_file=f"translate_task_{now_str}.md",
        )

    @crew
    def crew(self) -> Crew:
        """Creates the SbtProject crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
