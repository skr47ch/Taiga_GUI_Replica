import tkinter as tk
import Jikan as jikan
from tkinter import ttk

class DisplayStatistics(tk.Frame):
    def __init__(self, cont):
        tk.Frame.__init__(self, cont)
        self.root = cont

        # Anime List Section
        header_animelist = ttk.Label(self.root, text="Anime list")
        header_animelist.pack(anchor='nw', padx=5, pady=(15,5))

        separator_animelist = ttk.Separator(self.root, orient='horizontal')
        separator_animelist.pack(fill='x', padx='5')

        # Data
        animelist_animecount = ttk.Label(self.root, text=f"Anime count:     {jikan.anime_count}")
        animelist_animecount.pack(anchor='nw', padx=15)
        animelist_animecount = ttk.Label(self.root, text=f"Episode count:     {jikan.episode_count}")
        animelist_animecount.pack(anchor='nw', padx=15)
        animelist_animecount = ttk.Label(self.root, text=f"Days watched:     {jikan.days_watched}")
        animelist_animecount.pack(anchor='nw', padx=15)
        animelist_animecount = ttk.Label(self.root, text=f"Mean score:     {jikan.mean_score}")
        animelist_animecount.pack(anchor='nw', padx=15)


        # Score Distribution Section
        header_scoredist = ttk.Label(self.root, text="Score distribution")
        header_scoredist.pack(anchor='nw', padx=5, pady=(15,5))

        separator_scoredist = ttk.Separator(self.root, orient='horizontal')
        separator_scoredist.pack(fill='x', padx='5', pady=(0,5))

        # Data


        # Score Distribution Section
        header_localdb = ttk.Label(self.root, text="Local database")
        header_localdb.pack(anchor='nw', padx=5, pady=(15,5))

        separator_localdb = ttk.Separator(self.root, orient='horizontal')
        separator_localdb.pack(fill='x', padx='5')

        # Data


        # Score Distribution Section
        header_taiga = ttk.Label(self.root, text="Score distribution")
        header_taiga.pack(anchor='nw', padx=5, pady=(15,5))

        separator_taiga = ttk.Separator(self.root, orient='horizontal')
        separator_taiga.pack(fill='x', padx='5')

        # Data




if __name__ == "__main__":
    root = tk.Tk()
    root.minsize(400, 300)
    new_list = DisplayStatistics(root)
    root.mainloop()