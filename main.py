# #################################################################
# ### LQMS-2.0 for JAXA-Tanegashima E/S . RCC                   ###
# ### Release date 2022.10                                      ###
# ### Version 2.3.1                       TechnoBusiness Co.LTD ###
# #################################################################
VER = '2.3.1'

import shutil
import os
import serial
from time import sleep
import time
import warnings

import lqms_dt
import lqms_sno
import lqms_mgc
import lqms_ebn
import lqms_flt
import lqms_ping
import lqms_rtc
import lqms_eth
import lqms_fco0
import lqms_buc
import lqms_upc

# Disable warning display
warnings.simplefilter('ignore')

ACT_MD = ['','','','','','','','','','']    # 10-MODEMs
DIC_SR_MD = {}	# Active MODEMs / Serial
DIC_NT_MD = {}	# Active MODEMs / Ethernet
DIC_NT_BUC = {}  # Active BUCs / Ethernet
MAX_ACT_MD = 0
FLNa = ['','','','','','','','','','']
FLNb = ['','','','','','','','','','']
UPC = ['','','']
##### Delete plot file #####
FLNa[0] = '/home/xs4/basis/req_relFiles/EBN_MDA1_tmp.csv'
FLNa[1] = '/home/xs4/basis/req_relFiles/EBN_MDA2_tmp.csv'
FLNa[2] = '/home/xs4/basis/req_relFiles/EBN_MDB1_tmp.csv'
FLNa[3] = '/home/xs4/basis/req_relFiles/EBN_MDB2_tmp.csv'
FLNa[4] = '/home/xs4/basis/req_relFiles/EBN_MDC1_tmp.csv'
FLNa[5] = '/home/xs4/basis/req_relFiles/EBN_MDC2_tmp.csv'
FLNa[6] = '/home/xs4/basis/req_relFiles/EBN_MDE1_tmp.csv'
FLNa[7] = '/home/xs4/basis/req_relFiles/EBN_MDE2_tmp.csv'
FLNa[8] = '/home/xs4/basis/req_relFiles/BL_KuB_tmp.csv'
FLNa[9] = '/home/xs4/basis/req_relFiles/BL_CB_tmp.csv'
FLNb[0] = '/home/xs4/basis/req_relFiles/MDA1.svg'
FLNb[1] = '/home/xs4/basis/req_relFiles/MDA2.svg'
FLNb[2] = '/home/xs4/basis/req_relFiles/MDB1.svg'
FLNb[3] = '/home/xs4/basis/req_relFiles/MDB2.svg'
FLNb[4] = '/home/xs4/basis/req_relFiles/MDC1.svg'
FLNb[5] = '/home/xs4/basis/req_relFiles/MDC2.svg'
FLNb[6] = '/home/xs4/basis/req_relFiles/MDE1.svg'
FLNb[7] = '/home/xs4/basis/req_relFiles/MDE2.svg'
FLNb[8] = '/home/xs4/basis/req_relFiles/KUBUPC.svg'
FLNb[9] = '/home/xs4/basis/req_relFiles/CBUPC.svg'
for Co in range(0,10):
    is_file = os.path.isfile(FLNa[Co])
    if is_file:
        os.remove(FLNa[Co])
    is_file = os.path.isfile(FLNb[Co])
    if is_file:
        os.remove(FLNb[Co])
    
