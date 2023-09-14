

from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
import socket


def app():
    root.geometry("350x450")
    root.resizable(False, False)
    entry.place(x=2,y=425)

    Button_start.place(x=270, y=425)
    Button_delete.place(x=270, y=400)

    root.mainloop()
def start_button():
    global entry_
    entry_text = entry.get()
    print(entry_text)
def delete_button():
    entry.delete(0, END)
def ip_user():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)


#vid
root= Tk()

entry = ttk.Entry(width=43)
Button_start = ttk.Button(root,text="start!",command=start_button)
Button_delete = ttk.Button(root,text="delete",command=delete_button)

app()
