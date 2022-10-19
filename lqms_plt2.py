# #################################################################
# ### LQMS-2.0 for JAXA-Tanegashima E/S . RCC                   ###
# ### Release date 2022.10                                      ###
# ###   *Plotter for Beacon Carrier Level                       ###
# ### Version 1.5.6                       TechnoBusiness Co.LTD ###
# #################################################################
VER = '1.5.6'

import pandas as pd
import numpy as np
import csv
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import MultipleLocator,FormatStrFormatter

import lqms_dt
import os

df = pd.DataFrame([[],[]])
df = df.drop(df.index[0])
INI_PRM = 99
ToDsCB = []
ToDsKuB = []
LVCB = []
LVKuB = []

def ST(data,UPC):
    global sum
    global Co
    global df
    DTN = lqms_dt.RTC_CHK()
    print ('          ',DTN[1],'\033[1m\033[42m\033[37m\033[1m UPC \033[0m  CDMP Beacon Level Plotter.                                                lqms_plt2.py Ver.' + VER)
    BL = float(data)
    ToD = lqms_dt.RTC_CHK()
    df = pd.DataFrame([{'1':ToD[1] ,'2': BL}])

    DIR = '/home/xs4/basis/req_relFiles/'

    if (UPC == 'C-Band'):
        with open(DIR + 'BL_CB_tmp.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([ToD[1] , BL])
        dfw = pd.read_csv(DIR + 'BL_CB_tmp.csv' , index_col = False , header = None)
        if (len(dfw)>=480):
            df = dfw.drop(df.index[0])
            df.to_csv(DIR + 'BL_CB_tmp.csv', header = False , index = False , mode = 'w')
        if (len(dfw) >= 5):
            ToDsCB.append(pd.to_datetime(dfw.iloc[len(dfw)-1,0]))
            LVCB.append(dfw.iloc[len(dfw)-1,1])
            ax = plt.subplot()
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
            ax.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
            ax.axis([ToDsCB[0] , ToDsCB[len(ToDsCB)-1] , LVCB[0] , LVCB[len(LVCB)-1]])
            ax.set_ylim(-80,-50)

            plt.tick_params(which ='major',width=1 , length=3)
            plt.tick_params(which ='minor',width=0.75 , length=1.8)
            plt.minorticks_on()
            plt.xticks(fontsize=6)
            plt.xlabel('Time of day [HH:MM] / JST(UT+9H)' , fontsize=6)
            plt.yticks(fontsize=6.5)
            plt.ylabel('Beacon Level [dB]' , fontsize=6)
            plt.title('C-Band UPC Rx Beacon Level Scatter Plot' , fontsize=7)
            plt.grid(which='major' , axis='both' , linestyle='--' , linewidth=0.4 , color='grey')
            plt.grid(which='minor' , axis='both' , linestyle=':' , linewidth=0.4 , color='grey')

            if (len(dfw) < 60):
                plt.plot (ToDsCB, LVCB , color='darkorange' , linewidth=1.5)
            if (len(dfw) < 240):
                plt.plot (ToDsCB, LVCB , color='darkorange' , linewidth=1.0)
            else :
                plt.plot (ToDsCB, LVCB , color='darkorange' , linewidth=0.5)
            plt.savefig(DIR + 'CBUPC.svg' , dpi=600 , transparent=True)
            print ('          ',DTN[1],'\033[1m\033[42m\033[37m\033[1m UPC \033[0m  CDMP was end of drawing Beacon Level plot (C-Band).                       lqms_plt2.py Ver.' + VER)

    if (UPC == 'Ku-Band'):
        with open(DIR + 'BL_KuB_tmp.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([ToD[1] , BL])
        dfw = pd.read_csv(DIR + 'BL_KuB_tmp.csv' , index_col = False , header = None)
        if (len(dfw)>=480):
            df = dfw.drop(df.index[0])
            df.to_csv(DIR + 'BL_KuB_tmp.csv', header = False , index = False , mode = 'w')
        if (len(dfw) >= 5):
            ToDsKuB.append(pd.to_datetime(dfw.iloc[len(dfw)-1,0]))
            LVKuB.append(dfw.iloc[len(dfw)-1,1])
            #print (ToDsKuB , LVKuB)
            ax = plt.subplot()
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
            ax.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
            ax.axis([ToDsKuB[0] , ToDsKuB[len(ToDsKuB)-1] , LVKuB[0] , LVKuB[len(LVKuB)-1]])
            ax.set_ylim(-80,-50)

            plt.tick_params(which ='major',width=1 , length=3)
            plt.tick_params(which ='minor',width=0.75 , length=1.8)
            plt.minorticks_on()
            plt.xticks(fontsize=6)
            plt.xlabel('Time of day [HH:MM] / JST(UT+9H)' , fontsize=6)
            plt.yticks(fontsize=6.5)
            plt.ylabel('Beacon Level [dB]' , fontsize=6)
            plt.title('Ku-Band UPC Rx Beacon Level Scatter Plot' , fontsize=7)
            plt.grid(which='major' , axis='both' , linestyle='--' , linewidth=0.4 , color='lavender')
            plt.grid(which='minor' , axis='both' , linestyle=':' , linewidth=0.4 , color='lavender')

            if (len(dfw) < 60):
                plt.plot (ToDsKuB,LVKuB , color='darkorange' , linewidth=1.5)
            if (len(dfw) < 240):
                plt.plot (ToDsKuB,LVKuB , color='darkorange' , linewidth=1.0)
            else :
                plt.plot (ToDsKuB,LVKuB , color='darkorange' , linewidth=0.5)
            plt.savefig(DIR + 'KUBUPC.svg' , dpi=600 , transparent=True)
            print ('          ',DTN[1],'\033[1m\033[42m\033[37m\033[1m UPC \033[0m  CDMP was end of drawing Beacon Level plot (Ku-Band).                      lqms_plt2.py Ver.' + VER)
