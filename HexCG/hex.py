import tkinter as tk
import customtkinter
import datetime
from time import strftime
import pyautogui
from values import wind_bg, wind_bg2, error_font_bg, pt_main, npt_main, help_tools, help_tools_az
from averify import auto_fill, auto_verify, get_wifi_password, user_ssid_name, wifi_passwords, app_name, open_app, \
    fig, btc_get, get_bitcoin_value, bitcoin_value, u_speed, d_speed, test_internet_speed
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading
from values import font_bg
import time

cnt = 0

ock = datetime.datetime.now()
clock = ock.strftime("%H%M")
customtkinter.set_appearance_mode("Dark")


def on_enter(event):
    prompt_text = pt_main[-1]
    n_prompt_text = npt_main[-1]
    raw_command = cp.get("1.0", tk.END)
    command = raw_command.split(prompt_text)
    last_command = command[-1].strip().lower()
    if last_command == "help":
        cp.insert("end", help_tools)
        cp.insert("end", n_prompt_text)
        cp.see("end")
        pyautogui.press("backspace")
    elif last_command.startswith("help az"):
        cp.insert("end", help_tools_az)
        cp.insert("end", n_prompt_text)
        cp.see("end")
        pyautogui.press("backspace")
    elif not last_command or last_command == "hex-user>":
        cp.insert("end", n_prompt_text)
        cp.see("end")
        pyautogui.press("backspace")
    elif last_command.startswith("clean") or last_command.startswith("cl"):
        cp.delete("1.0", tk.END)
        cp.insert("end", prompt_text)
        pyautogui.press("backspace")
        cp.see("end")
    elif last_command == "d" or last_command.startswith("destroy"):
        wind.destroy()
    elif last_command.startswith("afill") or last_command.startswith("auto fill"):
        text_field_txt.place(rely=0.051, relx=0.525)
        auto_fill_box.place(rely=0.11, relx=0.525)
        cp.insert("end", "\nCopy your text into the TEXT FIELD and type the 'start af' command."
                         "\nthe process will begin in 10 seconds.")
        cp.insert("end", n_prompt_text)
        cp.see("end")
        pyautogui.press("backspace")
    elif last_command.startswith("start afill") or last_command.startswith("start af"):
        auto_fill(auto_fill_box)
        cp.insert("end", n_prompt_text)
        cp.see("end")
        pyautogui.press("backspace")
    elif last_command.startswith("remove afill") or last_command.startswith("remove af"):
        text_field_txt.place_forget()
        auto_fill_box.place_forget()
        cp.insert("end", n_prompt_text)
        cp.see("end")
        pyautogui.press("backspace")
    elif last_command.startswith("averify") or last_command.startswith("auto verify"):
        cp.insert("end", "\nFill fields and type the 'start av' command."
                         "\nThe process will begin in 10 seconds.")
        cp.insert("end", n_prompt_text)
        cp.see("end")
        pyautogui.press("backspace")
        auto_verify_assets()
    elif last_command.startswith("remove averify") or last_command.startswith("remove av"):
        remove_av()
        cp.insert("end", n_prompt_text)
        cp.see("end")
        pyautogui.press("backspace")
    elif last_command.startswith("start av"):
        auto_verify(nod_value, type_value, digits_value, atime_value, row_value, case_value)
        cp.insert("end", n_prompt_text)
        cp.see("end")
        pyautogui.press("backspace")
    elif last_command == "bitcoin" or last_command == "bitcoin value":
        get_bitcoin_value()
        canvas.get_tk_widget().place(relx=0.76, rely=0.8, anchor=tk.CENTER)
        bitcoin_thread.start()
        cp.insert("end", f"\nBitcoin value is {bitcoin_value[-1]}$")
        cp.insert("end", n_prompt_text)
        cp.see("end")
        pyautogui.press("backspace")
    elif last_command == "remove bitcoin" or last_command == "remove btc":
        canvas.get_tk_widget().destroy()
        cp.insert("end", n_prompt_text)
        cp.see("end")
        pyautogui.press("backspace")
    elif "enter ssid name>" in last_command:
        name_wifi = last_command.split("enter ssid name>")
        user_ssid_name.append(name_wifi[1].strip())
        get_wifi_password()
        cp.insert("end", f"\nPassword is `{wifi_passwords[-1]}`\nType 'SPEED TEST' to test")
        cp.insert("end", n_prompt_text)
        pyautogui.press("backspace")
        cp.see("end")
    elif last_command == "speedtest" or last_command == "speed test":
        test_internet_speed()
        cp.insert("end", f"\nDownload speed:{d_speed[-1]} Mbps\nUpload speed:{u_speed[-1]} Mbps")
        cp.insert("end", n_prompt_text)
        pyautogui.press("backspace")
        cp.see("end")
    elif "open" in last_command:
        name_app = last_command.split("open")
        app_name.append(name_app[1].strip())
        open_app()
        cp.insert("end", app_name[-1])
        cp.insert("end", n_prompt_text)
        pyautogui.press("backspace")
        cp.see("end")
    elif last_command.startswith("get wifi password") or last_command == "wp":
        cp.insert("end", "\nEnter SSID name> ")
        pyautogui.press("backspace")
        cp.see("end")
    elif last_command.startswith("cd"):
        before_splited = last_command.split("cd")
        user_cd = before_splited[1].strip()
        npt_main.append("\n" + user_cd + "> ")
        pt_main.append(user_cd + "> ")
        cp.insert("end", "\n" + user_cd + "> ")
        pyautogui.press("backspace")
        cp.see("end")
    else:
        cp.insert("end", f"\n`{last_command}` is an undefined command.")
        cp.insert("end", n_prompt_text)
        cp.see("end")
        pyautogui.press("backspace")


