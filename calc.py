
import tkinter as tk
'''import tkinter module tk is an alias for east access'''
'''button click handle'''
def press(v):
    entry.insert(tk.END,v)
    '''called when a number or operator button is clicked insert the pressed value at end of the entry widget'''
def clear():
    entry.delete(0,tk.END)
    '''clears the calculator screen delete all characters from index 0 to end'''
def backspace():
    """Removes only the last character entered (Go back one step)."""
    current_text = entry.get()
    if len(current_text) > 0:
        # Delete from the index of the last character to the end
        entry.delete(len(current_text) - 1, tk.END)    
    

#calculation function
def calculator():
    try:
        result=eval(entry.get()) 
        '''entry.get() retrives the expression e.g(2+6)  eval() evaluates the string as a python expression'''      
        entry.delete(0,tk.END) #clears the old expression
        entry.insert(0,result)  #display execption instead of crashing
    except:
        entry.delete(0,tk.END)
        entry.insert(0,"Invalid Expression")
        '''handles invalid expression (e.g. 5++) display expection instead of crashing'''

#main window creation 
root=tk.Tk() # creates the main application window
root.title("calculator") # sets window title
root.configure(bg="#1e1e1e") #sets background color
root.resizable(False,False) #disables  resizing of window

#entry widget (display screen)
entry=tk.Entry(
    root,
    font=("Times new roman",20),
    bg="#2d2d2d",
    fg="white",
    bd=0,
    justify="right"
)
'''text input filed acts as calculator display right-aligned for better calculator look'''
entry.grid(row=0,column=0,columnspan=4,padx=12,pady=12,ipady=10)

#buttom=n labels
buttons=[
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","=","+",
]
'''represent calculator buttons stroed in list to reduce repetitive code'''

#dynamic button creation
r=1
c=0
'''rows and column counter for grid layout'''
for b in buttons:
    cmd = calculator if b=="=" else lambda x=b:press(x)
    '''if button is "=" ,call calculator() else call press()'''

    tk.Button(
         root,
         text=b,
         command=cmd, #these three lines create a button widget
         font=("calbri",14),
          width=5,
          height=2,
          bg="#ff9500" if b in "+-/*" else "#3a3a3a",
          fg="white",
          bd=0
    ).grid(row=r,column=c,padx=6,pady=6)
    c+=1
    if c==4:
        r+=1
        c=0
        '''moves to next row after 5 buttons'''

#clear button 
tk.Button(
    root,
    text="clear",
    command=clear,
    font=("calbri",14),
    width=10,
    height=2,
    bg="#ff3b3b",
    fg="white",
    bd=0
).grid(row=r,column=0,columnspan=2,pady=4)
'''clears the calculator display screen spans accros all columns'''
tk.Button(
    root,
    text="Back",
    command=backspace, # Linked to the new backspace function
    font=("calibri",14),
    width=10,
    height=2,
    bg="#5c5c5c",
    fg="white",
    bd=0
).grid(row=r, column=2, columnspan=2,pady=4)

#event loop
root.mainloop()
'''keps the window running listens for user interactions'''