##### Copies of required underlying files #####
# MODEM-A1
shutil.copyfile("/home/xs4/basis/default/MDXX_DPT_DEF.csv", "/home/xs4/basis/req_relFiles/MDA1_DPT_TMP.csv")
shutil.copyfile("/home/xs4/basis/default/MDXX_ERR_DEF.csv", "/home/xs4/basis/req_relFiles/MDA1_ERR_TMP.csv")
shutil.copyfile("/home/xs4/basis/default/MDXX_FPC_DEF.csv", "/home/xs4/basis/req_relFiles/MDA1_FPC_TMP.csv")
shutil.copyfile("/home/xs4/basis/default/MDXX_IBP_DEF.csv", "/home/xs4/basis/req_relFiles/MDA1_IBP_TMP.csv")
shutil.copyfile("/home/xs4/basis/default/MDXX_OBP_DEF.csv", "/home/xs4/basis/req_relFiles/MDA1_OBP_TMP.csv")
shutil.copyfile("/home/xs4/basis/default/MDXX_RTC_DEF.csv", "/home/xs4/basis/req_relFiles/MDA1_RTC_TMP.csv")
# MODEM-A2
shutil.copyfile("/home/xs4/basis/default/MDXX_DPT_DEF.csv", "/home/xs4/basis/req_relFiles/MDA2_DPT_TMP.csv")
shutil.copyfile("/home/xs4/basis/default/MDXX_ERR_DEF.csv", "/home/xs4/basis/req_relFiles/MDA2_ERR_TMP.csv")
shutil.copyfile("/home/xs4/basis/default/MDXX_FPC_DEF.csv", "/home/xs4/basis/req_relFiles/MDA2_FPC_TMP.csv")
shutil.copyfile("/home/xs4/basis/default/MDXX_IBP_DEF.csv", "/home/xs4/basis/req_relFiles/MDA2_IBP_TMP.csv")
shutil.copyfile("/home/xs4/basis/default/MDXX_OBP_DEF.csv", "/home/xs4/basis/req_relFiles/MDA2_OBP_TMP.csv")
shutil.copyfile("/home/xs4/basis/default/MDXX_RTC_DEF.csv", "/home/xs4/basis/req_relFiles/MDA2_RTC_TMP.csv")
# MODEM-B1
shutil.copyfile("/home/xs4/basis/default/MDXX_DPT_DEF.csv", "/home/xs4/basis/req_relFiles/MDB1_DPT_TMP.csv")
shutil.copyfile("/home/xs4/basis/default/MDXX_ERR_DEF.csv", "/home/xs4/basis/req_relFiles/MDB1_ERR_TMP.csv")
shutil.copyfile("/home/xs4/basis/default/MDXX_FPC_DEF.csv", "/home/xs4/basis/req_relFiles/MDB1_FPC_TMP.csv")
shutil.copyfile("/home/xs4/basis/default/MDXX_IBP_DEF.csv", "/home/xs4/basis/req_relFiles/MDB1_IBP_TMP.csv")
shutil.copyfile("/home/xs4/basis/default/MDXX_OBP_DEF.csv", "/home/xs4/basis/req_relFiles/MDB1_OBP_TMP.csv")
shutil.copyfile("/home/xs4/basis/default/MDXX_RTC_DEF.csv", "/home/xs4/basis/req_relFiles/MDB1_RTC_TMP.csv")
# MODEM-B2
shutil.copyfile("/home/xs4/basis/default/MDXX_DPT_DEF.csv", "/home/xs4/basis/req_relFiles/MDB2_DPT_TMP.csv")
shutil.copyfile("/home/xs4/basis/default/MDXX_ERR_DEF.csv", "/home/xs4/basis/req_relFiles/MDB2_ERR_TMP.csv")
shutil.copyfile("/home/xs4/basis/default/MDXX_FPC_DEF.csv", "/home/xs4/basis/req_relFiles/MDB2_FPC_TMP.csv")
shutil.copyfile("/home/xs4/basis/default/MDXX_IBP_DEF.csv", "/home/xs4/basis/req_relFiles/MDB2_IBP_TMP.csv")
shutil.copyfile("/home/xs4/basis/default/MDXX_OBP_DEF.csv", "/home/xs4/basis/req_relFiles/MDB2_OBP_TMP.csv")
shutil.copyfile("/home/xs4/basis/default/MDXX_RTC_DEF.csv", "/home/xs4/basis/req_relFiles/MDB2_RTC_TMP.csv")
# MODEM-C1
shutil.copyfile("/home/xs4/basis/default/MDXX_DPT_DEF.csv", "/home/xs4/basis/req_relFiles/MDC1_DPT_TMP.csv")
shutil.copyfile("/home/xs4/basis/default/MDXX_ERR_DEF.csv", "/home/xs4/basis/req_relFiles/MDC1_ERR_TMP.csv")
shutil.copyfile("/home/xs4/basis/default/MDXX_FPC_DEF.csv", "/home/xs4/basis/req_relFiles/MDC1_FPC_TMP.csv")
shutil.copyfile("/home/xs4/basis/default/MDXX_IBP_DEF.csv", "/home/xs4/basis/req_relFiles/MDC1_IBP_TMP.csv")
shutil.copyfile("/home/xs4/basis/default/MDXX_OBP_DEF.csv", "/home/xs4/basis/req_relFiles/MDC1_OBP_TMP.csv")
shutil.copyfile("/home/xs4/basis/default/MDXX_RTC_DEF.csv", "/home/xs4/basis/req_relFiles/MDC1_RTC_TMP.csv")
# MODEM-C2
shutil.copyfile("/home/xs4/basis/default/MDXX_DPT_DEF.csv", "/home/xs4/basis/req_relFiles/MDC2_DPT_TMP.csv")
shutil.copyfile("/home/xs4/basis/default/MDXX_ERR_DEF.csv", "/home/xs4/basis/req_relFiles/MDC2_ERR_TMP.csv")
shutil.copyfile("/home/xs4/basis/default/MDXX_FPC_DEF.csv", "/home/xs4/basis/req_relFiles/MDC2_FPC_TMP.csv")
shutil.copyfile("/home/xs4/basis/default/MDXX_IBP_DEF.csv", "/home/xs4/basis/req_relFiles/MDC2_IBP_TMP.csv")
shutil.copyfile("/home/xs4/basis/default/MDXX_OBP_DEF.csv", "/home/xs4/basis/req_relFiles/MDC2_OBP_TMP.csv")
shutil.copyfile("/home/xs4/basis/default/MDXX_RTC_DEF.csv", "/home/xs4/basis/req_relFiles/MDC2_RTC_TMP.csv")
# MODEM-E1
shutil.copyfile("/home/xs4/basis/default/MDXX_DPT_DEF.csv", "/home/xs4/basis/req_relFiles/MDE1_DPT_TMP.csv")
shutil.copyfile("/home/xs4/basis/default/MDXX_ERR_DEF.csv", "/home/xs4/basis/req_relFiles/MDE1_ERR_TMP.csv")
shutil.copyfile("/home/xs4/basis/default/MDXX_FPC_DEF.csv", "/home/xs4/basis/req_relFiles/MDE1_FPC_TMP.csv")
shutil.copyfile("/home/xs4/basis/default/MDXX_IBP_DEF.csv", "/home/xs4/basis/req_relFiles/MDE1_IBP_TMP.csv")
shutil.copyfile("/home/xs4/basis/default/MDXX_OBP_DEF.csv", "/home/xs4/basis/req_relFiles/MDE1_OBP_TMP.csv")
shutil.copyfile("/home/xs4/basis/default/MDXX_RTC_DEF.csv", "/home/xs4/basis/req_relFiles/MDE1_RTC_TMP.csv")
# MODEM-E2
shutil.copyfile("/home/xs4/basis/default/MDXX_DPT_DEF.csv", "/home/xs4/basis/req_relFiles/MDE2_DPT_TMP.csv")
shutil.copyfile("/home/xs4/basis/default/MDXX_ERR_DEF.csv", "/home/xs4/basis/req_relFiles/MDE2_ERR_TMP.csv")
shutil.copyfile("/home/xs4/basis/default/MDXX_FPC_DEF.csv", "/home/xs4/basis/req_relFiles/MDE2_FPC_TMP.csv")
shutil.copyfile("/home/xs4/basis/default/MDXX_IBP_DEF.csv", "/home/xs4/basis/req_relFiles/MDE2_IBP_TMP.csv")
shutil.copyfile("/home/xs4/basis/default/MDXX_OBP_DEF.csv", "/home/xs4/basis/req_relFiles/MDE2_OBP_TMP.csv")
shutil.copyfile("/home/xs4/basis/default/MDXX_RTC_DEF.csv", "/home/xs4/basis/req_relFiles/MDE2_RTC_TMP.csv")
# MODEM-F1
shutil.copyfile("/home/xs4/basis/default/MDXX_DPT_DEF.csv", "/home/xs4/basis/req_relFiles/MDF1_DPT_TMP.csv")
shutil.copyfile("/home/xs4/basis/default/MDXX_ERR_DEF.csv", "/home/xs4/basis/req_relFiles/MDF1_ERR_TMP.csv")
shutil.copyfile("/home/xs4/basis/default/MDXX_FPC_DEF.csv", "/home/xs4/basis/req_relFiles/MDF1_FPC_TMP.csv")
shutil.copyfile("/home/xs4/basis/default/MDXX_IBP_DEF.csv", "/home/xs4/basis/req_relFiles/MDF1_IBP_TMP.csv")
shutil.copyfile("/home/xs4/basis/default/MDXX_OBP_DEF.csv", "/home/xs4/basis/req_relFiles/MDF1_OBP_TMP.csv")
shutil.copyfile("/home/xs4/basis/default/MDXX_RTC_DEF.csv", "/home/xs4/basis/req_relFiles/MDF1_RTC_TMP.csv")
# MODEM-F2
shutil.copyfile("/home/xs4/basis/default/MDXX_DPT_DEF.csv", "/home/xs4/basis/req_relFiles/MDF2_DPT_TMP.csv")
shutil.copyfile("/home/xs4/basis/default/MDXX_ERR_DEF.csv", "/home/xs4/basis/req_relFiles/MDF2_ERR_TMP.csv")
shutil.copyfile("/home/xs4/basis/default/MDXX_FPC_DEF.csv", "/home/xs4/basis/req_relFiles/MDF2_FPC_TMP.csv")
shutil.copyfile("/home/xs4/basis/default/MDXX_IBP_DEF.csv", "/home/xs4/basis/req_relFiles/MDF2_IBP_TMP.csv")
shutil.copyfile("/home/xs4/basis/default/MDXX_OBP_DEF.csv", "/home/xs4/basis/req_relFiles/MDF2_OBP_TMP.csv")
shutil.copyfile("/home/xs4/basis/default/MDXX_RTC_DEF.csv", "/home/xs4/basis/req_relFiles/MDF2_RTC_TMP.csv")
# BUCs
shutil.copyfile("/home/xs4/basis/default/BUC_ST_DEF.csv", "/home/xs4/basis/req_relFiles/KuBUC-As.csv")
shutil.copyfile("/home/xs4/basis/default/BUC_VL_DEF.csv", "/home/xs4/basis/req_relFiles/KuBUC-Av.csv")
shutil.copyfile("/home/xs4/basis/default/BUC_ST_DEF.csv", "/home/xs4/basis/req_relFiles/KuBUC-Bs.csv")
shutil.copyfile("/home/xs4/basis/default/BUC_VL_DEF.csv", "/home/xs4/basis/req_relFiles/KuBUC-Bv.csv")
shutil.copyfile("/home/xs4/basis/default/BUC_ST_DEF.csv", "/home/xs4/basis/req_relFiles/CBUC-As.csv")
shutil.copyfile("/home/xs4/basis/default/BUC_VL_DEF.csv", "/home/xs4/basis/req_relFiles/CBUC-Av.csv")
shutil.copyfile("/home/xs4/basis/default/BUC_ST_DEF.csv", "/home/xs4/basis/req_relFiles/CBUC-Bs.csv")
shutil.copyfile("/home/xs4/basis/default/BUC_VL_DEF.csv", "/home/xs4/basis/req_relFiles/CBUC-Bv.csv")
#UPCs
shutil.copyfile("/home/xs4/basis/default/UPC_DEF_TRK.csv", "/home/xs4/basis/req_relFiles/C_UPC_DEF_TRK.csv")
shutil.copyfile("/home/xs4/basis/default/UPC_DEF_UPC.csv", "/home/xs4/basis/req_relFiles/C_UPC_DEF_UPC.csv")
shutil.copyfile("/home/xs4/basis/default/UPC_DEF_STA.csv", "/home/xs4/basis/req_relFiles/C_UPC_DEF_STA.csv")
shutil.copyfile("/home/xs4/basis/default/UPC_DEF_TRK.csv", "/home/xs4/basis/req_relFiles/Ku_UPC_DEF_TRK.csv")
shutil.copyfile("/home/xs4/basis/default/UPC_DEF_UPC.csv", "/home/xs4/basis/req_relFiles/Ku_UPC_DEF_UPC.csv")
shutil.copyfile("/home/xs4/basis/default/UPC_DEF_STA.csv", "/home/xs4/basis/req_relFiles/Ku_UPC_DEF_STA.csv")

