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

    app_logger.debug(f" >>> target account : {sales_activity['account']}")
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
    def summarizer(self) -> Agent:
        return Agent(
            config=self.agents_config['summarizer'],  # type: ignore[index]
            verbose=True,
            knowledge_sources=[self.agent_knowledge]
        )

    @task
    def corporate_curation(self) -> Task:
        return Task(
            config=self.tasks_config['corporate_curation'], # type: ignore
            output_file=f"{self.target_account}_corporate_curation_{now_str}.md",
        )

    @task
    def corporate_profiling(self) -> Task:
        return Task(
            config=self.tasks_config['corporate_profiling'], # type: ignore[index]
            output_file=f"{self.target_account}_corporate_profiling_{now_str}.md",
        )

    @task
    def market_sizing(self) -> Task:
        return Task(
            config=self.tasks_config['market_sizing'],  # type: ignore[index]
            output_file=f"{self.target_account}_market_sizing_{now_str}.md",
        )

    @task
    def financials_normalization(self) -> Task:
        return Task(
            config=self.tasks_config['financials_normalization'],  # type: ignore[index]
            output_file=f"{self.target_account}_financials_normalization_{now_str}.md",
        )

    @task
    def risk_assessment(self) -> Task:
        return Task(
            config=self.tasks_config['risk_assessment'],  # type: ignore[index]
            output_file=f"{self.target_account}_risk_assessment_{now_str}.md",
        )

    @task
    def sales_data_cleansing(self) -> Task:
        return Task(
            config=self.tasks_config['sales_data_cleansing'],  # type: ignore[index]
            context=[self.corporate_curation(), self.corporate_profiling(), self.market_sizing(),
                     self.financials_normalization(), self.risk_assessment()],
            output_file=f"{self.target_account}_sales_data_cleansing_{now_str}.md",
        )

    @task
    def sales_effectiveness_review(self) -> Task:
        return Task(
            config=self.tasks_config['sales_effectiveness_review'],  # type: ignore[index]
            context=[self.corporate_curation(), self.corporate_profiling(), self.market_sizing(),
                     self.financials_normalization(), self.risk_assessment()],
            output_file=f"{self.target_account}_sales_effectiveness_review_{now_str}.md",
        )

    @task
    def pipeline_forecasting(self) -> Task:
        return Task(
            config=self.tasks_config['pipeline_forecasting'],  # type: ignore[index]
            context=[self.corporate_curation(), self.corporate_profiling(), self.market_sizing(),
                     self.financials_normalization(), self.risk_assessment()],
            output_file=f"{self.target_account}_pipeline_forecasting_{now_str}.md",
        )

    @task
    def sales_strategy_optimization(self) -> Task:
        return Task(
            config=self.tasks_config['sales_strategy_optimization'],  # type: ignore[index]
            context=[self.corporate_curation(), self.corporate_profiling(), self.market_sizing(),
                     self.financials_normalization(), self.risk_assessment()],
            output_file=f"{self.target_account}_sales_strategy_optimization_{now_str}.md",
        )

    @task
    def executive_sales_report(self) -> Task:
        return Task(
            config=self.tasks_config['executive_sales_report'],  # type: ignore[index]
            context=[self.corporate_curation(), self.corporate_profiling(), self.market_sizing(),
                     self.financials_normalization(), self.risk_assessment()],
            output_file=f"{self.target_account}_executive_sales_report_{now_str}.md",
        )

    @task
    def activity_log_normalization(self) -> Task:
        return Task(
            config=self.tasks_config['activity_log_normalization'],  # type: ignore[index]
            output_file=f"{self.target_account}_activity_log_normalization_{now_str}.md",
        )

    @task
    def engagement_summary(self) -> Task:
        return Task(
            config=self.tasks_config['engagement_summary'],  # type: ignore[index]
            output_file=f"{self.target_account}_engagement_summary_{now_str}.md",
        )

    @task
    def activity_anomaly_detection(self) -> Task:
        return Task(
            config=self.tasks_config['activity_anomaly_detection'],  # type: ignore[index]
            output_file=f"{self.target_account}_activity_anomaly_detection_{now_str}.md",
        )

    @task
    def one_page_sales_snapshot(self) -> Task:
        return Task(
            config=self.tasks_config['one_page_sales_snapshot'],  # type: ignore[index]
            output_file=f"{self.target_account}_one_page_sales_snapshot_{now_str}.md",
        )

    @crew
    def crew_2(self) -> Crew:
        """Creates the SbtProject crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )

