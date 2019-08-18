import yaml
import os


class Config:
    """Contains all data from Config file"""

    def __init__(self, config_file_path):
        self.config_path = config_file_path
        self.config_parsed = self.parse_yaml(config_file_path)

    def __str__(self):
        return str(self.config_parsed)

    @staticmethod
    def parse_yaml(file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                try:
                    config_parsed = yaml.safe_load(file)
                except yaml.YAMLError as e:
                    raise e
                else:
                    return config_parsed
        else:
            raise FileNotFoundError

    def get_rules_dir(self):
        rules_path = self.config_parsed['RulesDir']
        if os.path.exists(rules_path) and os.path.isdir(rules_path):
            return rules_path
        else:
            raise FileNotFoundError

    def get_main_es_data(self):
        return (
            self.config_parsed['MainES']['URL'],
            self.config_parsed['MainES']['Index']
        )



