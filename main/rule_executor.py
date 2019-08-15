
try:
    import requests
except ImportError:
    from botocore.vendored import requests


class Rule:
    def __init__(self, config, rule_path, child_conn, run=True):
        self.config = config
        self.rule = config.parse_yaml(rule_path)
        if run:
            self.run()

    def run(self):
        self._init_step()

    def _init_step(self):
        init_step_conf = self._get_step_config('InitQuery')
        if "ES" in init_step_conf:
            es = init_step_conf['ES']['URL']
            index = init_step_conf['ES']['Index']
        else:
            es, index = self.config.get_main_es_data()
        try:
            if init_step_conf['Type'] == 'raw':
                query = init_step_conf['Query']
                self._get_events_from_es(query, es, index)
        except KeyError as e:
            pass

    def _get_step_config(self, step):
        try:
            return self.rule[step]
        except KeyError as e:
            raise e

    def _get_events_from_es(self, query, es, index):
        try:
            url = "/".join([es, index, "_search"])
            print(url)
        except TypeError as e:
            raise e



class MultiRule:
    def __init__(self):
        pass