##### Transmit Serial Data for MODEM #####
def TRX(DAT):
    try :
        ser.write(DAT.encode("utf-8"))
        ser.flush
        sleep(0.5)
        Rcvd = ser.readline()
        RxDAT = Rcvd.decode('ascii')
        RxDAT = RxDAT = RxDAT.replace( '\r' , '' ).replace( '\n' , '' )
        ser.flush
        sleep(0.5)
        return(RxDAT)
    except(UnicodeDecodeError):
        RxDAT=''
        return(RxDAT)

##### CHECKSUM Calculate #####
def CL_CHK(CHK) :
    SUM = 0
    if len(CHK) == 6 :
        for i in range(0,6,2):
            SUM = SUM +	int(CHK[i:i+2],16)
    elif len(CHK) == 4 :
        for i in range(0,4,2):
            SUM = SUM +	int(CHK[i:i+2],16)
    SUM = SUM & 255
    CHK_SUM = hex(SUM)
    if len(CHK_SUM) == 4 :
        CHK_SUM = str(CHK_SUM[-2:])
    elif len(CHK_SUM) == 3 :
        CHK_SUM = '0' + str(CHK_SUM[-1])
    return (CHK_SUM)
    
##### Transmit Serial Data for UPC #####
def TRX2(ADD,CONT):
    RxD = ''
    recv_data = ''
    if (CONT == 'Status'):
        STx = '02'
        NONs = '06'
        MESs = '28'
        CHKs = CL_CHK( ADD + MESs ) 
        ETx = '03'
        TxD = STx + NONs + ADD + MESs + CHKs + ETx
        TxB = bytes.fromhex(TxD)
        ser.write(TxB)
        ser.flush
        sleep(1)
        recv_data = ser.read(76)
        RxD = recv_data.hex()

    elif (CONT == 'Tracking'):
        STx = '02'
        NONs = '07'
        MESs = '14'
        INFs = '4B'
        CHKs = CL_CHK( ADD + MESs + INFs )
        ETx = '03'
        TxDs = STx + NONs + ADD + MESs + INFs + CHKs + ETx
        TxB = bytes.fromhex(TxDs)
        ser.write(TxB)
        ser.flush
        sleep(1)
        recv_data = ser.read(100)
        RxD = recv_data.hex()
        ser.flush
        recv_data = ''
        sleep(1)

    elif (CONT == 'UPC'):
