# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource_with_etag_py3 import ResourceWithEtag


class Incident(ResourceWithEtag):
    """Represents an incident in Azure Security Insights.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id
    :vartype id: str
    :ivar name: Azure resource name
    :vartype name: str
    :ivar type: Azure resource type
    :vartype type: str
    :param etag: Etag of the azure resource
    :type etag: str
    :ivar additional_data: Additional data on the incident
    :vartype additional_data: ~securityinsights.models.IncidentAdditionalData
    :param classification: The reason the incident was closed. Possible values
     include: 'Undetermined', 'TruePositive', 'BenignPositive', 'FalsePositive'
    :type classification: str or
     ~securityinsights.models.IncidentClassification
    :param classification_comment: Describes the reason the incident was
     closed
    :type classification_comment: str
    :param classification_reason: The classification reason the incident was
     closed with. Possible values include: 'SuspiciousActivity',
     'SuspiciousButExpected', 'IncorrectAlertLogic', 'InaccurateData'
    :type classification_reason: str or
     ~securityinsights.models.IncidentClassificationReason
    :ivar created_time_utc: The time the incident was created
    :vartype created_time_utc: datetime
    :param description: The description of the incident
    :type description: str
    :param first_activity_time_utc: The time of the first activity in the
     incident
    :type first_activity_time_utc: datetime
    :ivar incident_url: The deep-link url to the incident in Azure portal
    :vartype incident_url: str
    :ivar incident_number: A sequential number
    :vartype incident_number: int
    :param labels: List of labels relevant to this incident
    :type labels: list[~securityinsights.models.IncidentLabel]
    :param last_activity_time_utc: The time of the last activity in the
     incident
    :type last_activity_time_utc: datetime
    :ivar last_modified_time_utc: The last time the incident was updated
    :vartype last_modified_time_utc: datetime
    :param owner: Describes a user that the incident is assigned to
    :type owner: ~securityinsights.models.IncidentOwnerInfo
    :ivar related_analytic_rule_ids: List of resource ids of Analytic rules
     related to the incident
    :vartype related_analytic_rule_ids: list[str]
    :param severity: Required. The severity of the incident. Possible values
     include: 'High', 'Medium', 'Low', 'Informational'
    :type severity: str or ~securityinsights.models.IncidentSeverity
    :param status: Required. The status of the incident. Possible values
     include: 'New', 'Active', 'Closed'
    :type status: str or ~securityinsights.models.IncidentStatus
    :param title: Required. The title of the incident
    :type title: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'additional_data': {'readonly': True},
        'created_time_utc': {'readonly': True},
        'incident_url': {'readonly': True},
        'incident_number': {'readonly': True},
        'last_modified_time_utc': {'readonly': True},
        'related_analytic_rule_ids': {'readonly': True},
        'severity': {'required': True},
        'status': {'required': True},
        'title': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'additional_data': {'key': 'properties.additionalData', 'type': 'IncidentAdditionalData'},
        'classification': {'key': 'properties.classification', 'type': 'str'},
        'classification_comment': {'key': 'properties.classificationComment', 'type': 'str'},
        'classification_reason': {'key': 'properties.classificationReason', 'type': 'str'},
        'created_time_utc': {'key': 'properties.createdTimeUtc', 'type': 'iso-8601'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'first_activity_time_utc': {'key': 'properties.firstActivityTimeUtc', 'type': 'iso-8601'},
        'incident_url': {'key': 'properties.incidentUrl', 'type': 'str'},
        'incident_number': {'key': 'properties.incidentNumber', 'type': 'int'},
        'labels': {'key': 'properties.labels', 'type': '[IncidentLabel]'},
        'last_activity_time_utc': {'key': 'properties.lastActivityTimeUtc', 'type': 'iso-8601'},
        'last_modified_time_utc': {'key': 'properties.lastModifiedTimeUtc', 'type': 'iso-8601'},
        'owner': {'key': 'properties.owner', 'type': 'IncidentOwnerInfo'},
        'related_analytic_rule_ids': {'key': 'properties.relatedAnalyticRuleIds', 'type': '[str]'},
        'severity': {'key': 'properties.severity', 'type': 'str'},
        'status': {'key': 'properties.status', 'type': 'str'},
        'title': {'key': 'properties.title', 'type': 'str'},
    }

    def __init__(self, *, severity, status, title: str, etag: str=None, classification=None, classification_comment: str=None, classification_reason=None, description: str=None, first_activity_time_utc=None, labels=None, last_activity_time_utc=None, owner=None, **kwargs) -> None:
        super(Incident, self).__init__(etag=etag, **kwargs)
        self.additional_data = None
        self.classification = classification
        self.classification_comment = classification_comment
        self.classification_reason = classification_reason
        self.created_time_utc = None
        self.description = description
        self.first_activity_time_utc = first_activity_time_utc
        self.incident_url = None
        self.incident_number = None
        self.labels = labels
        self.last_activity_time_utc = last_activity_time_utc
        self.last_modified_time_utc = None
        self.owner = owner
        self.related_analytic_rule_ids = None
        self.severity = severity
        self.status = status
        self.title = title