def toggle_fullscreen(event=None):
    state = not wind.attributes('-fullscreen')
    wind.attributes('-fullscreen', state)


def auto_verify_assets():
    base_y_position = 0.65

    nod_text.place(relx=0.04, rely=base_y_position)
    nod_value.place(relx=0.44, rely=base_y_position + 0.024, anchor=tk.CENTER)

    type_text.place(relx=0.04, rely=base_y_position + 0.05)
    type_value.place(relx=0.365, rely=base_y_position + 0.054)

    number_digits_text.place(relx=0.04, rely=base_y_position + 0.10)
    digits_value.place(relx=0.44, rely=base_y_position + 0.127, anchor=tk.CENTER)

    avarage_time_text.place(relx=0.04, rely=base_y_position + 0.15)
    atime_value.place(relx=0.44, rely=base_y_position + 0.18, anchor=tk.CENTER)

    row_text.place(relx=0.04, rely=base_y_position + 0.20)
    row_value.place(relx=0.44, rely=base_y_position + 0.23, anchor=tk.CENTER)

    case_text.place(relx=0.04, rely=base_y_position + 0.25)
    case_value.place(relx=0.44, rely=base_y_position + 0.28, anchor=tk.CENTER)


def time_refresh():
    now = strftime('%H:%M %p')
    ocklock.configure(text=now)
    wind.after(1000, time_refresh)


def get_bitcoin():
    while True:
        btc_get()
        canvas.draw()

        time.sleep(30)


def enterance(event):
    global cnt
    psw = user_input.get()
    okl = datetime.datetime.now()
    value_okl = okl.strftime("%H%M")
    if psw == value_okl:
        if cnt == 0:
            pass
        else:
            error.destroy()
        mainFrame.pack(fill=tk.BOTH, expand=True)
    elif cnt == 3:
        wind.destroy()
    else:
        error.place(relx=0.5, rely=0.68, anchor=tk.CENTER)
        cnt += 1


def remove_av():
    nod_text.place_forget()
    nod_value.place_forget()
    type_text.place_forget()
    type_value.place_forget()
    number_digits_text.place_forget()
    digits_value.place_forget()
    avarage_time_text.place_forget()
    atime_value.place_forget()
    row_text.place_forget()
    row_value.place_forget()
    case_text.place_forget()
    case_value.place_forget()


def focus_entry(event=None):
    user_input.focus_set()


wind = customtkinter.CTk()
wind.after(0, lambda: wind.state('zoomed'))
wind.title("CustomTkinter Test")
wind.config(bg=wind_bg)
wind.focus_set()
wind.bind("<F11>", toggle_fullscreen)
wind.bind("<Escape>", toggle_fullscreen)
# Enterance Assets
ocklock = customtkinter.CTkLabel(master=wind, height=25, width=150,
                                 fg_color=wind_bg, bg_color=wind_bg,
                                 text_color=font_bg, font=("Courier New", 15))
ocklock.place(relx=0.97, rely=0.01, anchor=tk.CENTER)
time_refresh()
version_text = customtkinter.CTkLabel(master=wind, height=25, width=150, text="Version: 1.0.0",
                                      fg_color=wind_bg, bg_color=wind_bg,
                                      text_color=font_bg, font=("helvectica", 10))
version_text.place(relx=0.03, rely=0.01, anchor=tk.CENTER)
entpwd_text = customtkinter.CTkLabel(master=wind, height=25, width=150, text="Enter Security Password",
                                     fg_color=wind_bg,
                                     text_color=font_bg, font=("helvectica", 30))
entpwd_text.place(relx=0.5, rely=0.41, anchor=tk.CENTER)
user_input = customtkinter.CTkEntry(master=wind, width=130, height=20, text_color=font_bg, fg_color=wind_bg2,
                                    font=("helvectica", 25), justify="center")
