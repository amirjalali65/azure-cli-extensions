# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class EventGroupingSettings(Model):
    """Event grouping settings property bag.

    :param aggregation_kind: Possible values include: 'SingleAlert',
     'AlertPerResult'
    :type aggregation_kind: str or
     ~securityinsights.models.EventGroupingAggregationKind
    """

    _attribute_map = {
        'aggregation_kind': {'key': 'aggregationKind', 'type': 'str'},
    }

    def __init__(self, *, aggregation_kind=None, **kwargs) -> None:
        super(EventGroupingSettings, self).__init__(**kwargs)
        self.aggregation_kind = aggregation_kind