#        print ('          ',DTN[1],'\033[1m\033[42m\033[37m\033[1m UPC \033[0m' + '\033[32m\033[1m  UPC Power Control System Query \033[0m' + '     main.py Ver.' + VER)
        STx = '02'
        NONs = '07'
        MESs = '14'
        INFs = '55'
        CHKs = CL_CHK( ADD + MESs + INFs )
        ETx = '03'
        TxDs = STx + NONs + ADD + MESs + INFs + CHKs + ETx
        TxB = bytes.fromhex(TxDs)
        ser.write(TxB)
        ser.flush
        sleep(1)
        recv_data = ser.read(63)
        RxD = recv_data.hex()
        recv_data = ''
        ser.flush

    return (RxD)

##### Start #####
if __name__ == '__main__':
    ports = '/dev/ttymxc1'
    try:
        ser = serial.Serial()
        ser.port = ports
        ser.baudrate ='19200'
        ser.timeout = 0.1
        ser.open()
    except:
        print('COM Port Error: ' + ports )
    print ('Serial Port Open')

for Co in range (1,9):
    DIC_NT_MD[Co] = ''

##### Ethernet Control #####
BUCKA = lqms_ping.ST('192.168.1.101')   # Ethernet SYS PING Procedure for Ku-Band BUC-A
BUCKB = lqms_ping.ST('192.168.1.102')   # Ethernet SYS PING Procedure for Ku-Band BUC-B
BUCCA = lqms_ping.ST('192.168.1.111')   # Ethernet SYS PING Procedure for C-Band BUC-A
BUCCB = lqms_ping.ST('192.168.1.112')   # Ethernet SYS PING Procedure for C-Band BUC-B
if (BUCKA == 'OK'):
    DIC_NT_BUC[0] = '192.168.1.101'
