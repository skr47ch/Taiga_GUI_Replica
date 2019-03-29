import tkinter as tk
from tkinter import ttk
import DisplayTable

_bgcolor = 'white'  # X11 color: #f5deb3

class Tabs(tk.Frame):
    def __init__(self, cont):
        tk.Frame.__init__(self, cont)

        self.frame = ttk.Frame(cont)
        self.frame.place(x=150, y=35, relwidth=1, relheight=0.90)

        notebook = ttk.Notebook(self.frame)

        self.tab_currently_watching = ttk.Frame(notebook)
        self.tab_completed = ttk.Frame(notebook)
        self.tab_on_hold = ttk.Frame(notebook)
        self.tab_dropped = ttk.Frame(notebook)
        self.tab_plan_to_watch = ttk.Frame(notebook)

        notebook.add(self.tab_currently_watching,  text='Currently Watching (0)')
        notebook.add(self.tab_completed, text='Completed (0)')
        notebook.add(self.tab_on_hold, text='On Hold (0)')
        notebook.add(self.tab_dropped, text='Dropped (0)')
        notebook.add(self.tab_plan_to_watch, text='Plan to Watch (0)')

        current_list = DisplayTable.DisplayTable(self.tab_currently_watching)
        completed_list = DisplayTable.DisplayTable(self.tab_completed)
        hold_list = DisplayTable.DisplayTable(self.tab_on_hold)
        dropped_list = DisplayTable.DisplayTable(self.tab_dropped)
        planned_list = DisplayTable.DisplayTable(self.tab_plan_to_watch)

        notebook.pack(fill='both', expand=True)

        # test data
        current_list.insert_new(['', 'Mushishi', '30/34', '10', 'Anime', 'Summer 2010'])
        current_list.insert_new(['', 'Haikyuu', '65/70', '9', 'Anime', 'Spring 2001'])
        current_list.insert_new(['', 'Deathnote', '1/2', '8.5', 'Movie', 'Summer 2012'])

        completed_list.insert_new(['', 'Hikaru no Go', '22/22', '9', 'Anime', 'Spring 2011'])
        completed_list.insert_new(['', 'Hunter X Hunter', '340/340', '8.5', 'Anime', 'Fall 2012'])

if __name__ == '__main__':
    root = tk.Tk()
    root.title(f'NiseTaiga')
    root.minsize(1000, 500)
    Tabs(root)
    root.mainloop()