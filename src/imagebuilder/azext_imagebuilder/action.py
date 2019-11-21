# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import argparse
from knack.util import CLIError


# pylint: disable=protected-access
class ImageBuilderAddCustomize(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(PeeringAddDirectConnections, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = dict(x.split('=', 1) for x in values)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'type':
                d['type'] = v
            elif kl == 'name':
                d['name'] = v
            elif kl == 'scripturi':
                d['script_uri'] = v
        return d


# pylint: disable=protected-access
class ImageBuilderAddDistribute(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(PeeringAddExchangeConnections, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = dict(x.split('=', 1) for x in values)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'type':
                d['type'] = v
            elif kl == 'location':
                d['location'] = v
            elif kl == 'runoutputname':
                d['runOutputName'] = v
            elif kl == 'imageid':
                d['image_id'] = v
            else:
                raise CLIError('usage error: {} is invalid'.format(k))
        return d