from tkinter import *

lay=[]


def print_1():
    print(1)
    print(lay)



root = Tk()
root.geometry('300x400+100+50')

top = None

def create():

    global top
    top = Toplevel()
    lay.append(top)

    top.title("Main Panel")
    top.geometry('500x500+100+450')
    msg = Message(top, text="Show on Sub-panel",width=100)
    msg.pack()

    def exit_btn():
        top.destroy()
        top.update()

    def show_btn():
        root.deiconify()
        #top.update()

    def hide_btn():
        root.withdraw()
        #top.update()

    def print_btn():
        root.withdraw()

    btn = Button(top,text='EXIT',command=exit_btn)
    btn.pack()
    btn1 = Button(top,text='SHOW MAIN',command=show_btn)
    btn1.pack()
    btn2 = Button(top,text='HIDE MAIN',command=hide_btn)
    btn2.pack()
    btn3 = Button(top,text='Print', command=print_1)
    btn3.pack()

Button(root, text="Click me,Create a sub-panel", command=create).pack()

mainloop()
