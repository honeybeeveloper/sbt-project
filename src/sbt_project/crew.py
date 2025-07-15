import datetime

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource
from crewai.knowledge.source.text_file_knowledge_source  import TextFileKnowledgeSource
from typing import List

from sbt_project import app_config, app_logger
from sbt_project.tools import TrendTool, VisualizationTool

now_str = datetime.datetime.now().strftime('%y%m%d_%H%M%S')

@CrewBase
class SbtProject():
    """SbtProject crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    company = app_config.company
    trand_tool = TrendTool()
    # visualization_tool = VisualizationTool()

    # knowledge
    # agent_knowledge = StringKnowledgeSource(
    #     content="SBT Global provide Salesforce implementation and consulting services. "
    #             "We specialize in custom development tailored to client needs, with strong expertise in consulting for Salesforce Sales Cloud, Service Cloud, and Partner Community."
    # )
    # web_source = CrewDoclingSource(file_paths="https://www.sbtglobal.com/kr/salesforce2")
    agent_knowledge = TextFileKnowledgeSource(file_paths=["SBT_knowledge.txt"])
    app_logger.debug(f'agent_knowledge : {agent_knowledge}')

    @agent
    def recommender(self) -> Agent:
        return Agent(
            config=self.agents_config['recommender'], # type: ignore[index]
            verbose=True,
            knowledge_sources=[self.agent_knowledge]
        )

    @agent
    def trend_investigator(self) -> Agent:
        return Agent(
            config=self.agents_config['trend_investigator'], # type: ignore[index]
            verbose=True
        )

    @agent
    def strategy_advisor(self) -> Agent:
        return Agent(
            config=self.agents_config['strategy_advisor'],  # type: ignore[index]
            verbose=True
        )

    # @agent
    # def translator(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config['translator'],  # type: ignore[index]
    #         verbose=True
    #     )

    @task
    def recommend_task(self) -> Task:
        return Task(
            config=self.tasks_config['recommend_task'], # type: ignore[index]
            output_file=f"{self.company}_keywords_{now_str}.md",
        )

    @task
    def investigate_task(self) -> Task:
        return Task(
            config=self.tasks_config['investigate_task'], # type: ignore[index]
            context=[self.recommend_task()],
            tools=[self.trand_tool],
        )

    @task
    def propose_strategy_task(self) -> Task:
        return Task(
            config=self.tasks_config['propose_strategy_task'],  # type: ignore[index]
            context=[self.recommend_task(), self.investigate_task()],
            output_file=f"{self.company}_propose_strategy_task_{now_str}.md",
        )

    # @task
    # def translate_task(self) -> Task:
    #     return Task(
    #         config=self.tasks_config['translate_task'],  # type: ignore[index]
    #         context=[self.investigate_task(), self.propose_strategy_task()],
    #         output_file=f"{self.company}_translate_task_{now_str}.md",
    #     )

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
            knowledge_sources=[self.agent_knowledge]
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