user_input.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
user_input.bind("<Return>", enterance)
user_input.bind("<Map>", focus_entry)

submit = customtkinter.CTkButton(master=wind, corner_radius=10, text="Submit", text_color=font_bg, fg_color=wind_bg,
                                 font=("helvectica", 30), hover_color=wind_bg2, bg_color=wind_bg,
                                 command=lambda: enterance(None))

submit.place(relx=0.5, rely=0.59, anchor=tk.CENTER)
error = customtkinter.CTkLabel(master=wind, height=25, width=150, text="Password is incorrect",
                               fg_color=wind_bg,
                               text_color=error_font_bg, font=("helvectica", 25))
# MainPage Assets
mainFrame = customtkinter.CTkFrame(master=wind, fg_color=wind_bg)
mainFrame.after(0, lambda: wind.state('zoomed'))
second_frame = customtkinter.CTkFrame(master=mainFrame, height=670, width=1300, fg_color=font_bg)
second_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
mFrame = customtkinter.CTkFrame(master=second_frame, height=660, width=1290, fg_color=wind_bg)
mFrame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
wind.after(100, lambda: user_input.focus_set())
# Command Prompt
cp = customtkinter.CTkTextbox(master=mFrame, height=410, width=650, font=("Courier New", 14), fg_color=wind_bg2,
                              text_color=font_bg)
cp.place(relx=0.01, rely=0.015)

infoEntry = "Tools Hex [version: 1.0.0, started 01.04.24]\n(c) HexCodeGroup Corporation. All rights " \
            "reserved.\n\nhex-user> "
cp.insert("end", infoEntry)
cp.bind("<Return>", on_enter)
# AUTO TEXT FIELD
text_field_txt = customtkinter.CTkLabel(master=wind, height=25, width=600, text="TEXT FIELD",
                                        fg_color=wind_bg,
                                        text_color=font_bg, font=("Courier New", 30))
auto_fill_box = customtkinter.CTkTextbox(master=wind, height=366, width=600, font=("Courier New", 14),
                                         fg_color=wind_bg2,
                                         text_color="white")
# AUTO VERIFY
nod_text = customtkinter.CTkLabel(master=wind, fg_color=wind_bg, text_color=font_bg, height=30, width=100,
                                  text="Number of characters:", font=("courier new", 20))
nod_value = customtkinter.CTkEntry(master=wind, width=80, height=20, text_color=font_bg, fg_color=wind_bg,
                                   font=("helvectica", 20), justify="center")
type_text = customtkinter.CTkLabel(master=wind, fg_color=wind_bg, text_color=font_bg, height=30, width=100,
                                   text="Select type:", font=("courier new", 20))
options = ["Numbers", "Letters", "Nums and Ltrs"]
type_value = customtkinter.CTkComboBox(master=wind, fg_color=wind_bg, text_color=font_bg, height=30, width=200,
                                       font=("courier new", 20), values=options)
number_digits_text = customtkinter.CTkLabel(master=wind, fg_color=wind_bg, text_color=font_bg, height=30, width=100,
                                            text="Loop times:", font=("courier new", 20))
digits_value = customtkinter.CTkEntry(master=wind, width=80, height=20, text_color=font_bg, fg_color=wind_bg,
                                      font=("helvectica", 20), justify="center")
digits_value.insert("end", 1)
avarage_time_text = customtkinter.CTkLabel(master=wind, fg_color=wind_bg, text_color=font_bg, height=30, width=100,
                                           text="Avarage time:", font=("courier new", 20))
atime_value = customtkinter.CTkEntry(master=wind, width=80, height=20, text_color=font_bg, fg_color=wind_bg,
                                     font=("helvectica", 20), justify="center")
atime_value.insert("end", 1)
row_text = customtkinter.CTkLabel(master=wind, fg_color=wind_bg, text_color=font_bg, height=30, width=100,
                                  text="Select type:", font=("courier new", 20))
options2 = ["Random", "0 to N"]
row_value = customtkinter.CTkComboBox(master=wind, fg_color=wind_bg, text_color=font_bg, height=30, width=200,
                                      font=("courier new", 20), values=options2)
case_text = customtkinter.CTkLabel(master=wind, fg_color=wind_bg, text_color=font_bg, height=30, width=100,
                                   text="Text size: ", font=("courier new", 20))
options3 = ["Low and Up", "Lowercase", "Uppercase"]
case_value = customtkinter.CTkComboBox(master=wind, fg_color=wind_bg, text_color=font_bg, height=30, width=200,
                                       font=("courier new", 20), values=options3)
# BITCOIN VALUE
canvas = FigureCanvasTkAgg(fig, master=mFrame)
canvas.draw()
bitcoin_thread = threading.Thread(target=get_bitcoin)
bitcoin_thread.daemon = True

wind.mainloop()
