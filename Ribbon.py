import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Ribbon(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)

        self.ribbon = tk.Frame(root)
        self.ribbon.place(relx=0.0, rely=0.0, relwidth=1, height=35)
        self.ribbon_top_separator = ttk.Separator(self.ribbon)
        self.ribbon_bottom_separator = ttk.Separator(self.ribbon)
        self.ribbon_top_separator.place(relx=0.0, rely=0.0, relwidth=1)
        self.ribbon_bottom_separator.place(relx=0.0, rely=0.9, relwidth=1)

        self.ribbon_vert_separator_1 = ttk.Separator(self.ribbon, orient='vertical')
        self.ribbon_vert_separator_1.place(x=35, relheight=0.9)
        self.ribbon_vert_separator_2 = ttk.Separator(self.ribbon, orient='vertical')
        self.ribbon_vert_separator_2.place(x=140, relheight=0.9)

        # Ribbon buttons
        self.refresh_icon = ImageTk.PhotoImage(Image.open('refresh-xxl.png').resize((25, 25)))
        self.add_new_folder_icon = ImageTk.PhotoImage(Image.open('folder.png').resize((25, 25)))
        self.external_link_icon = ImageTk.PhotoImage(Image.open('external-link-icon.png').resize((20, 20)))
        self.external_link_icon2 = ImageTk.PhotoImage(Image.open('external-link-icon.png').resize((18, 20)))

        self.refresh_label = ttk.Label(self.ribbon)
        self.add_new_folder_label = ttk.Menubutton(self.ribbon)
        self.external_link_label = ttk.Menubutton(self.ribbon)
        self.external_link_label2 = ttk.Label(self.ribbon)

        self.refresh_label.config(image=self.refresh_icon)
        self.add_new_folder_label.config(image=self.add_new_folder_icon)
        self.external_link_label.config(image=self.external_link_icon)
        self.external_link_label2.config(image=self.external_link_icon2)

        self.refresh_label.place(x=2, y=2, width=30, height=30)
        self.add_new_folder_label.place(x=40, y=2, width=45, height=30)
        self.external_link_label.place(x=90, y=2, width=45, height=30)
        # self.external_link_label2.place(x=130, y=2, width=50, height=30)
        #
        # Search field
        self.search_anime = ttk.Entry(self.ribbon)
        self.search_anime.place(x=200, y=3.5, width=200, height=25)
        self.search_anime.insert(0, 'Filter list or search anime')

        self.search_button = ttk.Button(self.ribbon, text='Search', command=lambda: search_entry(self.search_anime))
        self.search_button.place(x=410, y=3.5, height=25)

        #
        def search_entry(entry):
            print(entry.get())