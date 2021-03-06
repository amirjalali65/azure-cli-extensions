# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AlertsDataTypeOfDataConnector(Model):
    """Alerts data type for data connectors.

    :param alerts: Alerts data type connection.
    :type alerts: ~securityinsights.models.AlertsDataTypeOfDataConnectorAlerts
    """

    _attribute_map = {
        'alerts': {'key': 'alerts', 'type': 'AlertsDataTypeOfDataConnectorAlerts'},
    }

    def __init__(self, *, alerts=None, **kwargs) -> None:
        super(AlertsDataTypeOfDataConnector, self).__init__(**kwargs)
        self.alerts = alerts
