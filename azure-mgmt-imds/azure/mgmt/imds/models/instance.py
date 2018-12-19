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


class Instance(Model):
    """Instance.

    :param compute: Compute Metadata
    :type compute: ~azure.mgmt.imds.models.Compute
    :param network: Network Metadata
    :type network: ~azure.mgmt.imds.models.Network
    """

    _attribute_map = {
        'compute': {'key': 'compute', 'type': 'Compute'},
        'network': {'key': 'network', 'type': 'Network'},
    }

    def __init__(self, **kwargs):
        super(Instance, self).__init__(**kwargs)
        self.compute = kwargs.get('compute', None)
        self.network = kwargs.get('network', None)
