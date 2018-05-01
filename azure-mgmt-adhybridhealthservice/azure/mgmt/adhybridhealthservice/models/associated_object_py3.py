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


class AssociatedObject(Model):
    """Object that hold sync object details.

    :param display_name: The display name of the object.
    :type display_name: str
    :param distinguished_name: The distinguished name of the object.
    :type distinguished_name: str
    :param last_dir_sync_time: The last dirSync time.
    :type last_dir_sync_time: datetime
    :param mail: The email of the object.
    :type mail: str
    :param object_guid: The object guid.
    :type object_guid: str
    :param object_type: The object type.
    :type object_type: str
    :param onpremises_user_principal_name: The On-premises UPN.
    :type onpremises_user_principal_name: str
    :param proxy_addresses: The proxy addresses.
    :type proxy_addresses: str
    :param source_anchor: The source anchor.
    :type source_anchor: str
    :param source_of_authority: The source of authority.
    :type source_of_authority: str
    :param time_occured:  The time of the error.
    :type time_occured: datetime
    :param user_principal_name:  The UPN.
    :type user_principal_name: str
    """

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'distinguished_name': {'key': 'distinguishedName', 'type': 'str'},
        'last_dir_sync_time': {'key': 'lastDirSyncTime', 'type': 'iso-8601'},
        'mail': {'key': 'mail', 'type': 'str'},
        'object_guid': {'key': 'objectGuid', 'type': 'str'},
        'object_type': {'key': 'objectType', 'type': 'str'},
        'onpremises_user_principal_name': {'key': 'onpremisesUserPrincipalName', 'type': 'str'},
        'proxy_addresses': {'key': 'proxyAddresses', 'type': 'str'},
        'source_anchor': {'key': 'sourceAnchor', 'type': 'str'},
        'source_of_authority': {'key': 'sourceOfAuthority', 'type': 'str'},
        'time_occured': {'key': 'timeOccured', 'type': 'iso-8601'},
        'user_principal_name': {'key': 'userPrincipalName', 'type': 'str'},
    }

    def __init__(self, *, display_name: str=None, distinguished_name: str=None, last_dir_sync_time=None, mail: str=None, object_guid: str=None, object_type: str=None, onpremises_user_principal_name: str=None, proxy_addresses: str=None, source_anchor: str=None, source_of_authority: str=None, time_occured=None, user_principal_name: str=None, **kwargs) -> None:
        super(AssociatedObject, self).__init__(**kwargs)
        self.display_name = display_name
        self.distinguished_name = distinguished_name
        self.last_dir_sync_time = last_dir_sync_time
        self.mail = mail
        self.object_guid = object_guid
        self.object_type = object_type
        self.onpremises_user_principal_name = onpremises_user_principal_name
        self.proxy_addresses = proxy_addresses
        self.source_anchor = source_anchor
        self.source_of_authority = source_of_authority
        self.time_occured = time_occured
        self.user_principal_name = user_principal_name
