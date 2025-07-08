#!/usr/bin/env python
import os
import sys
import warnings

from sbt_project import app_config, ROOT_DIR
from sbt_project.common import utils
from sbt_project.crew import SbtProject

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

json_path = os.path.join(ROOT_DIR, 'converted_data.json')
input_test = utils.json_to_dict(json_path)

def run():
    """
    Run the crew.
    """

    print(f"{input_test['account']} / {input_test['activity']}")

    inputs = {
        'company' : input_test['account'],
        'input_test': input_test['activity'],
    }
    
    try:
        SbtProject().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'company': input_test['account'],
        'input_test': input_test['activity'],
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
        'company' : input_test['account'],
        'input_test': input_test['activity'],
    }
    try:
        SbtProject().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == '__main__':
    run()