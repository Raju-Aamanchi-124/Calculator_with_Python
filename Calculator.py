from tkinter import *
from tkinter import messagebox

def actionauthor():
    messagebox.showinfo("Author", "Raju")

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def casting(num):
    return float(num) if '.' in num else int(num)

def update_result(operation_name, result, fg_color, bg_color):
    Showtemplabel.delete(0, END)
    Showlabel.delete(0, END)
    Showtemplabel.config(fg=fg_color, bg=bg_color)
    Showtemplabel.insert(0, operation_name)
    Showtemplabel.place(relx=0.5, rely=0.5, anchor='center')
    Showlabel.insert(0, str(result))
    Showlabel.place(relx=0.5, rely=0.6, anchor='center')

def get_inputs():
    num1 = Numberentry1.get().strip()
    num2 = Numberentry2.get().strip()
    if not is_number(num1) or not is_number(num2):
        messagebox.showerror("Error", "Enter a valid number\ne.g. 123, 0.123, .123, -0.123, 123.456")
        return None, None
    return casting(num1), casting(num2)

def actionPlus():
    num1, num2 = get_inputs()
    if num1 is None or num2 is None:
        return
    ans = num1 + num2
    update_result('Summation', ans, 'red', '#9ed8ee')

def actionMinus():
    num1, num2 = get_inputs()
    if num1 is None or num2 is None:
        return
    ans = num1 - num2
    update_result('Subtraction', ans, 'green', '#ece7e2')

def actionMul():
    num1, num2 = get_inputs()
    if num1 is None or num2 is None:
        return
    ans = num1 * num2
    update_result('Multiplication', ans, 'blue', '#cacba9')

def actionDiv():
    num1, num2 = get_inputs()
    if num1 is None or num2 is None:
        return
    if num2 == 0:
        messagebox.showerror("Error", "Cannot divide by zero.")
        return
    ans = num1 / num2
    update_result('Division', ans, 'yellow', '#8dad96')

root = Tk()
root.title('My First Python Calculator')
root.geometry('380x300+200+250')

Titlelabel = Label(root, fg='green', font='none 10 bold underline',
                   text='Python Calculator', compound=CENTER)
Titlelabel.place(relx=0.5, rely=0.1, anchor='center')

Showlabel = Entry(root)
Showtemplabel = Entry(root)
Numberentry1 = Entry(root)
Numberentry2 = Entry(root)

Numberentry1.place(relx=0.5, rely=0.3, anchor='center')
Numberentry2.place(relx=0.5, rely=0.4, anchor='center')

plusbutton = Button(root, text="+", width=5, command=actionPlus)
plusbutton.place(relx=0.1, rely=0.7)

minusbutton = Button(root, text="-", width=5, command=actionMinus)
minusbutton.place(relx=0.3, rely=0.7)

mulbutton = Button(root, text="*", width=5, command=actionMul)
mulbutton.place(relx=0.5, rely=0.7)

divbutton = Button(root, text="/", width=5, command=actionDiv)
divbutton.place(relx=0.7, rely=0.7)

authorbutton = Button(root, text='Author', width=6, command=actionauthor)
authorbutton.place(relx=0.5, rely=0.95, anchor='center')

root.resizable(False, False)
root.mainloop()
