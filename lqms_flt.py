# #################################################################
# ### LQMS-2.0 for JAXA-Tanegashima E/S . RCC                   ###
# ### Release date 2022.10                                      ###
# ###   *FLT Command Query                                      ###
# ### Version 0.2.2                       TechnoBusiness Co.LTD ###
# #################################################################
VER = '0.2.2'

import lqms_dt
import csv

FN2 = '/mnt/ssd/log/facl/sys_'

def ST(RxDAT):
    DTN = lqms_dt.RTC_CHK()

    STx = RxDAT[0:1]
    ADD = RxDAT[1:5]
    CMD = RxDAT[6:9]
    ACK = RxDAT[9:10]
    DAT1 = RxDAT[10:11]
    DAT2 = RxDAT[11:12]
    DAT3 = RxDAT[12:13]
    DAT4 = RxDAT[13:14]
    DAT5 = RxDAT[14:15]
    DAT6 = RxDAT[15:16]

    if (ADD == '0011'):
        MD = 'MDA1'
        MD2 = 'MODEM-A1'
    elif (ADD == '0012'):
        MD = 'MDA2'
        MD2 = 'MODEM-A2'
    elif (ADD == '0013'):
        MD = 'MDB1'
        MD2 = 'MODEM-B1'
    elif (ADD == '0014'):
        MD = 'MDB2'
        MD2 = 'MODEM-B2'
    elif (ADD == '0015'):
        MD = 'MDC1'
        MD2 = 'MODEM-C1'
    elif (ADD == '0016'):
        MD = 'MDC2'
        MD2 = 'MODEM-C2'
    elif (ADD == '0017'):
        MD = 'MDE1'
        MD2 = 'MODEM-E1'
    elif (ADD == '0018'):
        MD = 'MDE2'
        MD2 = 'MODEM-E2'

    print ('          ',DTN[1],'\033[1m\033[44m\033[37m\033[1m M/D \033[0m  FLT Command Query.                                                        lqms_flt.py Ver.' + VER)
    with open(FN2 + DTN[5] + '.log', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([DTN[0], DTN[1], MD, 'FLT', 'Query FLT'])

    if (STx == '>' ):
        if ( ACK == '='):
            # Unit Status 
            if (DAT1 == '0'):
                DAT1 = 'No Faults'
            elif (DAT1 == '1'):
                DAT1 = 'PS-Fault  +5V'
            elif (DAT1 == '2'):
                DAT1 = 'PS-Fault +12V'
            elif (DAT1 == '3'):
                DAT1 = 'PS-Fault  -5V'
            elif (DAT1 == '4'):
                DAT1 = '---'
            elif (DAT1 == '5'):
                DAT1 = 'PS-Fault -12V'
            elif (DAT1 == '6'):
                DAT1 = 'Tx-SYNTH'
            elif (DAT1 == '7'):
                DAT1 = 'Rx 1st LO-SYNTH'
            elif (DAT1 == '8'):
                DAT1 = 'Rx 1st LO-SYNTH'
            elif (DAT1 == '9'):
                DAT1 = 'REF PLL'
            elif (DAT1 == 'A'):
                DAT1 = '---'
            elif (DAT1 == 'B'):
                DAT1 = '---'
            elif (DAT1 == 'C'):
                DAT1 = '---'
            elif (DAT1 == 'D'):
                DAT1 = '---'
            elif (DAT1 == 'E'):
                DAT1 = 'Packet Processor'
            elif (DAT1 == 'F'):
                DAT1 = '---'
            # Tx Traffic Status
            if (DAT2 == '0'):
                DAT2 = 'No Faults'
            elif (DAT2 == '1'):
                DAT2 = 'No Clock'
            elif (DAT2 == '2'):
                DAT2 = 'PaP ETH Linkdown'
            elif (DAT2 == '3'):
                DAT2 = 'FIFO Slip'
            elif (DAT2 == '4'):
                DAT2 = 'G.703 loss of Signnal'
            elif (DAT2 == '5'):
                DAT2 = 'Loss of EXT-REF'
            elif (DAT2 == '6'):
                DAT2 = '---'
            elif (DAT2 == '7'):
                DAT2 = 'AUPC UpperLimit'
            elif (DAT2 == '8'):
                DAT2 = '---'
            elif (DAT2 == '9'):
                DAT2 = 'AIS on incoming data'
            elif (DAT2 == 'A'):
                DAT2 = '---'
            elif (DAT2 == 'B'):
                DAT2 = 'Vipolar Violation on G.703'
            elif (DAT2 == 'C'):
                DAT2 = '---'
            elif (DAT2 == 'D'):
                DAT2 = '---'
            elif (DAT2 == 'E'):
                DAT2 = '---'
            elif (DAT2 == 'F'):
                DAT2 = 'BUC ALM'
            # Rx Traffic
            if (DAT3 == '0'):
                DAT3 = 'No Faults'
            elif (DAT3 == '1'):
                DAT3 = 'DEM Unlocked'
            elif (DAT3 == '2'):
                DAT3 = '---'
            elif (DAT3 == '3'):
                DAT3 = 'AGC ALM'
            elif (DAT3 == '4'):
                DAT3 = '---'
            elif (DAT3 == '5'):
                DAT3 = 'RS Frame sync'
            elif (DAT3 == '6'):
                DAT3 = '---'
            elif (DAT3 == '7'):
                DAT3 = 'EDMAC'
            elif (DAT3 == '8'):
                DAT3 = 'APC Band Mismatch'
            elif (DAT3 == '9'):
                DAT3 = '---'
            elif (DAT3 == 'A'):
                DAT3 = 'Buffer Underflow'
            elif (DAT3 == 'B'):
                DAT3 = 'Buffer Overflow'
            elif (DAT3 == 'C'):
                DAT3 = '---'
            elif (DAT3 == 'D'):
                DAT3 = 'Eb/N0 ALM'
            elif (DAT3 == 'E'):
                DAT3 = 'LNB ALM'
            elif (DAT3 == 'F'):
                DAT3 = 'AIS Detected in comming data'
            # ODU Status
            if (DAT4 == '0'):
                DAT4 = 'No Faults'
            elif (DAT4 == '1'):
                DAT4 = 'BUC PLL'
            elif (DAT4 == '2'):
                DAT4 = '---'
            elif (DAT4 == '3'):
                DAT4 = 'BUC Current'
            elif (DAT4 == '4'):
                DAT4 = '---'
            elif (DAT4 == '5'):
                DAT4 = 'BUC Voltage'
            elif (DAT4 == '6'):
                DAT4 = '---'
            elif (DAT4 == '7'):
                DAT4 = 'LNB Current'
            elif (DAT4 == '8'):
                DAT4 = '---'
            elif (DAT4 == '9'):
                DAT4 = 'LNB Voltage'
            elif (DAT4 == 'A'):
                DAT4 = '---'
            elif (DAT4 == 'B'):
                DAT4 = 'BUC Temperature'
            elif (DAT4 == 'C'):
                DAT4 = '---'
            elif (DAT4 == 'D'):
                DAT4 = 'BUC F/W Checksum'
            elif (DAT4 == 'E'):
                DAT4 = '---'
            elif (DAT4 == 'F'):
                DAT4 = '---'
            DTN = lqms_dt.RTC_CHK()

            if (MD == 'MDA1'):
                if (DAT5 == '1'):
                    with open('/mnt/ssd/log/mda1/MDA1_' + DTN[5] + '.log', 'a') as f:
                        writer = csv.writer(f)
                        writer.writerow([DTN[0], DTN[1], DAT1 , DAT2 , DAT3 , '---' , DAT5])
                    with open(FN2 + DTN[5] + '.log', 'a') as f:
                        writer = csv.writer(f)
                        writer.writerow([DTN[0], DTN[1], 'MDA1' ,'FLT', DAT1 , DAT2 , DAT3 , '---' , DAT5])
            elif (MD == 'MDA2'):
                if (DAT5 == '1'):
                    with open('/mnt/ssd/log/mda2/MDA2_' + DTN[5] + '.log', 'a') as f:
                        writer = csv.writer(f)
                        writer.writerow([DTN[0], DTN[1], DAT1 , DAT2 , DAT3 , '---' , DAT5])
                    with open(FN2 + DTN[5] + '.log', 'a') as f:
                        writer = csv.writer(f)
                        writer.writerow([DTN[0], DTN[1], 'MDA2' ,'FLT', DAT1 , DAT2 , DAT3 , '---' , DAT5])
            elif (MD == 'MDB1'):
                if (DAT5 == '1'):
                    with open('/mnt/ssd/log/mdb1/MDB1_' + DTN[5] + '.log', 'a') as f:
                        writer = csv.writer(f)
                        writer.writerow([DTN[0], DTN[1], DAT1 , DAT2 , DAT3 , '---' , DAT5])
                    with open(FN2 + DTN[5] + '.log', 'a') as f:
                        writer = csv.writer(f)
                        writer.writerow([DTN[0], DTN[1], 'MDB1' ,'FLT', DAT1 , DAT2 , DAT3 , '---' , DAT5])
            elif (MD == 'MDB2'):
                if (DAT5 == '1'):
                    with open('/mnt/ssd/log/mdb2/MDB2_' + DTN[5] + '.log', 'a') as f:
                        writer = csv.writer(f)
                        writer.writerow([DTN[0], DTN[1], DAT1 , DAT2 , DAT3 , '---' , DAT5])
                    with open(FN2 + DTN[5] + '.log', 'a') as f:
                        writer = csv.writer(f)
                        writer.writerow([DTN[0], DTN[1], 'MDB2' ,'FLT', DAT1 , DAT2 , DAT3 , '---' , DAT5])
            elif (MD == 'MDC1'):
                if (DAT5 == '1'):
                    with open('/mnt/ssd/log/mdc1/MDC1_' + DTN[5] + '.log', 'a') as f:
                        writer = csv.writer(f)
                        writer.writerow([DTN[0], DTN[1], DAT1 , DAT2 , DAT3 , '---' , DAT5])
                    with open(FN2 + DTN[5] + '.log', 'a') as f:
                        writer = csv.writer(f)
                        writer.writerow([DTN[0], DTN[1], 'MDC1' ,'FLT', DAT1 , DAT2 , DAT3 , '---' , DAT5])
            elif (MD == 'MDC2'):
                if (DAT5 == '1'):
                    with open('/mnt/ssd/log/mdc2/MDC2_' + DTN[5] + '.log', 'a') as f:
                        writer = csv.writer(f)
                        writer.writerow([DTN[0], DTN[1], DAT1 , DAT2 , DAT3 , '---' , DAT5])
                    with open(FN2 + DTN[5] + '.log', 'a') as f:
                        writer = csv.writer(f)
                        writer.writerow([DTN[0], DTN[1], 'MDC2' ,'FLT', DAT1 , DAT2 , DAT3 , '---' , DAT5])
            elif (MD == 'MDE1'):
                if (DAT5 == '1'):
                    with open('/mnt/ssd/log/mde1/MDE1_' + DTN[5] + '.log', 'a') as f:
                        writer = csv.writer(f)
                        writer.writerow([DTN[0], DTN[1], DAT1 , DAT2 , DAT3 , '---' , DAT5])
                    with open(FN2 + DTN[5] + '.log', 'a') as f:
                        writer = csv.writer(f)
                        writer.writerow([DTN[0], DTN[1], 'MDE1' ,'FLT', DAT1 , DAT2 , DAT3 , '---' , DAT5])
            elif (MD == 'MDE2'):
                if (DAT5 == '1'):
                    with open('/mnt/ssd/log/mde2/MDE2_' + DTN[5] + '.log', 'a') as f:
                        writer = csv.writer(f)
                        writer.writerow([DTN[0], DTN[1], DAT1 , DAT2 , DAT3 , '---' , DAT5])
                    with open(FN2 + DTN[5] + '.log', 'a') as f:
                        writer = csv.writer(f)
                        writer.writerow([DTN[0], DTN[1], 'MDE2' ,'FLT', DAT1 , DAT2 , DAT3 , '---' , DAT5])
            elif (MD == 'MDF1'):
                if (DAT5 == '1'):
                    with open('/mnt/ssd/log/mdf1/MDF1_' + DTN[5] + '.log', 'a') as f:
                        writer = csv.writer(f)
                        writer.writerow([DTN[0], DTN[1], DAT1 , DAT2 , DAT3 , '---' , DAT5])
                    with open(FN2 + DTN[5] + '.log', 'a') as f:
                        writer = csv.writer(f)
                        writer.writerow([DTN[0], DTN[1], 'MDF1' ,'FLT', DAT1 , DAT2 , DAT3 , '---' , DAT5])
            elif (MD == 'MDF2'):
                if (DAT5 == '1'):
                    with open('/mnt/ssd/log/mdf2/MDF2_' + DTN[5] + '.log', 'a') as f:
                        writer = csv.writer(f)
                        writer.writerow([DTN[0], DTN[1], DAT1 , DAT2 , DAT3 , '---' , DAT5])
                    with open(FN2 + DTN[5] + '.log', 'a') as f:
                        writer = csv.writer(f)
                        writer.writerow([DTN[0], DTN[1], 'MDF2' ,'FLT', DAT1 , DAT2 , DAT3 , '---' , DAT5])

        elif ( ACK == '?') :
            with open(FN2 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD , 'FLT', '[?] , Wrong Instructions'])
            print ('          ',DTN[1], '\33[1m\033[44m\033[37m' + ' M/D ' + '\033[0m' + '\033[1m\033[41m\033[37m FAULT \033[0m \033[31m' + MD2 + ' [?] , Wrong Instructions in FLT Command.' + '\033[0m' + '         lqms_flt.py Ver.' + VER)

        elif ( ACK == '!') :
            with open(FN2 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'FLT', '[!] , Wrong Command'])
            print ('          ',DTN[1], '\33[1m\033[44m\033[37m' + ' M/D ' + '\033[0m' + '\033[1m\033[41m\033[37m FAULT \033[0m \033[31m' + MD2 + ' [!] , Wrong Command.' + '\033[0m' + '         lqms_flt.py Ver.' + VER)
        elif ( ACK == '*') :
            with open(FN2 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'FLT', '[*] , The M/D was not in Remote Mode'])
            print ('          ',DTN[1], '\33[1m\033[44m\033[37m' + ' M/D ' + '\033[0m' + '\033[1m\033[41m\033[37m FAULT \033[0m \033[31m' + MD2 + ' [*] , The M/D was not in Remote Mode.' + '\033[0m' + '         lqms_flt.py Ver.' + VER)
        elif ( ACK == '+') :
            with open(FN2 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'FLT', '[+] , Command was accepted, but that other parameters were additionally changed.'])
            print ('          ',DTN[1], '\33[1m\033[44m\033[37m' + ' M/D ' + '\033[0m' + '\033[1m\033[41m\033[37m FAULT \033[0m \033[31m' + MD2 + ' [+] , Command was accepted, but that other parameters were additionally changed.' + '\033[0m' + '         lqms_mgc.py Ver.' + VER)
