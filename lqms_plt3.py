# #################################################################
# ### LQMS-2.0 for JAXA-Tanegashima E/S . RCC                   ###
# ### Release date 2022.10                                      ###
# ###   *Plotter for Forward Power Level                        ###
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
VER = '1.5.6'

df = pd.DataFrame([[],[]])
df = df.drop(df.index[0])
INI_PRM = 99
ToDsKuBUCA = []
ToDsKuBUCB = []
ToDsCBUCA = []
ToDsCBUCB = []
PWRKuBUCA = []
PWRKuBUCB = []
PWRCBUCA = []
PWRCBUCB = []

def ST(data,BUC):
    global sum
    global Co
    global df
    DTN = lqms_dt.RTC_CHK()
    print ('          ',DTN[1],'\033[1m\033[46m\033[37m\033[1m BUC \033[0m  CDMP Forward Power plot.\033[0m' + '                                                  lqms_plt3.py Ver.' + VER)
    BL = float(data)
    ToD = lqms_dt.RTC_CHK()
    df = pd.DataFrame([{'1':ToD[1] ,'2': BL}])

    DIR = '/home/xs4/basis/req_relFiles/'

    if (BUC == 'KuBUC-A'):
        with open(DIR + 'FPW_KuBUC-A.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([ToD[1] , BL])
        dfw = pd.read_csv(DIR + 'FPW_KuBUC-A.csv' , index_col = False , header = None)
        if (len(dfw)>=480):
            df = dfw.drop(df.index[0])
            df.to_csv(DIR + 'FPW_KuBUC-A.csv', header = False , index = False , mode = 'w')
        if (len(dfw) >= 5):
            ToDsKuBUCA.append(pd.to_datetime(dfw.iloc[len(dfw)-1,0]))
            PWRKuBUCA.append(dfw.iloc[len(dfw)-1,1])
            ax = plt.subplot()
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
            ax.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
            ax.axis([ToDsKuBUCA[0] , ToDsKuBUCA[len(ToDsKuBUCA)-1] , PWRKuBUCA[0] , PWRKuBUCA[len(PWRKuBUCA)-1]])
            ax.set_ylim(10,50)

            plt.tick_params(which ='major',width=1 , length=3)
            plt.tick_params(which ='minor',width=0.75 , length=1.8)
            plt.minorticks_on()
            plt.xticks(fontsize=6)
            plt.xlabel('Time of day [HH:MM] / JST(UT+9H)' , fontsize=6)
            plt.yticks(fontsize=6.5)
            plt.ylabel('Forward Power [dB]' , fontsize=6)
            plt.title('Ku-Band BUC-A Forward Power Scatter Plot' , fontsize=7)
            plt.grid(which='major' , axis='both' , linestyle='--' , linewidth=0.4 , color='grey')
            plt.grid(which='minor' , axis='both' , linestyle=':' , linewidth=0.4 , color='grey')

            if (len(dfw) < 60):
                plt.plot (ToDsKuBUCA, PWRKuBUCA , color='darkturquoise' , linewidth=1.5)
            if (len(dfw) < 240):
                plt.plot (ToDsKuBUCA, PWRKuBUCA , color='darkturquoise' , linewidth=1.0)
            else :
                plt.plot (ToDsKuBUCA, PWRKuBUCA , color='darkturquoise' , linewidth=0.5)
            plt.savefig(DIR + 'KuBUC-A.svg' , dpi=600 , transparent=True)
            print ('          ',DTN[1],'\033[1m\033[46m\033[37m\033[1m BUC \033[0m  CDMP was end of drawing Forward Power plot (Ku-Band BUC-A).               lqms_plt3.py Ver.' + VER)

    elif (BUC == 'KuBUC-B'):
        with open(DIR + 'FPW_KuBUC-B.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([ToD[1] , BL])
        dfw = pd.read_csv(DIR + 'FPW_KuBUC-B.csv' , index_col = False , header = None)
        if (len(dfw)>=480):
            df = dfw.drop(df.index[0])
            df.to_csv(DIR + 'FPW_KuBUC-B.csv', header = False , index = False , mode = 'w')
        if (len(dfw) >= 5):
            ToDsKuBUCB.append(pd.to_datetime(dfw.iloc[len(dfw)-1,0]))
            PWRKuBUCB.append(dfw.iloc[len(dfw)-1,1])
            #print (ToDsKuB , LVKuB)
            ax = plt.subplot()
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
            ax.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
            ax.axis([ToDsKuBUCB[0] , ToDsKuBUCB[len(ToDsKuBUCB)-1] , PWRKuBUCB[0] , PWRKuBUCB[len(PWRKuBUCB)-1]])
            ax.set_ylim(10,50)

            plt.tick_params(which ='major',width=1 , length=3)
            plt.tick_params(which ='minor',width=0.75 , length=1.8)
            plt.minorticks_on()
            plt.xticks(fontsize=6)
            plt.xlabel('Time of day [HH:MM] / JST(UT+9H)' , fontsize=6)
            plt.yticks(fontsize=6.5)
            plt.ylabel('Forward Power [dB]' , fontsize=6)
            plt.title('Ku-Band BUC-B Forward Power Scatter Plot' , fontsize=7)
            plt.grid(which='major' , axis='both' , linestyle='--' , linewidth=0.4 , color='lavender')
            plt.grid(which='minor' , axis='both' , linestyle=':' , linewidth=0.4 , color='lavender')

            if (len(dfw) < 60):
                plt.plot (ToDsKuBUCB,PWRKuBUCB , color='darkturquoise' , linewidth=1.5)
            if (len(dfw) < 240):
                plt.plot (ToDsKuBUCB,PWRKuBUCB , color='darkturquoise' , linewidth=1.0)
            else :
                plt.plot (ToDsKuBUCB,PWRKuBUCB , color='darkturquoise' , linewidth=0.5)
            plt.savefig(DIR + 'KuBUC-B.svg' , dpi=600 , transparent=True)
            print ('          ',DTN[1],'\033[1m\033[46m\033[37m\033[1m BUC \033[0m  CDMP was end of drawing Forward Power plot (Ku-Band BUC-B).               lqms_plt3.py Ver.' + VER)

    elif (BUC == 'CBUC-A'):
        with open(DIR + 'FPW_CBUC-A.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([ToD[1] , BL])
        dfw = pd.read_csv(DIR + 'FPW_CBUC-A.csv' , index_col = False , header = None)
        if (len(dfw)>=480):
            df = dfw.drop(df.index[0])
            df.to_csv(DIR + 'FPW_CBUC-A.csv', header = False , index = False , mode = 'w')
        if (len(dfw) >= 5):
            ToDsCBUCA.append(pd.to_datetime(dfw.iloc[len(dfw)-1,0]))
            PWRCBUCA.append(dfw.iloc[len(dfw)-1,1])
            ax = plt.subplot()
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
            ax.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
            ax.axis([ToDsCBUCA[0] , ToDsCBUCA[len(ToDsCBUCA)-1] , PWRCBUCA[0] , PWRCBUCA[len(PWRCBUCA)-1]])
            ax.set_ylim(10,50)

            plt.tick_params(which ='major',width=1 , length=3)
            plt.tick_params(which ='minor',width=0.75 , length=1.8)
            plt.minorticks_on()
            plt.xticks(fontsize=6)
            plt.xlabel('Time of day [HH:MM] / JST(UT+9H)' , fontsize=6)
            plt.yticks(fontsize=6.5)
            plt.ylabel('Forward Power [dB]' , fontsize=6)
            plt.title('C-Band BUC-A Forward Power Scatter Plot' , fontsize=7)
            plt.grid(which='major' , axis='both' , linestyle='--' , linewidth=0.4 , color='grey')
            plt.grid(which='minor' , axis='both' , linestyle=':' , linewidth=0.4 , color='grey')

            if (len(dfw) < 60):
                plt.plot (ToDsCBUCA, PWRCBUCA , color='darkturquoise' , linewidth=1.5)
            if (len(dfw) < 240):
                plt.plot (ToDsCBUCA, PWRCBUCA , color='darkturquoise' , linewidth=1.0)
            else :
                plt.plot (ToDsCBUCA, PWRCBUCA , color='darkturquoise' , linewidth=0.5)
            plt.savefig(DIR + 'CBUC-A.svg' , dpi=600 , transparent=True)
            print ('          ',DTN[1],'\033[1m\033[46m\033[37m\033[1m BUC \033[0m  CDMP was end of drawing Forward Power plot (C-Band BUC-A).                lqms_plt3.py Ver.' + VER)

    elif (BUC == 'CBUC-B'):
        with open(DIR + 'FPW_CBUC-B.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([ToD[1] , BL])
        dfw = pd.read_csv(DIR + 'FPW_CBUC-B.csv' , index_col = False , header = None)
        if (len(dfw)>=480):
            df = dfw.drop(df.index[0])
            df.to_csv(DIR + 'FPW_CBUC-B.csv', header = False , index = False , mode = 'w')
        if (len(dfw) >= 5):
            ToDsCBUCB.append(pd.to_datetime(dfw.iloc[len(dfw)-1,0]))
            PWRCBUCB.append(dfw.iloc[len(dfw)-1,1])
            #print (ToDsKuB , LVKuB)
            ax = plt.subplot()
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
            ax.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
            ax.axis([ToDsCBUCB[0] , ToDsCBUCB[len(ToDsCBUCB)-1] , PWRCBUCB[0] , PWRCBUCB[len(PWRCBUCB)-1]])
            ax.set_ylim(10,50)

            plt.tick_params(which ='major',width=1 , length=3)
            plt.tick_params(which ='minor',width=0.75 , length=1.8)
            plt.minorticks_on()
            plt.xticks(fontsize=6)
            plt.xlabel('Time of day [HH:MM] / JST(UT+9H)' , fontsize=6)
            plt.yticks(fontsize=6.5)
            plt.ylabel('Forward Power [dB]' , fontsize=6)
            plt.title('C-Band BUC-B Forward Power Scatter Plot' , fontsize=7)
            plt.grid(which='major' , axis='both' , linestyle='--' , linewidth=0.4 , color='lavender')
            plt.grid(which='minor' , axis='both' , linestyle=':' , linewidth=0.4 , color='lavender')

            if (len(dfw) < 60):
                plt.plot (ToDsCBUCB,PWRCBUCB , color='darkturquoise' , linewidth=1.5)
            if (len(dfw) < 240):
                plt.plot (ToDsCBUCB,PWRCBUCB , color='darkturquoise' , linewidth=1.0)
            else :
                plt.plot (ToDsCBUCB,PWRCBUCB , color='darkturquoise' , linewidth=0.5)
            plt.savefig(DIR + 'CBUC-B.svg' , dpi=600 , transparent=True)
            print ('          ',DTN[1],'\033[1m\033[46m\033[37m\033[1m BUC \033[0m  CDMP was end of drawing Forward Power plot (C-Band BUC-B).                lqms_plt3.py Ver.' + VER)
