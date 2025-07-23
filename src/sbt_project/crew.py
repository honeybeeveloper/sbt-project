import datetime

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.knowledge.source.text_file_knowledge_source  import TextFileKnowledgeSource
from typing import List

from sbt_project import app_config, app_logger, sales_activity

now_str = datetime.datetime.now().strftime('%y%m%d_%H%M%S')

@CrewBase
class SbtProject():
    """SbtProject crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # knowledge
    agent_knowledge = TextFileKnowledgeSource(file_paths=["SBTGlobal_knowledge.txt"])

    app_logger.debug(f" target account : {sales_activity['account']}")
    target_account = sales_activity['account']

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'], # type: ignore[index]
            verbose=True,
            knowledge_sources=[self.agent_knowledge]
        )

    @agent
    def analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['analyst'], # type: ignore[index]
            verbose=True,
            knowledge_sources=[self.agent_knowledge]
        )

    @agent
    def consultant(self) -> Agent:
        return Agent(
            config=self.agents_config['consultant'],  # type: ignore[index]
            verbose=True,
            knowledge_sources=[self.agent_knowledge]
        )

    @agent
    def summarizer(self) -> Agent:
        return Agent(
            config=self.agents_config['summarizer'],  # type: ignore[index]
            verbose=True,
            knowledge_sources=[self.agent_knowledge]
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
            output_file=f"{self.target_account}_analyze_task_{now_str}.json",
        )

    @task
    def consulting_task(self) -> Task:
        return Task(
            config=self.tasks_config['consulting_task'],  # type: ignore[index]
            context=[self.research_task(), self.analyze_task()],
            output_file=f"{self.target_account}_consulting_task_{now_str}.json",
        )

    @task
    def summarize_task(self) -> Task:
        return Task(
            config=self.tasks_config['summarize_task'],  # type: ignore[index]
            context=[self.research_task(), self.analyze_task()],
            output_file=f"{self.target_account}_summarize_task_{now_str}.json",
        )

    @crew
    def crew(self) -> Crew:
        """Creates the SbtProject crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )

