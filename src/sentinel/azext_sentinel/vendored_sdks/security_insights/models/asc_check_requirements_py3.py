# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .data_connectors_check_requirements_py3 import DataConnectorsCheckRequirements


class ASCCheckRequirements(DataConnectorsCheckRequirements):
    """Represents ASC (Azure Security Center) requirements check request.

    All required parameters must be populated in order to send to Azure.

    :param kind: Required. Constant filled by server.
    :type kind: str
    :param subscription_id: The subscription id to connect to, and get the
     data from.
    :type subscription_id: str
    """

    _validation = {
        'kind': {'required': True},
    }

    _attribute_map = {
        'kind': {'key': 'kind', 'type': 'str'},
        'subscription_id': {'key': 'properties.subscriptionId', 'type': 'str'},
    }

    def __init__(self, *, subscription_id: str=None, **kwargs) -> None:
        super(ASCCheckRequirements, self).__init__(**kwargs)
        self.subscription_id = subscription_id
        self.kind = 'AzureSecurityCenter'
