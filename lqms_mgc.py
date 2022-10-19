# #################################################################
# ### LQMS-2.0 for JAXA-Tanegashima E/S . RCC                   ###
# ### Release date 2022.10                                      ###
# ###  *MGC Command Query                                       ###                               
# ### Version 0.3.2                       TechnoBusiness Co.LTD ###
# #################################################################
VER = '0.3.2'

import lqms_dt
import os
import csv

FN2 = '/mnt/ssd/log/facl/sys_'

def ST(RxDAT):
    DTN = lqms_dt.RTC_CHK()
    STx = RxDAT[0:1]
    ADD = RxDAT[1:5]
    CMD = RxDAT[6:9]
    ACK = RxDAT[9:10]
    RxPLD = RxDAT[10:]

    if (ADD == '0011'):
        MD1 = 'mda1'
        MD2 = ' IP MODEM-A1 '
        DEF_FL = 'MDA1_MGC_DEF.csv'
    elif (ADD == '0012'):
        MD1 = 'mda2'
        MD2 = 'MODEM-A2'
        DEF_FL = 'MDA2_MGC_DEF.csv'
    elif (ADD == '0013'):
        MD1 = 'mdb1'
        MD2 = ' IP MODEM-B1 '
        DEF_FL = 'MDB1_MGC_DEF.csv'
    elif (ADD == '0014'):
        MD1 = 'mdb2'
        MD2 = ' IP MODEM-B2 '
        DEF_FL = 'MDB2_MGC_DEF.csv'
    elif (ADD == '0015'):
        MD1 = 'mdc1'
        MD2 = ' IP MODEM-C1 '
        DEF_FL = 'MDC1_MGC_DEF.csv'
    elif (ADD == '0016'):
        MD1 = 'mdc2'
        MD2 = ' IP MODEM-C2 '
        DEF_FL = 'MDC2_MGC_DEF.csv'
    elif (ADD == '0017'):
        MD1 = 'mde1'
        MD2 = ' IP MODEM-E1 '
        DEF_FL = 'MDE1_MGC_DEF.csv'
    elif (ADD == '0018'):
        MD1 = 'mde2'
        MD2 = ' IP MODEM-E2 '
        DEF_FL = 'MDE2_MGC_DEF.csv'
    else:
        MD = 'unidentified'

    fld = '/home/xs4/basis/req_relFiles/'
    DEF_FL = fld + DEF_FL

    print ('          ',DTN[1],'\033[1m\033[44m\033[37m\033[1m M/D \033[0m  MGC Command Query.                                                        lqms_mgc.py Ver.' + VER )
    with open(FN2 + DTN[5] + '.log', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([DTN[0], DTN[1], MD2, 'MGC', 'Query MGC'])

    DEF_PRM = [ '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

    # File Check
    is_file = os.path.isfile(DEF_FL)
    c=0
    if is_file:
        with open(DEF_FL) as f:
            reader = csv.reader(f)
            DEF_PRM = [row for row in reader]

    if (STx == '>' ):
        if ( ACK == '='):
            ERR1 = 0
            ERR2 = 0
            DTN = lqms_dt.RTC_CHK()
            # ITF = RxPLD[0:1]	# Unit Interface Type
            # LBO = RxPLD[1:2]	# T1 Line build-out
            # FRM = RxPLD[2:3]	# Unit Framing Mode
            TFQ = RxPLD[3:12]	# 01.Tx Frequency
            TFT = RxPLD[12:13]	# 02.Tx FEC Type
            TMD = RxPLD[13:14]	# 03.Tx Modulation Type
            TCR = RxPLD[14:15]	# 04.Tx FEC Rate
            TDR = RxPLD[15:24]	# 05.Tx Data Rate
            TSI = RxPLD[24:25]	# 06.Tx Spectrum Inversion
            TSC = RxPLD[25:26]	# 07.Tx Scrambler State
            TPL = RxPLD[26:30]	# 08.Tx Power Level
            # TCK = RxPLD[30:31]	# Tx Clock Source
            TDI = RxPLD[31:32]	# 09.Tx Data Invert
            TXO = RxPLD[32:33]	# 10.Tx Carrier State
            # AUP = RxPLD[33:34]	# AUPC Enable
            # APP = RxPLD[34:40]	# AUPC Parameter Setup
            # WUD = RxPLD[40:41]	# Warm up Delay
            # CEX = RxPLD[41:43]	# G.703 Clock Extension
            TXA = RxPLD[43:44]	# 11.Tx Alpha
            TCI = RxPLD[44:45]	# 12.Tx Clock Invert
            # xx1 = RxPLD[45:48]	# OPTION1
            RFQ = RxPLD[48:57]	# 13.Rx Frequency
            RFT = RxPLD[57:58]	# 14.Rx FEC Type
            RMD = RxPLD[58:59]	# 15.Rx Demodulation Type
            RCR = RxPLD[59:60]	# 16.Rx FEC Rate
            RDR = RxPLD[60:69]	# 17.Rx Data Rate
            RSI = RxPLD[69:70]	# 18.Rx Spectrum Inversion
            RDS = RxPLD[70:71]	# 19.Rx Descrambler State
            RDI = RxPLD[71:72]	# 20.Rx Data Invert
            RSW = RxPLD[72:75]	# 21.Rx Sweep Wodth
            EBA = RxPLD[75:79]	# 22.Eb/N0 ALM Point
            # RBS = RxPLD[79:80]	# Ex Buffer Size
            RXA = RxPLD[80:81]	# 23.Rx Alpha
            RCI = RxPLD[81:82]	# 24.Rx Clock Invert
            # xx2 = RxPLD[82:88]	# OPTION2
            # ERF = RxPLD[88:89]	# External Reference Frequency
            # EFM = RxPLD[89:90]	# EDMAC Framing Mode
            # ESA = RxPLD[90:94]	# EDMAC Slave Address
            # TST = RxPLD[94:95]	# Unit Test Mode
            # MSK = RxPLD[95:107]	# Unit Alarm Mask
            # RTS = RxPLD[107:108]	# RTS/CTS Control
            # SSI = RxPLD[108:109]	# Statistics Sampling Interval
            # ABA = RxPLD[109:110]	# Attach BUC Alarm to Tx Alarm
            # ALA = RxPLD[110:111]	# Arrach LNB Alarm to Rx Alarm
            # xx3 = RxPLD[111:117]	# OPTIONS3
            # ACM = RxPLD[117:121]	# ACM Parameters
            TSR = RxPLD[121:129]	# 25.Tx Symbole Rate
            RSR = RxPLD[129:137]	# 26.Rx Symbole Rate
            # BTX = RxPLD[137:138]	# Tx BERT State
            # TBP = RxPLD[138:139]	# Tx Bert Pattern
            # xx4 = RxPLD[139:140]	# OPTIONS4
            # RTX = RxPLD[140:141]	# Rx BERT State
            # RBP = RxPLD[141:142]	# Rx BERT Pattern
            # CNM = RxPLD[142:143]	# CnC Mode
            # CCF = RxPLD[143:146]	# CnC Frequency Offset
            # CSD = RxPLD[146:152]	# CnC Search Delays
            # CAI = RxPLD[152:153]	# Carrier ID State
            # xx5 = RxPLD[153:200]	# OPTIONS5

        	# 01.Tx Frequency
            if (TFQ != DEF_PRM[0][0]):
                with open('/mnt/ssd/log/' + MD1 +'/' + MD2 + '_' + DTN[5] + '.log', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([DTN[0], DTN[1], MD2, 'MGC', 'TFQ', DEF_PRM[0][0], TFQ])
                ERR1 = ERR1 + 1
        	# 02.Tx FEC Type
            if (TFT != DEF_PRM[0][1]):
                with open('/mnt/ssd/log/' + MD1 +'/' + MD2 + '_' + DTN[5] + '.log', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([DTN[0], DTN[1], MD2, 'MGC', 'TFT', DEF_PRM[0][1], TFT])
                ERR1 = ERR1 + 2
        	# 03.Tx Modulation Type
            if (TMD != DEF_PRM[0][2]):
                with open('/mnt/ssd/log/' + MD1 +'/' + MD2 + '_' + DTN[5] + '.log', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([DTN[0], DTN[1], MD2, 'MGC', 'TMD',DEF_PRM[0][2], TMD])
                ERR1 = ERR1 + 4
        	# 04.Tx FEC Rate
            if (TCR != DEF_PRM[0][3]):
                with open('/mnt/ssd/log/' + MD1 +'/' + MD2 + '_' + DTN[5] + '.log', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([DTN[0], DTN[1], MD2, 'MGC', 'TCR', DEF_PRM[0][3], TCR])
                ERR1 = ERR1 + 8
        	# 05.Tx Data Rate
            if (TDR != DEF_PRM[0][4]):
                with open('/mnt/ssd/log/' + MD1 +'/' + MD2 + '_' + DTN[5] + '.log', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([DTN[0], DTN[1], MD2, 'MGC', 'TDR', DEF_PRM[0][4], TDR])
                ERR1 = ERR1 + 16
        	# 06.Tx Spectrum Inversion
            if (TSI != DEF_PRM[0][5]):
                with open('/mnt/ssd/log/' + MD1 +'/' + MD2 + '_' + DTN[5] + '.log', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([DTN[0], DTN[1], MD2, 'MGC', 'TSI', DEF_PRM[0][5], TSI])
                ERR1 = ERR1 + 32
        	# 07.Tx Scrambler State
            if (TSC != DEF_PRM[0][6]):
                with open('/mnt/ssd/log/' + MD1 +'/' + MD2 + '_' + DTN[5] + '.log', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([DTN[0], DTN[1], MD2, 'MGC', 'TSC', DEF_PRM[0][6], TSC])
                ERR1 = ERR1 + 64
        	# 08.Tx Power Level
            if (TPL != DEF_PRM[0][7]):
                with open('/mnt/ssd/log/' + MD1 +'/' + MD2 + '_' + DTN[5] + '.log', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([DTN[0], DTN[1], MD2, 'MGC', 'TPL', DEF_PRM[0][7], TPL])
                ERR1 = ERR1 + 128
        	# 09.Tx Data Invert
            if (TDI != DEF_PRM[0][8]):
                with open('/mnt/ssd/log/' + MD1 +'/' + MD2 + '_' + DTN[5] + '.log', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([DTN[0], DTN[1], MD2, 'MGC', 'TDI', DEF_PRM[0][8], TDI])
                ERR1 = ERR1 + 256
            # 10.Tx Carrier State
            if (TXO != DEF_PRM[0][9]):
                with open('/mnt/ssd/log/' + MD1 +'/' + MD2 + '_' + DTN[5] + '.log', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([DTN[0], DTN[1], MD2, 'MGC', 'TXO', DEF_PRM[0][9], TXO])
                ERR1 = ERR1 + 512
        	# 11.Tx Alpha
            if (TXA != DEF_PRM[0][10]):
                with open('/mnt/ssd/log/' + MD1 +'/' + MD2 + '_' + DTN[5] + '.log', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([DTN[0], DTN[1], MD2, 'MGC', 'TXA', DEF_PRM[0][10], TXA])
                ERR1 = ERR1 + 1024
        	# 12.Tx Clock Invert
            if (TCI != DEF_PRM[0][11]):
                with open('/mnt/ssd/log/' + MD1 +'/' + MD2 + '_' + DTN[5] + '.log', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([DTN[0], DTN[1], MD2, 'MGC', 'TCI', DEF_PRM[0][11], TCI])
                ERR1 = ERR1 + 2048
            # 13.Rx Frequency
            if (RFQ != DEF_PRM[0][12]):
                with open('/mnt/ssd/log/' + MD1 +'/' + MD2 + '_' + DTN[5] + '.log', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([DTN[0], DTN[1], MD2, 'MGC', 'RFQ', DEF_PRM[0][12], RFQ])
                ERR2 = ERR2 + 1
            # 14.Rx FEC Type
            if (RFT != DEF_PRM[0][13]):
                with open('/mnt/ssd/log/' + MD1 +'/' + MD2 + '_' + DTN[5] + '.log', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([DTN[0], DTN[1], MD2, 'MGC', 'RFT', DEF_PRM[0][13], RFT])
                ERR2 = ERR2 + 2
            # 15.Rx Demodulation Type
            if (RMD != DEF_PRM[0][14]):
                with open('/mnt/ssd/log/' + MD1 +'/' + MD2 + '_' + DTN[5] + '.log', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([DTN[0], DTN[1], MD2, 'MGC', 'RMD', DEF_PRM[0][14], RMD])
                ERR2 = ERR2 + 4
        	# 16.Rx FEC Rate
            if (RCR != DEF_PRM[0][15]):
                with open('/mnt/ssd/log/' + MD1 +'/' + MD2 + '_' + DTN[5] + '.log', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([DTN[0], DTN[1], MD2, 'MGC', 'RCR', DEF_PRM[0][15], RCR])
                ERR2 = ERR2 + 8
            # 17.Rx Data Rate
            if (RDR != DEF_PRM[0][16]):
                with open('/mnt/ssd/log/' + MD1 +'/' + MD2 + '_' + DTN[5] + '.log', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([DTN[0], DTN[1], MD2, 'MGC', 'RDR', DEF_PRM[0][16], RDR])
                ERR2 = ERR2 + 16
            # 18.Rx Spectrum Inversion
            if (RSI != DEF_PRM[0][17]):
                with open('/mnt/ssd/log/' + MD1 +'/' + MD2 + '_' + DTN[5] + '.log', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([DTN[0], DTN[1], MD2, 'MGC', 'RSI', DEF_PRM[0][17], RSI])
                ERR2 = ERR2 + 32
            # 19.Rx Descrambler State
            if (RDS != DEF_PRM[0][18]):
                with open('/mnt/ssd/log/' + MD1 +'/' + MD2 + '_' + DTN[5] + '.log', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([DTN[0], DTN[1], MD2, 'MGC', 'RDS', DEF_PRM[0][18], RDS])
                ERR2 = ERR2 + 64
            # 20.Rx Data Invert
            if (RDI != DEF_PRM[0][19]):
                with open('/mnt/ssd/log/' + MD1 +'/' + MD2 + '_' + DTN[5] + '.log', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([DTN[0], DTN[1], MD2, 'MGC', 'RDI', DEF_PRM[0][19], RDI])
                ERR2 = ERR2 + 128
            # 21.Rx Sweep Wodth
            if (RSW != DEF_PRM[0][20]):
                with open('/mnt/ssd/log/' + MD1 +'/' + MD2 + '_' + DTN[5] + '.log', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([DTN[0], DTN[1], MD2, 'MGC', 'RSW', DEF_PRM[0][20], RSW])
                ERR2 = ERR2 + 256
            # 22.Eb/N0 ALM Point
            if (EBA != DEF_PRM[0][21]):
                with open('/mnt/ssd/log/' + MD1 +'/' + MD2 + '_' + DTN[5] + '.log', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([DTN[0], DTN[1], MD2, 'MGC', 'EBA', DEF_PRM[0][21], EBA])
                ERR2 = ERR2 + 512
            # 23.Rx Alpha
            if (RXA != DEF_PRM[0][22]):
                with open('/mnt/ssd/log/' + MD1 +'/' + MD2 + '_' + DTN[5] + '.log', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([DTN[0], DTN[1], MD2, 'MGC', 'RXA', DEF_PRM[0][22], RXA])
                ERR2 = ERR2 + 1024
            # 24.Rx Clock Invert
            if (RCI != DEF_PRM[0][23]):
                with open('/mnt/ssd/log/' + MD1 +'/' + MD2 + '_' + DTN[5] + '.log', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([DTN[0], DTN[1], MD2, 'MGC', 'RCI', DEF_PRM[0][23], RCI])
                ERR2 = ERR2 + 2048
            # 25.Tx Symbole Rate
            if (TSR != DEF_PRM[0][24]):
                with open('/mnt/ssd/log/' + MD1 +'/' + MD2 + '_' + DTN[5] + '.log', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([DTN[0], DTN[1], MD2, 'MGC', 'TSR', DEF_PRM[0][24], TSR])
                ERR2 = ERR2 + 4096
            # 26.Rx Symbole Rate
            if (RSR != DEF_PRM[0][25]):
                with open('/mnt/ssd/log/' + MD1 +'/' + MD2 + '_' + DTN[5] + '.log', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([DTN[0], DTN[1], MD2, 'MGC', 'RSR', DEF_PRM[0][25], RSR])
                ERR2 = ERR2 + 8192

            if (ERR1 == 0 and ERR2 == 0):
                with open(FN2 + DTN[5] + '.log', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([DTN[0], DTN[1], MD2, 'MGC', 'It has all settings correct'])
                with open('/mnt/ssd/log/' + MD1 +'/' + MD2 + '_' + DTN[5] + '.log', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([DTN[0], DTN[1], MD2, 'MGC','', 'The ' + MD2 + ' has all settings correct'])
                print ('          ',DTN[1], '\33[1m\033[44m\033[37m' + ' M/D ' + '\033[0m' + '  \033[1m\033[41m\033[37m  NOM  \033[0m \033[1m\033[32m' + MD2 + 'has all settings correct that Confirmed by MGC Command.' + '\033[0m lqms_mgc.py Ver.' + VER)

            else :
                with open(FN2 + DTN[5] + '.log', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([DTN[0], DTN[1], MD2, 'MGC', 'It has all settings correct'])
                with open('/mnt/ssd/log/' + MD1 +'/' + MD2 + '_' + DTN[5] + '.log', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([DTN[0], DTN[1], MD2, 'MGC','', 'The ' + MD2 +' has several wrong setup'])
                print ('          ',DTN[1], '\33[1m\033[44m\033[37m' + ' M/D ' + '\033[0m' + '  \033[1m\033[41m\033[37m FAULT \033[0m \033[1m\033[31m' + MD2 + ' has several wrong parameter according to MGC query.' + '\033[0m lqms_mgc.py Ver.' + VER)
            return(ERR1,ERR2)

        elif ( ACK == '?') :
            with open('/mnt/ssd/log/' + MD1 +'/' + MD2 + '_' + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD2 , 'MGC', '[?] , Wrong Instructions'])
            with open(FN2 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD2, 'MGC', '[?] , Wrong Instructions'])
            print ('          ',DTN[1], '\33[1m\033[44m\033[37m' + ' M/D ' + '\033[0m' + '  \033[1m\033[41m\033[37m FAULT \033[0m \033[1m\033[31m' + MD2 + ' [?] , Wrong Instructions in MGC Command.' + '\033[0m                lqms_mgc.py Ver.' + VER)
            return(99,99)
        elif ( ACK == '!') :
            with open('/mnt/ssd/log/' + MD1 +'/' + MD2 + '_' + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD2, 'MGC', '[!] , Wrong Command'])
            with open(FN2 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD2, 'MGC', '[!] , Wrong Command'])
            print ('          ',DTN[1], '\33[1m\033[44m\033[37m' + ' M/D ' + '\033[0m' + '  \033[1m\033[41m\033[37m FAULT \033[0m \033[1m\033[31m' + MD2 + ' [!] , Wrong Command' + '\033[0m                                    lqms_mgc.py Ver.' + VER)
            return(99,99)
        elif ( ACK == '*') :
            with open('/mnt/ssd/log/' + MD1 +'/' + MD2 + '_' + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD2, 'MGC', '[*] , The M/D was not in Remote Mode'])
            with open(FN2 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD2, 'MGC', '[*] , The M/D was not in Remote Mode'])
            print ('          ',DTN[1], '\33[1m\033[44m\033[37m' + ' M/D ' + '\033[0m' + '  \033[1m\033[41m\033[37m FAULT \033[0m \033[1m\033[31m' + MD2 + ' [*] , The M/D was not in Remote Mode' + '\033[0m                   lqms_mgc.py Ver.' + VER)
            return(99,99)
        elif ( ACK == '+') :
            with open('/mnt/ssd/log/' + MD1 +'/' + MD2 + '_' + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD2, 'MGC', '[+] , Command was accepted, but that other parameters were additionally changed.'])
            with open(FN2 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD2, 'MGC', '[+] , Command was accepted, but that other parameters were additionally changed.'])
            print ('          ',DTN[1], '\33[1m\033[44m\033[37m' + ' M/D ' + '\033[0m' + '  \033[1m\033[41m\033[37m FAULT \033[0m \033[1m\033[31m' + MD2 + ' [+] , Command was accepted, but that other parameters were additionally changed.' + '\033[0m  lqms_mgc.py Ver.' + VER)
            return(99,99)
