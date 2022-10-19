# #################################################################
# ### LQMS-2.0 for JAXA-Tanegashima E/S . RCC                   ###
# ### Release date 2022.10                                      ###
# ###  *SNO Command Query                                       ###                               
# ### Version 0.2.4                       TechnoBusiness Co.LTD ###
# #################################################################
VER = '0.2.4'

import lqms_dt
import csv

FN1 = '/mnt/ssd/log/error/err_'
FN2 = '/mnt/ssd/log/facl/sys_'

def ST(RxDAT):
    DTN = lqms_dt.RTC_CHK()

    STx = RxDAT[0:1]
    ADD = RxDAT[1:5]
    CMD = RxDAT[6:9]
    ACK = RxDAT[9:10]
    DAT = RxDAT[10:]

    if (ADD == '0011'):
        MD = 'MDA1'
        MDP = ' IP MODEM-A1 '
    elif (ADD == '0012'):
        MD = 'MDA2'
        MDP = ' IP MODEM-A2 '
    elif (ADD == '0013'):
        MD = 'MDB1'
        MDP = ' IP MODEM-B1 '
    elif (ADD == '0014'):
        MD = 'MDB2'
        MDP = ' IP MODEM-B2 '
    elif (ADD == '0015'):
        MD = 'MDC1'
        MDP = ' IP MODEM-C1 '
    elif (ADD == '0016'):
        MD = 'MDC2'
        MDP = ' IP MODEM-C2 '
    elif (ADD == '0017'):
        MD = 'MDE1'
        MDP = ' IP MODEM-E1 '
    elif (ADD == '0018'):
        MD = 'MDE2'
        MDP = ' IP MODEM-E2 '
    else:
        MD = 'unidentified'

    DTN = lqms_dt.RTC_CHK()
    print ('          ' , DTN[1] , '\033[1m\033[44m\033[37m\033[1m M/D \033[0m' + '  SNO Command Query                                                         lqms_sno.py Ver.' + VER )
    with open(FN2 + DTN[5] + '.log', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([DTN[0], DTN[1], MD, 'Query SNO'])

    if (STx == '>' ):
        if ( ACK == '='):
            with open(FN2 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'Serial No.', DAT])
            print ('          ',DTN[1], '\33[1m\033[44m\033[37m' + ' M/D ' + '\033[0m' +'  \033[1m\033[42m\033[37m  NOM  \033[0m \033[1m\033[32m' + MDP + ' Ser.' + DAT + '\033[0m\033[32m                                       lqms_sno.py Ver.' + VER + '\033[0m')
            return (DAT)
        elif ( ACK == '?') :
            with open(FN1 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'Serial No.', '[?] , Wrong Instructions'])
            print ('          ',DTN[1], '\33[1m\033[44m\033[37m' + ' M/D ' + '\033[0m' + '  \033[1m\033[41m\033[37m FAULT \033[0m \033[1m\033[31m' + MDP + ' [?] , Wrong Instructions in MGC Command.' + '\033[0m\033[32m' + '               lqms_sno.py Ver.' + VER)
            return ('---')
        elif ( ACK == '!') :
            with open(FN1 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'Serial No.', '[!] , Wrong Command'])
            print ('          ',DTN[1], '\33[1m\033[44m\033[37m' + ' M/D ' + '\033[0m' + '  \033[1m\033[41m\033[37m FAULT \033[0m \033[1m\033[31m' + MDP + ' [!] , Wrong Command.' + '\033[0m\033[32m' + '               lqms_sno.py Ver.' + VER)
            return ('---')
        elif ( ACK == '*') :
            with open(FN1 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'Serial No.', '[*] , The M/D was not in Remote Mode'])
            print ('          ',DTN[1], '\33[1m\033[44m\033[37m' + ' M/D ' + '\033[0m' + '  \033[1m\033[41m\033[37m FAULT \033[0m \033[1m\033[31m' + MDP + ' [*] , The M/D was not in Remote Mode.' + '\033[0m\033[32m' + '               lqms_sno.py Ver.' + VER + '\033[0m')
            return ('---')
        elif ( ACK == '+') :
            with open(FN1 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'Serial No.', '[+] , Command was accepted, but that other parameters were additionally changed.'])
            print ('          ',DTN[1], '\33[1m\033[44m\033[37m' + ' M/D ' + '\033[0m' + '  \033[1m\033[41m\033[37m FAULT \033[0m \033[1m\033[31m' + MDP + '[+] , Command was accepted, but that other parameters were additionally changed.' + '\033[0m\033[32m' + '               lqms_sno.py Ver.' + VER + '\033[0m')
            return ('---')





