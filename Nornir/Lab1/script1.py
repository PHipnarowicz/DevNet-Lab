from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result



def main():

    nr = InitNornir(config_file="config.yaml")

    results = nr.run(task=send_command, command="show ip interface brief")
    print_result(results)


if __name__ == "__main__":
    main()