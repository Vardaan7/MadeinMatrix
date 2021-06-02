'''import Licensing
import AppConfig
from tkinter import *


AppConfig.Init('.')
key = AppConfig.Get('License', 'Key')
Licensing.Init('.', key)
if not Licensing.IsLicensed():
    print 'Application not licensed: ' + Licensing.GetLicensingMsg()
    exit(1)

print('Hello World!');
'''
'''
from tkinter import *

# a subclass of Canvas for dealing with resizing of windows
class ResizingCanvas(Canvas):
    def __init__(self,parent,**kwargs):
        Canvas.__init__(self,parent,**kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

    def on_resize(self,event):
        # determine the ratio of old width/height to new width/height
        wscale = float(event.width)/self.width
        hscale = float(event.height)/self.height
        self.width = event.width
        self.height = event.height
        # resize the canvas
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "all" tag
        self.scale("all",0,0,wscale,hscale)

def main():
    root = Tk()
    myframe = Frame(root)
    myframe.pack(fill=BOTH, expand=YES)
    mycanvas = ResizingCanvas(myframe,width=850, height=400, bg="red", highlightthickness=0)
    mycanvas.pack(fill=BOTH, expand=YES)

    # add some widgets to the canvas
    mycanvas.create_line(0, 0, 200, 100)
    mycanvas.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
    mycanvas.create_rectangle(50, 25, 150, 75, fill="blue")

    # tag all of the drawn widgets
    mycanvas.addtag_all("all")
    root.mainloop()

if __name__ == "__main__":
    main()
'''
import tkinter as tk

app = tk.Tk()

frames = []
widgets = []

def createwidgets():
    global widgetNames
    global frameNames

    frame = tk.Frame(app, borderwidth=2, relief="groove")
    frames.append(frame)

    frame.pack(side="top", fill="x")

    for i in range(3):
        widget = tk.Entry(frame)
        widgets.append(widget)

        widget.pack(side="left")

createWidgetButton = tk.Button(app, text="createWidgets", command=createwidgets)
createWidgetButton.pack(side="bottom", fill="x")

app.mainloop()