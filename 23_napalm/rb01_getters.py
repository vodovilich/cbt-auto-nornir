from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def pull_info(task):
    task.run(task=napalm_get, getters=["get_config"])
    
results = nr.run(task=pull_info)
print_result(results)



"""
#GET_CONFIG
                             'ip http secure-server\n'
                             'ip http client source-interface '
                             'GigabitEthernet1\n'
                             '!\n'
                             'ip ssh pubkey-chain\n'
                             '  username frodo\n'
                             '   key-hash ssh-rsa '
                             '9E0422426EA11A0679430801859CF5B6 \n'
                             'ip scp server enable\n'
                             '!\n'
                             '!\n'
                             'ip access-list extended rfc1918-in-acl\n'
                             ' deny   ip 10.0.0.0 0.255.255.255 any\n'
                             
                             
#GET_FACTS
{ 'get_facts': { 'fqdn': 'iol-rtr157-02.atffc.hui',
                 'hostname': 'iol-rtr157-02',
                 'interface_list': [ 'Ethernet0/0',
                                     'Ethernet0/1',
                                     'Ethernet0/2',
                                     'Ethernet0/3',
                                     'Loopback0'],
                 'model': 'Unknown',
                 'os_version': 'Linux Software '
                               '(I86BI_LINUX-ADVENTERPRISEK9-M), Version '
                               '15.7(3)M0.1, DEVELOPMENT TEST SOFTWARE',
                 'serial_number': '67108912',
                 'uptime': 3360.0,
                 'vendor': 'Cisco'}}
                 
#GET_ENVIRONMENT - csr1000v only
{ 'get_environment': { 'cpu': {0: {'%usage': 0.0}},
                       'fans': {'invalid': {'status': True}},
                       'memory': { 'available_ram': 2237599872,
                                   'used_ram': 328839572},
                       'power': { 'invalid': { 'capacity': -1.0,
                                               'output': -1.0,
                                               'status': True}},
                       'temperature': { 'invalid': { 'is_alert': False,
                                                     'is_critical': False,
                                                     'temperature': -1.0}}}}

#GET_INTERFACES                                                 
  'get_interfaces': { 'GigabitEthernet1': { 'description': '',
                                            'is_enabled': True,
                                            'is_up': True,
                                            'last_flapped': -1.0,
                                            'mac_address': '50:00:00:06:00:00',
                                            'mtu': 1500,
                                            'speed': 1000.0},

#GET_INTERFACES_CCOUNTERS                                            
  'get_interfaces_counters': { 'GigabitEthernet1': { 'rx_broadcast_packets': 0,
                                                     'rx_discards': 0,
                                                     'rx_errors': 0,
                                                     'rx_multicast_packets': 0,
                                                     'rx_octets': 693241,
                                                     'rx_unicast_packets': 7379,
                                                     'tx_broadcast_packets': -1,
                                                     'tx_discards': 0,
                                                     'tx_errors': 0,
                                                     'tx_multicast_packets': -1,
                                                     'tx_octets': 734248,
                                                     'tx_unicast_packets': 3946},
                                                     
#GET_BGP_CONFIG
{ 'get_bgp_config': { '_': { 'apply_groups': [],
                             'description': '',
                             'export_policy': '',
                             'import_policy': '',
                             'local_address': '',
                             'local_as': 65001,
                             'multihop_ttl': 0,
                             'multipath': False,
                             'neighbors': { '192.168.100.6': { 'authentication_key': '',
                                                               'description': '',
                                                               'export_policy': '',
                                                               'import_policy': '',
                                                               'local_address': '',
                                                               'local_as': 65001,
                                                               'nhs': False,
                                                               'prefix_limit': { },
                                                               'remote_as': 65001,
                                                               'route_reflector_client': False},
                                                               

"""