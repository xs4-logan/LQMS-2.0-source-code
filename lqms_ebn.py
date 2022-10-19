# #################################################################
# ### LQMS-2.0 for JAXA-Tanegashima E/S . RCC                   ###
# ### Release date 2022.10                                      ###
# ###   *EBN Command Query                                      ###
# ### Version 0.3.7                       TechnoBusiness Co.LTD ###
# #################################################################
VER = '0.3.7'

import lqms_dt
import lqms_plt
import csv
from decimal import Decimal, ROUND_HALF_UP

FN2 = '/mnt/ssd/log/facl/sys_'

MDA1_EBN={}
MDA2_EBN={}
MDB1_EBN={}
MDB2_EBN={}
MDC1_EBN={}
MDC2_EBN={}
MDE1_EBN={}
MDE2_EBN={}
MDF1_EBN={}
MDF2_EBN={}

def ST(RxDAT,TN):
    DTN = lqms_dt.RTC_CHK()

    STx = RxDAT[0:1]
    ADD = RxDAT[1:5]
    CMD = RxDAT[6:9]
    ACK = RxDAT[9:10]
    DAT = RxDAT[10:]

    if ( DAT == '99.9'):
        DAT = '0.0'
    elif ( DAT == '+016'):
        DAT = '16.0'
    elif ( DAT == 'NoA'):
        DAT = '100'

    if (STx == '>' ):
        if ( ACK == '='):
            if (ADD == '0011'):
                MD = 'MDA1'
                MD2 = 'MODEM-A1'
                MDA1_EBN[TN] = float(DAT)
            if (ADD == '0012'):
                MD = 'MDA2'
                MD2 = 'MODEM-A2'
                MDA2_EBN[TN] = float(DAT)
            if (ADD == '0013'):
                MD = 'MDB1'
                MD2 = 'MODEM-B1'
                MDB1_EBN[TN] = float(DAT)
            if (ADD == '0014'):
                MD = 'MDB2'
                MD2 = 'MODEM-B2'
                MDB2_EBN[TN] = float(DAT)
            if (ADD == '0015'):
                MD = 'MDC1'
                MD2 = 'MODEM-C1'
                MDC1_EBN[TN] = float(DAT)
            if (ADD == '0016'):
                MD = 'MDC2'
                MD2 = 'MODEM-C2'
                MDC2_EBN[TN] = float(DAT)
            if (ADD == '0017'):
                MD = 'MDE1'
                MD2 = 'MODEM-E1'
                MDE1_EBN[TN] = float(DAT)
            if (ADD == '0018'):
                MD = 'MDE2'
                MD2 = 'MODEM-E2'
                MDE2_EBN[TN] = float(DAT)

            print ('          ',DTN[1],'\033[1m\033[44m\033[37m\033[1m M/D \033[0m  EBN Command Query.                                                        lqms_ebn.py Ver.' + VER)
            with open(FN2 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'EBN','Query EBN'])

            if (TN == 00):
                if (MD == 'MDA1'):
                    if (30 in MDA1_EBN.keys()):
                        if (MDA1_EBN[30] != 100 or MDA1_EBN[00] != 100) :
                            EBNavg = Decimal(str((MDA1_EBN[30] + MDA1_EBN[00])/2)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                        elif (MDA1_EBN[30] == 100) :
                            EBNavg = Decimal(str(MDA1_EBN[00])).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                        elif (MDA1_EBN[00] == 100) :
                            EBNavg = Decimal(str(MDA1_EBN[30])).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                        if (MDA1_EBN[00] < MDA1_EBN[30]):
                            EBNmin = MDA1_EBN[00]
                        else :
                            EBNmin = MDA1_EBN[30]
                    elif (30 not in MDA1_EBN.keys()):
                        EBNavg = MDA1_EBN[00]
                        EBNmin = MDA1_EBN[00]
                    DTN = lqms_dt.RTC_CHK()
                    with open('/mnt/ssd/log/mda1/MDA1_' + DTN[5] + '.log', 'a') as f:
                        writer = csv.writer(f)
                        writer.writerow([DTN[0], DTN[1], 'MDA1', 'EBN', str(EBNavg) , str(EBNmin)])
                    print ('          ', DTN[1], '\33[1m\033[44m\033[37m' + ' M/D ' + '\033[0m' + '\033[32m\033[1m  EBN (MDA1) Average:' + str(EBNavg) + '(dB) / Minimum:' + str(EBNmin) + '(dB)\033[0m                              lqms_ebn.py Ver.' + VER)
                    lqms_plt.ST(EBNmin,MD)
                if (MD == 'MDA2'):
                    if (30 in MDA2_EBN.keys()):
                        if (MDA2_EBN[30] != 100 or MDA2_EBN[00] != 100) :
                            EBNavg = Decimal(str((MDA2_EBN[00] + MDA2_EBN[30])/2)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                        elif (MDA2_EBN[30] == 100) :
                            EBNavg = Decimal(str(MDA2_EBN[00])).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                        elif (MDA2_EBN[00] == 100) :
                            EBNavg = Decimal(str(MDA2_EBN[30])).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                        if (MDA2_EBN[00] < MDA2_EBN[30]):
                            EBNmin = MDA2_EBN[00]
                        else :
                            EBNmin = MDA2_EBN[30]
                    elif (30 not in MDA2_EBN.keys()):
                        EBNavg = MDA2_EBN[00]
                        EBNmin = MDA2_EBN[00]
                    DTN = lqms_dt.RTC_CHK()
                    with open('/mnt/ssd/log/mda2/MDA2_' + DTN[5] + '.log', 'a') as f:
                        writer = csv.writer(f)
                        writer.writerow([DTN[0], DTN[1], 'MDA2', 'EBN', str(EBNavg) , str(EBNmin)])
                    print ('          ', DTN[1], '\33[1m\033[44m\033[37m' + ' M/D ' + '\033[0m' + '\033[32m\033[1m  EBN (MDA2) Average:' + str(EBNavg) + '(dB) / Minimum:' + str(EBNmin) + '(dB)\033[0m                              lqms_ebn.py Ver.' + VER)
                    lqms_plt.ST(EBNmin,MD)
                if (MD == 'MDB1'):
                    if (30 in MDB1_EBN.keys()):
                        if (MDB1_EBN[30] != 100 or MDB1_EBN[00] != 100) :
                            EBNavg = Decimal(str((MDB1_EBN[00] + MDB1_EBN[30])/2)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                        elif (MDB1_EBN[00] == 100) :
                            EBNavg = Decimal(str(MDB1_EBN[30])).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                        elif (MDB1_EBN[30] == 100) :
                            EBNavg = Decimal(str(MDB1_EBN[00])).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                        if (MDB1_EBN[00] < MDB1_EBN[30]):
                            EBNmin = MDB1_EBN[00]
                        else :
                            EBNmin = MDB1_EBN[30]
                    elif (30 not in MDB1_EBN.keys()):
                        EBNavg = MDB1_EBN[00]
                        EBNmin = MDB1_EBN[00]
                    DTN = lqms_dt.RTC_CHK()
                    with open('/mnt/ssd/log/mdb1/MDB1_' + DTN[5] + '.log', 'a') as f:
                        writer = csv.writer(f)
                        writer.writerow([DTN[0], DTN[1], 'MDB1', 'EBN', str(EBNavg) , str(EBNmin)])
                    print ('          ', DTN[1], '\33[1m\033[44m\033[37m' + ' M/D ' + '\033[0m' + '\033[32m\033[1m  EBN (MDB1) Average:' + str(EBNavg) + '(dB) / Minimum:' + str(EBNmin) + '(dB)\033[0m                              lqms_ebn.py Ver.' + VER)
                    lqms_plt.ST(EBNmin,MD)
                if (MD == 'MDB2'):
                    if (30 in MDB2_EBN.keys()):
                        if (MDB2_EBN[30] != 100 or MDB2_EBN[00] != 100) :
                            EBNavg = Decimal(str((MDB2_EBN[00] + MDB2_EBN[30])/2)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                        if (MDB2_EBN[00] == 100) :
                            EBNavg = Decimal(str( MDB2_EBN[30])).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                        if (MDB2_EBN[30] == 100) :
                            EBNavg = Decimal(str( MDB2_EBN[00])).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                        if (MDB2_EBN[00] < MDB2_EBN[30]):
                            EBNmin = MDB2_EBN[00]
                        else :
                            EBNmin = MDB2_EBN[30]
                    elif (30 not in MDB2_EBN.keys()):
                        EBNavg = MDB2_EBN[00]
                        EBNmin = MDB2_EBN[00]
                    DTN = lqms_dt.RTC_CHK()
                    with open('/mnt/ssd/log/mdb2/MDB2_' + DTN[5] + '.log', 'a') as f:
                        writer = csv.writer(f)
                        writer.writerow([DTN[0], DTN[1], 'MDB2', 'EBN', str(EBNavg) , str(EBNmin)])
                    print ('          ', DTN[1], '\33[1m\033[44m\033[37m' + ' M/D ' + '\033[0m' + '\033[32m\033[1m  EBN (MDB2) Average:' + str(EBNavg) + '(dB) / Minimum:' + str(EBNmin) + '(dB)\033[0m                              lqms_ebn.py Ver.' + VER)
                    lqms_plt.ST(EBNmin,MD)
                if (MD == 'MDC1'):
                    if (30 in MDC1_EBN.keys()):
                        if (MDC1_EBN[30] != 100 or MDC1_EBN[00] != 100) :
                            EBNavg = Decimal(str((MDC1_EBN[00] + MDC1_EBN[30])/2)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                        elif (MDC1_EBN[00] == 100) :
                            EBNavg = Decimal(str(MDC1_EBN[30])).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                        elif (MDC1_EBN[30] == 100) :
                            EBNavg = Decimal(str(MDC1_EBN[00])).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                        if (MDC1_EBN[00] < MDC1_EBN[30]):
                            EBNmin = MDC1_EBN[00]
                        else :
                            EBNmin = MDC1_EBN[30]
                    elif (30 not in MDC1_EBN.keys()):
                        EBNavg = MDC1_EBN[00]
                        EBNmin = MDC1_EBN[00]
                    DTN = lqms_dt.RTC_CHK()
                    with open('/mnt/ssd/log/mdc1/MDC1_' + DTN[5] + '.log', 'a') as f:
                        writer = csv.writer(f)
                        writer.writerow([DTN[0], DTN[1], 'MDC1', 'EBN', str(EBNavg) , str(EBNmin)])
                    print ('          ', DTN[1], '\33[1m\033[44m\033[37m' + ' M/D ' + '\033[0m' + '\033[32m\033[1m  EBN (MDC1) Average:' + str(EBNavg) + '(dB) / Minimum:' + str(EBNmin) + '(dB)\033[0m                              lqms_ebn.py Ver.' + VER)
                    lqms_plt.ST(EBNmin,MD)
                if (MD == 'MDC2'):
                    if (30 in MDC2_EBN.keys()):
                        if (MDC2_EBN[30] != 100 or MDC2_EBN[00] != 100) :
                            EBNavg = Decimal(str((MDC2_EBN[00] + MDC2_EBN[30])/2)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                        elif (MDC2_EBN[00] == 100) :
                            EBNavg = Decimal(str(MDC2_EBN[30])).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                        elif (MDC2_EBN[30] == 100) :
                            EBNavg = Decimal(str(MDC2_EBN[00])).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                        if (MDC2_EBN[00] < MDC2_EBN[30]):
                            EBNmin = MDC2_EBN[00]
                        else :
                            EBNmin = MDC2_EBN[30]
                    elif (30 not in MDC2_EBN.keys()):
                        EBNavg = MDC2_EBN[00]
                        EBNmin = MDC2_EBN[00]
                    DTN = lqms_dt.RTC_CHK()
                    with open('/mnt/ssd/log/mdc2/MDC2_' + DTN[5] + '.log', 'a') as f:
                        writer = csv.writer(f)
                        writer.writerow([DTN[0], DTN[1], 'MDC2', 'EBN', str(EBNavg) , str(EBNmin)])
                    print ('          ', DTN[1], '\33[1m\033[44m\033[37m' + ' M/D ' + '\033[0m' + '\033[32m\033[1m  EBN (MDC2) Average:' + str(EBNavg) + '(dB) / Minimum:' + str(EBNmin) + '(dB)\033[0m                              lqms_ebn.py Ver.' + VER)
                    lqms_plt.ST(EBNmin,MD)
                if (MD == 'MDE1'):
                    if (30 in MDE1_EBN.keys()):
                        if (MDE1_EBN[30] != 100 or MDE1_EBN[00] != 100) :
                            EBNavg = Decimal(str((MDE1_EBN[00] + MDE1_EBN[30])/2)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                        elif (MDE1_EBN[30] == 100) :
                            EBNavg = Decimal(str(MDE1_EBN[00]).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))
                        elif (MDE1_EBN[00] == 100) :
                            EBNavg = Decimal(str(MDE1_EBN[30]).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))
                        if (MDE1_EBN[00] < MDE1_EBN[30]):
                            EBNmin = MDE1_EBN[00]
                        else :
                            EBNmin = MDE1_EBN[30]
                    elif (30 not in MDE1_EBN.keys()):
                        EBNavg = MDE1_EBN[00]
                        EBNmin = MDE1_EBN[00]
                    DTN = lqms_dt.RTC_CHK()
                    with open('/mnt/ssd/log/mde1/MDE1_' + DTN[5] + '.log', 'a') as f:
                        writer = csv.writer(f)
                        writer.writerow([DTN[0], DTN[1], 'MDE1', 'EBN', str(EBNavg) , str(EBNmin)])
                    print ('          ', DTN[1], '\33[1m\033[44m\033[37m' + ' M/D ' + '\033[0m' + '\033[32m\033[1m  EBN (MDE1) Average:' + str(EBNavg) + '(dB) / Minimum:' + str(EBNmin) + '(dB)\033[0m                              lqms_ebn.py Ver.' + VER)
                    lqms_plt.ST(EBNmin,MD)
                if (MD == 'MDE2'):
                    if (30 in MDE2_EBN.keys()):
                        if (MDE2_EBN[30] != 100 or MDE2_EBN[00] != 100) :
                            EBNavg = Decimal(str((MDE2_EBN[00] + MDE2_EBN[30])/2)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                        elif (MDE2_EBN[00] == 100) :
                            EBNavg = Decimal(str(MDE2_EBN[30])).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                        elif (MDE2_EBN[30] == 100) :
                            EBNavg = Decimal(str(MDE2_EBN[00])).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                        if (MDE2_EBN[00] < MDE2_EBN[30]):
                            EBNmin = MDE2_EBN[00]
                        else :
                            EBNmin = MDE2_EBN[30]
                    elif (10 not in MDE2_EBN.keys()):
                        EBNavg = MDE2_EBN[00]
                        EBNmin = MDE2_EBN[00]
                    DTN = lqms_dt.RTC_CHK()
                    with open('/mnt/ssd/log/mde2/MDE2_' + DTN[5] + '.log', 'a') as f:
                        writer = csv.writer(f)
                        writer.writerow([DTN[0], DTN[1], 'MDE2', 'EBN', str(EBNavg) , str(EBNmin)])
                    print ('          ', DTN[1], '\33[1m\033[44m\033[37m' + ' M/D ' + '\033[0m' + '\033[32m\033[1m  EBN (MDE2) Average:' + str(EBNavg) + '(dB) / Minimum:' + str(EBNmin) + '(dB)\033[0m                              lqms_ebn.py Ver.' + VER)
                    lqms_plt.ST(EBNmin,MD)

        elif ( ACK == '?') :
            with open('/mnt/ssd/log/' + MD2 +'/' + MD + '_' + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'EBN', '[?] , Wrong Instructions'])
            with open(FN2 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD , 'EBN', '[?] , Wrong Instructions'])
            print ('          ',DTN[1], '\33[1m\033[44m\033[37m' + ' M/D ' + '\033[0m' + '\033[1m\033[41m\033[37m FAULT \033[0m \033[31m' + MD2 + '[?] , Wrong Instructions in MGC Command.' + '\033[0m' + '             lqms_mgc.py Ver.' + VER)
        elif ( ACK == '!') :
            with open('/mnt/ssd/log/' + MD2 +'/' + MD + '_' + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'EBN', '[!] , Wrong Command'])
            with open(FN2 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'EBN', '[!] , Wrong Command'])
            print ('          ',DTN[1], '\33[1m\033[44m\033[37m' + ' M/D ' + '\033[0m' + '\033[1m\033[41m\033[37m FAULT \033[0m \033[31m' + MD2 + '[!] , Wrong Command.' + '\033[0m' + '             lqms_mgc.py Ver.' + VER)
        elif ( ACK == '*') :
            with open('/mnt/ssd/log/' + MD2 +'/' + MD + '_' + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'EBN', '[*] , The M/D was not in Remote Mode'])
            with open(FN2 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'EBN', '[*] , The M/D was not in Remote Mode'])
            print ('          ',DTN[1], '\33[1m\033[44m\033[37m' + ' M/D ' + '\033[0m' + '\033[1m\033[41m\033[37m FAULT \033[0m \033[31m' + MD2 + '[*] , The M/D was not in Remote Mode.' + '\033[0m' + '             lqms_mgc.py Ver.' + VER)
        elif ( ACK == '+') :
            with open('/mnt/ssd/log/' + MD2 +'/' + MD + '_' + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'EBN', '[+] , Command was accepted, but that other parameters were additionally changed.'])
            with open(FN2 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'EBN', '[+] , Command was accepted, but that other parameters were additionally changed.'])
            print ('          ',DTN[1], '\33[1m\033[44m\033[37m' + ' M/D ' + '\033[0m' + '\033[1m\033[41m\033[37m FAULT \033[0m \033[31m' + MD2 + '[+] , Command was accepted, but that other parameters were additionally changed.' + '\033[0m' + '             lqms_mgc.py Ver.' + VER)
