import os
from configs.config import Config
from configs.logging import get_logger

from common import utils

app_config = Config(config_file='env.yaml')
app_logger = get_logger('sbt-project', app_config)

# ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

json_path = os.path.join('./converted_data.json')
sales_activity = utils.json_to_dict(json_path)
