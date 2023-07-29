import sys
import getpass
from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

"""
iol-01
    gandalf grey
    bilbo baggins
    ususer uspas
iol-02
    gandalf grey
    bilbo baggins
    euser eupas
csr-01
    gandalf grey
    bilbo baggins
    csruser csrpas
default.yaml
    gandalf grey
"""
#SHOWING WHAT IS IN defaults.yaml
print("\nDEFAULT ACCORDING TO DEFAULT.YAML")

def credential_test(task):
    task.run(task=send_command, command="show users")
    
results = nr.run(task=credential_test)
print_result(results)
nr.close_connections()



#SHOWING OVERWRITTEN DEFAULTS 
print("\n\n\nMODIFYING DEFAULT.YAML SETTINGS:")
passwrd = getpass.getpass()
nr.inventory.defaults.password = passwrd
nr.inventory.defaults.username = "bilbo" #nr.inventory.defaults.username = sys.argv[1] -----> you can give it as an argument

def credential_test(task):
    task.run(task=send_command, command="show users")
    
results = nr.run(task=credential_test)
print_result(results)
nr.close_connections()


#SHOWING OVERWRITTEN DEFAULTS BASED ON GROUPS/HOSTS yamls
print("\n\n\nMODIFYING DEFAULT.YAML SETTINGS PER GROUP/HOST:")


usa_pass = getpass.getpass(prompt="\nEnter USA GROUP password: ")
euro_pass = getpass.getpass(prompt="\nEnter EURO GROUP password: ")
csr_01_pass = getpass.getpass(prompt="\nEnter iol-01 HOST password: ")

nr.inventory.groups["usa_group"].password = usa_pass
nr.inventory.groups["euro_group"].password = euro_pass
nr.inventory.hosts["csr-01"].password = csr_01_pass

nr.inventory.groups["usa_group"].username = "ususer"
nr.inventory.groups["euro_group"].username = "euser"
nr.inventory.hosts["csr-01"].username = "csruser"

def credential_test(task):
    task.run(task=send_command, command="show users")
    
results = nr.run(task=credential_test)
print_result(results)


"""
DEFAULT ACCORDING TO DEFAULT.YAML
* csr-01 *      gandalf    idle                 00:00:00 192.168.100.4
* iol-01 *      gandalf    idle                 00:00:00 192.168.100.4
* iol-02 *      gandalf    idle                 00:00:00 192.168.100.4

MODIFYING DEFAULT.YAML SETTINGS:
Password: 
csr-01 *     bilbo      idle                 00:00:00 192.168.100.4
iol-01 *     bilbo      idle                 00:00:00 192.168.100.4
iol-02 *     bilbo      idle                 00:00:00 192.168.100.4


MODIFYING DEFAULT.YAML SETTINGS PER GROUP/HOST:
Enter USA GROUP password: 
Enter EURO GROUP password: 
Enter iol-01 HOST password: 
csr-01 *     csruser    idle                 00:00:00 192.168.100.4
iol-01 *     ususer     idle                 00:00:00 192.168.100.4
iol-02 *     euser      idle                 00:00:00 192.168.100.4
"""