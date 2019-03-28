import tkinter as tk

class DisplayPanedWindow(tk.Frame):
    def __init__(self, cont):
        self.cont = cont
        tk.Frame.__init__(self, cont)

        panel = tk.PanedWindow(self.cont, orient='horizontal')
        panel.configure(sashrelief='groove', sashwidth=1.5)
        panel.pack(fill='both', expand=1)

        self.pane_anime_status = tk.Frame(panel)
        self.pane_anime_title = tk.Frame(panel)
        self.pane_progress = tk.Frame(panel)
        self.pane_score = tk.Frame(panel)
        self.pane_type = tk.Frame(panel)
        self.pane_season = tk.Frame(panel)
        self.pane_end = tk.Frame(panel)

        panel.add(self.pane_anime_status)
        panel.add(self.pane_anime_title)
        panel.add(self.pane_progress)
        panel.add(self.pane_score)
        panel.add(self.pane_type)
        panel.add(self.pane_season)
        panel.add(self.pane_end)

        panel.paneconfigure(self.pane_anime_status, minsize=20)
        panel.paneconfigure(self.pane_anime_title, minsize=250)
        panel.paneconfigure(self.pane_progress, minsize=200)
        panel.paneconfigure(self.pane_score, minsize=50)
        panel.paneconfigure(self.pane_type, minsize=60)
        panel.paneconfigure(self.pane_season, minsize=200)
        panel.paneconfigure(self.pane_end, minsize=100)

        self.label_anime_title = tk.Label(self.pane_anime_title, text='Anime title')
        self.label_progress = tk.Label(self.pane_progress, text='Progress')
        self.label_score = tk.Label(self.pane_score, text='Score')
        self.label_type = tk.Label(self.pane_type, text='Type')
        self.label_season = tk.Label(self.pane_season, text='Season')

        self.label_anime_title.place(x=5)
        self.label_progress.place(x=5)
        self.label_score.place(x=5)
        self.label_type.place(x=5)
        self.label_season.place(x=5)


    def add_entry(self, pane_anime_title, pane_progress, pane_score, pane_type, pane_season, y):
        self.add_label(self.pane_anime_title, pane_anime_title, y)
        self.add_label(self.pane_progress, pane_progress, y)
        self.add_label(self.pane_score, pane_score, y)
        self.add_label(self.pane_type, pane_type, y)
        self.add_label(self.pane_season, pane_season, y)

    def add_label(self, cont, text, y1):
        label = tk.Label(cont, text=f'{text}')
        label.place(x=5, y=y1)

if __name__ == '__main__':
    root = tk.Tk()
    root.title(f'NiseTaiga')
    root.minsize(1000, 500)
    DisplayPanedWindow(root)
    root.mainloop()
