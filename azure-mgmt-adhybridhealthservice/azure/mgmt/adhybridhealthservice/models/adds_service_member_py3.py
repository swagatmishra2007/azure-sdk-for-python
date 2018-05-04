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


class AddsServiceMember(Model):
    """The server details for ADDS service.

    :param domain_name: The domain name.
    :type domain_name: str
    :param site_name: The site name.
    :type site_name: str
    :param adds_roles: The list of ADDS roles.
    :type adds_roles: list[str]
    :param gc_reachable: Indicates if the global catalog for this domain is
     reachable or not.
    :type gc_reachable: bool
    :param is_advertising: Indicates if the Dc is advertising or not.
    :type is_advertising: bool
    :param pdc_reachable: Indicates if the primary domain controller is
     reachable or not.
    :type pdc_reachable: bool
    :param sysvol_state: Indicates if the SYSVOL state is healthy or not.
    :type sysvol_state: bool
    :param dc_types: The list of domain controller types.
    :type dc_types: list[str]
    :param service_member_id: The id of the server.
    :type service_member_id: str
    :param service_id: The service id to whom this server belongs.
    :type service_id: str
    :param tenant_id: The tenant id to whom this server belongs.
    :type tenant_id: str
    :param active_alerts: The total number of alerts that are currently active
     for the server.
    :type active_alerts: int
    :param additional_information: The additional information, if any, for the
     server.
    :type additional_information: str
    :param created_date: The date time , in UTC, when the server was
     onboaraded to Azure Active Directory Connect Health.
    :type created_date: datetime
    :param dimensions: The server specific configuration related dimensions.
    :type dimensions: object
    :param disabled: Indicates if the server is disabled or not.
    :type disabled: bool
    :param disabled_reason: The reason for disabling the server. Possible
     values include: 'None', 'GdprStopCollection', 'DeletedFromPortal',
     'DisabledDueToInactivity'
    :type disabled_reason: str or
     ~azure.mgmt.adhybridhealthservice.models.ServerDisabledReason
    :param installed_qfe: The list of installed QFEs for the server.
    :type installed_qfe: object
    :param last_disabled: The date and time , in UTC, when the server was last
     disabled.
    :type last_disabled: datetime
    :param last_reboot: The date and time, in UTC, when the server was last
     rebooted.
    :type last_reboot: datetime
    :param last_server_reported_monitoring_level_change: The date and time, in
     UTC, when the server's data monitoring configuration was last changed.
    :type last_server_reported_monitoring_level_change: datetime
    :param last_updated: The date and time, in UTC, when the server proeprties
     were last updated.
    :type last_updated: datetime
    :param machine_id: The id of the machine.
    :type machine_id: str
    :param machine_name: The name of the server.
    :type machine_name: str
    :param monitoring_configurations_computed: The monitoring configuration of
     the server which determines what activities are monitored by Azure Active
     Directory Connect Health.
    :type monitoring_configurations_computed: object
    :param monitoring_configurations_customized: The customized monitoring
     configuration of the server which determines what activities are monitored
     by Azure Active Directory Connect Health.
    :type monitoring_configurations_customized: object
    :param os_name: The name of the operating system installed in the machine.
    :type os_name: str
    :param os_version: The version of the operating system installed in the
     machine.
    :type os_version: str
    :param properties: Server specific properties.
    :type properties: object
    :param recommended_qfes: The list of recommended hotfixes for the server.
    :type recommended_qfes: object
    :param resolved_alerts: The total count of alerts that are resolved for
     this server.
    :type resolved_alerts: int
    :param role: The service role that is being monitored in the server.
    :type role: str
    :param server_reported_monitoring_level: The monitoring level reported by
     the server. Possible values include: 'Partial', 'Full', 'Off'
    :type server_reported_monitoring_level: str or
     ~azure.mgmt.adhybridhealthservice.models.MonitoringLevel
    :param status: The health status of the server.
    :type status: str
    """

    _attribute_map = {
        'domain_name': {'key': 'domainName', 'type': 'str'},
        'site_name': {'key': 'siteName', 'type': 'str'},
        'adds_roles': {'key': 'addsRoles', 'type': '[str]'},
        'gc_reachable': {'key': 'gcReachable', 'type': 'bool'},
        'is_advertising': {'key': 'isAdvertising', 'type': 'bool'},
        'pdc_reachable': {'key': 'pdcReachable', 'type': 'bool'},
        'sysvol_state': {'key': 'sysvolState', 'type': 'bool'},
        'dc_types': {'key': 'dcTypes', 'type': '[str]'},
        'service_member_id': {'key': 'serviceMemberId', 'type': 'str'},
        'service_id': {'key': 'serviceId', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'active_alerts': {'key': 'activeAlerts', 'type': 'int'},
        'additional_information': {'key': 'additionalInformation', 'type': 'str'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'dimensions': {'key': 'dimensions', 'type': 'object'},
        'disabled': {'key': 'disabled', 'type': 'bool'},
        'disabled_reason': {'key': 'disabledReason', 'type': 'ServerDisabledReason'},
        'installed_qfe': {'key': 'installedQfe', 'type': 'object'},
        'last_disabled': {'key': 'lastDisabled', 'type': 'iso-8601'},
        'last_reboot': {'key': 'lastReboot', 'type': 'iso-8601'},
        'last_server_reported_monitoring_level_change': {'key': 'lastServerReportedMonitoringLevelChange', 'type': 'iso-8601'},
        'last_updated': {'key': 'lastUpdated', 'type': 'iso-8601'},
        'machine_id': {'key': 'machineId', 'type': 'str'},
        'machine_name': {'key': 'machineName', 'type': 'str'},
        'monitoring_configurations_computed': {'key': 'monitoringConfigurationsComputed', 'type': 'object'},
        'monitoring_configurations_customized': {'key': 'monitoringConfigurationsCustomized', 'type': 'object'},
        'os_name': {'key': 'osName', 'type': 'str'},
        'os_version': {'key': 'osVersion', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'object'},
        'recommended_qfes': {'key': 'recommendedQfes', 'type': 'object'},
        'resolved_alerts': {'key': 'resolvedAlerts', 'type': 'int'},
        'role': {'key': 'role', 'type': 'str'},
        'server_reported_monitoring_level': {'key': 'serverReportedMonitoringLevel', 'type': 'MonitoringLevel'},
        'status': {'key': 'status', 'type': 'str'},
    }

    def __init__(self, *, domain_name: str=None, site_name: str=None, adds_roles=None, gc_reachable: bool=None, is_advertising: bool=None, pdc_reachable: bool=None, sysvol_state: bool=None, dc_types=None, service_member_id: str=None, service_id: str=None, tenant_id: str=None, active_alerts: int=None, additional_information: str=None, created_date=None, dimensions=None, disabled: bool=None, disabled_reason=None, installed_qfe=None, last_disabled=None, last_reboot=None, last_server_reported_monitoring_level_change=None, last_updated=None, machine_id: str=None, machine_name: str=None, monitoring_configurations_computed=None, monitoring_configurations_customized=None, os_name: str=None, os_version: str=None, properties=None, recommended_qfes=None, resolved_alerts: int=None, role: str=None, server_reported_monitoring_level=None, status: str=None, **kwargs) -> None:
        super(AddsServiceMember, self).__init__(**kwargs)
        self.domain_name = domain_name
        self.site_name = site_name
        self.adds_roles = adds_roles
        self.gc_reachable = gc_reachable
        self.is_advertising = is_advertising
        self.pdc_reachable = pdc_reachable
        self.sysvol_state = sysvol_state
        self.dc_types = dc_types
        self.service_member_id = service_member_id
        self.service_id = service_id
        self.tenant_id = tenant_id
        self.active_alerts = active_alerts
        self.additional_information = additional_information
        self.created_date = created_date
        self.dimensions = dimensions
        self.disabled = disabled
        self.disabled_reason = disabled_reason
        self.installed_qfe = installed_qfe
        self.last_disabled = last_disabled
        self.last_reboot = last_reboot
        self.last_server_reported_monitoring_level_change = last_server_reported_monitoring_level_change
        self.last_updated = last_updated
        self.machine_id = machine_id
        self.machine_name = machine_name
        self.monitoring_configurations_computed = monitoring_configurations_computed
        self.monitoring_configurations_customized = monitoring_configurations_customized
        self.os_name = os_name
        self.os_version = os_version
        self.properties = properties
        self.recommended_qfes = recommended_qfes
        self.resolved_alerts = resolved_alerts
        self.role = role
        self.server_reported_monitoring_level = server_reported_monitoring_level
        self.status = status
