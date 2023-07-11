from nornir import InitNornir
from nornir_scrapli.tasks import send_configs
from nornir_utils.plugins.functions import print_result
#sends MANY config commands
nr = InitNornir(config_file="config.yaml")

def send_configs_test(task):
    task.run(task=send_configs, configs = ["logging buffer 12345", "ntp server 1.2.3.4"])
results = nr.run(task=send_configs_test)
print_result(results)

