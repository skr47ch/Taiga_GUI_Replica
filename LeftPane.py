import tkinter as tk
from tkinter import ttk

class LeftPane(tk.Frame):
    def __init__(self, cont):
        tk.Frame.__init__(self, cont)
        self.pane = tk.Frame(cont)
        self.pane.place(x=0, y=35, width=150, relheight=0.90)

        self.pane_right_separator = ttk.Separator(self.pane, orient='vertical')
        self.pane_right_separator.place(relx=0.99, rely=0.0, relheight=1)

        self.label_now_playing = ttk.Label(self.pane, text='Icon Now Playing')
        self.label_now_playing.place(x=5, y=5)

        self.pane_separator_1 = ttk.Separator(self.pane)
        self.pane_separator_1.place(y=35, relx=0.03, relwidth=0.94)

        self.label_anime_list = ttk.Label(self.pane, text='Icon Anime List')
        self.label_anime_list.place(x=5, y=45)

        self.label_history = ttk.Label(self.pane, text='Icon History')
        self.label_history.place(x=5, y=65)

        self.label_statistics = ttk.Label(self.pane, text='Icon Statistics')
        self.label_statistics.place(x=5, y=85)

        self.pane_separator_1 = ttk.Separator(self.pane)
        self.pane_separator_1.place(y=115, relx=0.03, relwidth=0.94)

        self.label_search = ttk.Label(self.pane, text='Icon Search')
        self.label_search.place(x=5, y=125)

        self.label_seasons = ttk.Label(self.pane, text='Icon Seasons')
        self.label_seasons.place(x=5, y=145)

        self.label_torrents = ttk.Label(self.pane, text='Icon Torrents')
        self.label_torrents.place(x=5, y=165)