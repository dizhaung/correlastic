import multiprocessing
import rule_executor
import config
import os


class CorrelasticHandler:
    def __init__(self, config_path="../config/config.yaml", rules_prefix="rule"):
        self.config = config.Config(config_path)
        self.rules_path = self.config.get_rules_dir()
        self.rules_prefix = rules_prefix

    def run_rules(self):
        parent_connections = []
        processes = []
        for file in os.listdir(self.rules_path):
            full_path = os.path.join(self.rules_path, file)
            if os.path.isfile(full_path):
                if file[:len(self.rules_prefix)] == self.rules_prefix:
                    parent_conn, child_conn = multiprocessing.Pipe()
                    parent_connections.append(parent_conn)
                    process = multiprocessing.Process(target=rule_executor.Rule, args=(self.config,
                                                                                       full_path,
                                                                                       child_conn,))
                    processes.append(process)
            else:
                # TBD for MultiRules
                if file[:len(self.rules_prefix)] == self.rules_prefix:
                    pass
        if parent_connections and processes:
            for process in processes:
                process.start()
            for process in processes:
                process.join()


if __name__ == "__main__":
    c = CorrelasticHandler()
    c.run_rules()
