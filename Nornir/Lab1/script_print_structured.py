from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

from nornir_scrapli.functions import print_structured_result

from nornir.core.filter import F

def custom_task(task):
    task.run(task=send_command, command="show ip interface brief")


def main():

    nr = InitNornir(config_file="config.yaml")

    results = nr.run(task=custom_task)
    print_structured_result(result=results, parser="textfsm")

    filtered_nr_1 = nr.filter(F(platform="ios"))
    results_1 = filtered_nr_1.run(task=custom_task)
    print_structured_result(result=results_1, parser="genie")


if __name__ == "__main__":
    main()