from nornir import InitNornir
from nornir_scrapli.tasks import send_config
from nornir_utils.plugins.functions import print_result
#sends ONE config command
nr = InitNornir(config_file="config.yaml")

def send_config_test(task):
    task.run(task=send_config, config = "logging buffer 23456")
results = nr.run(task=send_config_test)
print_result(results)

