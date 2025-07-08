#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from sbt_project import app_config
from sbt_project.crew import SbtProject

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """
    inputs = {
        'input_test': input_test,
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
        "input_test": input_test,
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
        "input_test": input_test,
    }
    
    try:
        SbtProject().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")


input_test = [
        {
            "Account.Name": "쏘카",
            "Subject": "현업 미팅 (w. 변재춘 부장)",
            "Description": ''
        },
        {
            "Account.Name": "쏘카",
            "Subject": "개발장비 구축, 환경 셋팅 중",
            "Description": ''
        },
        {
            "Account.Name": "쏘카",
            "Subject": "서버(인프라) 구성 협의 (w. 변재춘)",
            "Description": "암호화 서버 (A/I), DB: My-sql요청 --> 사용 불가 - Maria DB 제안"
        },
        {
            "Account.Name": "쏘카",
            "Subject": "수주: 펜타시큐리티  (My-sql 지원)",
            "Description": ''
        },
        {
            "Account.Name": "SK 네트웍스",
            "Subject": "FI, BC 컨설턴트 / ABAP 개발자 추가 견적 (8월 1일 투입)",
            "Description": "기간: 22.08.01 ~ 23.1.15_x000D_\nFI 김민아 5.5_x000D_\nBC 신평식 2.5_x000D_\nABAP 주태영 3"
        },
        {
            "Account.Name": "㈜대현환경",
            "Subject": "실험성적서 개발(PC용) 협의 -  라온아이티 이관, 구축",
            "Description": ''
        },
        {
            "Account.Name": "㈜대현환경",
            "Subject": "PC용 실험성적서 출력 프로그램 개발 (라온아이티) 완료보고",
            "Description": ''
        },
        {
            "Account.Name": "한전KDN㈜",
            "Subject": "한국전력공사 차세대 1차 사업",
            "Description": ''
        },
        {
            "Account.Name": "재영솔루텍㈜",
            "Subject": "내부승인완료(사장님)",
            "Description": "계약진행"
        },
        {
            "Account.Name": "중부발전",
            "Subject": "Weekly Report 10/10/23",
            "Description": "‘23~‘25년도 SAP License MA (2년)_x000D_\n10/10 14시 입찰 참가 신청_x000D_\n10/12 14시 입찰 (규격입찰서 제출 및 가격 투찰) _x000D_\n최저가 입찰"
        },
        {
            "Account.Name": "중부발전",
            "Subject": "Weekly Report 10/23/23",
            "Description": "적격 통보 및 가격 투찰 _x000D_\n이번 주 결과 확인 예정"
        },
        {
            "Account.Name": "중부발전",
            "Subject": "Weekly Report 11/13/23",
            "Description": "SAP와 License MA 계약 협의 (계약 금액 및 대금지급 조건 등)"
        }
    ]


if __name__ == '__main__':
    # print(input_test)
    run()