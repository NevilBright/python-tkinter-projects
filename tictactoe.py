from tkinter import *

window = Tk()
window.title("tictactoe")

turn = "X"

def click(button):
    global turn
    if button["text"] == "":
        button["text"] = turn
        if turn =="X":
            turn = "O"
        else: 
            turn = "X"
        
        
for i in range(3):
    for j in range(3):
        b = Button(window, text="", width=8, height=4)
        b.config(command=lambda
        button=b: click(button))
        b.grid(row=i, column=j)
        
window.mainloop()
        
        
    
    
        
        
        

        
    
    


        

        


