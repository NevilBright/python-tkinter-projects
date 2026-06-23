from tkinter import *

root = Tk()

root.title("Simple Calculator")
root.geometry("300x400")

entry = Entry(root,
              width=20,
              font=("Arial",20),
              justify="right")

entry.grid(row=0,column=0,columnspan=4,pady=10)

def button_click(value):

    current = entry.get()

    entry.delete(0,END)

    entry.insert(0,current + str(value))

def button_clear():

    entry.delete(0,END)

def button_equal():

    try:

        result = eval(entry.get())

        entry.delete(0,END)

        entry.insert(0,result)

    except:

        entry.delete(0,END)

        entry.insert(0,"Error")

buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    'C','0','=','+'
]

row = 1
col = 0

for button in buttons:

    if button == "C":

        Button(root,
               text=button,
               width=5,
               height=2,
               command=button_clear).grid(row=row,column=col)

    elif button == "=":

        Button(root,
               text=button,
               width=5,
               height=2,
               command=button_equal).grid(row=row,column=col)

    else:

        Button(root,
               text=button,
               width=5,
               height=2,
               command=lambda b=button: button_click(b)
              ).grid(row=row,column=col)

    col += 1

    if col > 3:
        col = 0
        row += 1

root.mainloop()