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


class QuotaCounterContract(Model):
    """Quota counter details.

    All required parameters must be populated in order to send to Azure.

    :param counter_key: Required. The Key value of the Counter. Must not be
     empty.
    :type counter_key: str
    :param period_key: Required. Identifier of the Period for which the
     counter was collected. Must not be empty.
    :type period_key: str
    :param period_start_time: Required. The date of the start of Counter
     Period. The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ`
     as specified by the ISO 8601 standard.
    :type period_start_time: datetime
    :param period_end_time: Required. The date of the end of Counter Period.
     The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as
     specified by the ISO 8601 standard.
    :type period_end_time: datetime
    :param value: Quota Value Properties
    :type value:
     ~azure.mgmt.apimanagement.models.QuotaCounterValueContractProperties
    """

    _validation = {
        'counter_key': {'required': True, 'min_length': 1},
        'period_key': {'required': True, 'min_length': 1},
        'period_start_time': {'required': True},
        'period_end_time': {'required': True},
    }

    _attribute_map = {
        'counter_key': {'key': 'counterKey', 'type': 'str'},
        'period_key': {'key': 'periodKey', 'type': 'str'},
        'period_start_time': {'key': 'periodStartTime', 'type': 'iso-8601'},
        'period_end_time': {'key': 'periodEndTime', 'type': 'iso-8601'},
        'value': {'key': 'value', 'type': 'QuotaCounterValueContractProperties'},
    }

    def __init__(self, **kwargs):
        super(QuotaCounterContract, self).__init__(**kwargs)
        self.counter_key = kwargs.get('counter_key', None)
        self.period_key = kwargs.get('period_key', None)
        self.period_start_time = kwargs.get('period_start_time', None)
        self.period_end_time = kwargs.get('period_end_time', None)
        self.value = kwargs.get('value', None)