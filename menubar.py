import tkinter as tk
import external_links


class Example(tk.Frame):

    def __init__(self, root):

        tk.Frame.__init__(self,  root)
        menubar = tk.Menu(self)

        # main menu items
        filemenu = tk.Menu(self, tearoff=False)
        servicesmenu = tk.Menu(self, tearoff=False)
        toolsmenu = tk.Menu(self, tearoff=False)
        viewmenu = tk.Menu(self, tearoff=False)
        helpmenu = tk.Menu(self, tearoff=False)

        menubar.insert_cascade(index=0, label='File', menu=filemenu)
        menubar.insert_cascade(index=1, label='Services', menu=servicesmenu)
        menubar.insert_cascade(index=2, label='Tools', menu=toolsmenu)
        menubar.insert_cascade(index=3, label='View', menu=viewmenu)
        menubar.insert_cascade(index=4, label='Help', menu=helpmenu)

        # file menu items
        library_folders = tk.Menu(self, tearoff=False)

        filemenu.insert_cascade(index=0, label='Library Folders', menu=library_folders)
        filemenu.insert_cascade(index=1, label='Scan available episodes'),
        filemenu.insert_cascade(index=3, label='Play next episodes          Ctrl+N')
        filemenu.insert_cascade(index=4, label='Play random anime        Ctrl+R')
        filemenu.insert_cascade(index=6, label='Exit', command=root.quit)
        filemenu.insert_separator(index=2)
        filemenu.insert_separator(index=5)

        library_folders.insert_cascade(index=0, label='Add new folder ...')

        # services menu items
        anilist = tk.Menu(self, tearoff=False)
        kitsu = tk.Menu(self, tearoff=False)
        myanimelist = tk.Menu(self, tearoff=False)

        servicesmenu.insert_cascade(index=0, label='Synchronize list       Ctrl+S')
        servicesmenu.insert_cascade(index=2, label='AniList', menu=anilist)
        servicesmenu.insert_cascade(index=3, label='Kitsu', menu=kitsu)
        servicesmenu.insert_cascade(index=4, label='MyAnimeList', menu=myanimelist)
        servicesmenu.insert_separator(index=1)

        anilist.insert_cascade(index=0, label='Go to my profile')
        anilist.insert_cascade(index=1, label='Go to my stats')

        kitsu.insert_cascade(index=0, label='Go to my feed')
        kitsu.insert_cascade(index=1, label='Go to my library')
        kitsu.insert_cascade(index=2, label='Go to my profile')

        myanimelist.insert_cascade(index=0, label='Go to my panel')
        myanimelist.insert_cascade(index=1, label='Go to my profile')
        myanimelist.insert_cascade(index=2, label='Go to my history')

        # tools menu items
        exportanimelist = tk.Menu(self, tearoff=False)
        externallinks = tk.Menu(self, tearoff=False)

        toolsmenu.insert_cascade(index=0, label='Export anime list', menu=exportanimelist)
        toolsmenu.insert_cascade(index=1, label='External links', menu=externallinks)
        toolsmenu.insert_checkbutton(index=3, label='Enable anime recognition', onvalue=1, offvalue=False)
        toolsmenu.insert_checkbutton(index=4, label='Enable auto sharing', onvalue=1, offvalue=False)
        toolsmenu.insert_checkbutton(index=5, label='Enable auto synchronization')
        toolsmenu.insert_cascade(index=7, label='Settings')
        toolsmenu.insert_separator(index=2)
        toolsmenu.insert_separator(index=6)

        exportanimelist.insert_cascade(index=0, label='Export as Markdown')
        exportanimelist.insert_cascade(index=1, label='Export as MyAnimeList XML')

        externallinks.insert_cascade(index=0, label='Hibari', command=lambda: self.open_external_links('hibari'))
        externallinks.insert_cascade(index=1, label='MALgraph', command=lambda: self.open_external_links('malgraph'))
        externallinks.insert_cascade(index=3, label='AniChart', command=lambda: self.open_external_links('anichart'))
        externallinks.insert_cascade(index=4, label='Monthly.moe', command=lambda: self.open_external_links('monthly_moe'))
        externallinks.insert_cascade(index=5, label='Senpai Anime Charts', command=lambda: self.open_external_links('senpai_anime_charts'))
        externallinks.insert_cascade(index=7, label='Anime Streaming Search Engine', command=lambda: self.open_external_links('anime_streaming_search_engine'))
        externallinks.insert_cascade(index=8, label='The Fansub Database', command=lambda: self.open_external_links('the_fansub_database'))
        externallinks.insert_separator(index=2)
        externallinks.insert_separator(index=6)

        # view menu items
        viewmenu.insert_radiobutton(index=0, label='Now Playing')
        viewmenu.insert_radiobutton(index=1, label='Anime List')
        viewmenu.insert_radiobutton(index=2, label='History')
        viewmenu.insert_radiobutton(index=3, label='Statistics')
        viewmenu.insert_radiobutton(index=4, label='Search')
        viewmenu.insert_radiobutton(index=5, label='Seasons')
        viewmenu.insert_radiobutton(index=6, label='Torrents')
        viewmenu.add_separator()
        viewmenu.add_checkbutton(label='Show Sidebar')
        root.configure(menu=menubar)

        # help menu items
        helpmenu.insert_cascade(index=0, label='About Taiga')
        helpmenu.insert_cascade(index=1, label='Support                   F11')
        helpmenu.insert_cascade(index=3, label='Check for updates')
        helpmenu.insert_separator(index=2)

    def open_external_links(self, extlink):
        try:
            external_links.OpenLink(extlink)
        except KeyError as e:
            print(f"Key error on the value {e}")


if __name__ == "__main__":
    root = tk.Tk()
    root.minsize(500, 300)
    Example(root)
    root.mainloop()