else :
    DIC_NT_BUC[0] = '---'
if (BUCKB == 'OK'):
    DIC_NT_BUC[1] = '192.168.1.102'
else :
    DIC_NT_BUC[1] = '---'
if (BUCCA == 'OK'):
    DIC_NT_BUC[2] = '192.168.1.111'
else :
    DIC_NT_BUC[2] = '---'
if (BUCCB == 'OK'):
    DIC_NT_BUC[3] = '192.168.1.112'
else :
    DIC_NT_BUC[3] = '---'

##### Serial Control  :  SNO Command Query #####
for ADD in range (11,19):
    TxADD = '00' + str(ADD)
    TxCMD = 'SNO?'
    TxDAT = '<' + TxADD + '/' + TxCMD + '\r\n'
    ANS = TRX(TxDAT)
    if (ANS == ''):
        ANS = 'NUC'
        if (TxADD == '0011'):
            DIC_NT_MD[1] = ''
        elif (TxADD == '0012'):
            DIC_NT_MD[2] = ''
        elif (TxADD == '0013'):
            DIC_NT_MD[3] = ''
        elif (TxADD == '0014'):
            DIC_NT_MD[4] = ''
        elif (TxADD == '0015'):
            DIC_NT_MD[5] = ''
        elif (TxADD == '0016'):
            DIC_NT_MD[6] = ''
        elif (TxADD == '0017'):
            DIC_NT_MD[7] = ''
        elif (TxADD == '0018'):
            DIC_NT_MD[8] = ''
    else :
        if (TxADD == '0011'):
            MDA1 = lqms_ping.ST('192.168.1.11')   # Ethernet SYS PING Procedure for MDA1
            if (MDA1 == 'OK'):
                DIC_NT_MD[1] = '192.168.1.11'
        elif (TxADD == '0012'):
            MDA2 = lqms_ping.ST('192.168.1.12')   # Ethernet SYS PING Procedure for MDA2
            if (MDA2 == 'OK'):
                DIC_NT_MD[2] = '192.168.1.12'
        elif (TxADD == '0013'):
            MDB1 = lqms_ping.ST('192.168.1.21')   # Ethernet SYS PING Procedure for MDB1
            if (MDB1 == 'OK'):
                DIC_NT_MD[3] = '192.168.1.21'
        elif (TxADD == '0014'):
            MDB2 = lqms_ping.ST('192.168.1.22')   # Ethernet SYS PING Procedure for MDB2
            if (MDB2 == 'OK'):
                DIC_NT_MD[4] = '192.168.1.22'
        elif (TxADD == '0015'):
            MDC1 = lqms_ping.ST('192.168.1.23')   # Ethernet SYS PING Procedure for MDC1
            if (MDC1 == 'OK'):
                DIC_NT_MD[5] = '192.168.1.23'
        elif (TxADD == '0016'):
            MDC2 = lqms_ping.ST('192.168.1.24')   # Ethernet SYS PING Procedure for MDC2
            if (MDC2 == 'OK'):
                DIC_NT_MD[6] = '192.168.1.24'
        elif (TxADD == '0017'):
            MDE1 = lqms_ping.ST('192.168.1.25')   # Ethernet SYS PING Procedure for MDE1
            if (MDE1 == 'OK'):
                DIC_NT_MD[7] = '192.168.1.25'
        elif (TxADD == '0018'):
            MDE2 = lqms_ping.ST('192.168.1.26')   # Ethernet SYS PING Procedure for MDE2
            if (MDE2 == 'OK'):
                DIC_NT_MD[8] = '192.168.1.26'

        ANS = lqms_sno.ST(ANS)
    DIC_SR_MD[TxADD] = ANS
