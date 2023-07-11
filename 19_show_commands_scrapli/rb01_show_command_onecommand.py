from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def show_command_test(task):
    task.run(task=send_command, command="sh run | i logging buf")

results = nr.run(task=show_command_test)
print_result(results)