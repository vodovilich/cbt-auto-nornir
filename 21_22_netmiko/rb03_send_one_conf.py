from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_config
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")


def another_config_test(task):
    task.run(task=netmiko_send_config, config_commands=["logging buffer 45678", "ntp server 3.4.5.6"])

results = nr.run(task=another_config_test)
print_result(results)