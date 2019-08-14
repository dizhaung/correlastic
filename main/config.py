import yaml
import os

config_file_map = {
    'rules_dir': 'RulesDir'
}


class Config:
    """ Contains all data from Config file """

    def __init__(self, config_file_path):
        self.config_path = config_file_path
        self.config_parsed = self._parse_config(config_file_path)

    def __str__(self):
        return str(self.config_parsed)

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

    def get_rules_dir(self):
        rules_path = self.config_parsed[config_file_map['rules_dir']]
        if os.path.exists(rules_path) and os.path.isdir(rules_path):
            return rules_path
        else:
            raise FileNotFoundError

