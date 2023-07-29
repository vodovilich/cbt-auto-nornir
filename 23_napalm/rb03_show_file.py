from nornir import InitNornir
from nornir_scrapli.tasks import send_configs_from_file
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")


def push_conf_file(task):
  task.run(task=send_configs_from_file, file="rb03_commands.txt")
    
results = nr.run(task=push_conf_file)
print_result(results)