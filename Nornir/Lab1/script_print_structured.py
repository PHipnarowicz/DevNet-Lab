from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

from nornir_scrapli.functions import print_structured_result

from nornir.core.filter import F

from pprint import pp


def custom_task_1(task):
    task.run(task=send_command, command="show ip interface brief")


def custom_task_2(task):
    show_version_results = task.run(task=send_command, command="show version")
    task.host["facts"] = show_version_results.scrapli_response.textfsm_parse_output()
    pp(task.host["facts"])


def custom_task_3(task):
    show_version_results = task.run(task=send_command, command="show version")
    task.host["facts"] = show_version_results.scrapli_response.genie_parse_output()
    pp(task.host["facts"])


def main():

    nr = InitNornir(config_file="config.yaml")

    results = nr.run(task=custom_task_1, name="Filtrowanie TextFSM dla IOS i EOS")
    print_structured_result(result=results, parser="textfsm")

    filtered_nr_1 = nr.filter(F(platform="ios"))
    results_1 = filtered_nr_1.run(task=custom_task_1, name="Filtrowanie Genie dla IOS")
    print_structured_result(result=results_1, parser="genie")

    filtered_nr_2 = nr.filter(F(platform="eos"))
    results_2 = filtered_nr_2.run(task=custom_task_1, name="Filtrowanie Genie dla EOS")
    print_structured_result(result=results_2, parser="genie")

    nr.run(task=custom_task_2, name="Filtrowanie TextFSM dla IOS i EOS")

    filtered_nr_1 = nr.filter(F(platform="ios"))
    filtered_nr_1.run(task=custom_task_3, name="Filtrowanie Genie dla IOS")

    iltered_nr_2 = nr.filter(F(platform="eos"))
    filtered_nr_2.run(task=custom_task_3, name="Filtrowanie Genie dla EOS")

if __name__ == "__main__":
    main()