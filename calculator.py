from tkinter import *

root = Tk()
root.title("calculator")
operator = ""
nums = Entry(root, width=38, borderwidth=5)
nums.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def click(number):
    present = nums.get()
    nums.delete(0, END)
    nums.insert(0,str(present) + str(number))

def clear():
    nums.delete(0, END)

def add():
    global first_num
    global operation
    operation = "+"
    first_num = int(nums.get())
    nums.delete(0,END)

def subtract():
    global first_num
    global operation
    operation = "-"
    first_num = int(nums.get())
    nums.delete(0,END)


def multiply():
    global first_num
    global operation
    operation = "*"
    first_num = int(nums.get())
    nums.delete(0,END)


def divide():
    global first_num
    global operation
    operation = "/"
    first_num = int(nums.get())
    nums.delete(0,END)



def calculate():
    second_num = int(nums.get())
    nums.delete(0,END)
    match operation:
        case "+":
            nums.insert(0,first_num+second_num)
        case "-":
            nums.insert(0,first_num-second_num)
        case "*":
            nums.insert(0,first_num*second_num)
        case "/":
            nums.insert(0,first_num/second_num)



button_1 = Button(root, text="1", padx=30, pady=20, command=lambda:click(1))
button_2 = Button(root, text="2", padx=30, pady=20, command=lambda:click(2))
button_3 = Button(root, text="3", padx=30, pady=20, command=lambda:click(3))
button_4 = Button(root, text="4", padx=30, pady=20, command=lambda:click(4))
button_5 = Button(root, text="5", padx=30, pady=20, command=lambda:click(5))
button_6 = Button(root, text="6", padx=30, pady=20, command=lambda:click(6)) 
button_7 = Button(root, text="7", padx=30, pady=20, command=lambda:click(7))
button_8 = Button(root, text="8", padx=30, pady=20, command=lambda:click(8))
button_9 = Button(root, text="9", padx=30, pady=20, command=lambda:click(9))
button_0 = Button(root, text="0", padx=30, pady=20, command=lambda:click(0))  
button_clear = Button(root, text="clear", padx=30, pady=20, command=clear)  
button_add = Button(root, text="+", padx=30, pady=20, command=add)
button_sub = Button(root, text="-", padx=30, pady=20, command=subtract)
button_mul = Button(root, text="*", padx=30, pady=20, command=multiply)
button_div = Button(root, text="/", padx=30, pady=20, command=divide)
button_equals = Button(root, text="=", padx=30, pady=20, command=calculate)  
# Displaying buttons with adjusted padx values
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_equals.grid(row=4, column=2)  # Adjusted column and columnspan for equals
button_add.grid(row=1, column=4)
button_sub.grid(row=2, column=4)
button_mul.grid(row=3, column=4)
button_div.grid(row=4,column=4)



root.mainloop()

