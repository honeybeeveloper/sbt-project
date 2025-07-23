#!/usr/bin/env python
import os
import sys
import warnings

from sbt_project import app_config, ROOT_DIR, app_logger, sales_activity
from sbt_project.common import utils
from sbt_project.crew import SbtProject
from sbt_project.crew_2 import SbtProject

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run_2():
    """
    Run the crew.
    """
    app_logger.debug(f" >>> target account : {sales_activity['account']}")

    inputs = {
        'company': sales_activity['account'],
        'sales_activity': sales_activity['activity'],
    }

    try:
        SbtProject().crew_2().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def run():
    """
    Run the crew.
    """
    app_logger.debug(f" target account : {sales_activity['account']}")

    inputs = {
        'company' : sales_activity['account'],
        'sales_activity': sales_activity['activity'],
    }
    
    try:
        return SbtProject().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'company': sales_activity['account'],
        'sales_activity': sales_activity['activity'],
    }
    try:
        SbtProject().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        SbtProject().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'company' : sales_activity['account'],
        'sales_activity': sales_activity['activity'],
    }
    try:
        SbtProject().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == '__main__':
    run_2()