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


class Connector(Model):
    """The connect details.

    :param id: The connector Id.
    :type id: str
    :param name: The connector name.
    :type name: str
    :param version: The connector version
    :type version: int
    :param type: The connector type.
    :type type: str
    :param description: The connector description.
    :type description: str
    :param schema_xml: The schema xml for the connector.
    :type schema_xml: str
    :param password_management_settings: The password management settings of
     the connector.
    :type password_management_settings: object
    :param password_hash_sync_configuration: The password hash synchronization
     configuration of the connector.
    :type password_hash_sync_configuration: object
    :param time_created: The date and time when this connector was created.
    :type time_created: datetime
    :param time_last_modified: The date and time when this connector was last
     modified.
    :type time_last_modified: datetime
    :param partitions: The partitions of the connector.
    :type partitions: list[~azure.mgmt.adhybridhealthservice.models.Partition]
    :param run_profiles: The run profiles of the connector.
    :type run_profiles:
     list[~azure.mgmt.adhybridhealthservice.models.RunProfiles]
    :param classes_included: The class inclusion list of the connector.
    :type classes_included: list[str]
    :param attributes_included: The attribute inclusion list of the connector.
    :type attributes_included: list[str]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'version': {'key': 'version', 'type': 'int'},
        'type': {'key': 'type', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'schema_xml': {'key': 'schemaXml', 'type': 'str'},
        'password_management_settings': {'key': 'passwordManagementSettings', 'type': 'object'},
        'password_hash_sync_configuration': {'key': 'passwordHashSyncConfiguration', 'type': 'object'},
        'time_created': {'key': 'timeCreated', 'type': 'iso-8601'},
        'time_last_modified': {'key': 'timeLastModified', 'type': 'iso-8601'},
        'partitions': {'key': 'partitions', 'type': '[Partition]'},
        'run_profiles': {'key': 'runProfiles', 'type': '[RunProfiles]'},
        'classes_included': {'key': 'classesIncluded', 'type': '[str]'},
        'attributes_included': {'key': 'attributesIncluded', 'type': '[str]'},
    }

    def __init__(self, *, id: str=None, name: str=None, version: int=None, type: str=None, description: str=None, schema_xml: str=None, password_management_settings=None, password_hash_sync_configuration=None, time_created=None, time_last_modified=None, partitions=None, run_profiles=None, classes_included=None, attributes_included=None, **kwargs) -> None:
        super(Connector, self).__init__(**kwargs)
        self.id = id
        self.name = name
        self.version = version
        self.type = type
        self.description = description
        self.schema_xml = schema_xml
        self.password_management_settings = password_management_settings
        self.password_hash_sync_configuration = password_hash_sync_configuration
        self.time_created = time_created
        self.time_last_modified = time_last_modified
        self.partitions = partitions
        self.run_profiles = run_profiles
        self.classes_included = classes_included
        self.attributes_included = attributes_included
