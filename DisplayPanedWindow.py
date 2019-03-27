import tkinter as tk
from tkinter import ttk

class DisplayPanedWindow(tk.Frame):
    def __init__(self, cont):
        tk.Frame.__init__(self, cont)

        panel = tk.PanedWindow(cont, orient='horizontal')
        panel.configure(sashrelief='groove', sashwidth=1.5)
        panel.pack(fill='both', expand=1)

        pane_anime_status = tk.Frame(panel)
        pane_anime_title = tk.Frame(panel)
        pane_progress = tk.Frame(panel)
        pane_score = tk.Frame(panel)
        pane_type = tk.Frame(panel)
        pane_season = tk.Frame(panel)
        pane_end = tk.Frame(panel)

        panel.add(pane_anime_status)
        panel.add(pane_anime_title)
        panel.add(pane_progress)
        panel.add(pane_score)
        panel.add(pane_type)
        panel.add(pane_season)
        panel.add(pane_end)

        panel.paneconfigure(pane_anime_status, minsize=20)
        panel.paneconfigure(pane_anime_title, minsize=250)
        panel.paneconfigure(pane_progress, minsize=200)
        panel.paneconfigure(pane_score, minsize=50)
        panel.paneconfigure(pane_type, minsize=60)
        panel.paneconfigure(pane_season, minsize=200)
        panel.paneconfigure(pane_end, minsize=100)


        label_anime_title = tk.Label(pane_anime_title, text='Anime title')
        label_progress = tk.Label(pane_progress, text='Progress')
        label_score = tk.Label(pane_score, text='Score')
        label_type = tk.Label(pane_type, text='Type')
        label_season = tk.Label(pane_season, text='Season')

        label_anime_title.place(x=5)
        label_progress.place(x=5)
        label_score.place(x=5)
        label_type.place(x=5)
        label_season.place(x=5)


if __name__ == '__main__':
    root = tk.Tk()
    root.title(f'NiseTaiga')
    root.minsize(1000, 500)
    DisplayPanedWindow(root)
    root.mainloop()
