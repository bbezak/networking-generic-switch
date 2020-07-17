# Copyright 2020 StackHPC
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
import re

from networking_generic_switch.devices import netmiko_devices


class Cumulus(netmiko_devices.NetmikoSwitch):
    """Built for Cumulus 4.x

    Note for this switch you want config like this:

    [genericswitch:<hostname>]
    device_type = netmiko_cumulus
    ip = <ip>
    username = <username>
    password = <password>
    secret = <password for sudo>
    ngs_physical_networks = physnet1
    ngs_max_connections = 1
    ngs_port_default_vlan = 123
    ngs_disable_inactive_ports = False
    """
    NETMIKO_DEVICE_TYPE = "linux"

    # TODO(johngarbutt): for now, assume allowed VLANs are on trunks already
    #  But really this should be implemented and then opt out via config.
    ADD_NETWORK = []
    DELETE_NETWORK = []

    PLUG_PORT_TO_NETWORK = [
        'net add interface {port} bridge access {segmentation_id}',
    ]

    DELETE_PORT = [
        'net del interface {port} bridge access {segmentation_id}',
    ]

    ENABLE_PORT = [
        'net del interface {port} link down',
    ]

    DISABLE_PORT = [
        'net add interface {port} link down',
    ]

    SAVE_CONFIGURATION = [
        'net commit'
    ]

    ERROR_MSG_PATTERNS = [
        re.compile(r'configuration does not have "bridge-access'),
    ]
