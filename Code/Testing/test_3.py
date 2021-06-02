from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

og_hn = [0.05910599854263686, 0.011142584592575501, 0, 0, 0.018365996754446414, 0.01582135489243939, 0.030227854321010095]

sn_level_table = [['Item/Parameter', 'Level 1', 'Level 2'],
                [1, -9.32, -15.24],
                [2, -12.36, -12.2],
                [3, -12.01, -12.55],
                [4, -13.27, -11.28],
                [5, -12.01, -12.54],
                [6, -12.26, -12.3],
                [7, -10.68, -13.88]]
sn_change_table = [['Item/Parameter', 'SN Ratio % Change'],
                    [1, 38.84064354678576],
                    [2, -1.2511999496057187],
                    [3, 4.326010466545918],
                    [4, -17.63507427992913],
                    [5, 4.230586075521442],
                    [6, 0.3109422596251765],
                    [7, 23.09254574567266]]


graph_data = []
'''for i in range(len(level_data)-1):
    graph_data.append(["P"+str(i+1)+" L1",level_data[i+1][1]])
    graph_data.append(["P"+str(i+1)+" L2",level_data[i+1][2]])
'''
for i in range(len(sn_level_table[1:])):
    sn_data = {"Level": ["L 1", "L 2"], "SN Ratio": [sn_level_table[i+1][1],sn_level_table[i+1][2]]} #"Material": [level_data[i+1][0]],
    graph_data.append(sn_data)

#print(df.groupby("Level").sum())

#for i in range(len(level_data)-1):

#    data.append()

#for i in graph_data:
#    print(i)

#df1 = pd.DataFrame(graph_data, columns=["Parameter and Level","Integrated Estimate SN Ratio"])

#df1 = pd.DataFrame(level_data[1:], columns=[level_data[0]])

#df1 = df1.groupby('Parameter and Level').sum()
#print(df1.iloc[1:3,:])

#print(df1)

#df = df1.iloc[0:2]

#print(df)

#data = {'Year': [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010],
#         'Unemployment_Rate': [9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]
#        }
#df2 = pd.DataFrame(data, columns=['Year','Unemployment_Rate'])

#print(df2.groupby("Year").sum())

#for i in range

plot_data = Tk()

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
    if sn_change_table[i+1][1]>2 and og_hn[i]>0:
        c = 'g'
    elif sn_change_table[i+1][1]>0 and og_hn[i]>0:
        c = 'y'
    else:
        c = 'r'
    df.plot(ax=axs[i], color=c, marker='o', fontsize=10)
    #axs[i].xaxis.set_major_locator(MultipleLocator(2))
    axs[i].set_title("Parameter "+str(i+1))


edit_data = Button(plot_data,text='Edit Data',command=None)
edit_data.pack()


predict_btn = Button(plot_data,text='Predict',command=None)
predict_btn.pack()


def quit():
    #sys.exit()
    plot_data.quit()
    #print(1)

plot_data.protocol("WM_DELETE_WINDOW", quit)


plot_data.mainloop()


'''
for i in range(len(level_data)-1):
    figure2 = plt.Figure(figsize=(3,4), dpi=100)
    ax2 = figure2.add_subplot(111)
    line2 = FigureCanvasTkAgg(figure2, root)
    line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    df = pd.DataFrame(graph_data[i], columns=["Level","SN Ratio"])
    df.plot(kind='line', legend=True, ax=ax2, color='r',marker='o', fontsize=10)
    ax2.set_title('SN Ratio Change')
'''
#figure1 = plt.Figure(figsize=(5,3), dpi=100)
#ax2 = figure1.add_subplot(111)
#line2 = FigureCanvasTkAgg(figure1, root)
#line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
#df1 = df1.groupby('Parameter and Level').sum()
#df1.iloc[:2,:].plot(kind='line', legend=True, ax=ax2, color='r',marker='o', fontsize=10)
#for i in range(len(level_data)-1):
#    df = df1.iloc[i:i+2,:]
#    df.plot(kind='line', legend=True, ax=ax2, color='r',marker='o', fontsize=10)
#ax2.set_title('Parameter wise SN Ratio Change')

#Scatter Graph
#figure3 = plt.Figure(figsize=(5,4), dpi=100)
#ax3 = figure3.add_subplot(111)
#ax3.scatter(df3['Interest_Rate'],df3['Stock_Index_Price'], color = 'g')
#scatter3 = FigureCanvasTkAgg(figure3, root)
#scatter3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
#ax3.legend(['Stock_Index_Price'])
#ax3.set_xlabel('Interest Rate')
#ax3.set_title('Interest Rate Vs. Stock Index Price')
#def edit_data():
