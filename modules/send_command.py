from netmiko import ConnectHandler
def send_command(command):
    ssh_cli = ConnectHandler(
            device_type="cisco_ios",
            host="10.176.161.15",
            port="22",
            username="jan",
            password="jand",
            secret=""
        )
    return ssh_cli.send_command(command)