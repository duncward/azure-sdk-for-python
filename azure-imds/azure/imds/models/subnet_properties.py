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


class SubnetProperties(Model):
    """This contains the properties of the subnet.

    :param address: This is the address range of the subnet.
    :type address: str
    :param prefix: This is the prefix of the subnet.
    :type prefix: str
    """

    _attribute_map = {
        'address': {'key': 'address', 'type': 'str'},
        'prefix': {'key': 'prefix', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SubnetProperties, self).__init__(**kwargs)
        self.address = kwargs.get('address', None)
        self.prefix = kwargs.get('prefix', None)
