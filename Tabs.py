import tkinter as tk
from tkinter import ttk
import DisplayTable
import Jikan

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

        notebook.add(self.tab_currently_watching,  text=f'Currently Watching ({len(Jikan.watching)})')
        notebook.add(self.tab_completed, text=f'Completed ({len(Jikan.completed)})')
        notebook.add(self.tab_on_hold, text='On Hold (0)')
        notebook.add(self.tab_dropped, text='Dropped (0)')
        notebook.add(self.tab_plan_to_watch, text='Plan to Watch (0)')

        current_list = DisplayTable.DisplayTable(self.tab_currently_watching)
        completed_list = DisplayTable.DisplayTable(self.tab_completed)
        hold_list = DisplayTable.DisplayTable(self.tab_on_hold)
        dropped_list = DisplayTable.DisplayTable(self.tab_dropped)
        planned_list = DisplayTable.DisplayTable(self.tab_plan_to_watch)

        notebook.pack(fill='both', expand=True)

        for anime in Jikan.watching:
            current_list.insert_new([anime['airing_status']
              , anime['title']
              , str(anime['watched_episodes']) + "/" + str(anime['total_episodes'])
              , anime['type']
              , anime['score']
              , str(anime['season_name']) + "  " + str(anime['season_year'])])

        for anime in Jikan.completed:
            completed_list.insert_new([anime['airing_status']
              , anime['title']
              , str(anime['watched_episodes']) + "/" + str(anime['total_episodes'])
              , anime['type']
              , anime['score']
              , str(anime['season_name']) + "  " + str(anime['season_year'])])


if __name__ == '__main__':
    root = tk.Tk()
    root.title(f'NiseTaiga')
    root.minsize(1000, 500)
    Tabs(root)
    root.mainloop()