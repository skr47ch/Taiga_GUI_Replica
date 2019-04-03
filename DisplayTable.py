import tkinter as tk
from tkinter import ttk

headers = ['', 'Anime Title', 'Progress', 'Score', 'Type', 'Season', ' ']
default_width = [15, 250, 100, 50, 70, 80, 450]
min_width = [15, 100, 100, 50, 70, 80, 400]
align = ['nw', 'nw', 'n', 'n', 'n', 'e', 'e']

class DisplayTable(tk.Frame):
    def __init__(self, cont):
        tk.Frame.__init__(self, cont)
        self.root = cont
        self.setup_widget()
        self.build_tree()

    def setup_widget(self):
        container = ttk.Frame(self.root)
        container.pack(fill='both', expand=True)

        self.tree = ttk.Treeview(columns=headers, show="headings")
        vsb = ttk.Scrollbar(orient='vertical', command=self.tree.yview)
        hsb = ttk.Scrollbar(orient='horizontal', command=self.tree.xview)

        self.tree.configure(yscrollcommand=vsb.set)
        self.tree.configure(xscrollcommand=hsb.set)

        # Cant figure out how to get scrollbar to the right and bottom
        # self.tree.place(relheight=1, relwidth=1)
        # vsb.place(relheight=1, width=20, anchor='nw')

        # Cant figure out how to fill screen with grid
        self.tree.grid(column=0, row=0, sticky='nsew', in_=container)
        vsb.grid(column=1, row=0, sticky='ns', in_=container)
        hsb.grid(column=0, row=1, sticky='ew', in_=container)

    def build_tree(self):
        for header, width, minwidth, anchor  in zip(headers, default_width, min_width, align):
            self.tree.heading(header, text=header.title(), anchor=anchor,
                              command=lambda h=header: sort_by(self.tree, h, 0))

            # adjust the column's width to header string
            self.tree.column(header, width=width, minwidth=minwidth, anchor=anchor)

    def insert_new(self, anime_list):
        self.tree.insert('', 'end', values=anime_list)

def sort_by(tree, col, descending):
    """sort tree contents when a column header is clicked on"""

    data = [(tree.set(child, col), child) for child in tree.get_children('')]
    # if the data to be sorted is numeric change to float
    # data =  change_numeric(data)
    # now sort the data in place
    data.sort(reverse=descending)

    for ix, item in enumerate(data):
        tree.move(item[1], '', ix)

    # switch the heading so it will sort in opposite direction
    tree.heading(col, command=lambda  col=col: sort_by(tree, col, int(not descending)))


if __name__ == "__main__":
    root = tk.Tk()
    new_list = DisplayTable(root)
    new_list.insert_new(['Act', 'Mushishi', '22/41', '9', 'Anime', 'Fall 2000'])
    root.mainloop()