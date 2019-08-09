import yaml
import os


class Config:
    """ Contains all data from Config file """

    def __init__(self, config_file_path="default.yaml"):
        self.config_path = config_file_path
        self.config_parsed = self._parse_config(config_file_path)

    def _load_rules(self):
        pass

    def _parse_config(self, config_path):
        if os.path.exists(config_path):
            with open(config_path, 'r') as file:
                try:
                    config_parsed = yaml.safe_load(file)
                except yaml.YAMLError as e:
                    raise e
                else:
                    return config_parsed
        else:
            raise FileNotFoundError
