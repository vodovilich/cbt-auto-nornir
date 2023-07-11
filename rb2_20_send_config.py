from nornir import InitNornir
from nornir_scrapli.tasks import send_config
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def random_config(task):
#send one config command
 #   task.run(task=send_config, config="ntp server 1.1.1.1") - not cool, better use f-strings for substitution:
    task.run(task=send_config, config=f"ntp server {task.host['ntp_server']}")

results = nr.run(task=random_config)
print_result(results)