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


class ExplicitListItem(Model):
    """Explicit list item.

    :param id: The explicit list item ID.
    :type id: long
    :param explicit_list_item: The explicit list item value.
    :type explicit_list_item: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'long'},
        'explicit_list_item': {'key': 'explicitListItem', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ExplicitListItem, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.explicit_list_item = kwargs.get('explicit_list_item', None)