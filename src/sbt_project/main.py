#!/usr/bin/env python
import os
import sys
import warnings

from sbt_project import app_config, sales_activity
from sbt_project.common import utils
from sbt_project.crew_2 import SbtProject
from sbt_project.common.exception import CustomException

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """

    print(f"{sales_activity['account']} / {sales_activity['activity']}")

    inputs = {
        'company' : sales_activity['account'],
        'sales_activity': sales_activity['activity'],
    }
    
    try:
        # SbtProject().crew().kickoff(inputs=inputs)
        crew_instance = SbtProject().crew_2()
        result = crew_instance.kickoff(inputs=inputs)  # 중요한 부분: 결과를 받아야 함
        return result
    except CustomException as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'company': sales_activity['account'],
        'input_test': sales_activity['activity'],
    }
    try:
        SbtProject().crew_2().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        SbtProject().crew_2().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'company' : sales_activity['account'],
        'input_test': sales_activity['activity'],
    }
    try:
        SbtProject().crew_2().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == '__main__':
    run()