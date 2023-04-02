from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

command_list = ["show run | i ^host", "show ver | i IOS", "show cdp neig",]

def show_command_test(task):
    for cmd in command_list:
        task.run(task=send_command, command=cmd)
results = nr.run(task=show_command_test)
print_result(results)
