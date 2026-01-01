import datetime
def save_running_config(device_config):
    datetimestring = str(datetime.datetime.now())
    with open("saved_outputs/" + 'running-config-' + datetimestring + ".txt", 'w') as file:
        for line in device_config.splitlines():
            file.write(line.strip() + "\n")