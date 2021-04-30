# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ScheduledAlertRuleCommonProperties(Model):
    """Scheduled alert rule template property bag.

    :param query: The query that creates alerts for this rule.
    :type query: str
    :param query_frequency: The frequency (in ISO 8601 duration format) for
     this alert rule to run.
    :type query_frequency: timedelta
    :param query_period: The period (in ISO 8601 duration format) that this
     alert rule looks at.
    :type query_period: timedelta
    :param severity: The severity for alerts created by this alert rule.
     Possible values include: 'High', 'Medium', 'Low', 'Informational'
    :type severity: str or ~alertrules.models.AlertSeverity
    :param trigger_operator: The operation against the threshold that triggers
     alert rule. Possible values include: 'GreaterThan', 'LessThan', 'Equal',
     'NotEqual'
    :type trigger_operator: str or ~alertrules.models.TriggerOperator
    :param trigger_threshold: The threshold triggers this alert rule.
    :type trigger_threshold: int
    :param event_grouping_settings: The event grouping settings.
    :type event_grouping_settings: ~alertrules.models.EventGroupingSettings
    :param custom_details: Dictionary of string key-value pairs of columns to
     be attached to the alert
    :type custom_details: dict[str, str]
    :param entity_mappings: Array of the entity mappings of the alert rule
    :type entity_mappings: list[~alertrules.models.EntityMapping]
    :param alert_details_override: The alert details override settings
    :type alert_details_override: ~alertrules.models.AlertDetailsOverride
    """

    _attribute_map = {
        'query': {'key': 'query', 'type': 'str'},
        'query_frequency': {'key': 'queryFrequency', 'type': 'duration'},
        'query_period': {'key': 'queryPeriod', 'type': 'duration'},
        'severity': {'key': 'severity', 'type': 'str'},
        'trigger_operator': {'key': 'triggerOperator', 'type': 'TriggerOperator'},
        'trigger_threshold': {'key': 'triggerThreshold', 'type': 'int'},
        'event_grouping_settings': {'key': 'eventGroupingSettings', 'type': 'EventGroupingSettings'},
        'custom_details': {'key': 'customDetails', 'type': '{str}'},
        'entity_mappings': {'key': 'entityMappings', 'type': '[EntityMapping]'},
        'alert_details_override': {'key': 'alertDetailsOverride', 'type': 'AlertDetailsOverride'},
    }

    def __init__(self, *, query: str=None, query_frequency=None, query_period=None, severity=None, trigger_operator=None, trigger_threshold: int=None, event_grouping_settings=None, custom_details=None, entity_mappings=None, alert_details_override=None, **kwargs) -> None:
        super(ScheduledAlertRuleCommonProperties, self).__init__(**kwargs)
        self.query = query
        self.query_frequency = query_frequency
        self.query_period = query_period
        self.severity = severity
        self.trigger_operator = trigger_operator
        self.trigger_threshold = trigger_threshold
        self.event_grouping_settings = event_grouping_settings
        self.custom_details = custom_details
        self.entity_mappings = entity_mappings
        self.alert_details_override = alert_details_override