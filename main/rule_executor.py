try:
    import requests
except ImportError:
    from botocore.vendored import requests


class Rule:
    def __init__(self, config, rule_path, child_conn, run=True):
        self.config = config
        self.rule = config.parse_yaml(rule_path)
        self.init_step_conf = self._get_step_config('InitQuery')
        self.second_step_config = self._get_step_config('Enrich')
        if run:
            self.run()

    def run(self):
        self._init_step()

    def _init_step(self):
        if "ES" in self.init_step_conf:
            es = self.init_step_conf['ES']['URL']
            index = self.init_step_conf['ES']['Index']
        else:
            es, index = self.config.get_main_es_data()
        try:
            if self.init_step_conf['Type'] == 'raw':
                query = self.init_step_conf['Query']
                es_response_data = self._get_events_from_es(query, es, index)
                if "CorrelationAggBucket" in self.init_step_conf:
                    fields = self._get_correlation_events_from_bucket(es_response_data)
                    self._second_step(fields)
                else:
                    pass
        except KeyError as e:
            raise e

    def _get_step_config(self, step):
        try:
            return self.rule[step]
        except KeyError:
            return

    def _get_events_from_es(self, query, es, index):
        try:
            url = "/".join([es, index, "_search"])
            headers = {"Content-type": "application/json"}
            r = requests.get(url, data=query, headers=headers)
            return r.json()
        except TypeError as e:
            raise e

    def _second_step(self, fields):
        if self.second_step_config:
            pass
        else:
            pass

    def _get_correlation_events_from_bucket(self, es_response_data):
        try:
            path = self.init_step_conf["CorrelationAggBucket"]["Path"]
            name = self.init_step_conf["CorrelationAggBucket"]["CorrelationFieldName"]
        except KeyError as e:
            raise e
        bucket = es_response_data
        for key in path.split('.'):
            bucket = bucket[key]
        result = []
        for dic in bucket:
            result.append({name: dic['key']})
        return result

    def _third_step(self, fields):
        pass


class MultiRule:
    def __init__(self):
        pass
