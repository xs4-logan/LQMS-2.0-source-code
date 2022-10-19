import pandas as pd
import numpy as np

import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import MultipleLocator,FormatStrFormatter

import lqms_dt
import os
VER = '1.5.6'

df = pd.DataFrame([[],[]])
df = df.drop(df.index[0])
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
    print ('     ' , DTN[1] , 'CDMP for LQMS-2.0E Version ' + VER)
    EBN = float(data)
    ToD = lqms_dt.RTC_CHK()
    df = pd.DataFrame([{'1':ToD[1] ,'2': EBN}])

    DIR = '/home/xs4/basis/req_relFiles/'

    if (MD == 'MDA1'):
        df.to_csv(DIR + 'EBN_MDA1_tmp.csv', header = False , index = False , mode = 'a')
        dfw = pd.read_csv(DIR + 'EBN_MDA1_tmp.csv' , index_col = False , header = None)
        if (len(dfw)>=480):
            df = dfw.drop(df.index[0])
            df.to_csv(DIR + 'EBN_MDA1_tmp.csv', header = False , index = False , mode = 'w')

        if (len(dfw) >= 5):
            ToDsA1.append(pd.to_datetime(dfw.iloc[len(dfw)-1,0]))
            EBNsA1.append(dfw.iloc[len(dfw)-1,1])
            print (ToDsA1 , EBNsA1)
            fg , ax = plt.subplots()
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
            ax.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
            ax.axis([ToDsA1[0] , ToDsA1[len(ToDsA1)-1] , EBNsA1[0] , EBNsA1[len(EBNsA1)-1]])
            ax.set_ylim(0,16)

            plt.tick_params(which ='major',width=1 , length=3)
            plt.tick_params(which ='minor',width=0.75 , length=1.8)
            plt.minorticks_on()
            plt.xticks(fontsize=6)
            plt.xlabel('Time of day [HH:MM] / JST(UT+9H)' , fontsize=6)
            plt.yticks(fontsize=6.5)
            plt.ylabel('Eb/N0 [dB]' , fontsize=6)
            plt.title('MODEM-A1 Rx Eb/N0 Scatter Plot' , fontsize=7)
            plt.grid(which='major' , axis='both' , linestyle='--' , linewidth=0.4 , color='grey')
            plt.grid(which='minor' , axis='both' , linestyle=':' , linewidth=0.4 , color='grey')

            if (len(dfw) < 60):
                plt.plot (ToDsA1, EBNsA1 , color='teal' , linewidth=1.5)
            if (len(dfw) < 240):
                plt.plot (ToDsA1, EBNsA1 , color='teal' , linewidth=1.0)
            else :
                plt.plot (ToDsA1, EBNsA1 , color='teal' , linewidth=0.5)
            plt.savefig(DIR + 'MDA1.svg' , dpi=600 , transparent=True)
            print ('     ' , DTN[1] , 'CDMP was end of drawing Eb/N0 plot (MODEM-A1).')

    if (MD == 'MDA2'):
        df.to_csv(DIR + 'EBN_MDA2_tmp.csv', header = False , index = False , mode = 'a')
        dfw = pd.read_csv(DIR + 'EBN_MDA2_tmp.csv' , index_col = False , header = None)
        if (len(dfw)>=480):
            df = dfw.drop(df.index[0])
            df.to_csv(DIR + 'EBN_MDA2_tmp.csv', header = False , index = False , mode = 'w')

        if (len(dfw) >= 5):
            ToDsA2.append(pd.to_datetime(dfw.iloc[len(dfw)-1,0]))
            EBNsA2.append(dfw.iloc[len(dfw)-1,1])
            print (ToDsA2 , EBNsA2)
            ax = plt.subplots()
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
            ax.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
            ax.axis([ToDsA2[0] , ToDsA2[len(ToDsA2)-1] , EBNsA2[0] , EBNsA2[len(EBNsA2)-1]])
            ax.set_ylim(0,16)

            plt.tick_params(which ='major',width=1 , length=3)
            plt.tick_params(which ='minor',width=0.75 , length=1.8)
            plt.minorticks_on()
            plt.xticks(fontsize=6)
            plt.xlabel('Time of day [HH:MM] / JST(UT+9H)' , fontsize=6)
            plt.yticks(fontsize=6.5)
            plt.ylabel('Eb/N0 [dB]' , fontsize=6)
            plt.title('MODEM-A2 Rx Eb/N0 Scatter Plot' , fontsize=7)
            plt.grid(which='major' , axis='both' , linestyle='--' , linewidth=0.4 , color='lavender')
            plt.grid(which='minor' , axis='both' , linestyle=':' , linewidth=0.4 , color='lavender')

            if (len(dfw) < 60):
                plt.plot (ToDsA2,EBNsA2 , color='teal' , linewidth=1.5)
            if (len(dfw) < 240):
                plt.plot (ToDsA2,EBNsA2 , color='teal' , linewidth=1.0)
            else :
                plt.plot (ToDsA2,EBNsA2 , color='teal' , linewidth=0.5)
            plt.savefig(DIR + 'MDA2.svg' , dpi=600 , transparent=True)
            print ('     ' , DTN[1] , 'CDMP was end of drawing Eb/N0 plot (MODEM-A2).')

    if (MD == 'MDB1'):
        df.to_csv(DIR + 'EBN_MDB1_tmp.csv', header = False , index = False , mode = 'a')
        dfw = pd.read_csv(DIR + 'EBN_MDB1_tmp.csv' , index_col = False , header = None)
        if (len(dfw)>=480):
            df = dfw.drop(df.index[0])
            df.to_csv(DIR + 'EBN_MDB1_tmp.csv', header = False , index = False , mode = 'w')

        if (len(dfw) >= 5):
            ToDsB1.append(pd.to_datetime(dfw.iloc[len(dfw)-1,0]))
            EBNsB1.append(dfw.iloc[len(dfw)-1,1])
    #        print (ToDs , EBNs)
            fig , ax = plt.subplots()
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
            ax.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
            ax.axis([ToDsB1[0] , ToDsB1[len(ToDsB1)-1] , EBNsB1[0] , EBNsB1[len(EBNsB1)-1]])
            ax.set_ylim(0,16)

            plt.tick_params(which ='major',width=1 , length=3)
            plt.tick_params(which ='minor',width=0.75 , length=1.8)
            plt.minorticks_on()
            plt.xticks(fontsize=6)
            plt.xlabel('Time of day [HH:MM] / JST(UT+9H)' , fontsize=6)
            plt.yticks(fontsize=6.5)
            plt.ylabel('Eb/N0 [dB]' , fontsize=6)
            plt.title('MODEM-B1 Rx Eb/N0 Scatter Plot' , fontsize=7)
            plt.grid(which='major' , axis='both' , linestyle='--' , linewidth=0.4 , color='lavender')
            plt.grid(which='minor' , axis='both' , linestyle=':' , linewidth=0.4 , color='lavender')

            if (len(dfw) < 60):
                plt.plot (ToDsB1,EBNsB1 , color='teal' , linewidth=1.5)
            if (len(dfw) < 240):
                plt.plot (ToDsB1,EBNsB1 , color='teal' , linewidth=1.0)
            else :
                plt.plot (ToDsB1,EBNsB1 , color='teal' , linewidth=0.5)
            plt.savefig(DIR + 'MDB1.svg' , dpi=600 , transparent=True)
            print ('     ' , DTN[1] , 'CDMP was end of drawing Eb/N0 plot (MODEM-B1).')

    if (MD == 'MDB2'):
        df.to_csv(DIR + 'EBN_MDB2_tmp.csv', header = False , index = False , mode = 'a')
        dfw = pd.read_csv(DIR + 'EBN_MDB2_tmp.csv' , index_col = False , header = None)
        if (len(dfw)>=480):
            df = dfw.drop(df.index[0])
            df.to_csv(DIR + 'EBN_MDB2_tmp.csv', header = False , index = False , mode = 'w')

        if (len(dfw) >= 5):
            ToDsB2.append(pd.to_datetime(dfw.iloc[len(dfw)-1,0]))
            EBNsB2.append(dfw.iloc[len(dfw)-1,1])
            print (ToDsB2 , EBNsB2)
            fig , ax = plt.subplots()
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
            ax.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
            ax.axis([ToDsB2[0] , ToDsB2[len(ToDsB2)-1] , EBNsB2[0] , EBNsB2[len(EBNsB2)-1]])
            ax.set_ylim(0,16)

            plt.tick_params(which ='major',width=1 , length=3)
            plt.tick_params(which ='minor',width=0.75 , length=1.8)
            plt.minorticks_on()
            plt.xticks(fontsize=6)
            plt.xlabel('Time of day [HH:MM] / JST(UT+9H)' , fontsize=6)
            plt.yticks(fontsize=6.5)
            plt.ylabel('Eb/N0 [dB]' , fontsize=6)
            plt.title('MODEM-B2 Rx Eb/N0 Scatter Plot' , fontsize=7)
            plt.grid(which='major' , axis='both' , linestyle='--' , linewidth=0.4 , color='lavender')
            plt.grid(which='minor' , axis='both' , linestyle=':' , linewidth=0.4 , color='lavender')

            if (len(dfw) < 60):
                plt.plot (ToDsB2,EBNsB2 , color='teal' , linewidth=1.5)
            if (len(dfw) < 240):
                plt.plot (ToDsB2,EBNsB2 , color='teal' , linewidth=1.0)
            else :
                plt.plot (ToDsB2,EBNsB2 , color='teal' , linewidth=0.5)
            plt.savefig(DIR + 'MDB2.svg' , dpi=600 , transparent=True)
            print ('     ' , DTN[1] , 'CDMP was end of drawing Eb/N0 plot (MODEM-B2).')

    if (MD == 'MDC1'):
        df.to_csv(DIR + 'EBN_MDC1_tmp.csv', header = False , index = False , mode = 'a')
        dfw = pd.read_csv(DIR + 'EBN_MDC1_tmp.csv' , index_col = False , header = None)
        if (len(dfw)>=480):
            df = dfw.drop(df.index[0])
            df.to_csv(DIR + 'EBN_MDC1_tmp.csv', header = False , index = False , mode = 'w')

        if (len(dfw) >= 5):
            ToDsC1.append(pd.to_datetime(dfw.iloc[len(dfw)-1,0]))
            EBNsC1.append(dfw.iloc[len(dfw)-1,1])
            print (ToDsC1 , EBNsC1)
            ax = plt.subplots()
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
            ax.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
            ax.axis([ToDsC1[0] , ToDsC1[len(ToDsC1)-1] , EBNsC1[0] , EBNsC1[len(EBNsC1)-1]])
            ax.set_ylim(0,16)

            plt.tick_params(which ='major',width=1 , length=3)
            plt.tick_params(which ='minor',width=0.75 , length=1.8)
            plt.minorticks_on()
            plt.xticks(fontsize=6)
            plt.xlabel('Time of day [HH:MM] / JST(UT+9H)' , fontsize=6)
            plt.yticks(fontsize=6.5)
            plt.ylabel('Eb/N0 [dB]' , fontsize=6)
            plt.title('MODEM-C1 Rx Eb/N0 Scatter Plot' , fontsize=7)
            plt.grid(which='major' , axis='both' , linestyle='--' , linewidth=0.4 , color='lavender')
            plt.grid(which='minor' , axis='both' , linestyle=':' , linewidth=0.4 , color='lavender')

            if (len(dfw) < 60):
                plt.plot (ToDsC1,EBNsC1 , color='teal' , linewidth=1.5)
            if (len(dfw) < 240):
                plt.plot (ToDsC1,EBNsC1 , color='teal' , linewidth=1.0)
            else :
                plt.plot (ToDsC1,EBNsC1 , color='teal' , linewidth=0.5)
            plt.savefig(DIR + 'MDC1.svg' , dpi=600 , transparent=True)
            print ('     ' , DTN[1] , 'CDMP was end of drawing Eb/N0 plot (MODEM-C1).')

    if (MD == 'MDC2'):
        df.to_csv(DIR + 'EBN_MDC2_tmp.csv', header = False , index = False , mode = 'a')
        dfw = pd.read_csv(DIR + 'EBN_MDC2_tmp.csv' , index_col = False , header = None)
        if (len(dfw)>=480):
            df = dfw.drop(df.index[0])
            df.to_csv(DIR + 'EBN_MDC2_tmp.csv', header = False , index = False , mode = 'w')

        if (len(dfw) >= 5):
            ToDsC2.append(pd.to_datetime(dfw.iloc[len(dfw)-1,0]))
            EBNsC2.append(dfw.iloc[len(dfw)-1,1])
            print (ToDsC2 , EBNsC2)
            ax = plt.subplots()
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
            ax.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
            ax.axis([ToDsC2[0] , ToDsC2[len(ToDsC2)-1] , EBNsC2[0] , EBNsC2[len(EBNsC2)-1]])
            ax.set_ylim(0,16)

            plt.tick_params(which ='major',width=1 , length=3)
            plt.tick_params(which ='minor',width=0.75 , length=1.8)
            plt.minorticks_on()
            plt.xticks(fontsize=6)
            plt.xlabel('Time of day [HH:MM] / JST(UT+9H)' , fontsize=6)
            plt.yticks(fontsize=6.5)
            plt.ylabel('Eb/N0 [dB]' , fontsize=6)
            plt.title('MODEM-C2 Rx Eb/N0 Scatter Plot' , fontsize=7)
            plt.grid(which='major' , axis='both' , linestyle='--' , linewidth=0.4 , color='lavender')
            plt.grid(which='minor' , axis='both' , linestyle=':' , linewidth=0.4 , color='lavender')

            if (len(dfw) < 60):
                plt.plot (ToDsC2,EBNsC2 , color='teal' , linewidth=1.5)
            if (len(dfw) < 240):
                plt.plot (ToDsC2,EBNsC2 , color='teal' , linewidth=1.0)
            else :
                plt.plot (ToDsC2,EBNsC2 , color='teal' , linewidth=0.5)
            plt.savefig(DIR + 'MDC2.svg' , dpi=600 , transparent=True)
            print ('     ' , DTN[1] , 'CDMP was end of drawing Eb/N0 plot (MODEM-C2).')

    if (MD == 'MDE1'):
        df.to_csv(DIR + 'EBN_MDE1_tmp.csv', header = False , index = False , mode = 'a')
        dfw = pd.read_csv(DIR + 'EBN_MDE1_tmp.csv' , index_col = False , header = None)
        if (len(dfw)>=480):
            df = dfw.drop(df.index[0])
            df.to_csv(DIR + 'EBN_MDE1_tmp.csv', header = False , index = False , mode = 'w')

        if (len(dfw) >= 5):
            ToDsE1.append(pd.to_datetime(dfw.iloc[len(dfw)-1,0]))
            EBNsE1.append(dfw.iloc[len(dfw)-1,1])
            print (ToDsE1 , EBNsE1)
            ax = plt.subplots()
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
            ax.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
            ax.axis([ToDsE1[0] , ToDsE1[len(ToDsE1)-1] , EBNsE1[0] , EBNsE1[len(EBNsE1)-1]])
            ax.set_ylim(0,16)

            plt.tick_params(which ='major',width=1 , length=3)
            plt.tick_params(which ='minor',width=0.75 , length=1.8)
            plt.minorticks_on()
            plt.xticks(fontsize=6)
            plt.xlabel('Time of day [HH:MM] / JST(UT+9H)' , fontsize=6)
            plt.yticks(fontsize=6.5)
            plt.ylabel('Eb/N0 [dB]' , fontsize=6)
            plt.title('MODEM-E1 Rx Eb/N0 Scatter Plot' , fontsize=7)
            plt.grid(which='major' , axis='both' , linestyle='--' , linewidth=0.4 , color='lavender')
            plt.grid(which='minor' , axis='both' , linestyle=':' , linewidth=0.4 , color='lavender')

            if (len(dfw) < 60):
                plt.plot (ToDsE1,EBNsE1 , color='teal' , linewidth=1.5)
            if (len(dfw) < 240):
                plt.plot (ToDsE1,EBNsE1 , color='teal' , linewidth=1.0)
            else :
                plt.plot (ToDsE1,EBNsE1 , color='teal' , linewidth=0.5)
            plt.savefig(DIR + 'MDE1.svg' , dpi=600 , transparent=True)
            print ('     ' , DTN[1] , 'CDMP was end of drawing Eb/N0 plot (MODEM-E1).')

    if (MD == 'MDE2'):
        df.to_csv(DIR + 'EBN_MDE2_tmp.csv', header = False , index = False , mode = 'a')
        dfw = pd.read_csv(DIR + 'EBN_MDE2_tmp.csv' , index_col = False , header = None)
        if (len(dfw)>=480):
            df = dfw.drop(df.index[0])
            df.to_csv(DIR + 'EBN_MDE2_tmp.csv', header = False , index = False , mode = 'w')

        if (len(dfw) >= 5):
            ToDsE2.append(pd.to_datetime(dfw.iloc[len(dfw)-1,0]))
            EBNsE2.append(dfw.iloc[len(dfw)-1,1])
            print (ToDsE2 , EBNsE2)
            ax = plt.subplots()
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
            ax.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
            ax.axis([ToDsE2[0] , ToDsE2[len(ToDsE2)-1] , EBNsE2[0] , EBNsE2[len(EBNsE2)-1]])
            ax.set_ylim(0,16)

            plt.tick_params(which ='major',width=1 , length=3)
            plt.tick_params(which ='minor',width=0.75 , length=1.8)
            plt.minorticks_on()
            plt.xticks(fontsize=6)
            plt.xlabel('Time of day [HH:MM] / JST(UT+9H)' , fontsize=6)
            plt.yticks(fontsize=6.5)
            plt.ylabel('Eb/N0 [dB]' , fontsize=6)
            plt.title('MODEM-E2 Rx Eb/N0 Scatter Plot' , fontsize=7)
            plt.grid(which='major' , axis='both' , linestyle='--' , linewidth=0.4 , color='lavender')
            plt.grid(which='minor' , axis='both' , linestyle=':' , linewidth=0.4 , color='lavender')

            if (len(dfw) < 60):
                plt.plot (ToDsE2,EBNsE2 , color='teal' , linewidth=1.5)
            if (len(dfw) < 240):
                plt.plot (ToDsE2,EBNsE2 , color='teal' , linewidth=1.0)
            else :
                plt.plot (ToDsE2,EBNsE2 , color='teal' , linewidth=0.5)
            plt.savefig(DIR + 'MDE2.svg' , dpi=600 , transparent=True)
            print ('     ' , DTN[1] , 'CDMP was end of drawing Eb/N0 plot (MODEM-E2).')
