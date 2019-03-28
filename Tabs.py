import tkinter as tk
from tkinter import ttk
import DisplayPanedWindow

_bgcolor = 'white'  # X11 color: #f5deb3

class Tabs(tk.Frame):
    def __init__(self, cont):
        tk.Frame.__init__(self, cont)

        self.frame = ttk.Frame(cont)
        self.frame.place(x=150, y=35, relwidth=1, relheight=0.90)

        notebook = ttk.Notebook(self.frame)

        self.tab_currently_watching = ttk.Frame(notebook)
        notebook.add(self.tab_currently_watching,  text='Currently Watching (0)')

        self.tab_completed = ttk.Frame(notebook)
        notebook.add(self.tab_completed, text='Completed (0)')
        # DisplayPanedWindow.DisplayPanedWindow(self.tab_completed)

        self.tab_on_hold = ttk.Frame(notebook)
        notebook.add(self.tab_on_hold, text='On Hold (0)')
        # DisplayPanedWindow.DisplayPanedWindow(self.tab_on_hold)

        self.tab_dropped = ttk.Frame(notebook)
        notebook.add(self.tab_dropped, text='Dropped (0)')
        # DisplayPanedWindow.DisplayPanedWindow(self.tab_dropped)

        self.tab_plan_to_watch = ttk.Frame(notebook)
        notebook.add(self.tab_plan_to_watch, text='Plan to Watch (0)')
        # DisplayPanedWindow.DisplayPanedWindow(self.tab_plan_to_watch)

        notebook.place(relwidth=1, relheight=1)

        d1 = DisplayPanedWindow.DisplayPanedWindow(self.tab_currently_watching)
        d1.add_entry('Mushishi', '30/34', '10', 'Anime', 'Summer 2010', 20)
        d1.add_entry('Mushishi', '30/34', '10', 'Anime', 'Summer 2010', 50)
        d1.add_entry('Mushishi', '30/34', '10', 'Anime', 'Summer 2010', 90)

        f1 = DisplayPanedWindow.DisplayPanedWindow(self.tab_plan_to_watch)
        f1.add_entry('Mushishi', '30/34', '10', 'Anime', 'Summer 2010', 30)
        f1.add_entry('Mushishi2', '30/34', '10', 'Anime', 'Summer 2010', 50)

if __name__ == '__main__':
    root = tk.Tk()
    root.title(f'NiseTaiga')
    root.minsize(1000, 500)
    Tabs(root)


    root.mainloop()