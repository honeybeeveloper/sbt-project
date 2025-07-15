from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

import time
import pandas as pd
from pytrends.request import TrendReq

from sbt_project import app_logger
from sbt_project.tools.visualization_tool import VisualizationTool

class TrendToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    keywords: list = Field(..., description="search keyword")

class TrendTool(BaseTool):
    name: str = "TrendTool"
    description: str = (
        "A tool for exploring keywords and retrieving trending search data from Google Trends."
    )
    args_schema: Type[BaseModel] = TrendToolInput


    def _run(self, keywords: list) -> str:
        app_logger.debug(f'keywords : {keywords}')
        data = self.__keywords(keywords=keywords)
        app_logger.debug(f'data : {data}')
        VisualizationTool.visualize(data.to_dict())
        return ''


    def  __keywords(self, keywords: list) -> list:
        """
        검색어(keyword)로 탐색
        """
        # 구글 트렌드 요청
        pytrends = TrendReq(hl='en-US', tz=360)  # hl=ko-KR

        # 트렌드 데이터 요청
        pytrends.build_payload(keywords, cat=0, timeframe='today 12-m', geo='', gprop='')

        # 관심도 데이터
        data = pytrends.interest_over_time()  # 시간별 관심도 (Interest over Time) 데이터
        app_logger.debug(f'__keywords : {data}')
        return data


    def  __popular_searches(self) -> list:
        """
        실시간 인기 - Not available
        """
        # 구글 트렌드 요청
        pytrends = TrendReq(hl='en-US', tz=360)  # hl=ko-KR
        time.sleep(3)
        # 현재 인기 검색어 (전체 또는 지역별)
        trending = pytrends.trending_searches(pn='united_states')  # 특정 지역 코드 사용
        app_logger.debug(f'__popular_searches : {trending}')
        return trending