DTN=lqms_dt.RTC_CHK()
# print ('          ',DTN[1],'\033[1m\033[44m\033[37m\033[1m M/D \033[0m' + '\033[34m\033[1m  SNO Command Query \033[0m' + '     main.py Ver.' + VER)

# Only active MODEMs are extracted from the dictionary(DIC_SR_MD)
Co = 0
for k,v in DIC_SR_MD.items():
    if ( v != 'NUC'):
        ACT_MD[Co] = k
        SN = v
        Co += 1
MAX_ACT_MD = Co-1

##### Serial Control : MGC Command Query #####
for Co in range (0,MAX_ACT_MD+1):
    TxADD = ACT_MD[Co]
    TxCMD = 'MGC?'
    TxDAT = '<' + TxADD + '/' + TxCMD +'\r\n'
    ANS = TRX(TxDAT)
    ANS = lqms_mgc.ST(ANS)
# print ('          ',DTN[1],'\033[1m\033[44m\033[37m\033[1m M/D \033[0m' + '\033[34m\033[1m  MGC Command Query \033[0m' + '     main.py Ver.' + VER)

##### Serial Control : UPC #####
for add in range(31,33):
    ANS = TRX2(str(add),'Tracking')
    ADD = add -31
    if (len(ANS) != 0):
        ANS = lqms_upc.TK(Co,ANS)
        UPC[ADD] = 'OK'
    else :
        UPC[ADD] = '---'
    sleep(2)


while True:
    time.sleep(1)
    DTN = lqms_dt.RTC_CHK()
    ##### Serial Control  :  EBN Command Query #####
    if (DTN[4] == 30 or DTN[4] == 0):
        for Co in range (0,MAX_ACT_MD+1):
            TxADD = ACT_MD[Co]
            TxCMD = 'EBN?'
            TxDAT = '<' + TxADD + '/' + TxCMD +'\r\n'
            ANS = TRX(TxDAT)
            if (ANS != ''):
                ANS = lqms_ebn.ST(ANS,DTN[4])
#    print ('          ',DTN[1],'\033[1m\033[44m\033[37m\033[1m M/D \033[0m' + '\033[34m\033[1m  EBN Command Query \033[0m' + '     main.py Ver.' + VER)

    ##### Serial Control  :  FLT Command Query #####
    if (DTN[4] == 20):
        for Co in range (0,MAX_ACT_MD+1):
            TxADD = ACT_MD[Co]
            TxCMD = 'FLT?'
            TxDAT = '<' + TxADD + '/' + TxCMD +'\r\n'
            ANS = TRX(TxDAT)
            if (ANS != ''):
                ANS = lqms_flt.ST(ANS)
