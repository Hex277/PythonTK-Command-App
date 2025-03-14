import tkinter as tk


def on_entry_change(*args):
    current_text = entry_var.get()
    if not current_text.startswith(prefix):
        entry_var.set(prefix)


root = tk.Tk()

prefix = "Merhaba "
entry_var = tk.StringVar()
entry_var.set(prefix)
entry_var.trace_add("write", on_entry_change)

entry = tk.Entry(root, textvariable=entry_var)
entry.pack()

# Kullanıcının sadece "Merhaba " kısmından sonra yazmasına izin ver
entry.icursor(len(prefix))

root.mainloop()
