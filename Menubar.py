import tkinter as tk
import external_links
import about_page

class Menubar(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.root = root
        self.menubar = tk.Menu(self)
        self.make_menubar()
        self.root.configure(menu=self.menubar)

    def make_menubar(self):
        # File
        self.filemenu = tk.Menu(self, tearoff=False)
        self.menubar.insert_cascade(index=1, label='File', menu=self.filemenu)
        self.make_filemenu()
        # Services
        self.servicesmenu = tk.Menu(self, tearoff=False)
        self.menubar.insert_cascade(index=2, label='Services', menu=self.servicesmenu)
        self.make_servicesmenu()
        # Tools
        self.toolsmenu = tk.Menu(self, tearoff=False)
        self.menubar.insert_cascade(index=3, label='Tools', menu=self.toolsmenu)
        self.make_toolsmenu()
        # View
        self.viewmenu = tk.Menu(self, tearoff=False)
        self.menubar.insert_cascade(index=4, label='View', menu=self.viewmenu)
        self.make_viewmenu()
        # Help
        self.helpmenu = tk.Menu(self, tearoff=False)
        self.menubar.insert_cascade(index=5, label='Help', menu=self.helpmenu)
        self.make_helpmenu()

    def make_filemenu(self):
        library_folders = tk.Menu(self, tearoff=False)

        self.filemenu.insert_cascade(index=0, label='Library Folders', menu=library_folders)
        self.filemenu.insert_cascade(index=1, label='Scan available episodes'),
        self.filemenu.insert_cascade(index=3, label='Play next episodes       Ctrl+N')
        self.filemenu.insert_cascade(index=4, label='Play random anime        Ctrl+R')
        self.filemenu.insert_cascade(index=6, label='Exit', command=self.root.quit)
        self.filemenu.insert_separator(index=2)
        self.filemenu.insert_separator(index=5)

        library_folders.insert_cascade(index=0, label='Add new folder ...')

    def make_servicesmenu(self):
        anilist = tk.Menu(self, tearoff=False)
        kitsu = tk.Menu(self, tearoff=False)
        myanimelist = tk.Menu(self, tearoff=False)

        self.servicesmenu.insert_cascade(index=0, label='Synchronize list       Ctrl+S')
        self.servicesmenu.insert_cascade(index=2, label='AniList', menu=anilist)
        self.servicesmenu.insert_cascade(index=3, label='Kitsu', menu=kitsu)
        self.servicesmenu.insert_cascade(index=4, label='MyAnimeList', menu=myanimelist)
        self.servicesmenu.insert_separator(index=1)

        anilist.insert_cascade(index=0, label='Go to my profile')
        anilist.insert_cascade(index=1, label='Go to my stats')

        kitsu.insert_cascade(index=0, label='Go to my feed')
        kitsu.insert_cascade(index=1, label='Go to my library')
        kitsu.insert_cascade(index=2, label='Go to my profile')

        myanimelist.insert_cascade(index=0, label='Go to my panel')
        myanimelist.insert_cascade(index=1, label='Go to my profile')
        myanimelist.insert_cascade(index=2, label='Go to my history')

    def make_toolsmenu(self):
        exportanimelist = tk.Menu(self, tearoff=False)
        externallinks = tk.Menu(self, tearoff=False)

        self.toolsmenu.insert_cascade(index=0, label='Export anime list', menu=exportanimelist)
        self.toolsmenu.insert_cascade(index=1, label='External links', menu=externallinks)
        self.toolsmenu.insert_checkbutton(index=3, label='Enable anime recognition', onvalue=1, offvalue=False)
        self.toolsmenu.insert_checkbutton(index=4, label='Enable auto sharing', onvalue=1, offvalue=False)
        self.toolsmenu.insert_checkbutton(index=5, label='Enable auto synchronization')
        self.toolsmenu.insert_cascade(index=7, label='Settings')
        self.toolsmenu.insert_separator(index=2)
        self.toolsmenu.insert_separator(index=6)

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

    def make_viewmenu(self):
        self.viewmenu.insert_radiobutton(index=0, label='Now Playing')
        self.viewmenu.insert_radiobutton(index=1, label='Anime List')
        self.viewmenu.insert_radiobutton(index=2, label='History')
        self.viewmenu.insert_radiobutton(index=3, label='Statistics')
        self.viewmenu.insert_radiobutton(index=4, label='Search')
        self.viewmenu.insert_radiobutton(index=5, label='Seasons')
        self.viewmenu.insert_radiobutton(index=6, label='Torrents')
        self.viewmenu.insert_checkbutton(index=8, label='Show Sidebar')
        self.viewmenu.insert_separator(index=7)

    def make_helpmenu(self):
        self.helpmenu.insert_cascade(index=0, label='About Taiga', command=self.about_taiga)
        self.helpmenu.insert_cascade(index=1, label='Support    F11'
                                     , command=lambda: self.open_external_links('help_support'))
        self.helpmenu.insert_cascade(index=3, label='Check for updates')
        self.helpmenu.insert_separator(index=2)

    def open_external_links(self, extlink):
        try:
            external_links.OpenLink(extlink)
        except KeyError as e:
            print(f"Key error on the value {e}")

    def about_taiga(self):
        about_page.AboutPage()

if __name__ == "__main__":
    root = tk.Tk()
    root.minsize(500, 300)
    Menubar(root)
    root.mainloop()


