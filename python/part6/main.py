import json
import requests

# Disable SSL warnings
requests.packages.urllib3.disable_warnings()

# -----------------------------
# Configuration
# -----------------------------
device_ip = "192.168.129.149"
username = "cisco"
password = "cisco123!"
basicauth = (username, password)

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

# -----------------------------
# Part 1: GET request - list interfaces
# -----------------------------
get_url = f"https://{device_ip}/restconf/data/ietf-interfaces:interfaces"

resp_get = requests.get(get_url, auth=basicauth, headers=headers, verify=False)
print("GET Request Response Code:", resp_get.status_code)

if resp_get.status_code == 200:
    interfaces = resp_get.json()
    print("Current Interfaces:")
    print(json.dumps(interfaces, indent=4))
else:
    print("Error GETting interfaces:", resp_get.text)

# -----------------------------
# Part 2: PUT request - create Loopback2
# -----------------------------
put_url = f"https://{device_ip}/restconf/data/ietf-interfaces:interfaces/interface=Loopback2"

yang_payload = {
    "ietf-interfaces:interface": {
        "name": "Loopback2",
        "description": "Configured via Python RESTCONF",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "10.2.1.1",
                    "netmask": "255.255.255.0"
                }
            ]
        },
        "ietf-ip:ipv6": {}
    }
}

resp_put = requests.put(
    put_url,
    auth=basicauth,
    headers=headers,
    data=json.dumps(yang_payload),
    verify=False
)

if 200 <= resp_put.status_code <= 299:
    print(f"PUT Request Successful: {resp_put.status_code}")
else:
    print(f"PUT Request Failed: {resp_put.status_code}")
    try:
        print(json.dumps(resp_put.json(), indent=4))
    except Exception:
        print(resp_put.text)
