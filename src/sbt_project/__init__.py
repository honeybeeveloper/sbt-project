import os

from sbt_project.common import utils
from sbt_project.configs.config import Config
from sbt_project.configs.logging import get_logger

app_config = Config(config_file='env.yaml')
app_logger = get_logger('sbt-project', app_config)

json_path = os.path.join(app_config.env_dir, 'converted_data.json')
sales_activity = utils.json_to_dict(json_path)
