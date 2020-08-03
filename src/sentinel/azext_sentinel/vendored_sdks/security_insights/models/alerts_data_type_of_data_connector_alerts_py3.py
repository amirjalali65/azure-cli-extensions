# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .data_connector_data_type_common_py3 import DataConnectorDataTypeCommon


class AlertsDataTypeOfDataConnectorAlerts(DataConnectorDataTypeCommon):
    """Alerts data type connection.

    :param state: Describe whether this data type connection is enabled or
     not. Possible values include: 'Enabled', 'Disabled'
    :type state: str or ~securityinsights.models.DataTypeState
    """

    _attribute_map = {
        'state': {'key': 'state', 'type': 'str'},
    }

    def __init__(self, *, state=None, **kwargs) -> None:
        super(AlertsDataTypeOfDataConnectorAlerts, self).__init__(state=state, **kwargs)
