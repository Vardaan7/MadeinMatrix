import tkinter as tk

class ButtonBlock(object):
    def __init__(self, master):
        self.master = master
        self.button = []
        self.button_val = tk.IntVar()
        entry = tk.Entry()
        entry.grid(row=0, column=0)
        entry.bind('<Return>', self.onEnter)
    def onEnter(self, event):
        entry = event.widget
        num = int(entry.get())
        for button in self.button:
            button.destroy()
        for i in range(1, num+1):
            self.button.append(tk.Radiobutton(
                self.master, text=str(i), variable=self.button_val, value=i,
                command=self.onSelect))
            self.button[-1].grid(sticky='WENS', row=i, column=0, padx=1, pady=1)
    def onSelect(self):
        print(self.button_val.get())

if __name__ == '__main__':
    root = tk.Tk()
    ButtonBlock(root)
    root.mainloop()
