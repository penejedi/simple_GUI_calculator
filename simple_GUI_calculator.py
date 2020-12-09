from tkinter import *

master = Tk()
master.title("Basic Calculator")

screen = Entry(master, width=35, borderwidth=3)
screen.grid(row=0, column=0, columnspan=4, padx=5, pady=5)


def clear_all():
    screen.delete(0, END)


def button_click(number):
    current = screen.get()
    screen.delete(0, END)
    screen.insert(0, current + str(number))


def button_add():
    first_num = screen.get()
    global f_num
    global operation
    operation = "add"
    f_num = float(first_num)
    screen.delete(0, END)


def button_minus():
    first_num = screen.get()
    global f_num
    global operation
    operation = "minus"
    f_num = float(first_num)
    screen.delete(0, END)


def button_multiply():
    first_num = screen.get()
    global f_num
    global operation
    operation = "multiply"
    f_num = float(first_num)
    screen.delete(0, END)


def button_divide():
    first_num = screen.get()
    global f_num
    global operation
    operation = "divide"
    f_num = float(first_num)
    screen.delete(0, END)


def button_equal():
    sec_num = screen.get()
    screen.delete(0, END)
    if operation == "add":
        screen.insert(0, float(f_num) + float(sec_num))
    elif operation == "minus":
        screen.insert(0, float(f_num) - float(sec_num))
    elif operation == "multiply":
        screen.insert(0, float(f_num) * float(sec_num))
    else:
        screen.insert(0, round(float(f_num) / float(sec_num), 10))


button_1 = Button(master, text="1", padx=30, pady=20, command=lambda: button_click(1))
button_1.grid(row=3, column=0)
button_2 = Button(master, text="2", padx=30, pady=20, command=lambda: button_click(2))
button_2.grid(row=3, column=1)
button_3 = Button(master, text="3", padx=30, pady=20, command=lambda: button_click(3))
button_3.grid(row=3, column=2)
button_4 = Button(master, text="4", padx=30, pady=20, command=lambda: button_click(4))
button_4.grid(row=2, column=0)
button_5 = Button(master, text="5", padx=30, pady=20, command=lambda: button_click(5))
button_5.grid(row=2, column=1)
button_6 = Button(master, text="6", padx=30, pady=20, command=lambda: button_click(6))
button_6.grid(row=2, column=2)
button_7 = Button(master, text="7", padx=30, pady=20, command=lambda: button_click(7))
button_7.grid(row=1, column=0)
button_8 = Button(master, text="8", padx=30, pady=20, command=lambda: button_click(8))
button_8.grid(row=1, column=1)
button_9 = Button(master, text="9", padx=30, pady=20, command=lambda: button_click(9))
button_9.grid(row=1, column=2)
button_0 = Button(master, text="0", padx=30, pady=20, command=lambda: button_click(0))
button_0.grid(row=4, column=0)
button_point = Button(master, text=".", padx=32, pady=20, command=lambda: button_click("."))
button_point.grid(row=4, column=1)
button_equal = Button(master, text="=", padx=140, pady=20, command=button_equal)
button_equal.grid(row=7, column=0, columnspan=4)
button_clear = Button(master, text="CLEAR", padx=13, pady=20, command=clear_all)
button_clear.grid(row=4, column=2)
button_add = Button(master, text="+", padx=30, pady=20, command=button_add)
button_add.grid(row=1, column=3)
button_minus = Button(master, text="-", padx=32, pady=20, command=button_minus)
button_minus.grid(row=2, column=3)
button_multiply = Button(master, text="x", padx=31, pady=20, command=button_multiply)
button_multiply.grid(row=3, column=3)
button_division = Button(master, text="÷", padx=29, pady=20, command=button_divide)
button_division.grid(row=4, column=3)


master.mainloop()
