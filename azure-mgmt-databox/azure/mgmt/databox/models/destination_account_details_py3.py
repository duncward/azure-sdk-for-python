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


class DestinationAccountDetails(Model):
    """Details for the destination account.

    All required parameters must be populated in order to send to Azure.

    :param account_id: Required. Destination storage account id.
    :type account_id: str
    """

    _validation = {
        'account_id': {'required': True},
    }

    _attribute_map = {
        'account_id': {'key': 'accountId', 'type': 'str'},
    }

    def __init__(self, *, account_id: str, **kwargs) -> None:
        super(DestinationAccountDetails, self).__init__(**kwargs)
        self.account_id = account_id