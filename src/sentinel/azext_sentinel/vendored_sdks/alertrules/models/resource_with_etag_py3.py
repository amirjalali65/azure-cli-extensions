# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource_py3 import Resource


class ResourceWithEtag(Resource):
    """An azure resource object with an Etag property.

    Variables are only populated by the server, and will be ignored when
    sending a request.

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
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'system_data': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, *, etag: str=None, **kwargs) -> None:
        super(ResourceWithEtag, self).__init__(**kwargs)
        self.etag = etag
