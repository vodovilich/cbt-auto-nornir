"""
to run venv in vscode terminal for windows launch the powershell as an administrator and enter the following command with the 'Y' confirmation:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine

And this is how to turn virtual environment on in vscode termnial:
.\my-venv\Scripts\ activate
deactivate
"""
from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result


nr = InitNornir(config_file="config.yaml")
results = nr.run(task=send_command, command="show clock")

print_result(results)

print("zato sto ti si peder") 