#    print ('          ',DTN[1],'\033[1m\033[44m\033[37m\033[1m M/D \033[0m' + '\033[34m\033[1m  FLT Command Query \033[0m' + '     main.py Ver.' + VER)

    ##### Ethernet Control  :  BUC Web Scraping #####
    if (DTN[4] == 10):
        for Co in range (0,4):
            if (DIC_NT_BUC[Co] != '---'):
                lqms_buc.ST(DIC_NT_BUC[Co])    # Ethernet SYS Router Counter Check Procedure

    ##### Serial Control  :  UPC Query #####
    if (DTN[4] == 40):
        if (DTN[3] %2 == 0):
            for Co in range (0,2):
                if (UPC[Co] != '---'):
                    ADD = str(Co + 31)
                    ANS = TRX2(ADD , 'UPC')    # UPC Status Query
                    ANS = lqms_upc.UPC(ADD,ANS)

        elif (DTN[3] %2 != 0):
            for Co in range (0,2):
                if (UPC[Co] != '---'):
                    ADD = str(Co + 31)
                    ANS = TRX2(ADD , 'Status')    # UPC Status Query
                    ANS = lqms_upc.ST(ADD,ANS)
            #print ('          ',DTN[1],'\033[1m\033[42m\033[37m\033[1m UPC \033[0m' + '\033[32m\033[1m  UPC Status Query \033[0m' + '     main.py Ver.' + VER)
    ##### Serial Control  :  SNO Command Query (Health Check for MODEM) #####
    if ( DTN[3] %5 == 0 ) :
        if ( DTN[4] ==25 ):
            for ADD in range (11,19):
                TxADD = '00' + str(ADD)
                TxCMD = 'SNO?'
                TxDAT = '<' + TxADD + '/' + TxCMD + '\r\n'
                ANS = TRX(TxDAT)
                if (ANS == ''):
                    ANS = 'NUC'
                    if (TxADD == '0011'):
                        DIC_NT_MD[1] = ''
                        FLNa[0] = '/home/xs4/basis/req_relFiles/EBN_MDA1_tmp.csv'
                        FLNb[0] = '/home/xs4/basis/req_relFiles/MDA1.svg'
                    elif (TxADD == '0012'):
                        DIC_NT_MD[2] = ''
                        FLNa[1] = '/home/xs4/basis/req_relFiles/EBN_MDA2_tmp.csv'
                        FLNb[1] = '/home/xs4/basis/req_relFiles/MDA2.svg'
                    elif (TxADD == '0013'):
                        DIC_NT_MD[3] = ''
                        FLNa[2] = '/home/xs4/basis/req_relFiles/EBN_MDB1_tmp.csv'
                        FLNb[2] = '/home/xs4/basis/req_relFiles/MDB1.svg'
                    elif (TxADD == '0014'):
                        DIC_NT_MD[4] = ''
                        FLNa[3] = '/home/xs4/basis/req_relFiles/EBN_MDB2_tmp.csv'
                        FLNb[3] = '/home/xs4/basis/req_relFiles/MDB2.svg'
                    elif (TxADD == '0015'):
                        DIC_NT_MD[5] = ''
                        FLNa[4] = '/home/xs4/basis/req_relFiles/EBN_MDC1_tmp.csv'
                        FLNb[4] = '/home/xs4/basis/req_relFiles/MDC1.svg'
                    elif (TxADD == '0016'):
                        DIC_NT_MD[6] = ''
                        FLNa[5] = '/home/xs4/basis/req_relFiles/EBN_MDC2_tmp.csv'
                        FLNb[5] = '/home/xs4/basis/req_relFiles/MDC2.svg'
                    elif (TxADD == '0017'):
                        DIC_NT_MD[7] = ''
                        FLNa[6] = '/home/xs4/basis/req_relFiles/EBN_MDE1_tmp.csv'
                        FLNb[6] = '/home/xs4/basis/req_relFiles/MDE1.svg'
                    elif (TxADD == '0018'):
                        DIC_NT_MD[8] = ''
                        FLNa[7] = '/home/xs4/basis/req_relFiles/EBN_MDE2_tmp.csv'
                        FLNb[7] = '/home/xs4/basis/req_relFiles/MDE2.svg'
                    for Co in range(0,9):
                        is_file = os.path.isfile(FLNa[Co])
                        if is_file:
                            os.remove(FLNa[Co])
                        is_file = os.path.isfile(FLNb[Co])
                        if is_file:
                            os.remove(FLNb[Co])
                else :
                    if (TxADD == '0011'):
                        MDA1 = lqms_ping.ST('192.168.1.11')   # Ethernet SYS PING Procedure for MDA1
                        if (MDA1 == 'OK'):
                            DIC_NT_MD[1] = '192.168.1.11'
                    elif (TxADD == '0012'):
                        MDA2 = lqms_ping.ST('192.168.1.12')   # Ethernet SYS PING Procedure for MDA2
                        if (MDA2 == 'OK'):
                            DIC_NT_MD[2] = '192.168.1.12'
                    elif (TxADD == '0013'):
                        MDB1 = lqms_ping.ST('192.168.1.21')   # Ethernet SYS PING Procedure for MDB1
                        if (MDB1 == 'OK'):
                            DIC_NT_MD[3] = '192.168.1.21'
                    elif (TxADD == '0014'):
                        MDB2 = lqms_ping.ST('192.168.1.22')   # Ethernet SYS PING Procedure for MDB2
                        if (MDB2 == 'OK'):
                            DIC_NT_MD[4] = '192.168.1.22'
                    elif (TxADD == '0015'):
                        MDC1 = lqms_ping.ST('192.168.1.23')   # Ethernet SYS PING Procedure for MDC1
                        if (MDC1 == 'OK'):
                            DIC_NT_MD[5] = '192.168.1.23'
                    elif (TxADD == '0016'):
                        MDC2 = lqms_ping.ST('192.168.1.24')   # Ethernet SYS PING Procedure for MDC2
                        if (MDC2 == 'OK'):
                            DIC_NT_MD[6] = '192.168.1.24'
                    elif (TxADD == '0017'):
                        MDE1 = lqms_ping.ST('192.168.1.25')   # Ethernet SYS PING Procedure for MDE1
                        if (MDE1 == 'OK'):
                            DIC_NT_MD[7] = '192.168.1.25'
                    elif (TxADD == '0018'):
                        MDE2 = lqms_ping.ST('192.168.1.26')   # Ethernet SYS PING Procedure for MDE2
                        if (MDE2 == 'OK'):
                            DIC_NT_MD[8] = '192.168.1.26'
                ANS = lqms_sno.ST(ANS)
                DIC_SR_MD[TxADD] = ANS
            DTN=lqms_dt.RTC_CHK()
