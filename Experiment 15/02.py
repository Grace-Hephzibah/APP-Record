from tkinter import *

def Ok():
    result = float(e2.get())
    if(result > 50000) :
        tax = result * 10/100
    elif(result > 30000) :
        tax = result * 5/100
    else :
        tax = 0
    taxText.set(tax)
    nsal =  result - tax
    nsalText.set(nsal)
    
root = Tk()
root.title("Employee Salary Calculation System")
root.geometry("300x400")
global e1
global e2
global taxText
global nsalText
taxText = StringVar()
nsalText = StringVar()
Label(root, text="Employee Name").place(x=10, y=10)
Label(root, text="Salary").place(x=10, y=40)
Label(root, text="Tax").place(x=10, y=80)
Label(root, text="Total:").place(x=10, y=110)
e1 = Entry(root)
e1.place(x=100, y=10)
e2 = Entry(root)
e2.place(x=100, y=40)
tax = Label(root, text="", textvariable=taxText).place(x=100,y=80)
nsal = Label(root, text="", textvariable=nsalText).place(x=100, y=110)
Button(root, text="Cal", command=Ok ,height = 1, width =3).place(x=10, y=150)
empname = Entry(root)
empsal = Entry(root)
root.mainloop()
