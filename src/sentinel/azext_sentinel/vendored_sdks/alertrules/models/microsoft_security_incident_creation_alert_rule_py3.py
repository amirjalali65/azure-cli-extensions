# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .alert_rule_py3 import AlertRule


class MicrosoftSecurityIncidentCreationAlertRule(AlertRule):
    """Represents MicrosoftSecurityIncidentCreation rule.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id
    :vartype id: str
    :ivar name: Azure resource name
    :vartype name: str
    :ivar type: Azure resource type
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy
     and modifiedBy information.
    :vartype system_data: ~alertrules.models.SystemData
    :param etag: Etag of the azure resource
    :type etag: str
    :param kind: Required. Constant filled by server.
    :type kind: str
    :param display_names_filter: the alerts' displayNames on which the cases
     will be generated
    :type display_names_filter: list[str]
    :param display_names_exclude_filter: the alerts' displayNames on which the
     cases will not be generated
    :type display_names_exclude_filter: list[str]
    :param product_filter: Required. The alerts' productName on which the
     cases will be generated. Possible values include: 'Microsoft Cloud App
     Security', 'Azure Security Center', 'Azure Advanced Threat Protection',
     'Azure Active Directory Identity Protection', 'Azure Security Center for
     IoT', 'Office 365 Advanced Threat Protection', 'Microsoft Defender
     Advanced Threat Protection'
    :type product_filter: str or
     ~alertrules.models.MicrosoftSecurityProductName
    :param severities_filter: the alerts' severities on which the cases will
     be generated
    :type severities_filter: list[str or ~alertrules.models.AlertSeverity]
    :param alert_rule_template_name: The Name of the alert rule template used
     to create this rule.
    :type alert_rule_template_name: str
    :param description: The description of the alert rule.
    :type description: str
    :param display_name: Required. The display name for alerts created by this
     alert rule.
    :type display_name: str
    :param enabled: Required. Determines whether this alert rule is enabled or
     disabled.
    :type enabled: bool
    :ivar last_modified_utc: The last time that this alert has been modified.
    :vartype last_modified_utc: datetime
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'system_data': {'readonly': True},
        'kind': {'required': True},
        'product_filter': {'required': True},
        'display_name': {'required': True},
        'enabled': {'required': True},
        'last_modified_utc': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
        'etag': {'key': 'etag', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'display_names_filter': {'key': 'properties.displayNamesFilter', 'type': '[str]'},
        'display_names_exclude_filter': {'key': 'properties.displayNamesExcludeFilter', 'type': '[str]'},
        'product_filter': {'key': 'properties.productFilter', 'type': 'str'},
        'severities_filter': {'key': 'properties.severitiesFilter', 'type': '[str]'},
        'alert_rule_template_name': {'key': 'properties.alertRuleTemplateName', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'enabled': {'key': 'properties.enabled', 'type': 'bool'},
        'last_modified_utc': {'key': 'properties.lastModifiedUtc', 'type': 'iso-8601'},
    }

    def __init__(self, *, product_filter, display_name: str, enabled: bool, etag: str=None, display_names_filter=None, display_names_exclude_filter=None, severities_filter=None, alert_rule_template_name: str=None, description: str=None, **kwargs) -> None:
        super(MicrosoftSecurityIncidentCreationAlertRule, self).__init__(etag=etag, **kwargs)
        self.display_names_filter = display_names_filter
        self.display_names_exclude_filter = display_names_exclude_filter
        self.product_filter = product_filter
        self.severities_filter = severities_filter
        self.alert_rule_template_name = alert_rule_template_name
        self.description = description
        self.display_name = display_name
        self.enabled = enabled
        self.last_modified_utc = None
        self.kind = 'MicrosoftSecurityIncidentCreation'