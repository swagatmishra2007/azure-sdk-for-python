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


class ConnectorObjectErrors(Model):
    """The list of connector object errors.

    :param value:
    :type value:
     list[~azure.mgmt.adhybridhealthservice.models.ConnectorObjectError]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ConnectorObjectError]'},
    }

    def __init__(self, *, value=None, **kwargs) -> None:
        super(ConnectorObjectErrors, self).__init__(**kwargs)
        self.value = value
