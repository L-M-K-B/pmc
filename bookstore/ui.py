from tkinter import *
import backend

window = Tk()


# - # Functions # - #
def close_window():
    window.mainloop()


# - # Input # - #
t_title = Label(window, height=1, width=8, text="Title")
t_title.grid(row=1, column=1)

e_title_value = StringVar()
e_title = Entry(window, textvariable=e_title_value)
e_title.grid(row=1, column=2)

t_year = Label(window, height=1, width=8, text="Year")
t_year.grid(row=2, column=1)

e_year_value = StringVar()
e_year = Entry(window, textvariable=e_year_value)
e_year.grid(row=2, column=2)

t_author = Label(window, height=1, width=8, text="Author")
t_author.grid(row=1, column=3)

e_author_value = StringVar()
e_author = Entry(window, textvariable=e_author_value)
e_author.grid(row=1, column=4)

t_isbn = Label(window, height=1, width=8, text="ISBN")
t_isbn.grid(row=2, column=3)

e_isbn_value = StringVar()
e_isbn = Entry(window, textvariable=e_isbn_value)
e_isbn.grid(row=2, column=4)

# - # Buttons # - #
b_view_all = Button(window, text="View All", width=16)
b_view_all.grid(row=3, column=4)

b_search = Button(window, text="Search Entry", width=16)
b_search.grid(row=4, column=4)

b_add = Button(window, text="Add Entry", width=16)
b_add.grid(row=5, column=4)

b_update = Button(window, text="Update Selected", width=16)
b_update.grid(row=6, column=4)

b_delete = Button(window, text="Delete Selected", width=16)
b_delete.grid(row=7, column=4)

b_close = Button(window, text="Close", command=close_window)
b_close.grid(row=8, column=4)

# - # Result # - #
result = Listbox(window, height=6, width=35)
result.grid(row=4, column=1, rowspan=4, columnspan=2)

scroll = Scrollbar(window)
scroll.grid(row=5, column=3, rowspan=2)

result.configure(yscrollcommand=scroll.set)
scroll.configure(command=result.yview)


window.mainloop()
