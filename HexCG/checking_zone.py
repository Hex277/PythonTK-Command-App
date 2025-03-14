import tkinter as tk
import customtkinter
import pyautogui
from values import wind_bg, wind_bg2, pt_main, npt_main, font_bg

cnt = 0
help_tools = "\nFor more information on a specific command:" \
             "\nCLEAR (cl)                   Clears the command screen" \
             "\nCD (cd)                      Displays the Name" \
             "\nDESTROY (d)                  Closes the program"


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


wind = customtkinter.CTk()
wind.after(0, lambda: wind.state('zoomed'))
wind.title("CustomTkinter Test")
wind.config(bg=wind_bg)
mainFrame = customtkinter.CTkFrame(master=wind, fg_color=wind_bg)
mainFrame.after(0, lambda: wind.state('zoomed'))
mainFrame.pack(fill=tk.BOTH, expand=True)
second_frame = customtkinter.CTkFrame(master=mainFrame, height=670, width=1300, fg_color=font_bg)
second_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
mFrame = customtkinter.CTkFrame(master=second_frame, height=660, width=1290, fg_color=wind_bg)
mFrame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

cp = customtkinter.CTkTextbox(master=mFrame, height=410, width=650, font=("Courier New", 14), fg_color=wind_bg2,
                              text_color=font_bg)
cp.place(relx=0.01, rely=0.01)
infoEntry = "Tools Hex [version: 1.0.0, started 01.04.24]\n(c) HexCodeGroup Corporation. All rights " \
            "reserved.\n\nhex-user> "
cp.insert("end", infoEntry)
cp.bind("<Return>", on_enter)

wind.mainloop()
