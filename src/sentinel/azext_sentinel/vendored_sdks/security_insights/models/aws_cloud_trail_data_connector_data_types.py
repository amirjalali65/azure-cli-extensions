# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AwsCloudTrailDataConnectorDataTypes(Model):
    """The available data types for Amazon Web Services CloudTrail data connector.

    :param logs: Logs data type.
    :type logs:
     ~securityinsights.models.AwsCloudTrailDataConnectorDataTypesLogs
    """

    _attribute_map = {
        'logs': {'key': 'logs', 'type': 'AwsCloudTrailDataConnectorDataTypesLogs'},
    }

    def __init__(self, **kwargs):
        super(AwsCloudTrailDataConnectorDataTypes, self).__init__(**kwargs)
        self.logs = kwargs.get('logs', None)
