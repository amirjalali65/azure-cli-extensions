# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class HistoryServerPropertiesResponse(Model):
    """HistoryServerPropertiesResponse.

    :param web_proxy_endpoint:
    :type web_proxy_endpoint: str
    """

    _attribute_map = {
        'web_proxy_endpoint': {'key': 'webProxyEndpoint', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(HistoryServerPropertiesResponse, self).__init__(**kwargs)
        self.web_proxy_endpoint = kwargs.get('web_proxy_endpoint', None)