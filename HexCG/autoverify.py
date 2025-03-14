import subprocess


def get_wifi_password():
    command = "netsh wlan show profile name=Wifi. key=clear"
    result = subprocess.check_output(command)
    res = result.decode("utf-8")
    lines = res.split("\n")
    for line in lines:
        if "Key Content" in line:
            password = line.split(":")[1].strip()
            print("Password:", password)


get_wifi_password()
