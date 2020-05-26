# by oran collins
# github.com/wisehackermonkey
# oranbusiness@gmail.com
# 20200526

import tkinter as tk
import __init__
window = tk.Tk()



greeting = tk.Label(text="Demo updating app:")
greeting.pack()

version_float = tk.StringVar()
version_float.set(__init__.__version__)
version = tk.Label(window, textvariable=version_float)
version.pack()
window.mainloop()