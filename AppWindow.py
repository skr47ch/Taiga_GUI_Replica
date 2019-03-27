import tkinter as tk
import Menubar
import Ribbon
import LeftPane
import Tabs

username = 'skr47ch'

class AppWindow(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.root = root

        Menubar.Menubar(root)
        Ribbon.Ribbon(root)
        Tabs.Tabs(root)
        LeftPane.LeftPane(root)

if __name__ == '__main__':
    root = tk.Tk()
    root.title(f'NiseTaiga - {username}')
    root.minsize(1000, 500)
    AppWindow(root)
    root.mainloop()





