import tkinter as tk
from tkinter import ttk
import Menubar
import Ribbon
import LeftPane

username = 'skr47ch'

class AppWindow(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.root = root

        Menubar.Menubar(root)
        Ribbon.Ribbon(root)
        LeftPane.LeftPane(root)



if __name__ == '__main__':
    root = tk.Tk()
    root.title(f'NiseTaiga - {username}')
    root.minsize(500, 300)
    AppWindow(root)
    root.mainloop()





