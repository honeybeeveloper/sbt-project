import os
import json

from sbt_project.configs.config import Config

def create_dir(dir_path):
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)

def json_to_dict(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data