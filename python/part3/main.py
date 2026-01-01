from modules.save_running_config import save_running_config
from modules.save_output import save_output
from modules.send_command import send_command

def main():
    output = []
    device_config = send_command("show running-config brief")
    output.append(send_command("show ip interface brief"))
    output.append(send_command("show arp"))

    save_output(output)
    save_running_config(device_config)

main()