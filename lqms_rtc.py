# #################################################################
# ### LQMS-2.0 for JAXA-Tanegashima E/S . RCC                   ###
# ### Release date 2022.10                                      ###
# ###   *Web Scraping Router Counters                           ###
# ### Version 0.3.3                       TechnoBusiness Co.LTD ###
# #################################################################
VER = '0.3.3'

import lqms_dt
import csv
from bs4 import BeautifulSoup
import requests
import os

FN1 = '/mnt/ssd/log/error/err_'
FN2 = '/mnt/ssd/log/facl/sys_'

def ST(IPA):

    try:

        os.chdir('/home/xs4/basis/')

        DTN = lqms_dt.RTC_CHK()

        RCT = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
        RCS = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
        RCT_1 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
        DPT = ['','','','','','','','','','','']
        DPS = ['','','','','','','','','','','']
        DPT_1 = ['','','','','','','','','','','']
        FPC = ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
        FPS = ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
        FPC_1 = ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']

        # Reading HLD data file
        if (IPA == '192.168.1.11'):
            MD = 'MDA1'
            MD2 = ' IP MODEM-A1 '
            FLN1 = 'MDA1_RTC_TMP.csv'
            FLN2 = 'MDA1_DPT_TMP.csv'
            FLN3 = 'MDA1_FPC_TMP.csv'
            FN3 = '/mnt/ssd/log/mda1/MDA1_'
        elif (IPA == '192.168.1.12'):
            MD = 'MDA2'
            MD2 = ' IP MODEM-A2 '
            FLN1 = 'MDA2_RTC_TMP.csv'
            FLN2 = 'MDA2_DPT_TMP.csv'
            FLN3 = 'MDA2_FPC_TMP.csv'
            FN3 = '/mnt/ssd/log/mda2/MDA2_'
        elif (IPA == '192.168.1.21'):
            MD = 'MDB1'
            MD2 = ' IP MODEM-B1 '
            FLN1 = 'MDB1_RTC_TMP.csv'
            FLN2 = 'MDB1_DPT_TMP.csv'
            FLN3 = 'MDB1_FPC_TMP.csv'
            FN3 = '/mnt/ssd/log/mdb1/MDB1_'
        elif (IPA == '192.168.1.22'):
            MD = 'MDB2'
            MD2 = ' IP MODEM-B2 '
            FLN1 = 'MDB2_RTC_TMP.csv'
            FLN2 = 'MDB2_DPT_TMP.csv'
            FLN3 = 'MDB2_FPC_TMP.csv'
            FN3 = '/mnt/ssd/log/mdb2/MDB2_'
        elif (IPA == '192.168.1.23'):
            MD = 'MDC1'
            MD2 = ' IP MODEM-C1 '
            FLN1 = 'MDC1_RTC_TMP.csv'
            FLN2 = 'MDC1_DPT_TMP.csv'
            FLN3 = 'MDC1_FPC_TMP.csv'
            FN3 = '/mnt/ssd/log/mdc1/MDC1_'
        elif (IPA == '192.168.1.24'):
            MD = 'MDC2'
            MD2 = ' IP MODEM-C2 '
            FLN1 = 'MDC2_RTC_TMP.csv'
            FLN2 = 'MDC2_DPT_TMP.csv'
            FLN3 = 'MDC2_FPC_TMP.csv'
            FN3 = '/mnt/ssd/log/mdc2/MDC2_'
        elif (IPA == '192.168.1.25'):
            MD = 'MDE1'
            MD2 = ' IP MODEM-E1 '
            FLN1 = 'MDE1_RTC_TMP.csv'
            FLN2 = 'MDE1_DPT_TMP.csv'
            FLN3 = 'MDE1_FPC_TMP.csv'
            FN3 = '/mnt/ssd/log/mde1/MDE1_'
        elif (IPA == '192.168.1.26'):
            MD = 'MDE2'
            MD2 = ' IP MODEM-E2 '
            FLN1 = 'MDE2_RTC_TMP.csv'
            FLN2 = 'MDE2_DPT_TMP.csv'
            FLN3 = 'MDE2_FPC_TMP.csv'
            FN3 = '/mnt/ssd/log/mde2/MDE2_'

        fld = '/home/xs4/basis/req_relFiles/'
        FLN1 = fld + FLN1
        FLN2 = fld + FLN2
        FLN3 = fld + FLN3

        # File Check
        with open(FLN1) as f:
            reader = csv.reader(f)
            RCT_1 = [row for row in reader]

    #    print(RCT_1[0][0],RCT_1[0][1],RCT_1[0][2],RCT_1[0][3],RCT_1[0][4],RCT_1[0][5],RCT_1[0][6],RCT_1[0][7],RCT_1[0][8],RCT_1[0][9],RCT_1[0][10],RCT_1[0][11],RCT_1[0][12],RCT_1[0][13])
        URL = 'http://' + IPA + ':8080/pp_status_trafficstats_router.htm'

        # MODEM Traffic Statistics | Router
        res = requests.get(URL,auth=('comtech','comtech'))
        content = res.content
        soup = BeautifulSoup(content, 'html.parser')
        print ('          ',DTN[1],'\033[1m\033[44m\033[37m\033[1m M/D \033[0m  Router Counter Monitor & Recorder.                                        lqms_rtc.py Ver.' + VER)
        with open(FN2 + DTN[5] + '.log', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([DTN[0], DTN[1], MD, 'RTC','Web Analysis', 'Router Counters'])

        ###############################
        #Router Counters
        ###############################
        cot = 0
        for Co in range ( 5 , 33 , 2 ):
            if Co < 9 :
                RCS[cot] = (soup.select('body td')[Co].string).replace('\n','')
                RCT[cot] = (soup.select('body td')[Co+1].string).replace('\n','')
            else:
                RCS[cot] = (soup.select('td')[Co].string).replace('\n','')
                RCT[cot] = (soup.select('td')[Co+1].string).replace('\n','')
    #        print (cot , RCS[cot] , RCT[cot])

            # Recording LOG ( only data with state change )
            if (RCT_1[0][cot] != RCT[cot]):
                RCT_1[0][cot] = RCT[cot]
    #            print ('RCT-1 :' + RCT_1[0][cot] , 'RCT   :' + RCT[cot], cot)
                DTN = lqms_dt.RTC_CHK()
                # Log Record ( Unit log )
                with open(FN3 + DTN[5] + '.log', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([DTN[0], DTN[1], MD, 'RCT', RCS[cot], RCT[cot]])
            cot += 1
    #    print(RCT[0],RCT[1],RCT[2],RCT[3],RCT[4],RCT[5],RCT[6],RCT[7],RCT[8],RCT[9],RCT[10],RCT[11],RCT[12],RCT[13])
        # Recording HLD ( all data about for compare to next data )
        with open(FLN1, 'w') as f:
            writer = csv.writer(f)
            writer.writerow([RCT[0],RCT[1],RCT[2],RCT[3],RCT[4],RCT[5],RCT[6],RCT[7],RCT[8],RCT[9],RCT[10],RCT[11],RCT[12],RCT[13]])
        DTN = lqms_dt.RTC_CHK()
        print ('          ',DTN[1], '\33[1m\033[44m\033[37m' + ' M/D ' + '\033[0m' + '  \033[1m\033[42m\033[37m  NOM  \033[0m \033[1m\033[32m' + MD2 + 'Finished processing for Router Counters.' + '\033[0m             lqms_rtc.py Ver.' + VER)

        ###############################
        #Dropped Packets
        ###############################
        # File Check
        with open(FLN2) as f:
            reader = csv.reader(f)
            DPT_1 = [row for row in reader]

    #    print(DPT_1[0][0],DPT_1[0][1],DPT_1[0][2],DPT_1[0][3],DPT_1[0][4],DPT_1[0][5],DPT_1[0][6],DPT_1[0][7],DPT_1[0][8],DPT_1[0][9],DPT_1[0][10])
        cot = 0
        dpt = ''
        with open(FN2 + DTN[5] + '.log', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([DTN[0], DTN[1], MD, 'DRP','Web Analysis', 'Dropped Packets'])
        for Co in range ( 35 , 56 , 2 ):
            DPS[cot] = (soup.select('td')[Co].string).replace('\n','')
            DPT[cot] = (soup.select('td')[Co + 1].string).replace('\n','')
            #print (cot , DPS[cot] , DPT[cot])

            if (DPT_1[0][cot] != DPT[cot]):
                DPT_1[0][cot] = DPT[cot]
                DTN = lqms_dt.RTC_CHK()
                with open(FN3 + DTN[5] + '.log', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([DTN[0], DTN[1], MD, 'DRP', DPS[cot], DPT[cot]])
            cot = cot + 1
        #print(DPT[0],DPT[1],DPT[2],DPT[3],DPT[4],DPT[5],DPT[6],DPT[7],DPT[8],DPT[9],DPT[10])
        # Recording HLD ( all data about for compare to next data )
        with open(FLN2, 'w') as f:
            writer = csv.writer(f)
            writer.writerow([DPT[0],DPT[1],DPT[2],DPT[3],DPT[4],DPT[5],DPT[6],DPT[7],DPT[8],DPT[9],DPT[10]])
        DTN = lqms_dt.RTC_CHK()
        print ('          ',DTN[1], '\33[1m\033[44m\033[37m' + ' M/D ' + '\033[0m' + '  \033[1m\033[42m\033[37m  NOM  \033[0m \033[1m\033[32m' + MD2 + 'Finished processing for Dropped Packets Counters.' + '\033[0m    lqms_rtc.py Ver.' + VER)

        ###############################
        #Filetered Packets
        ###############################
        # File Check
        with open(FLN3) as f:
            reader = csv.reader(f)
            FPC_1 = [row for row in reader]

        #print(FPC_1[0][0],FPC_1[0][1],FPC_1[0][2],FPC_1[0][3],FPC_1[0][4],FPC_1[0][5],FPC_1[0][6],FPC_1[0][7],FPC_1[0][8],FPC_1[0][9],FPC_1[0][10],FPC_1[0][11],FPC_1[0][12],FPC_1[0][13],FPC_1[0][14],FPC_1[0][15],FPC_1[0][16],FPC_1[0][17],FPC_1[0][18],FPC_1[0][19],FPC_1[0][20],FPC_1[0][21],FPC_1[0][22],FPC_1[0][23],FPC_1[0][24],FPC_1[0][25],FPC_1[0][26])
        cot = 0
        with open(FN2 + DTN[5] + '.log', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([DTN[0], DTN[1], MD, 'FIL','Web Analysis', 'Filtered Packets'])
        for Co in range ( 59 , 112 , 2 ):
            FPS[cot] = (soup.select('td')[Co].string).replace('\n','')
            FPC[cot] = (soup.select('td')[Co + 1].string).replace('\n','')
            #print (cot , FPS[cot] , FPC[cot])

            if (FPC_1[0][cot] != FPC[cot]):
                FPC_1[0][cot] = FPC[cot]
                DTN = lqms_dt.RTC_CHK()
                with open(FN3 + DTN[5] + '.log', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([DTN[0], DTN[1], MD, 'FIL', FPS[cot], FPC[cot]])
            cot = cot + 1
        #print(FPC[0],FPC[1],FPC[2],FPC[3],FPC[4],FPC[5],FPC[6],FPC[7],FPC[8],FPC[9],FPC[10],FPC[11],FPC[12],FPC[13],FPC[14],FPC[15],FPC[16],FPC[17],FPC[18],FPC[19],FPC[20],FPC[21],FPC[22],FPC[23],FPC[24],FPC[25],FPC[26])
        # Recording HLD ( all data about for compare to next data )
        with open(FLN3,mode = 'w') as f:
            writer = csv.writer(f)
            writer.writerow([FPC[0],FPC[1],FPC[2],FPC[3],FPC[4],FPC[5],FPC[6],FPC[7],FPC[8],FPC[9],FPC[10],FPC[11],FPC[12],FPC[13],FPC[14],FPC[15],FPC[16],FPC[17],FPC[18],FPC[19],FPC[20],FPC[21],FPC[22],FPC[23],FPC[24],FPC[25],FPC[26]])
        DTN = lqms_dt.RTC_CHK()
        print ('          ',DTN[1], '\33[1m\033[44m\033[37m' + ' M/D ' + '\033[0m' + '  \033[1m\033[42m\033[37m  NOM  \033[0m \033[1m\033[32m' + MD2 + 'Finished processing for Filtered Packets Counters.' + '\033[0m   lqms_rtc.py Ver.' + VER)
    
    except Exception as e:
        print ('          ',DTN[1], '\33[1m\033[44m\033[37m' + ' M/D ' + '\033[0m' + '  \033[1m\033[41m\033[37m FAULT \033[0m \033[1m\033[31m' + MD2 + ' Something Error in Router Counter Scraping Process.' + '\033[0m    lqms_rtc.py Ver.' + VER)
