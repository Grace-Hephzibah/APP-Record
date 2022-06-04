from tkinter import *

root = Tk()

def rightclick(ev):
    print("rightclick")
    
def leftclick(ev):
    print("leftclick")
    
def middleclick(event):
    print("middleclick")
    
frame = Frame(root,width=300,height=200)
frame.bind("<Button-1>",leftclick)
frame.bind("<Button-2>",middleclick)
frame.bind("<Button-3>",rightclick)
frame.pack()
root.mainloop()
