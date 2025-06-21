import yaml
import os

CONFIG = None

def load_config(config_path="config/default.yaml"):
    """加载配置文件"""
    global CONFIG
    if CONFIG is None:
        with open(config_path, 'r', encoding='utf-8') as file:
            CONFIG = yaml.safe_load(file)
    return CONFIG

def get_config():
    """获取配置"""
    return load_config()