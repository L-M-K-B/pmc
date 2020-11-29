from tkinter import *
from backend_oop import BooksBackend

backend = BooksBackend()


class Window(object):

    def __init__(self, window):
        self.window = window
        self.window.wm_title("Bookstore")

        # - # Input # - #
        t_title = Label(window, height=1, width=8, text="Title")
        t_title.grid(row=1, column=1)

        self.e_title_value = StringVar()
        self.e_title = Entry(window, textvariable=self.e_title_value)
        self.e_title.grid(row=1, column=2)

        t_year = Label(window, height=1, width=8, text="Year")
        t_year.grid(row=2, column=1)

        self.e_year_value = StringVar()
        self.e_year = Entry(window, textvariable=self.e_year_value)
        self.e_year.grid(row=2, column=2)

        t_author = Label(window, height=1, width=8, text="Author")
        t_author.grid(row=1, column=3)

        self.e_author_value = StringVar()
        self.e_author = Entry(window, textvariable=self.e_author_value)
        self.e_author.grid(row=1, column=4)

        t_isbn = Label(window, height=1, width=8, text="ISBN")
        t_isbn.grid(row=2, column=3)

        self.e_isbn_value = StringVar()
        self.e_isbn = Entry(window, textvariable=self.e_isbn_value)
        self.e_isbn.grid(row=2, column=4)

        # - # Buttons # - #
        b_view_all = Button(window, text="View All", width=16, command=self.view_all)
        b_view_all.grid(row=3, column=4)

        b_search = Button(window, text="Search Entry", width=16, command=self.search)
        b_search.grid(row=4, column=4)

        b_add = Button(window, text="Add Entry", width=16, command=self.insert)
        b_add.grid(row=5, column=4)

        b_update = Button(window, text="Update Selected", width=16, command=self.update)
        b_update.grid(row=6, column=4)

        b_delete = Button(window, text="Delete Selected", width=16, command=self.delete)
        b_delete.grid(row=7, column=4)

        b_close = Button(window, text="Close", width=16, command=self.close_window)
        b_close.grid(row=8, column=4)

        # - # Result # - #
        self.result = Listbox(window, height=6, width=35)
        self.result.grid(row=4, column=1, rowspan=4, columnspan=2)

        scroll = Scrollbar(window)
        scroll.grid(row=5, column=3, rowspan=2)

        self.result.configure(yscrollcommand=scroll.set)
        scroll.configure(command=self.result.yview)

    # - # Methods # - #
    def get_input(self):
        title = self.e_title_value.get()
        year = self.e_year_value.get()
        author = self.e_author_value.get()
        isbn = self.e_isbn_value.get()
        return title, year, author, isbn

    def show_result(self, r):
        self.result.delete(0, END)
        for item in r:
            self.result.insert(END, item)

    def view_all(self):
        r = backend.view_all()
        self.show_result(r)

    def search(self):
        r = backend.search(*self.get_input())
        self.show_result(r)

    def insert(self):
        backend.insert(*self.get_input())
        self.view_all()

    def update(self):
        backend.update(self.result.get(self.result.curselection())[0], *self.get_input())
        self.view_all()

    def delete(self):
        backend.delete(self.result.get(self.result.curselection())[0])
        self.view_all()

    def close_window(self):
        self.window.destroy()


window = Tk()
Window(window)
window.mainloop()
