import tkinter as tk
from tkinter import ttk
import DisplayTable
import MAL_API

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
        for item in MAL_API.watching:
            current_list.insert_new([item['anime_airing_status'],
                    item['anime_title'],
                    str(item['num_watched_episodes']) + "/" + str(item['anime_num_episodes']),
                    item['score'],
                    item['anime_media_type_string'],
                    item['anime_start_date_string']])

        for item in MAL_API.completed:
            completed_list.insert_new([item['anime_airing_status'],
                    item['anime_title'],
                    str(item['num_watched_episodes']) + "/" + str(item['anime_num_episodes']),
                    item['score'],
                    item['anime_media_type_string'],
                    item['anime_start_date_string']])


if __name__ == '__main__':
    root = tk.Tk()
    root.title(f'NiseTaiga')
    root.minsize(1000, 500)
    Tabs(root)
    root.mainloop()