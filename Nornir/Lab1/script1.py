from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result



def custom_task(task):
    task.run(task=send_command, command="show ip interface brief")


def main():

    nr = InitNornir(config_file="config.yaml")

    results = nr.run(task=custom_task)
    print_result(results)


if __name__ == "__main__":
    main()