import getpass
from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")
passwrd = getpass.getpass()
nr.inventory.defaults.password = passwrd
#THIS REQUIRES TO COMMENT groups.yaml->cisco_group->password line

def credential_test(task):
    task.run(task=send_command, command="show ip int br")
    
results = nr.run(task=credential_test)
print_result(results)