from unicodedata import name
from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

from nornir.core.filter import F

def custom_task(task):
    task.run(task=send_command, command="show ip interface brief")


def main():

    nr = InitNornir(config_file="config.yaml")

    filtered_nr_1 = nr.filter(name="R1")
    results_1 = filtered_nr_1.run(task=custom_task)
    print_result(results_1)

    filtered_nr_2 = nr.filter(F(platform="eos"))
    results_2 = filtered_nr_2.run(task=custom_task)
    print_result(results_2)

    filtered_nr_3 = nr.filter(F(platform="eos") & F(name="R3"))
    results_3 = filtered_nr_3.run(task=custom_task)
    print_result(results_3)

if __name__ == "__main__":
    main()