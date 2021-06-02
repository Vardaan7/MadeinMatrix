
#table for test
import pandas as pd

taguchi_table = [[1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,2,2,2,2,2,2],
                [1,1,2,2,2,1,1,1,2,2,2],
                [1,2,1,2,2,1,2,2,1,1,2],
                [1,2,2,1,2,2,1,2,1,2,1],
                [1,2,2,2,1,2,2,1,2,1,1],
                [2,1,2,2,1,1,2,2,1,2,1],
                [2,1,2,1,2,2,2,1,1,1,2],
                [2,1,1,2,2,2,1,2,2,1,1],
                [2,2,2,1,1,1,1,2,2,1,2],
                [2,2,1,2,1,2,1,1,1,2,2],
                [2,2,1,1,2,1,2,1,2,2,1]]

#for i in tally_table:
#    print(i)

#data = pd.read_csv("tdata.csv")
#print(data)

#full computation of SN ratio

#def sn_calc(data)

#how_many = int(input("How many terms are in the equation?"))
#
#terms = [] # empty list
#
#for i in range(how_many):
#    var = int(input("Enter the coefficient for variable"))
#    terms.append(var)
#
#how_many = int(input("How many terms are in the equation?"))

#terms = {}

#for i in range(how_many):
#    var = int(input("Enter the coefficient for variable"))
#    terms["T{}".format(i)] = var

#print(terms)

import tkinter as tk



n = 0
t = 0
Header = {}


class MaTrix(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Main_window, Data_details):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Main_window)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class Main_window(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="MaTrix")
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="Enter Data Details",
                            command=lambda: controller.show_frame(Data_details))
        button.pack()

        #button2 = tk.Button(self, text="Visit Page 2",
        #                    command=lambda: controller.show_frame(Data_Input))
        #button2.pack()


class Data_details(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Enter the Number of Materials and Test Cases")
        label.pack(pady=10,padx=10)

        #button1 = tk.Button(self, text="Go Back",
        #                    command=lambda: controller.show_frame(Main_window))
        #button1.pack()

        #n_label = tk.Label(self, text="Number of Materials/Additives:")
        #n_input = ""
        #global n
        n_entry = tk.Entry(self)
        n_entry.pack()

        #t_label = tk.Label(self, text="Number of Test Cases:")
        #t_input = ""
        #global t
        t_entry = tk.Entry(self)
        t_entry.pack()

        def detail_final():
            global n
            global t
            n = int(n_entry.get())
            t = int(t_entry.get())
            data_entry = tk.Toplevel(Data_details)
            #print(n, t)
            #controller.show_frame(Data_Input)

        #def open_data_entry_table():

        #    data_entry = Toplevel(MaTrix)

        #    data_entry.title("Input Data")


        button2 = tk.Button(self, text="Proceed to Enter Data",
                            command= detail_final)
        button2.pack()



#class Data_Input(tk.Frame):

#    def __init__(self, parent, controller):
#        tk.Frame.__init__(self, parent)


        #def create_dataframe():
        #    global n
        #    Material_list = {}
        #    for i in range(n):


        #for j in range()
        #label = tk.Label(self, text="Enter the Data")
        #label.pack(pady=10,padx=10)

        #button0 = tk.Button(self, text="Print i",
        #                    command=create_dataframe)
        #button0.pack()


        #button1 = tk.Button(self, text="Main Window",
        #                    command=lambda: controller.show_frame(Main_window))
        #button1.pack()

        #button2 = tk.Button(self, text="Go Back",
        #                    command=lambda: controller.show_frame(Data_details))
        #button2.pack()

        #def warning():
        #    warning_window = Toplevel(self)

        #t1 = tk.Text(self)
        #t1.grid(row=0,column=0)
        #t2 = tk.Text(self)
        #t2.pack()




app = MaTrix()
#app.configure(bg='cornflower blue')
#print(n, t)
#print(Header)
app.mainloop()
print(n, t)
