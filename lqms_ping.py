# #################################################################
# ### LQMS-2.0 for JAXA-Tanegashima E/S . RCC                   ###
# ### Release date 2022.10                                      ###
# ###   *Ping Checker (Using PING3)                             ###
# ### Version 0.3.2                       TechnoBusiness Co.LTD ###
# #################################################################
VER = '0.3.2'

from ping3 import ping
import lqms_dt
import csv
FN2 = '/mnt/ssd/log/facl/sys_'

def ST(IPA):
    DTN = lqms_dt.RTC_CHK()

    if (IPA == '192.168.1.11'):
        MD = 'MDA1'
        MDP = ' IP MODEM-A1 '
        FN3 = '/mnt/ssd/log/mda1/MDA1_'
        print ('          ',DTN[1],'\033[1m\033[44m\033[37m M/D \033[0m' + '\033[32m  IP MODEM-A1 Query                                                         lqms_ping.py Ver.' + VER + '\033[0m')
    elif (IPA == '192.168.1.12'):
        MD = 'MDA2'
        MDP = ' IP MODEM-A2 '
        FN3 = '/mnt/ssd/log/mda2/MDA2_'
        print ('          ',DTN[1],'\033[1m\033[44m\033[37m M/D \033[0m' + '\033[32m  IP MODEM-A2 Query                                                         lqms_ping.py Ver.' + VER + '\033[0m')
    elif (IPA == '192.168.1.21'):
        MD = 'MDB1'
        MDP = ' IP MODEM-B1 '
        FN3 = '/mnt/ssd/log/mdb1/MDB1_'
        print ('          ',DTN[1],'\033[1m\033[44m\033[37m M/D \033[0m' + '\033[32m  IP MODEM-B1 Query                                                         lqms_ping.py Ver.' + VER + '\033[0m')
    elif (IPA == '192.168.1.22'):
        MD = 'MDB2'
        MDP = ' IP MODEM-B2 '
        FN3 = '/mnt/ssd/log/mdb2/MDB2_'
        print ('          ',DTN[1],'\033[1m\033[44m\033[37m M/D \033[0m' + '\033[32m  IP MODEM-B2 Query                                                         lqms_ping.py Ver.' + VER + '\033[0m')
    elif (IPA == '192.168.1.23'):
        MD = 'MDC1'
        MDP = ' IP MODEM-C1 '
        FN3 = '/mnt/ssd/log/mdc1/MDC1_'
        print ('          ',DTN[1],'\033[1m\033[44m\033[37m M/D \033[0m' + '\033[32m  IP MODEM-C1 Query                                                         lqms_ping.py Ver.' + VER + '\033[0m')
    elif (IPA == '192.168.1.24'):
        MD = 'MDC2'
        MDP = ' IP MODEM-C2 '
        FN3 = '/mnt/ssd/log/mdc2/MDC2_'
        print ('          ',DTN[1],'\033[1m\033[44m\033[37m M/D \033[0m' + '\033[32m  IP MODEM-C2 Query                                                         lqms_ping.py Ver.' + VER + '\033[0m')
    elif (IPA == '192.168.1.25'):
        MD = 'MDE1'
        MDP = ' IP MODEM-E1 '
        FN3 = '/mnt/ssd/log/mde1/MDE1_'
        print ('          ',DTN[1],'\033[1m\033[44m\033[37m M/D \033[0m' + '\033[32m  IP MODEM-E1 Query                                                         lqms_ping.py Ver.' + VER + '\033[0m')
    elif (IPA == '192.168.1.26'):
        MD = 'MDE2'
        MDP = ' IP MODEM-E2 '
        FN3 = '/mnt/ssd/log/mde2/MDE2_'
        print ('          ',DTN[1],'\033[1m\033[44m\033[37m M/D \033[0m' + '\033[32m  IP MODEM-E2 Query                                                         lqms_ping.py Ver.' + VER + '\033[0m')

    elif (IPA == '192.168.1.101'):
        MD = 'Ku-BUC-A'
        MDP = 'Ku band BUC-A'
        FN3 = '/mnt/ssd/log/kubuc-a/KUBUC-A_'
        print ('          ',DTN[1],'\033[1m\033[46m\033[37m BUC \033[0m' + '\033[32m  Ku band BUC-A Query                                                       lqms_ping.py Ver.' + VER + '\033[0m')
    elif (IPA == '192.168.1.102'):
        MD = 'Ku-BUC-B'
        MDP = 'Ku band BUC-B'
        FN3 = '/mnt/ssd/log/kubuc-b/KUBUC-B_'
        print ('          ',DTN[1],'\033[1m\033[46m\033[37m BUC \033[0m' + '\033[32m  Ku band BUC-B Query                                                       lqms_ping.py Ver.' + VER + '\033[0m')
    elif (IPA == '192.168.1.111'):
        MD = 'C-BUC-A'
        MDP = ' C band BUC-A'
        FN3 = '/mnt/ssd/log/cbuc-a/CBUC-A_'
        print ('          ',DTN[1],'\033[1m\033[46m\033[37m BUC \033[0m' + '\033[32m  C band BUC-A Query                                                        lqms_ping.py Ver.' + VER + '\033[0m')
    elif (IPA == '192.168.1.112'):
        MD = 'C-BUC-B'
        MDP = ' C band BUC-B'
        FN3 = '/mnt/ssd/log/cbuc-b/CBUC-B_'
        print ('          ',DTN[1],'\033[1m\033[46m\033[37m BUC \033[0m' + '\033[32m  C band BUC-B Query                                                        lqms_ping.py Ver.' + VER + '\033[0m')

    ANS = ping(IPA)

    if (ANS == None):
        with open(FN3 + DTN[5] + '.log', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([DTN[0], DTN[1], MD, 'PING-ER01', 'The unit was not Ping-responding.' ])
        with open(FN2 + DTN[5] + '.log', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([DTN[0], DTN[1], MD, 'PING-ER01', 'The unit was not Ping-responding.' ])
        if ('BUC' in MD):
            print ('          ',DTN[1], '\33[1m\033[46m\033[37m' + ' BUC ' + '\033[0m' +'  \033[1m\033[41m\033[37m FAULT \033[0m \033[1m\033[32m' + MDP + ' The unit was not Ping-responding.\033[0m\033[32m                   lqms_ping.py Ver.' + VER + '\033[0m')
        elif ('BUC' not in MD):
            print ('          ',DTN[1], '\33[1m\033[44m\033[37m' + ' M/D ' + '\033[0m' +'  \033[1m\033[41m\033[37m FAULT \033[0m \033[1m\033[32m' + MDP + ' The unit was not Ping-responding.\033[0m\033[32m                   lqms_ping.py Ver.' + VER + '\033[0m')

        STATE = 'ER.01'
    elif (ANS == False):
        with open(FN3 + DTN[5] + '.log', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([DTN[0], DTN[1], MD, 'PING-ER02', 'The unit was not boot or disconnected.' ])
        with open(FN2 + DTN[5] + '.log', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([DTN[0], DTN[1], MD, 'PING-ER02', 'The unit was not boot or disconnected.' ])
        if ('BUC' in MD):
            print ('          ',DTN[1], '\33[1m\033[46m\033[37m' + ' BUC ' + '\033[0m' +'  \033[1m\033[41m\033[37m FAULT \033[0m \033[1m\033[32m' + MDP + ' The unit was not boot or disconnected.\033[0m\033[32m              lqms_ping.py Ver.' + VER + '\033[0m')
        elif ('BUC' not in MD):
            print ('          ',DTN[1], '\33[1m\033[44m\033[37m' + ' M/D ' + '\033[0m' +'  \033[1m\033[41m\033[37m FAULT \033[0m \033[1m\033[32m' + MDP + ' The unit was not boot or disconnected.\033[0m\033[32m              lqms_ping.py Ver.' + VER + '\033[0m')

        STATE = 'ER.02'
    else:
        with open(FN2 + DTN[5] + '.log', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([DTN[0], DTN[1], MD, 'PNG', 'The unit was respond Ping.' ])
        with open(FN3 + DTN[5] + '.log', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([DTN[0], DTN[1], MD, 'PNG', 'The unit was respond Ping.'])

        if ('BUC' in MD):
            print ('          ',DTN[1], '\33[1m\033[46m\033[37m' + ' BUC ' + '\033[0m' +'  \033[1m\033[42m\033[37m  NOM  \033[0m \033[1m\033[32m' + MDP + ' The unit was respond Ping.\033[0m\033[32m                          lqms_ping.py Ver.' + VER + '\033[0m')
        elif ('BUC' not in MD):
            print ('          ',DTN[1], '\33[1m\033[44m\033[37m' + ' M/D ' + '\033[0m' +'  \033[1m\033[42m\033[37m  NOM  \033[0m \033[1m\033[32m' + MDP + ' The unit was respond Ping.\033[0m\033[32m                          lqms_ping.py Ver.' + VER + '\033[0m')
        STATE = 'OK'
    return(STATE)
