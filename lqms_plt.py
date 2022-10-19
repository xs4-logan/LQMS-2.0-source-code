# #################################################################
# ### LQMS-2.0 for JAXA-Tanegashima E/S . RCC                   ###
# ### Release date 2022.10                                      ###
# ###   *Plotter                                                ###
# ### Version 2.3.1                       TechnoBusiness Co.LTD ###
# #################################################################
VER = '2.3.1'

import pandas as pdA1
import pandas as pdA2
import pandas as pdB1
import pandas as pdB2
import pandas as pdC1
import pandas as pdC2
import pandas as pdE1
import pandas as pdE2
import numpy as np
import csv
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as pltA1
import matplotlib.pyplot as pltA2
import matplotlib.pyplot as pltB1
import matplotlib.pyplot as pltB2
import matplotlib.pyplot as pltC1
import matplotlib.pyplot as pltC2
import matplotlib.pyplot as pltE1
import matplotlib.pyplot as pltE2
import matplotlib.dates as mdates
from matplotlib.ticker import MultipleLocator,FormatStrFormatter
from time import sleep

import lqms_dt
import os
FN2 = '/mnt/ssd/log/facl/sys_'
dfA1 = pdA1.DataFrame([[],[]])
dfA1 = dfA1.drop(dfA1.index[0])
dfA2 = pdA2.DataFrame([[],[]])
dfA2 = dfA2.drop(dfA2.index[0])
dfB1 = pdB1.DataFrame([[],[]])
dfB1 = dfB1.drop(dfB1.index[0])
dfB2 = pdB2.DataFrame([[],[]])
dfB2 = dfB2.drop(dfB2.index[0])
dfC1 = pdC1.DataFrame([[],[]])
dfC1 = dfC1.drop(dfC1.index[0])
dfC2 = pdC2.DataFrame([[],[]])
dfC2 = dfC2.drop(dfC2.index[0])
dfE1 = pdE1.DataFrame([[],[]])
dfE1 = dfE1.drop(dfE1.index[0])
dfE2 = pdE2.DataFrame([[],[]])
dfE2 = dfE2.drop(dfE2.index[0])

INI_PRM = 99
ToDsA1 = []
ToDsA2 = []
ToDsB1 = []
ToDsB2 = []
ToDsC1 = []
ToDsC2 = []
ToDsD1 = []
ToDsD2 = []
ToDsE1 = []
ToDsE2 = []
EBNsA1 = []
EBNsA2 = []
EBNsB1 = []
EBNsB2 = []
EBNsC1 = []
EBNsC2 = []
EBNsD1 = []
EBNsD2 = []
EBNsE1 = []
EBNsE2 = []

