import os

from sbt_project.common import utils
from sbt_project.configs.config import Config
from sbt_project.configs.logging import get_logger

app_config = Config(config_file='env.yaml')
app_logger = get_logger('sbt-project', app_config)

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

json_path = os.path.join(ROOT_DIR, 'converted_data.json')
# json_path = os.path.join(ROOT_DIR,'src','sbt_project' , 'converted_data.json') // out-main.py
sales_activity = utils.json_to_dict(json_path)