import os
from configs.config import Config
from configs.logging import get_logger

app_config = Config(config_file='env.yaml')
app_logger = get_logger('sbt-project', app_config)

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))