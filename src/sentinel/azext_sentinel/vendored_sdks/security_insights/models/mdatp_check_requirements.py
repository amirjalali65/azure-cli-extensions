# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .data_connectors_check_requirements import DataConnectorsCheckRequirements


class MDATPCheckRequirements(DataConnectorsCheckRequirements):
    """Represents MDATP (Microsoft Defender Advanced Threat Protection)
    requirements check request.

    All required parameters must be populated in order to send to Azure.

    :param kind: Required. Constant filled by server.
    :type kind: str
    :param tenant_id: The tenant id to connect to, and get the data from.
    :type tenant_id: str
    """

    _validation = {
        'kind': {'required': True},
    }

    _attribute_map = {
        'kind': {'key': 'kind', 'type': 'str'},
        'tenant_id': {'key': 'properties.tenantId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(MDATPCheckRequirements, self).__init__(**kwargs)
        self.tenant_id = kwargs.get('tenant_id', None)
        self.kind = 'MicrosoftDefenderAdvancedThreatProtection'
