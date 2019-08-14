import multiprocessing
import config
import os


class CorrelasticHandler:
    def __init__(self, config_path="../config/config.yaml", rules_prefix="rule"):
        self.config = config.Config(config_path)
        self.rules_path = self.config.get_rules_dir()
        self.rules_prefix = rules_prefix
        self._get_rules_list()

    def _get_rules_list(self):
        for file in os.listdir(self.rules_path):
            full_path = os.path.join(self.rules_path, file)
            if os.path.isfile(full_path):
                if file[:len(self.rules_prefix)] == self.rules_prefix:
                    print(file)
            else:
                if file[:len(self.rules_prefix)] == self.rules_prefix:
                    print(file)


if __name__ == "__main__":
    CorrelasticHandler()
