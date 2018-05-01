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


class AdditionalInformation(Model):
    """The addtional information for a property.

    :param title_name: The title name for the property.
    :type title_name: str
    :param title_value: The title value for the property.
    :type title_value: str
    :param properties: The list of properties which are included in the
     aditional information.
    :type properties: object
    """

    _attribute_map = {
        'title_name': {'key': 'titleName', 'type': 'str'},
        'title_value': {'key': 'titleValue', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'object'},
    }

    def __init__(self, *, title_name: str=None, title_value: str=None, properties=None, **kwargs) -> None:
        super(AdditionalInformation, self).__init__(**kwargs)
        self.title_name = title_name
        self.title_value = title_value
        self.properties = properties
