import tkinter as tk

calculation = ""

# defining the input of different variables to the calculation
def add_to_input(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

# defining the output of the total calculation
def evaluate():
    global calculation
    print(calculation)
    try:
        calculation  = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_input()
        # if the calculation can't work (x/0)
        text_result.insert(1.0, "Error")
        pass

# defines the function of the clear button
def clear_input():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


# create object and run the main loop
root = tk.Tk()
root.geometry("69x420")

# calc output section
text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)

# these are the numerical buttons and the positions they are in on the GUI
btn_1 = tk.Button(root, text="1", command=lambda: add_to_input(1), width=5, font=("Arial", 14))
btn_1.grid(row=2, column=1)
btn_2 = tk.Button(root, text="2", command=lambda: add_to_input(2), width=5, font=("Arial", 14))
btn_2.grid(row=2, column=2)
btn_3 = tk.Button(root, text="3", command=lambda: add_to_input(3), width=5, font=("Arial", 14))
btn_3.grid(row=2, column=3)
btn_4 = tk.Button(root, text="4", command=lambda: add_to_input(4), width=5, font=("Arial", 14))
btn_4.grid(row=3, column=1)
btn_5 = tk.Button(root, text="5", command=lambda: add_to_input(5), width=5, font=("Arial", 14))
btn_5.grid(row=3, column=2)
btn_6 = tk.Button(root, text="6", command=lambda: add_to_input(6), width=5, font=("Arial", 14))
btn_6.grid(row=3, column=3)
btn_7 = tk.Button(root, text="7", command=lambda: add_to_input(7), width=5, font=("Arial", 14))
btn_7.grid(row=4, column=1)
btn_8 = tk.Button(root, text="8", command=lambda: add_to_input(8), width=5, font=("Arial", 14))
btn_8.grid(row=4, column=2)
btn_9 = tk.Button(root, text="9", command=lambda: add_to_input(9), width=5, font=("Arial", 14))
btn_9.grid(row=4, column=3)
btn_0 = tk.Button(root, text="0", command=lambda: add_to_input(0), width=5, font=("Arial", 14))
btn_0.grid(row=5, column=2)

# these are the operative buttons and where they are placed in the GUI
btn_plus = tk.Button(root, text="+", command=lambda: add_to_input("+"), width=5, font=("Arial", 14))
btn_plus.grid(row=2, column=4)
btn_minus = tk.Button(root, text="-", command=lambda: add_to_input("-"), width=5, font=("Arial", 14))
btn_minus.grid(row=3, column=4)
btn_multiply = tk.Button(root, text="x", command=lambda: add_to_input("*"), width=5, font=("Arial", 14))
btn_multiply.grid(row=4, column=4)
btn_divide = tk.Button(root, text="/", command=lambda: add_to_input("/"), width=5, font=("Arial", 14))
btn_divide.grid(row=5, column=4)
btn_open = tk.Button(root, text="(", command=lambda: add_to_input("("), width=5, font=("Arial", 14))
btn_open.grid(row=5, column=1)
btn_close = tk.Button(root, text=")", command=lambda: add_to_input(")"), width=5, font=("Arial", 14))
btn_close.grid(row=5, column=3)

# these are the equal and clear buttons, they are placed on the bottom
btn_equal = tk.Button(root, text="=", command=evaluate, width=11, font=("Arial", 14))
btn_equal.grid(row=6, column=3, columnspan=2)
btn_clear = tk.Button(root, text="C", command=clear_input, width=11, font=("Arial", 14))
btn_clear.grid(row=6, column=1, columnspan=2)


root.mainloop()