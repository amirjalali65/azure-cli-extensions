# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .entity import Entity


class HuntingBookmark(Entity):
    """Represents a Hunting bookmark entity.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id
    :vartype id: str
    :ivar name: Azure resource name
    :vartype name: str
    :ivar type: Azure resource type
    :vartype type: str
    :param kind: Required. Constant filled by server.
    :type kind: str
    :ivar additional_data: A bag of custom fields that should be part of the
     entity and will be presented to the user.
    :vartype additional_data: dict[str, object]
    :ivar friendly_name: The graph item display name which is a short humanly
     readable description of the graph item instance. This property is optional
     and might be system generated.
    :vartype friendly_name: str
    :param created: The time the bookmark was created
    :type created: datetime
    :param created_by: Describes a user that created the bookmark
    :type created_by: ~securityinsights.models.UserInfo
    :param display_name: Required. The display name of the bookmark
    :type display_name: str
    :param event_time: The time of the event
    :type event_time: datetime
    :param labels: List of labels relevant to this bookmark
    :type labels: list[str]
    :param notes: The notes of the bookmark
    :type notes: str
    :param query: Required. The query of the bookmark.
    :type query: str
    :param query_result: The query result of the bookmark.
    :type query_result: str
    :param updated: The last time the bookmark was updated
    :type updated: datetime
    :param updated_by: Describes a user that updated the bookmark
    :type updated_by: ~securityinsights.models.UserInfo
    :param incident_info: Describes an incident that relates to bookmark
    :type incident_info: ~securityinsights.models.IncidentInfo
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'kind': {'required': True},
        'additional_data': {'readonly': True},
        'friendly_name': {'readonly': True},
        'display_name': {'required': True},
        'query': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'additional_data': {'key': 'properties.additionalData', 'type': '{object}'},
        'friendly_name': {'key': 'properties.friendlyName', 'type': 'str'},
        'created': {'key': 'properties.created', 'type': 'iso-8601'},
        'created_by': {'key': 'properties.createdBy', 'type': 'UserInfo'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'event_time': {'key': 'properties.eventTime', 'type': 'iso-8601'},
        'labels': {'key': 'properties.labels', 'type': '[str]'},
        'notes': {'key': 'properties.notes', 'type': 'str'},
        'query': {'key': 'properties.query', 'type': 'str'},
        'query_result': {'key': 'properties.queryResult', 'type': 'str'},
        'updated': {'key': 'properties.updated', 'type': 'iso-8601'},
        'updated_by': {'key': 'properties.updatedBy', 'type': 'UserInfo'},
        'incident_info': {'key': 'properties.incidentInfo', 'type': 'IncidentInfo'},
    }

    def __init__(self, **kwargs):
        super(HuntingBookmark, self).__init__(**kwargs)
        self.additional_data = None
        self.friendly_name = None
        self.created = kwargs.get('created', None)
        self.created_by = kwargs.get('created_by', None)
        self.display_name = kwargs.get('display_name', None)
        self.event_time = kwargs.get('event_time', None)
        self.labels = kwargs.get('labels', None)
        self.notes = kwargs.get('notes', None)
        self.query = kwargs.get('query', None)
        self.query_result = kwargs.get('query_result', None)
        self.updated = kwargs.get('updated', None)
        self.updated_by = kwargs.get('updated_by', None)
        self.incident_info = kwargs.get('incident_info', None)
        self.kind = 'Bookmark'
