from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

commands = input("\nEnter Your Commands: ")
cmds = commands.split(",")

def show_list(task):
  for cmd in cmds:
    task.run(task=send_command, command=cmd)
    
results = nr.run(task=show_list)
print_result(results)