def ST(data,MD):
    global sum
    global Co
    global df
    DTN = lqms_dt.RTC_CHK()
    print ('          ',DTN[1],'\033[1m\033[44m\033[37m\033[1m M/D \033[0m  CDMP Eb/N0 Plotter.\033[0m' + '                                                       lqms_plt.py Ver.' + VER)

    DIR = '/home/xs4/basis/req_relFiles/'

    if (MD == 'MDA1'):
        EBN = float(data)
        ToD = lqms_dt.RTC_CHK()
        dfA1 = pdA1.DataFrame([{'1':ToD[1] ,'2': EBN}])
        dfA1.to_csv(DIR + 'EBN_MDA1_tmp.csv', header = False , index = False , mode = 'a')
        dfwA1 = pdA1.read_csv(DIR + 'EBN_MDA1_tmp.csv' , index_col = False , header = None)
        if (len(dfwA1)>=480):
            dfA1 = dfwA1.drop(dfA1.index[0])
            dfA1.to_csv(DIR + 'EBN_MDA1_tmp.csv', header = False , index = False , mode = 'w')

        if (len(dfwA1) >= 5):
            ToDsA1.append(pdA1.to_datetime(dfwA1.iloc[len(dfwA1)-1,0]))
            EBNsA1.append(dfwA1.iloc[len(dfwA1)-1,1])
            axA1 = pltA1.subplot()
            axA1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
            axA1.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
            axA1.axis([ToDsA1[0] , ToDsA1[len(ToDsA1)-1] , EBNsA1[0] , EBNsA1[len(EBNsA1)-1]])
            axA1.set_ylim(0,16)

            pltA1.tick_params(which ='major',width=1 , length=3)
            pltA1.tick_params(which ='minor',width=0.75 , length=1.8)
            pltA1.minorticks_on()
            pltA1.xticks(fontsize=6)
            pltA1.xlabel('Time of day [HH:MM] / JST(UT+9H)' , fontsize=6)
            pltA1.yticks(fontsize=6.5)
            pltA1.ylabel('Eb/N0 [dB]' , fontsize=6)
            pltA1.title('MODEM-A1 Rx Eb/N0 Scatter Plot' , fontsize=7)
            pltA1.grid(which='major' , axis='both' , linestyle='--' , linewidth=0.4 , color='grey')
            pltA1.grid(which='minor' , axis='both' , linestyle=':' , linewidth=0.4 , color='grey')

            if (len(dfwA1) < 60):
                pltA1.plot (ToDsA1, EBNsA1 , color='teal' , linewidth=1.5)
            if (len(dfwA1) < 240):
                pltA1.plot (ToDsA1, EBNsA1 , color='teal' , linewidth=1.0)
            else :
                pltA1.plot (ToDsA1, EBNsA1 , color='teal' , linewidth=0.5)
            pltA1.savefig(DIR + 'MDA1.svg' , dpi=600 , transparent=True)
            print ('          ',DTN[1],'\033[1m\033[44m\033[37m\033[1m M/D \033[0m  CDMP was end of drawing Eb/N0 plot (IP MODEM-A1).                            lqms_plt.py Ver.' + VER)
            with open(FN2 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'PLT', 'CDMP was end of drawing Eb/N0 plot (MODEM-A1).'])

    if (MD == 'MDA2'):
        EBN = float(data)
        ToD = lqms_dt.RTC_CHK()
        dfA2 = pdA2.DataFrame([{'1':ToD[1] ,'2': EBN}])
        dfA2.to_csv(DIR + 'EBN_MDA2_tmp.csv', header = False , index = False , mode = 'a')
        dfwA2 = pdA2.read_csv(DIR + 'EBN_MDA2_tmp.csv' , index_col = False , header = None)
        if (len(dfwA2)>=480):
            dfA2 = dfwA2.drop(df.index[0])
            dfA2.to_csv(DIR + 'EBN_MDA2_tmp.csv', header = False , index = False , mode = 'w')

        if (len(dfwA2) >= 5):
            ToDsA2.append(pdA2.to_datetime(dfwA2.iloc[len(dfwA2)-1,0]))
            EBNsA2.append(dfwA2.iloc[len(dfwA2)-1,1])
            axA2 = pltA2.subplot()
            axA2.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
            axA2.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
            axA2.axis([ToDsA2[0] , ToDsA2[len(ToDsA2)-1] , EBNsA2[0] , EBNsA2[len(EBNsA2)-1]])
            axA2.set_ylim(0,16)

            pltA2.tick_params(which ='major',width=1 , length=3)
            pltA2.tick_params(which ='minor',width=0.75 , length=1.8)
            pltA2.minorticks_on()
            pltA2.xticks(fontsize=6)
            pltA2.xlabel('Time of day [HH:MM] / JST(UT+9H)' , fontsize=6)
            pltA2.yticks(fontsize=6.5)
            pltA2.ylabel('Eb/N0 [dB]' , fontsize=6)
            pltA2.title('MODEM-A2 Rx Eb/N0 Scatter Plot' , fontsize=7)
            pltA2.grid(which='major' , axis='both' , linestyle='--' , linewidth=0.4 , color='lavender')
            pltA2.grid(which='minor' , axis='both' , linestyle=':' , linewidth=0.4 , color='lavender')

            if (len(dfwA2) < 60):
                pltA2.plot (ToDsA2,EBNsA2 , color='teal' , linewidth=1.5)
            if (len(dfwA2) < 240):
                pltA2.plot (ToDsA2,EBNsA2 , color='teal' , linewidth=1.0)
            else :
                pltA2.plot (ToDsA2,EBNsA2 , color='teal' , linewidth=0.5)
            pltA2.savefig(DIR + 'MDA2.svg' , dpi=600 , transparent=True)
            print ('          ',DTN[1],'\033[1m\033[44m\033[37m\033[1m M/D \033[0m  CDMP was end of drawing Eb/N0 plot (MODEM-A2).                            lqms_plt.py Ver.' + VER)
            with open(FN2 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'PLT', 'CDMP was end of drawing Eb/N0 plot (MODEM-A2).'])

    if (MD == 'MDB1'):
        EBN = float(data)
        ToD = lqms_dt.RTC_CHK()
        dfB1 = pdB1.DataFrame([{'1':ToD[1] ,'2': EBN}])
        dfB1.to_csv(DIR + 'EBN_MDB1_tmp.csv', header = False , index = False , mode = 'a')
        dfwB1 = pdB1.read_csv(DIR + 'EBN_MDB1_tmp.csv' , index_col = False , header = None)
        if (len(dfwB1)>=480):
            dfB1 = dfwB1.drop(df.index[0])
            dfB1.to_csv(DIR + 'EBN_MDB1_tmp.csv', header = False , index = False , mode = 'w')

        if (len(dfwB1) >= 5):
            ToDsB1.append(pdB1.to_datetime(dfwB1.iloc[len(dfwB1)-1,0]))
            EBNsB1.append(dfwB1.iloc[len(dfwB1)-1,1])
            axB1 = pltB1.subplot()
            axB1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
            axB1.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
            axB1.axis([ToDsB1[0] , ToDsB1[len(ToDsB1)-1] , EBNsB1[0] , EBNsB1[len(EBNsB1)-1]])
            axB1.set_ylim(0,16)

            pltB1.tick_params(which ='major',width=1 , length=3)
            pltB1.tick_params(which ='minor',width=0.75 , length=1.8)
            pltB1.minorticks_on()
            pltB1.xticks(fontsize=6)
            pltB1.xlabel('Time of day [HH:MM] / JST(UT+9H)' , fontsize=6)
            pltB1.yticks(fontsize=6.5)
            pltB1.ylabel('Eb/N0 [dB]' , fontsize=6)
            pltB1.title('MODEM-B1 Rx Eb/N0 Scatter Plot' , fontsize=7)
            pltB1.grid(which='major' , axis='both' , linestyle='--' , linewidth=0.4 , color='lavender')
            pltB1.grid(which='minor' , axis='both' , linestyle=':' , linewidth=0.4 , color='lavender')

            if (len(dfwB1) < 60):
                pltB1.plot (ToDsB1,EBNsB1 , color='teal' , linewidth=1.5)
            if (len(dfwB1) < 240):
                pltB1.plot (ToDsB1,EBNsB1 , color='teal' , linewidth=1.0)
            else :
                pltB1.plot (ToDsB1,EBNsB1 , color='teal' , linewidth=0.5)
            pltB1.savefig(DIR + 'MDB1.svg' , dpi=600 , transparent=True)
            print ('          ',DTN[1],'\033[1m\033[44m\033[37m\033[1m M/D \033[0m  CDMP was end of drawing Eb/N0 plot (MODEM-B1).                            lqms_plt.py Ver.' + VER)
            with open(FN2 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'PLT', 'CDMP was end of drawing Eb/N0 plot (MODEM-B1).'])

    if (MD == 'MDB2'):
        EBN = float(data)
        ToD = lqms_dt.RTC_CHK()
        dfB2 = pdB2.DataFrame([{'1':ToD[1] ,'2': EBN}])
        dfB2.to_csv(DIR + 'EBN_MDB2_tmp.csv', header = False , index = False , mode = 'a')
        dfwB2 = pdB2.read_csv(DIR + 'EBN_MDB2_tmp.csv' , index_col = False , header = None)
        if (len(dfwB2)>=480):
            dfB2 = dfwB2.drop(dfB2.index[0])
            dfB2.to_csv(DIR + 'EBN_MDB2_tmp.csv', header = False , index = False , mode = 'w')

        if (len(dfwB2) >= 5):
            ToDsB2.append(pdB2.to_datetime(dfwB2.iloc[len(dfwB2)-1,0]))
            EBNsB2.append(dfwB2.iloc[len(dfwB2)-1,1])
            axB2 = pltB2.subplot()
            axB2.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
            axB2.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
            axB2.axis([ToDsB2[0] , ToDsB2[len(ToDsB2)-1] , EBNsB2[0] , EBNsB2[len(EBNsB2)-1]])
            axB2.set_ylim(0,16)

            pltB2.tick_params(which ='major',width=1 , length=3)
            pltB2.tick_params(which ='minor',width=0.75 , length=1.8)
            pltB2.minorticks_on()
            pltB2.xticks(fontsize=6)
            pltB2.xlabel('Time of day [HH:MM] / JST(UT+9H)' , fontsize=6)
            pltB2.yticks(fontsize=6.5)
            pltB2.ylabel('Eb/N0 [dB]' , fontsize=6)
            pltB2.title('MODEM-B2 Rx Eb/N0 Scatter Plot' , fontsize=7)
            pltB2.grid(which='major' , axis='both' , linestyle='--' , linewidth=0.4 , color='lavender')
            pltB2.grid(which='minor' , axis='both' , linestyle=':' , linewidth=0.4 , color='lavender')

            if (len(dfwB2) < 60):
                pltB2.plot (ToDsB2,EBNsB2 , color='teal' , linewidth=1.5)
            if (len(dfwB2) < 240):
                pltB2.plot (ToDsB2,EBNsB2 , color='teal' , linewidth=1.0)
            else :
                pltB2.plot (ToDsB2,EBNsB2 , color='teal' , linewidth=0.5)
            pltB2.savefig(DIR + 'MDB2.svg' , dpi=600 , transparent=True)
            print ('          ',DTN[1],'\033[1m\033[44m\033[37m\033[1m M/D \033[0m  CDMP was end of drawing Eb/N0 plot (MODEM-B2).                            lqms_plt.py Ver.' + VER)
            with open(FN2 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'PLT', 'CDMP was end of drawing Eb/N0 plot (MODEM-B2).'])

    if (MD == 'MDC1'):
        EBN = float(data)
        ToD = lqms_dt.RTC_CHK()
        dfC1 = pdC1.DataFrame([{'1':ToD[1] ,'2': EBN}])

        dfC1.to_csv(DIR + 'EBN_MDC1_tmp.csv', header = False , index = False , mode = 'a')
        dfwC1 = pdC1.read_csv(DIR + 'EBN_MDC1_tmp.csv' , index_col = False , header = None)
        if (len(dfwC1)>=480):
            dfC1 = dfwC1.drop(df.index[0])
            dfC1.to_csv(DIR + 'EBN_MDC1_tmp.csv', header = False , index = False , mode = 'w')

        if (len(dfwC1) >= 5):
            ToDsC1.append(pdC1.to_datetime(dfwC1.iloc[len(dfwC1)-1,0]))
            EBNsC1.append(dfwC1.iloc[len(dfwC1)-1,1])
            axC1 = pltC1.subplot()
            axC1.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
            axC1.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
            axC1.axis([ToDsC1[0] , ToDsC1[len(ToDsC1)-1] , EBNsC1[0] , EBNsC1[len(EBNsC1)-1]])
            axC1.set_ylim(0,16)

            pltC1.tick_params(which ='major',width=1 , length=3)
            pltC1.tick_params(which ='minor',width=0.75 , length=1.8)
            pltC1.minorticks_on()
            pltC1.xticks(fontsize=6)
            pltC1.xlabel('Time of day [HH:MM] / JST(UT+9H)' , fontsize=6)
            pltC1.yticks(fontsize=6.5)
            pltC1.ylabel('Eb/N0 [dB]' , fontsize=6)
            pltC1.title('MODEM-C1 Rx Eb/N0 Scatter Plot' , fontsize=7)
            pltC1.grid(which='major' , axis='both' , linestyle='--' , linewidth=0.4 , color='lavender')
            pltC1.grid(which='minor' , axis='both' , linestyle=':' , linewidth=0.4 , color='lavender')

            if (len(dfwC1) < 60):
                pltC1.plot (ToDsC1,EBNsC1 , color='teal' , linewidth=1.5)
            if (len(dfwC1) < 240):
                pltC1.plot (ToDsC1,EBNsC1 , color='teal' , linewidth=1.0)
            else :
                pltC1.plot (ToDsC1,EBNsC1 , color='teal' , linewidth=0.5)
            pltC1.savefig(DIR + 'MDC1.svg' , dpi=600 , transparent=True)
            print ('          ',DTN[1],'\033[1m\033[44m\033[37m\033[1m M/D \033[0m  CDMP was end of drawing Eb/N0 plot (MODEM-C1).                            lqms_plt.py Ver.' + VER)
            with open(FN2 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'PLT', 'CDMP was end of drawing Eb/N0 plot (MODEM-C1).'])

    if (MD == 'MDC2'):
        EBN = float(data)
        ToD = lqms_dt.RTC_CHK()
        dfC2 = pdC2.DataFrame([{'1':ToD[1] ,'2': EBN}])
        dfC2.to_csv(DIR + 'EBN_MDC2_tmp.csv', header = False , index = False , mode = 'a')
        dfwC2 = pdC2.read_csv(DIR + 'EBN_MDC2_tmp.csv' , index_col = False , header = None)
        if (len(dfwC2)>=480):
            dfC2 = dfwC2.drop(dfC2.index[0])
            dfC2.to_csv(DIR + 'EBN_MDC2_tmp.csv', header = False , index = False , mode = 'w')

        if (len(dfwC2) >= 5):
            ToDsC2.append(pdC2.to_datetime(dfwC2.iloc[len(dfwC2)-1,0]))
            EBNsC2.append(dfwC2.iloc[len(dfwC2)-1,1])
            axC2 = pltC2.subplot()
            axC2.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
            axC2.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
            axC2.axis([ToDsC2[0] , ToDsC2[len(ToDsC2)-1] , EBNsC2[0] , EBNsC2[len(EBNsC2)-1]])
            axC2.set_ylim(0,16)

            pltC2.tick_params(which ='major',width=1 , length=3)
            pltC2.tick_params(which ='minor',width=0.75 , length=1.8)
            pltC2.minorticks_on()
            pltC2.xticks(fontsize=6)
            pltC2.xlabel('Time of day [HH:MM] / JST(UT+9H)' , fontsize=6)
            pltC2.yticks(fontsize=6.5)
            pltC2.ylabel('Eb/N0 [dB]' , fontsize=6)
            pltC2.title('MODEM-C2 Rx Eb/N0 Scatter Plot' , fontsize=7)
            pltC2.grid(which='major' , axis='both' , linestyle='--' , linewidth=0.4 , color='lavender')
            pltC2.grid(which='minor' , axis='both' , linestyle=':' , linewidth=0.4 , color='lavender')

            if (len(dfwC2) < 60):
                pltC2.plot (ToDsC2,EBNsC2 , color='teal' , linewidth=1.5)
            if (len(dfwC2) < 240):
                pltC2.plot (ToDsC2,EBNsC2 , color='teal' , linewidth=1.0)
            else :
                pltC2.plot (ToDsC2,EBNsC2 , color='teal' , linewidth=0.5)
            pltC2.savefig(DIR + 'MDC2.svg' , dpi=600 , transparent=True)
            print ('          ',DTN[1],'\033[1m\033[44m\033[37m\033[1m M/D \033[0m  CDMP was end of drawing Eb/N0 plot (MODEM-C2).                            lqms_plt.py Ver.' + VER)
            with open(FN2 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'PLT', 'CDMP was end of drawing Eb/N0 plot (MODEM-C2).'])

    if (MD == 'MDE1'):
        EBN = float(data)
        ToD = lqms_dt.RTC_CHK()
        dfE1 = pdE1.DataFrame([{'1':ToD[1] ,'2': EBN}])
        dfE1.to_csv(DIR + 'EBN_MDE1_tmp.csv', header = False , index = False , mode = 'a')
        dfwE1 = pdE1.read_csv(DIR + 'EBN_MDE1_tmp.csv' , index_col = False , header = None)
        if (len(dfwE1)>=480):
            dfE1 = dfwE1.drop(df.index[0])
            dfE1.to_csv(DIR + 'EBN_MDE1_tmp.csv', header = False , index = False , mode = 'w')

        if (len(dfwE1) >= 5):
            ToDsE1.append(pdE1.to_datetime(dfwE1.iloc[len(dfwE1)-1,0]))
            EBNsE1.append(dfwE1.iloc[len(dfwE1)-1,1])
            axE1 = pltE1.subplot()
            axE1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
            axE1.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
            axE1.axis([ToDsE1[0] , ToDsE1[len(ToDsE1)-1] , EBNsE1[0] , EBNsE1[len(EBNsE1)-1]])
            axE1.set_ylim(0,16)

            pltE1.tick_params(which ='major',width=1 , length=3)
            pltE1.tick_params(which ='minor',width=0.75 , length=1.8)
            pltE1.minorticks_on()
            pltE1.xticks(fontsize=6)
            pltE1.xlabel('Time of day [HH:MM] / JST(UT+9H)' , fontsize=6)
            pltE1.yticks(fontsize=6.5)
            pltE1.ylabel('Eb/N0 [dB]' , fontsize=6)
            pltE1.title('MODEM-E1 Rx Eb/N0 Scatter Plot' , fontsize=7)
            pltE1.grid(which='major' , axis='both' , linestyle='--' , linewidth=0.4 , color='lavender')
            pltE1.grid(which='minor' , axis='both' , linestyle=':' , linewidth=0.4 , color='lavender')

            if (len(dfwE1) < 60):
                pltE1.plot (ToDsE1,EBNsE1 , color='teal' , linewidth=1.5)
            if (len(dfwE1) < 240):
                pltE1.plot (ToDsE1,EBNsE1 , color='teal' , linewidth=1.0)
            else :
                pltE1.plot (ToDsE1,EBNsE1 , color='teal' , linewidth=0.5)
            pltE1.savefig(DIR + 'MDE1.svg' , dpi=600 , transparent=True)
            print ('          ',DTN[1],'\033[1m\033[44m\033[37m\033[1m M/D \033[0m  CDMP was end of drawing Eb/N0 plot (MODEM-E1).                            lqms_plt.py Ver.' + VER)
            with open(FN2 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'PLT', 'CDMP was end of drawing Eb/N0 plot (MODEM-E1).'])

    if (MD == 'MDE2'):
        EBN = float(data)
        ToD = lqms_dt.RTC_CHK()
        dfE2 = pdE2.DataFrame([{'1':ToD[1] ,'2': EBN}])
        dfE2.to_csv(DIR + 'EBN_MDE2_tmp.csv', header = False , index = False , mode = 'a')
        dfwE2 = pdE2.read_csv(DIR + 'EBN_MDE2_tmp.csv' , index_col = False , header = None)
        if (len(dfwE2)>=480):
            df = dfwE2.drop(df.index[0])
            df.to_csv(DIR + 'EBN_MDE2_tmp.csv', header = False , index = False , mode = 'w')

        if (len(dfwE2) >= 5):
            ToDsE2.append(pdE2.to_datetime(dfwE2.iloc[len(dfwE2)-1,0]))
            EBNsE2.append(dfwE2.iloc[len(dfwE2)-1,1])
            axE2 = pltE2.subplot()
            axE2.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
            axE2.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
            axE2.axis([ToDsE2[0] , ToDsE2[len(ToDsE2)-1] , EBNsE2[0] , EBNsE2[len(EBNsE2)-1]])
            axE2.set_ylim(0,16)

            pltE2.tick_params(which ='major',width=1 , length=3)
            pltE2.tick_params(which ='minor',width=0.75 , length=1.8)
            pltE2.minorticks_on()
            pltE2.xticks(fontsize=6)
            pltE2.xlabel('Time of day [HH:MM] / JST(UT+9H)' , fontsize=6)
            pltE2.yticks(fontsize=6.5)
            pltE2.ylabel('Eb/N0 [dB]' , fontsize=6)
            pltE2.title('MODEM-E2 Rx Eb/N0 Scatter Plot' , fontsize=7)
            pltE2.grid(which='major' , axis='both' , linestyle='--' , linewidth=0.4 , color='lavender')
            pltE2.grid(which='minor' , axis='both' , linestyle=':' , linewidth=0.4 , color='lavender')

            if (len(dfwE2) < 60):
                pltE2.plot (ToDsE2,EBNsE2 , color='teal' , linewidth=1.5)
            if (len(dfwE2) < 240):
                pltE2.plot (ToDsE2,EBNsE2 , color='teal' , linewidth=1.0)
            else :
                pltE2.plot (ToDsE2,EBNsE2 , color='teal' , linewidth=0.5)
            pltE2.savefig(DIR + 'MDE2.svg' , dpi=600 , transparent=True)
            print ('          ',DTN[1],'\033[1m\033[44m\033[37m\033[1m M/D \033[0m  CDMP was end of drawing Eb/N0 plot (MODEM-E2).                            lqms_plt.py Ver.' + VER)

            with open(FN2 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'PLT', 'CDMP was end of drawing Eb/N0 plot (MODEM-E2).'])
