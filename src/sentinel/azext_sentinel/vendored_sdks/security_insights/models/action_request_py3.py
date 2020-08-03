# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource_with_etag_py3 import ResourceWithEtag


class ActionRequest(ResourceWithEtag):
    """Action for alert rule.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Azure resource Id
    :vartype id: str
    :ivar name: Azure resource name
    :vartype name: str
    :ivar type: Azure resource type
    :vartype type: str
    :param etag: Etag of the azure resource
    :type etag: str
    :param logic_app_resource_id: Logic App Resource Id,
     /subscriptions/{my-subscription}/resourceGroups/{my-resource-group}/providers/Microsoft.Logic/workflows/{my-workflow-id}.
    :type logic_app_resource_id: str
    :param trigger_uri: Logic App Callback URL for this specific workflow.
    :type trigger_uri: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'logic_app_resource_id': {'key': 'properties.logicAppResourceId', 'type': 'str'},
        'trigger_uri': {'key': 'properties.triggerUri', 'type': 'str'},
    }

    def __init__(self, *, etag: str=None, logic_app_resource_id: str=None, trigger_uri: str=None, **kwargs) -> None:
        super(ActionRequest, self).__init__(etag=etag, **kwargs)
        self.logic_app_resource_id = logic_app_resource_id
        self.trigger_uri = trigger_uri
