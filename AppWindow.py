import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import menubar

username = 'skr47ch'

root = tk.Tk()
root.title(f'NiseTaiga - {username}')
root.minsize(500, 300)

# Menubar
menubar.Example(root)

# Frame
ribbon = tk.Frame(root)
ribbon.place(relx=0.0, rely=0.0, relwidth=1, height=35)

# Ribbon separators
ribbon_top_separator = ttk.Separator(ribbon)
ribbon_bottom_separator = ttk.Separator(ribbon)
ribbon_top_separator.place(relx=0.0, rely=0.0, relwidth=1)
ribbon_bottom_separator.place(relx=0.0, rely=0.9, relwidth=1)

ribbon_vert_separator_1 = ttk.Separator(ribbon, orient='vertical')
ribbon_vert_separator_1.place(x=35, relheight=0.9)
ribbon_vert_separator_2 = ttk.Separator(ribbon, orient='vertical')
ribbon_vert_separator_2.place(x=120, relheight=0.9)

# Ribbon buttons
refresh_icon = ImageTk.PhotoImage(Image.open('refresh-xxl.png').resize((28,28)))
add_new_folder_icon = ImageTk.PhotoImage(Image.open('folder.png').resize((28,28)))
external_link_icon = ImageTk.PhotoImage(Image.open('external-link-icon.png').resize((25,25)))

refresh_label = tk.Label(ribbon)
add_new_folder_label = tk.Label(ribbon)
external_link_label = tk.Label(ribbon)

refresh_label.config(image=refresh_icon)
add_new_folder_label.config(image=add_new_folder_icon)
external_link_label.config(image=external_link_icon)

refresh_label.place(x=2, y=2, width=30, height=30)
add_new_folder_label.place(x=45, y=2, width=30, height=30)
external_link_label.place(x = 80, y=2, width=30, height=30)

# Search field
search_anime = tk.Entry(ribbon)
search_anime.place(x=290, y=3.5, width=200, height = 25)

root.mainloop()
