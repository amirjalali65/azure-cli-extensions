# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import SDKClient
from msrest import Configuration, Serializer, Deserializer
from .version import VERSION
from .operations.alert_rules_operations import AlertRulesOperations
from .operations.actions_operations import ActionsOperations
from .operations.alert_rule_templates_operations import AlertRuleTemplatesOperations
from . import models


class SecurityInsightsConfiguration(Configuration):
    """Configuration for SecurityInsights
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, subscription_id, base_url=None):

        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(SecurityInsightsConfiguration, self).__init__(base_url)

        self.add_user_agent('securityinsights/{}'.format(VERSION))

        self.subscription_id = subscription_id


class SecurityInsights(SDKClient):
    """API spec for Microsoft.SecurityInsights (Azure Security Insights) resource provider

    :ivar config: Configuration for client.
    :vartype config: SecurityInsightsConfiguration

    :ivar alert_rules: AlertRules operations
    :vartype alert_rules: alertrules.operations.AlertRulesOperations
    :ivar actions: Actions operations
    :vartype actions: alertrules.operations.ActionsOperations
    :ivar alert_rule_templates: AlertRuleTemplates operations
    :vartype alert_rule_templates: alertrules.operations.AlertRuleTemplatesOperations

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, subscription_id, base_url=None):

        self.config = SecurityInsightsConfiguration(subscription_id, base_url)
        super(SecurityInsights, self).__init__(None, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2021-03-01-preview'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.alert_rules = AlertRulesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.actions = ActionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.alert_rule_templates = AlertRuleTemplatesOperations(
            self._client, self.config, self._serialize, self._deserialize)
