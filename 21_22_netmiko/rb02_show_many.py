from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")
command_list = ["sh run | i hostname", "show run | i logging buff", "sh ip int br"]
def another_show_command(task):
    for cmd in command_list:
        task.run(task=netmiko_send_command, command_string=cmd)

results = nr.run(task=another_show_command)
print_result(results)