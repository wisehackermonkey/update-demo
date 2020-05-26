# by oran collins
# github.com/wisehackermonkey
# oranbusiness@gmail.com
# 20200526

import tkinter as tk
from client_config import ClientConfig
from update import check_for_update
import pkg_resources.py2_warn
window = tk.Tk()

# todo unzip downloaded file to location of exe 

greeting = tk.Label(text="Demo updating app: 2")
greeting.pack()
greeting2 = tk.Label(text="this allows for autoudates!_2222")
greeting2.pack()

version_float = tk.StringVar()
version_float.set(ClientConfig.APP_VERSION)
version = tk.Label(window, textvariable=version_float)
version.pack()

update_button = tk.Button(window, text="Update",command=check_for_update)
update_button.pack()
window.mainloop()