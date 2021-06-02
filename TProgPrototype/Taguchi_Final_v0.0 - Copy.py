# Taguchi Method Final

from tkinter import *
import pandas as pd
import math
import copy
import tkinter.messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


main_window = Tk()

#Heading = Label(main_window, text = "MaTrix")
#Heading.grid(row=0,column=1)

n = 0
t = 0
us = []
sn = []
og_n = 0
og_t = 0
og_bn = []
og_hn = []
sn_level_table = []
sn_change_table = []
Mt_o_table = []
useful_parameters = []
sn_case_table = []
predict_data = []

#def reset_values():
#    n = 0
#    t = 0
#    us = []
#    sn = []
#    og_n = 0
#    og_t = 0
#    og_bn = []
#    og_hn = []
#    sn_level_table = []
#    sn_change_table = []
#    Mt_o_table = []
#    useful_parameters = []
#    sn_case_table = []
#    predict_data = []


#tdata = []

main_window.title("MADEIN MaTrix")

def enter_data_details_window():

    main_window.withdraw()

    data_details = Toplevel(main_window)
    data_details.title("Enter Data Details")

    parameter_label = Label(data_details, text="Enter Number of Parameters:")
    parameter_label.grid(row=0, column=0)

    parameter_entry = Entry(data_details)
    parameter_entry.grid(row=0, column=1)

    testcase_label = Label(data_details, text="Enter Number of Test Cases:")
    testcase_label.grid(row=1, column=0)


    testcase_entry = Entry(data_details)
    testcase_entry.grid(row=1, column=1)

    def input_data_window():

        data_details.withdraw()

        global n
        n = parameter_entry.get()
        global t
        t = testcase_entry.get()
        #print(n,t)
        input_data = Toplevel(data_details)
        input_data.title("Input Data")

        def run():
            #global tdata
            global n
            global t
            n = int(n)
            t = int(t)
            #print(n,t)
            #print(dataset[0][0].get())
            #n = len(dataset[0])-1
            #t = len(dataset)

            test_data = []
            for j in range(t):
                test_data.append([])
                for i in range(n+1):
                    test_data[j].append(float(dataset[j][i].get()))
                    #test_data[j][i] = float(test_data[j][i])
            #    for i in range(n+1):
            #        tdata[j][i]=dataset[j][i].get()
            #tdata = []
            #tdata = copy.deepcopy(dataset)
            #print(tdata)
            tally_table = [[1,1,1,1,1,1,1,1,1,1,1],
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

            '''
            sample_data =[[34.27,7.10,20.08,24.30,9.48,1.17,3.60,49.77],
                        [26.78,21.71,15.23,23.84,7.00,1.74,3.70,53.73],
                        [17.01,26.04,19.65,23.16,9.41,1.12,3.60,54.10],
                        [23.77,22.25,15.40,25.67,7.00,2.21,3.70,54.29],
                        [22.11,21.71,19.91,23.84,7.00,1.74,3.70,56.27],
                        [22.14,30.49,11.15,23.88,7.00,1.74,3.60,56.45],
                        [22.11,21.71,19.91,23.84,7.00,1.74,3.70,59.14],
                        [20.81,21.05,19.25,26.56,7.00,1.63,3.69,59.89],
                        [12.18,31.64,19.91,23.84,7.00,1.74,3.70,60.59],
                        [19.66,23.15,21.35,22.75,7.00,2.37,3.71,61.51]]
            


            sample_data = [[575.0,274.0,205.5,210.5,5.0,180.0,81.55],
                            [575.0,304.0,207.5,218.5,6.0,120.0,82.99],
                            [570.0,279.0,199.5,207.5,7.0,120.0,83.03],
                            [577.0,205.0,173.0,164.0,7.0,120.0,84.56],
                            [573.0,254.0,160.0,164.0,7.0,120.0,84.60],
                            [577.0,216.0,176.0,168.0,6.0,120.0,85.52],
                            [582.0,222.5,171.0,167.0,5.0,180.0,89.47]]
            '''
            #test_data1 = [[6,15,0.5,0,0,0,10,0.57],
            #            [6,15,0.5,3,5,5,13,0.43],
            #            [6,25,2.5,0,0,5,13,0.51],
            #            [6,25,2.5,3,5,0,10,0.51],
            #            [10,15,2.5,0,5,0,13,0.51],
            #            [10,15,2.5,3,0,5,10,0.55],
            #            [10,25,0.5,0,5,5,10,0.5]]

            #tdata = copy.deepcopy(sample_data)
            tdata = copy.deepcopy(test_data)

            for i in tdata:
                print(i)
            #print(tdata)

            #n = len(tdata[0])-1
            #t = len(tdata)


            #adding parameter(strength in this case) to new list
            z = []
            for j in range(t):
                z.append(tdata[j][-1])

            #computing avg
            zavg = sum(z)/len(z)
            zsub = []

            #finding two test case parameter values(strength) closest to avg
            for j in range(t):
                zsub.append([j,abs(z[j]-zavg)])
            zsub = sorted(zsub, key = lambda a:a[1])
            close2 = [zsub[0][0], zsub[1][0]]

            #creating unit space
            global us
            us = []
            for i in range(n+1):
                us.append((tdata[zsub[0][0]][i]+tdata[zsub[1][0]][i])/2)
            print(us)

            deleted_testcase_index = [zsub[0][0],zsub[1][0]]

            tdata.pop(zsub[0][0])
            tdata.pop(zsub[1][0])
            #testdata is now signal data

            for j in range(t-2):
                for i in range(n+1):
                    tdata[j][i] = tdata[j][i] - us[i]
            #testdata is now normalized signal data

            nsdata = copy.deepcopy(tdata)

            global sn
            sn = []
            global og_n
            og_n = n
            global og_bn
            og_bn = []
            global og_hn
            og_hn = []

            #SN Ratio Calculation Function
            def snr_calc(mat_used):
                global n
                global t
                global og_n

                tdata = copy.deepcopy(nsdata)
                i_c = 0

                for i in range(n-1,-1,-1):
                    if mat_used[i]==2:
                        i_c += 1
                        for j in range(t-2):
                            tdata[j].pop(i)
                n = n - i_c

                #Printing current rounded off tdata
                #for j in tdata:
                #    for i in j:
                #        print(round(i,2),end = " ")
                #    print("")

                #b and sb calculation (propotional coefficient and variation of propotional term)
                bn = []
                sbn = []
                #calc r
                r = 0
                for j in range(t-2):
                    r = r + tdata[j][-1]**2
                #adding each b
                for i in range(n):
                    b = 0
                    sb = 0
                    for j in range(t-2):
                        b = b + tdata[j][i]*tdata[j][-1]
                    bn.append(b/r)
                    sbn.append((b**2)/r)

                global og_bn
                if n == og_n:
                    og_bn = bn

                ### Printing b values
                #print("Propotional Coefficient Values: ")
                #print(bn)
                #print("")

                ### Printing rounded off b values
                #for i in bn:
                #    print(round(i,3), end=" ")
                #print("")

                #st calculation
                stn = []
                for i in range(n):
                    st = 0
                    for j in range(t-2):
                        st = st + tdata[j][i]**2
                    stn.append(st)

                #se calculation
                sen = []
                for i in range(n):
                    sen.append(stn[i] - sbn[i])

                #ve calculation
                ven = []
                #l value
                l = t-2
                for i in range(n):
                    ve = sen[i]/(l-1)
                    ven.append(ve)

                #comparing ve and sb to get h(sn ratio) value
                hn = []
                for i in range(n):
                    if sbn[i]>ven[i]:
                        h = (sbn[i]-ven[i])/(r*ven[i])
                    else:
                        h = 0
                    hn.append(h)

                #print(hn)

                global og_hn
                if n == og_n:
                    og_hn = hn


                ### Printing h values
                #print(hn)
                #print("")

                ### Printing rounded off h values
                #for i in hn:
                #    print(round(i,3), end=" ")
                #print("")

                #rounding off
                #for i in range(n):
                #    bn[i] = round(bn[i],3)
                #    hn[i] = round(hn[i],3)
                #print(bn)
                #print(hn)

                #computation of integrated estimated strength value M for each data item
                Mt = []
                hsum = 0
                for i in hn:
                    hsum = hsum + i
                for j in range(t-2):
                    m = 0
                    for i in range(n):
                        m += (hn[i] * tdata[j][i])/bn[i]
                    Mt.append(m/hsum)

                #M est and actual table creation
                Mtable = [["Data No.","Measured M","Integrated Estimated M"]]
                for j in range(t-2):
                    Mtable.append([j,tdata[j][-1],Mt[j]])

                ### Printing M change table
                #for i in Mtable:
                #    print(i)
                #print("")

                #propotional equation L calculation
                lm = 0
                for j in range(t-2):
                    lm += tdata[j][-1]*Mt[j]

                #total variation St calculation
                stm = 0
                for j in range(t-2):
                    stm += Mt[j]**2

                #variation of propotional term calculation
                sbm = (lm**2)/r

                #error variation calculation
                sem = stm - sbm

                #error variance calculation
                vem = sem/(l-1)

                ### Integrated SN Ratio Calculation

                snh = (sbm - vem)/(r*vem)
                snh = 10*(math.log(snh,10))

                #sn.append(round(snh,2))

                n = og_n

                return snh

            #SN ratio for all cases
            for k in range(12):
                sn.append(snr_calc(tally_table[k]))

            ### Printing integrated SN ratio values
            #print(sn)

            ### Printing rounded off integrated SN ratio values
            #for i in sn:
            #    print(round(i,2),end=" ")
            #print("")

            #material wise relative importance calculation
            # Level 1 = used ; Level 2 = not used
            global sn_level_table
            sn_level_table = [["Item/Parameter","Level 1","Level 2"]]
            for i in range(n):
                l1 = 0
                l2 = 0
                for j in range(12):
                    if tally_table[j][i]==1:
                        l1 += sn[j]
                    else:
                        l2 += sn[j]
                sn_level_table.append([i+1,l1/6,l2/6])

            # SN Percentage Change Table
            global sn_change_table
            sn_change_table = [["Item/Parameter", "SN Ratio % Change"]]

            for i in range(n):
                sn_pchange = ((sn_level_table[i+1][2]-sn_level_table[i+1][1])/sn_level_table[i+1][2])*100
                sn_change_table.append([i+1, sn_pchange])

            # Taking SN Percentage Change to be taken if greater than 4%
            snr_g5 = []
            for i in range(n):
                if sn_change_table[i+1][1] > 4:
                    snr_g5.append(sn_change_table[i+1][0])

            ### Printing Level Table (SN Ratio Change)


            for i in range(n):
                for j in range(2):
                    sn_level_table[i+1][j+1]=round(sn_level_table[i+1][j+1],2)

            for i in sn_level_table:
                print(i)


            ### CASE 1

            # Printing SN ( h ) Values when all materials used
            #print(og_hn)

            #global og_hn
            case1_index = []
            for i in range(n):
                if og_hn[i]>0:
                    case1_index.append(i+1)
            case1_tally = [2,2,2,2,2,2,2,2,2,2,2]
            for i in case1_index:
                case1_tally[i-1]=1

            #print(case1_index)

            ### CASE 2

            case2_index = []
            '''
            for i in range(1,n+1):
                if sn_level_table[i][1]>sn_level_table[i][2]:
                    case2_index.append(i)
            '''
            for i in range(1,n+1):
                if sn_change_table[i][1]>1:
                    case2_index.append(i)
            case2_tally = [2,2,2,2,2,2,2,2,2,2,2]
            for i in case2_index:
                case2_tally[i-1]=1


            #print(case2_index)

            # Finding Useful Parameters
            global useful_parameters


            useful_parameters = [value for value in case1_index if value in case2_index and value in snr_g5]
            #useful_parameters.pop(2)
            print(useful_parameters)


            # Printing original b values when all materials used
            #print(og_bn)

            # Computing integrated estimated M value under optimum conditions
            #global og_bn
            Mt_o = []
            hsum_o = 0
            for i in useful_parameters:
                hsum_o += og_hn[i-1]
            for j in range(t-2):
                M_o = 0
                for i in useful_parameters:
                    M_o += (og_hn[i-1]*nsdata[j][i-1])/og_bn[i-1]
                Mt_o.append(M_o/hsum_o)

            #print(Mt_o)
            global Mt_o_table
            Mt_o_table = [["Data No.", "Measured Value M", "Intergrated Estimate Value M"]]
            for j in range(t-2):
                Mt_o_table.append([j+1, round(nsdata[j][-1],2), round(Mt_o[j],2)])

            # Printing Measured M value and integrated estimate M value in case 2
            for i in Mt_o_table:
                print(i)

            #Printing Comparision of the Integrated Estimate SN Ratio for both Cases
            global sn_case_table
            sn_case_table = [["Case", "Used Items/Parameters", "Integrated Estimate SN Ratio (dB)"]]
            sn_case_table.append([1, case1_index, snr_calc(case1_tally)])
            sn_case_table.append([2, useful_parameters, snr_calc(case2_tally)])

            for i in sn_case_table:
                print(i)

            input_data.withdraw()

            graph_data = []
            for i in range(len(sn_level_table[1:])):
                sn_data = {"Level": ["L 1", "L 2"], "SN Ratio": [sn_level_table[i+1][1],sn_level_table[i+1][2]]} #"Material": [level_data[i+1][0]],
                graph_data.append(sn_data)

            plot_data = Toplevel(input_data)
            plot_data.title("Plotting Data")

            fig, axs = plt.subplots(1, len(sn_level_table[1:]), sharey=True, figsize=(15,5))
            fig.suptitle('Parameter Wise SN Ratio Change')
            graph = FigureCanvasTkAgg(fig, plot_data)
            graph.get_tk_widget().pack() #side=tk.LEFT, fill=tk.BOTH
            #df1 = df1.groupby('Parameter and Level').sum()
            #axs = plt.subplots(1, len(level_data)-1, sharey=True)
            for i in range(len(sn_level_table[1:])):
                df = pd.DataFrame(graph_data[i], columns=["Level","SN Ratio"])
                df = df.groupby("Level").sum()
                c = ""
                if sn_change_table[i+1][1]>4 and og_hn[i]>0:
                    c = 'g'
                elif sn_change_table[i+1][1]>0 and og_hn[i]>0:
                    c = 'y'
                else:
                    c = 'r'
                df.plot(ax=axs[i], color=c, marker='o', fontsize=10)
                    #axs[i].xaxis.set_major_locator(MultipleLocator(2))
                axs[i].set_title("Parameter "+str(i+1))

            def edit_data():
                input_data.deiconify()
                plot_data.destroy()

            edit_data_btn = Button(plot_data,text='Edit Data',command=edit_data)
            edit_data_btn.pack()

            ### Predicting Window
            def predict_input():
                prediction_input = Toplevel(input_data)
                prediction_input.title("Enter Data to Predict Feature")

                global useful_parameters

                parameter_vars = []
                for i in range(int(n)):
                    state = IntVar()
                    select_parameter = Checkbutton(prediction_input, text = "Parameter "+str(i+1), variable=state)
                    select_parameter.grid(row=0, column=i+1)
                    parameter_vars.append(state)
                    if i+1 in useful_parameters:
                        select_parameter.select()

                feature_name = Label(prediction_input, text="Feature")
                feature_name.grid(row=0, column=int(n)+1)
                feature_prediction = Text(prediction_input, height=1,width=15)
                feature_prediction.grid(row=1, column=int(n)+1)

                global predict_data
                predict_data = []

                def predict():
                    global useful_parameters
                    predict_parameters = []

                    for i in range(len(useful_parameters)):
                        predict_parameters.append(useful_parameters[i])
                    for i in range(int(n)):
                        if parameter_vars[i].get()==1 and i+1 not in predict_parameters:
                            predict_parameters.append(i+1)

                    global predict_data
                    #print(predict_data)
                    #for i in range(len(predict_data)):

                    #predict_data = [23.77,22.25,15.40,25.67,7.00,2.21,3.70]
                    #predict_data = [563.0,306.5,185.5,183.5,2.8,60.0]
                    #predict_data = [17.44,21.71,24.58,23.84,7.00,1.74,3.70]
                    global us
                    for i in range(len(predict_data)):
                        predict_data[i] = float(predict_data[i].get()) - us[i]

                    M_p = 0
                    hsum_p = 0
                    for i in predict_parameters:
                        hsum_p += og_hn[i-1]
                    for i in predict_parameters:
                        M_p += (og_hn[i-1]*predict_data[i-1])/og_bn[i-1]
                    M_p = M_p/hsum_p

                    M_predicted = us[-1]+M_p

                    feature_prediction.delete(END)
                    feature_prediction.insert(END, M_predicted)

                predict_button = Button(prediction_input, text="Predict", command=predict)
                predict_button.grid(row=1, column=0)

                #predict_more = Button(prediction_input, text="Clear Values", command=None)
                #predict_more.grid(row=1, column=0)

                for i in range(int(n)):
                    predict_entry = Entry(prediction_input)
                    predict_entry.grid(row=1, column=i+1)
                    predict_data.append(predict_entry)

                def closeall():
                    prediction_input.destroy()
                    plot_data.destroy()
                    main_window.destroy()

                prediction_input.protocol("WM WM_DELETE_WINDOW", closeall)
                prediction_input.mainloop()

                #plot_data.withdraw()


            predict_btn = Button(plot_data,text='Predict',command=predict_input)
            predict_btn.pack()

            def quit():
                #sys.exit()
                plot_data.destroy()
                if tkinter.messagebox.askokcancel("Quit", "Do you really wish to quit?"):
                    main_window.destroy()
                main_window.quit()
                #print(1)
            plot_data.protocol("WM_DELETE_WINDOW", quit)
            plot_data.mainloop()



            #    input_data.withdraw()
            #    print(1)

            #indentation run func

        def edit_details():
            MsgBox = tkinter.messagebox.askquestion('Go Back','You will lose the input data, do you want to continue?',icon = 'warning')
            if MsgBox == 'yes':
                data_details.deiconify()
                input_data.destroy()


        edit_data_details = Button(input_data, text="Edit Data Details", command=edit_details)
        edit_data_details.grid(row=0, column=0)

        for i in range(int(n)):
            header = Label(input_data, text="Parameter "+str(i+1))
            header.grid(row=0, column=i+1)

        feature_label = Label(input_data, text="Feature")
        feature_label.grid(row=0, column=int(n)+1)

        for j in range(int(t)):
            index = Label(input_data, text="Test Case "+str(j+1))
            index.grid(row=j+1, column=0)

        dataset = []
        for j in range(int(t)):
            test_case_data=[]
            for i in range(int(n)+1):
                data_entry = Entry(input_data)
                data_entry.grid(row=j+1, column=i+1)
                test_case_data.append(data_entry)
            dataset.append(test_case_data)

        make_calculations = Button(input_data, text="Run", command=run)
        make_calculations.grid(row=int(t)+2,column=int(n)+3)


        def quitconfirm():
            if tkinter.messagebox.askokcancel("Quit", "Do you really wish to quit?"):
                main_window.destroy()

        input_data.protocol("WM_DELETE_WINDOW", quitconfirm)

        input_data.mainloop()


    input_data_button = Button(data_details, text="Input Data", command=input_data_window)
    input_data_button.grid(row=2, column=1)


    def quitconfirm():
        if tkinter.messagebox.askokcancel("Quit", "Do you really wish to quit?"):
            main_window.destroy()

    data_details.protocol("WM_DELETE_WINDOW", quitconfirm)


    data_details.mainloop()

Data_Input = Button(main_window, text="Enter Data Set", command=enter_data_details_window)
Data_Input.grid(row=0, column=0, padx=90, pady=20)
#main_window.filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("jpg files", "*.jpg"),("all files", "*.*")))

def quitconfirm():
    if tkinter.messagebox.askokcancel("Quit", "Do you really wish to quit?"):
        main_window.destroy()

main_window.protocol("WM_DELETE_WINDOW", quitconfirm)


main_window.mainloop()



#print(n,t)