#            print ('          ',DTN[1],'\033[1m\033[44m\033[37m\033[1m M/D \033[0m' + '\033[34m\033[1m  SNO Command Query \033[0m' + '     main.py Ver.' + VER)

            # Only active MODEMs are extracted from the dictionary(DIC_SR_MD)
            Co = 0
            for k,v in DIC_SR_MD.items():
                if ( v != 'NUC'):
                    ACT_MD[Co] = k
                    SN = v
                    Co += 1
            MAX_ACT_MD = Co-1

            ##### Serial Control : MGC Command Query #####
            for Co in range (0,MAX_ACT_MD+1):
                TxADD = ACT_MD[Co]
                TxCMD = 'MGC?'
                TxDAT = '<' + TxADD + '/' + TxCMD +'\r\n'
                ANS = TRX(TxDAT)
                if (ANS != ''):
                    ANS = lqms_mgc.ST(ANS)
            # print ('          ',DTN[1],'\033[1m\033[44m\033[37m\033[1m M/D \033[0m' + '\033[34m\033[1m  MGC Command Query \033[0m' + '     main.py Ver.' + VER)

    if ( DTN[3] == 5 or DTN[3] == 15 or DTN[3] == 25 or DTN[3] == 35 or DTN[3] == 45 or DTN[3] == 55 ) :
        if( DTN[4] == 50 ):
            ##### Ethernet Control  :  Ethernet Router Counter #####
            for Co in range (1,9):
                if (DIC_NT_MD[Co]  != ''):
                    lqms_rtc.ST(DIC_NT_MD[Co])    # Ethernet SYS Router Counter Check Procedure
#            print ('          ',DTN[1],'\033[1m\033[44m\033[37m\033[1m M/D \033[0m' + '\033[34m\033[1m  Router Counter of MODEM \033[0m' + '                                   main.py Ver.' + VER)

    if ( DTN[3] == 0 or DTN[3] == 10 or DTN[3] == 20 or DTN[3] == 30 or DTN[3] == 40 or DTN[3] == 50 ) :
        if ( DTN[4] == 50 ):
            ##### Ethernet Control  :  Ethernet counter #####
            for Co in range (1,9):
                if (DIC_NT_MD[Co]  != ''):
                    lqms_eth.ST(DIC_NT_MD[Co])    # Ethernet SYS Ethernet Counter Check Procedure
#            print ('          ',DTN[1],'\033[1m\033[44m\033[37m\033[1m M/D \033[0m' + '\033[34m\033[1m  Ethernet Counter of MODEM \033[0m' + '                                   main.py Ver.' + VER)
                              
    if ( DTN[2] == 0 or DTN[3] == 0 ) :
        if(DTN[4] == 40):
                lqms_fco0.ST()
