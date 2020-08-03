# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource import Resource


class EntityQuery(Resource):
    """Specific entity query.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Azure resource Id
    :vartype id: str
    :ivar name: Azure resource name
    :vartype name: str
    :ivar type: Azure resource type
    :vartype type: str
    :param data_sources: List of the data sources that are required to run the
     query
    :type data_sources: list[str]
    :param display_name: The query display name
    :type display_name: str
    :param input_entity_type: The type of the query's source entity. Possible
     values include: 'Account', 'Host', 'File', 'AzureResource',
     'CloudApplication', 'DNS', 'FileHash', 'IP', 'Malware', 'Process',
     'RegistryKey', 'RegistryValue', 'SecurityGroup', 'URL', 'IoTDevice',
     'SecurityAlert', 'HuntingBookmark'
    :type input_entity_type: str or ~securityinsights.models.EntityType
    :param input_fields: List of the fields of the source entity that are
     required to run the query
    :type input_fields: list[str]
    :param output_entity_types: List of the desired output types to be
     constructed from the result
    :type output_entity_types: list[str or
     ~securityinsights.models.EntityType]
    :param query_template: The template query string to be parsed and
     formatted
    :type query_template: str
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
        'data_sources': {'key': 'properties.dataSources', 'type': '[str]'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'input_entity_type': {'key': 'properties.inputEntityType', 'type': 'str'},
        'input_fields': {'key': 'properties.inputFields', 'type': '[str]'},
        'output_entity_types': {'key': 'properties.outputEntityTypes', 'type': '[str]'},
        'query_template': {'key': 'properties.queryTemplate', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(EntityQuery, self).__init__(**kwargs)
        self.data_sources = kwargs.get('data_sources', None)
        self.display_name = kwargs.get('display_name', None)
        self.input_entity_type = kwargs.get('input_entity_type', None)
        self.input_fields = kwargs.get('input_fields', None)
        self.output_entity_types = kwargs.get('output_entity_types', None)
        self.query_template = kwargs.get('query_template', None)
