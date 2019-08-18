try:
    import requests
except ImportError:
    from botocore.vendored import requests


def events(fields, rule_name, config):
    """
    Function take care about creating and sending correlation events
    :param list fields : Contains fields that have to be included in correlation events
    :param str rule_name : Name of rule
    :param config : Class with necessary configuration strings as es correlation domain/index
    :return: Final status - success/fail
    """

    es_domain, index = ""


def hardcoded_event():
    pass
