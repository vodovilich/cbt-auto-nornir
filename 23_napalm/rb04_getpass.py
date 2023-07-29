import sys
import getpass
from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

"""
WHEN YOU HAVE PASSWORD ON DEVICE, BUT NOT IN YAMLs:
IF THERE IS PASSWORD IN GROUPS FILE => works regardless of what you enter
passwrd = getpass.getpass()
nr.inventory.defaults.password = passwrd
THIS REQUIRES TO COMMENT groups.yaml->cisco_group->password line
"""


#HERE IS WHEN configured password differs from in configuration
# DO NOT DO THIS IT WONT WORK AND FUCK IT just go on
usa_pass = getpass.getpass(prompt="\nEnter USA GROUP password: ")
euro_pass = getpass.getpass(prompt="\nEnter EURO GROUP password: ")
iol_01_pass = getpass.getpass(prompt="\nEnter iol-01 HOST password: ")


nr.inventory.groups["usa_group"].password = usa_pass
nr.inventory.groups["euro_group"].password = euro_pass
nr.inventory.hosts["iol-01"].password = iol_01_pass
nr.inventory.defaults.username = sys.argv[1]

def credential_test(task):
    task.run(task=send_command, command="show ip int br")
    
results = nr.run(task=credential_test)
print_result(results)

