from tkinter import *

# expects a kilogram input value and converts that value to grams, pounds, and ounces

window = Tk()


def convert_weight():
    entry = e_value.get()

    t_g.delete("1.0", END)
    t_lbs.delete("1.0", END)
    t_oz.delete("1.0", END)

    t_g.insert(END, float(entry)*1000)
    t_lbs.insert(END, float(entry)*2.20462)
    t_oz.insert(END, float(entry)*35.274)


t = Text(window, height=1, width=20)
t.insert(END, "Enter a weight in kg")
t.grid(row=1, column=1)

e_value = StringVar()
e = Entry(window, textvariable = e_value)
e.grid(row=1, column=2)

b = Button(window, text="Convert", command=convert_weight)
b.grid(row=1, column=3)

t_g_label = Text(window, height=1, width=20)
t_g_label.insert(END, "In grams")
t_g_label.grid(row=3, column=1)

t_lbs_label = Text(window, height=1, width=20)
t_lbs_label.insert(END, "In pounds")
t_lbs_label.grid(row=3, column=2)

t_oz_label = Text(window, height=1, width=20)
t_oz_label.insert(END, "In ounces")
t_oz_label.grid(row=3, column=3)

t_g = Text(window, height=1, width=20)
t_g.grid(row=4, column=1)

t_lbs = Text(window, height=1, width=20)
t_lbs.grid(row=4, column=2)

t_oz = Text(window, height=1, width=20)
t_oz.grid(row=4, column=3)

window.mainloop()
