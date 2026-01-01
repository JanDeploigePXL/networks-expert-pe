import datetime
def save_output(output):
    datetimestring = str(datetime.datetime.now())
    with open("saved_outputs/" + datetimestring + '.txt', 'w') as file:
        for output_item in output:
            print("="*60)
            for line in output_item.splitlines():
                print(line.strip())
                file.write(line.strip() + "\n")