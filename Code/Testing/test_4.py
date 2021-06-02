from tkinter import *
import matplotlib.pyplot as plt
import pandas as pd
#import numpy as np
# dataframe sample data
prediction_input = Tk()
n = 7
useful_parameters = [1,5,7]
parameter_vars = []
#for i in range(int(n)):
#    parameter_vars.append(IntVar())
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

us = [22.125, 26.1, 15.530000000000001, 23.86, 7.0, 1.74, 3.6500000000000004, 56.36]
og_bn = [-1.154629723456719, 0.9897830342393807, 0.28607182436855755, -0.010755801328913336, -0.1752405860600825, 0.05662438013803838, 0.008108268954546392]
og_hn = [0.05910599854263686, 0.011142584592575501, 0, 0, 0.018365996754446414, 0.01582135489243939, 0.030227854321010095]

def predict():
    global useful_parameters
    predict_parameters = []

    for i in range(len(useful_parameters)):
        predict_parameters.append(useful_parameters[i])
    for i in range(int(n)):
        if parameter_vars[i].get()==1 and i+1 not in predict_parameters:
            predict_parameters.append(i+1)

    global predict_data
    #for i in range(len(predict_data)):
    predict_data = [23.77,22.25,15.40,25.67,7.00,2.21,3.70]
    predict_data = [17.44,21.71,24.58,23.84,7.00,1.74,3.70]
    global us
    for i in range(len(predict_data)):
        predict_data[i] = predict_data[i] - us[i]

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
    #print(predict_parameters)


predict_button = Button(prediction_input, text="Predict", command=predict)
predict_button.grid(row=0, column=0)

predict_more = Button(prediction_input, text="Clear Values", command=None)
predict_more.grid(row=1, column=0)

predict_data = [23.77,22.25,15.40,25.67,7.00,2.21,3.70]
for i in range(int(n)):
    predict_entry = Entry(prediction_input)
    predict_entry.grid(row=1, column=i+1)
    predict_data.append(predict_entry)

prediction_input.mainloop()
#df1 = np.transpose(df1)
#print(df1)
