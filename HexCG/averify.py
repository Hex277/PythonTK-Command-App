import random
import string
import webbrowser
import pyautogui
import subprocess
import time
from matplotlib.figure import Figure
import requests
import os
import speedtest
from values import font_bg

user_ssid_name = ["None"]
wifi_passwords = ["Not found"]
app_name = ["\nApp is opening..."]
bitcoin_value = ["not found"]

x_values = []
y_values = []
fig = Figure(figsize=(7, 3), dpi=90)
fig.set_facecolor("#1f1f1f")
plot = fig.add_subplot(1, 1, 1)
plot.plot([], [])
plot.set_ylim(0, 1)


def btc_get():
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = response.json()
    bitcoin_val = float(data["bpi"]["USD"]["rate"].replace(",", ""))

    x_values.append(len(x_values) + 1)
    y_values.append(bitcoin_val)

    plot.clear()
    plot.set_facecolor("#0f0f0f")
    plot.spines['top'].set_color(font_bg)
    plot.spines['bottom'].set_color(font_bg)
    plot.spines['left'].set_color(font_bg)
    plot.spines['right'].set_color(font_bg)
    plot.tick_params(axis='x', colors='green')
    plot.tick_params(axis='y', colors='green')
    plot.plot(x_values, y_values)
    plot.set_ylim(min(y_values) * 0.95, max(y_values) * 1.05)

    plot.text(x_values[-1], y_values[-1], f"${bitcoin_val:.2f}", fontsize=10, ha='right', va='bottom',
              color='green')


def get_bitcoin_value():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        bitcoin_price = data['bitcoin']['usd']
        bitcoin_value.append(bitcoin_price)
    else:
        bitcoin_value.append("not found")


def open_app():
    app = app_name[-1]
    # WEB
    if app == "chrome":
        webbrowser.open_new_tab("https://www.google.com/")
        app_name.append("\nApp is opening...")
    elif app == "youtube":
        webbrowser.open_new_tab("https://youtube.com/")
        app_name.append("\nApp is opening...")
    elif app == "youtube studio":
        webbrowser.open_new_tab("https://studio.youtube.com/")
        app_name.append("\nApp is opening...")
    elif app == "gpt":
        webbrowser.open_new_tab("https://chatgpt.com/")
        app_name.append("\nApp is opening...")
    # Local APPS
    elif app == "note" or app == "notepad":
        subprocess.Popen(['notepad.exe'])
        app_name.append("\nApp is opening...")
    elif app == "optimizator":
        subprocess.Popen(["C:\\Users\\user\\Desktop\\optimizator.exe"])
        app_name.append("\nApp is opening...")
    elif app == "cmd":
        os.system("start cmd")
        app_name.append("\nApp is opening...")
    else:
        app_name.append("\nApp is not found")

d_speed = [""]
u_speed = [""]


def test_internet_speed():
    try:
        st = speedtest.Speedtest()
        download_speed = st.download() / 1000000
        upload_speed = st.upload() / 1000000
        d_speed.append(download_speed)
        u_speed.append(upload_speed)

    except speedtest.SpeedtestException as e:
        d_speed.append("Error")
        u_speed.append("Error")


def get_wifi_password():
    ssid_name = user_ssid_name[-1]
    command = f"netsh wlan show profile name={ssid_name} key=clear"
    try:
        result = subprocess.check_output(command, shell=True)
        res = result.decode("utf-8")
        lines = res.split("\n")

        for line in lines:
            if "Key Content" in line:
                password = line.split(":")[1].strip()
                wifi_passwords.append(password)

        if wifi_passwords[-1] == "Not found":
            wifi_passwords.append("not found\nModem has enabled security or has been set to hidden.")

    except subprocess.CalledProcessError:
        wifi_passwords.append("not found\nYou can only get passwords for connected networks.")


def auto_fill(auto_fill_box):
    time.sleep(10)
    user_text = auto_fill_box.get("1.0", "end-1c")
    pyautogui.typewrite(user_text, interval=0.1)


def auto_verify(nod_value, type_value, digits_value, atime_value, row_value, case_value):
    random_codes = []

    def start_typewrite(code):
        time.sleep(av_time)
        pyautogui.hotkey("ctrl", "a")
        pyautogui.press("backspace")
        pyautogui.typewrite(code)
        pyautogui.press("enter")

    nod = int(nod_value.get())
    u_type = type_value.get()
    count = int(digits_value.get())
    av_time = int(atime_value.get())
    row = row_value.get()
    case = case_value.get()
    time.sleep(10)

    if u_type == "Numbers":
        if row == "Random":
            for _ in range(count):
                random_code = ''.join([str(random.randint(0, 9)) for _ in range(nod)])
                random_codes.append(random_code)
                start_typewrite(random_code)
        elif row == "0 to N":
            start_number = int("1" + "0" * (nod - 1))
            for i in range(count):
                random_code = start_number + i
                random_codes.append(random_code)
                start_typewrite(str(random_code))
    elif u_type == "Letters":
        if case == "Low and Up":
            for _ in range(count):
                random_code = ''.join(random.choice(string.ascii_letters) for _ in range(nod))
                random_codes.append(random_code)
                start_typewrite(random_code)
        elif case == "Lowercase":
            for _ in range(count):
                random_code = ''.join(random.choice(string.ascii_letters.lower()) for _ in range(nod))
                random_codes.append(random_code)
                start_typewrite(random_code)
        elif case == "Uppercase":
            for _ in range(count):
                random_code = ''.join(random.choice(string.ascii_letters.upper()) for _ in range(nod))
                random_codes.append(random_code)
                start_typewrite(random_code)
    elif u_type == "Nums and Ltrs":
        if case == "Low and Up":
            for _ in range(count):
                characters = string.ascii_letters + string.digits
                random_code = ''.join(random.choice(characters) for _ in range(nod))
                random_codes.append(random_code)
                start_typewrite(random_code)
        elif case == "Lowercase":
            for _ in range(count):
                characters = string.ascii_letters.lower() + string.digits
                random_code = ''.join(random.choice(characters) for _ in range(nod))
                random_codes.append(random_code)
                start_typewrite(random_code)
        elif case == "Uppercase":
            for _ in range(count):
                characters = string.ascii_letters.upper() + string.digits
                random_code = ''.join(random.choice(characters) for _ in range(nod))
                random_codes.append(random_code)
                start_typewrite(random_code)
