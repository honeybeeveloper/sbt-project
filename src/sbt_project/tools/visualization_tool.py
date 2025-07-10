from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

import datetime
import pandas as pd
import matplotlib.pyplot as plt

from sbt_project import app_logger

now_str = datetime.datetime.now().strftime('%y%m%d_%H%M%S')

class VisualizationToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    input_data: dict = Field(..., description="")

class VisualizationTool(BaseTool):
    name: str = "VisualizationTool"
    description: str = (
        ""
    )
    args_schema: Type[BaseModel] = VisualizationToolInput

    def _run(self, input_data: dict) -> str:
        return '>>'

    @staticmethod
    def visualize(input_data: dict):
        try:
            app_logger.debug(f'input_data : {input_data}')
            # Convert dict to DataFrame
            df = pd.DataFrame.from_dict(input_data)
            df.index = pd.to_datetime(df.index)
            app_logger.debug(f'df.index : {df.index}')
            app_logger.debug(f'df.columns : {df.columns}')

            # Plot bar chart of top trending terms
            df["루닛"].plot(title="Interest Over Time", figsize=(10, 6))
            plt.ylabel("Interest")
            plt.xlabel('Date')
            plt.tight_layout()
            plt.show()
            plt.savefig(f'image_{now_str}.jpg')
            plt.close()
            return "Trending searches visualized successfully."
        except Exception as e:
            return f"Error during visualization: {str(e)}"