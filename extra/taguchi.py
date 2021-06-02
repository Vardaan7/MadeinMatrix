from tkinter import *
import pandas as pd
import math
import copy
import csv
#n = int(input("Enter Number of Raw Materials / Additives: "))
#t = int(input("Enter Number of Test Cases: "))

#taguchi standard table
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

#print("Input the test data: ")

#tdata = [[float(input()) for i in range(n+1)] for j in range(t)]
#n = 7
#t = 10
tdata =[[34.27,7.10,20.08,24.30,9.48,1.17,3.60,49.77],
        [26.78,21.71,15.23,23.84,7.00,1.74,3.70,53.73],
        [17.01,26.04,19.65,23.16,9.41,1.12,3.60,54.10],
        [23.77,22.25,15.40,25.67,7.00,2.21,3.70,54.29],
        [22.11,21.71,19.91,23.84,7.00,1.74,3.70,56.27],
        [22.14,30.49,11.15,23.88,7.00,1.74,3.60,56.45],
        [22.11,21.71,19.91,23.84,7.00,1.74,3.70,59.14],
        [20.81,21.05,19.25,26.56,7.00,1.63,3.69,59.89],
        [12.18,31.64,19.91,23.84,7.00,1.74,3.70,60.59],
        [19.66,23.15,21.35,22.75,7.00,2.37,3.71,61.51]]
n = len(tdata[0])-1
t = len(tdata)

#print("Data Set: ")
#for j in range(t):
#    print(tdata[j])
#print("")

#storing original data in new two dimensional array:
ogdata = tdata

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
us = []
for i in range(n+1):
    us.append((tdata[zsub[0][0]][i]+tdata[zsub[1][0]][i])/2)

deleted_testcase_index = [zsub[0][0],zsub[1][0]]

### Printing unit space
#print(us)
#print("")

tdata.pop(zsub[0][0])
tdata.pop(zsub[1][0])
#testdata is now signal data

for j in range(t-2):
    for i in range(n+1):
        tdata[j][i] = tdata[j][i] - us[i]
#testdata is now normalized signal data

nsdata = copy.deepcopy(tdata)

sn = []
og_n = n
og_bn = []
og_hn = []

### Printing Normalized Signal Data
#for i in tdata:
#    print(i)
#print("")

### Printing Rounded off Normalized Signal Data
#for j in tdata:
#    for i in j:
#        print(round(i,2),end = " ")
#    print("")

#SN Ratio Calculation Function
def snr_calc(mat_used):
#for k in range(12):
    global n
    global t
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
    #if n==og_n:
    #    for i in Mtable:
    #        print(i)
    #    print("")


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

### Printing Level Table (SN Ratio Change)
for i in range(n):
    for j in range(2):
        sn_level_table[i+1][j+1]=round(sn_level_table[i+1][j+1],2)

#for i in sn_level_table:
#    print(i)


### CASE 1

# Printing SN ( h ) Values when all materials used
#print(og_hn)

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
for i in range(1,n+1):
    if sn_level_table[i][1]>sn_level_table[i][2]:
        case2_index.append(i)
case2_tally = [2,2,2,2,2,2,2,2,2,2,2]
for i in case2_index:
    case2_tally[i-1]=1


#print(case2_index)

# Finding Useful Parameters

useful_parameters = [value for value in case1_index if value in case2_index]
useful_parameters.pop(2)
#print(useful_parameters)


# Printing original b values when all materials used
#print(og_bn)

# Computing integrated estimated M value under optimum conditions
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

Mt_o_table = ["Data No.", "Measured Value M", "Intergrated Estimate Value M"]
for j in range(t-2):
    Mt_o_table.append([1, round(nsdata[j][-1],2), round(Mt_o[j],2)])

# Printing Measured M value and integrated estimate M value in case 2
#for i in Mt_o_table:
#    print(i)

#Printing Comparision of the Integrated Estimate SN Ratio for both Cases

sn_case_table = [["Case", "Used Items/Parameters", "Integrated Estimate SN Ratio (dB)"]]
sn_case_table.append([1, case1_index, snr_calc(case1_tally)])
sn_case_table.append([2, case2_index, snr_calc(case2_tally)])

for i in sn_case_table:
    print(i)















    
#print testing

#print(sbn)
#print(stn)
#print(sen)
#print(ven)
#print(hn)
#print(Mt)
#print(lm,stm)
#print(sbm, sem, vem)
#print(r)
#print(l)
