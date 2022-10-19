#####
# BUC Status reader for LQMS-2.0E Version 0.0.4
# 2022.08.28 Yoshiaki Sato[Technobiz]
#####
import lqms_dt
import lqms_plt3
import csv
from bs4 import BeautifulSoup
import requests
import os

VER = '0.0.4'
FN1 = '/mnt/ssd/log/error/err_'
FN2 = '/mnt/ssd/log/facl/sys_'

DAT1=['','','','','','','','','','','','','','','','','','','','','','']
DAT2=['','','','','','','','','','','','','','','','','','','','','','','','','','']
def ST(IPA):
    os.chdir('/home/xs4/basis/')
    DTN = lqms_dt.RTC_CHK()

    # Parameter of Outbound Packets [Counters]
#    DAT1[0] = ''   # 24V PS1               DAT1[1] = ''   # 24V PS2 
#    DAT1[2] = ''   # 13.5V PS              DAT1[3] = ''   # 10V PS1
#    DAT1[4] = ''   # 10V PS2 N/A           DAT1[5] = ''   # 10V RFPS1
#    DAT1[6] = ''   # 10V RFPS2 N/A         DAT1[7] = ''   # 7.8V PS
#    DAT1[8] = ''   # 5.8V PS               DAT1[9] = ''   # 2.5V PS
#    DAT1[10] = ''   # 1.2V PS              DAT1[11] = ''   # -5.8V PS
#    DAT1[12] = ''   # LNB PS N/A           DAT1[13] = ''   # LNB CUR N/A
#    DAT1[14] = ''   # FRD POWER            DAT1[15] = ''   # REV POWER N/A
#    DAT1[16] = ''   # RED SW               DAT1[17] = ''   # RED LNK
#    DAT1[18] = ''   # FAN1 SPD             DAT1[19] = ''   # FAN2 SPD N/A
#    DAT1[20] = ''   # FAN3 SPD N/A         DAT1[21] = ''   # AMP TEMP

#    DAT2[0] = ''   # 24V PS1               DAT2[1] = ''   # 24V PS2
#    DAT2[2] = ''   # 13.5V PS              DAT2[3] = ''   # 10V PS1
#    DAT2[4] = ''   # 10V PS2 N/A           DAT2[5] = ''   # 10V RFPS1
#    DAT2[6] = ''   # 10V RFPS1             DAT2[7] = ''   # 7.8V PS
#    DAT2[8] = ''   # 5.8V PS               DAT2[9] = ''   # 2.5V PS
#    DAT2[10] = ''   # 1.2V PS               DAT2[11] = ''   # -5.8V PS
#    DAT2[12] = ''   # LNB PS N/A           DAT2[13] = ''   # LNB CUR N/A
#    DAT2[14] = ''   # FRD POWER            DAT2[15] = ''   # REV POWER N/A
#    DAT2[16] = ''   # RED SW               DAT2[17] = ''   # RED LNK
#    DAT2[18] = ''   # FAN1 SPD             DAT2[19] = ''   # FAN2 SPD N/A
#    DAT2[20] = ''   # FAN3 SPD N/A         DAT2[21] = ''   # AMP TEMP
#    DAT2[22] = ''   # PVER TEMP            DAT2[23] = ''   # FLASH CHKSUM
#    DAT2[24] = ''   # FPGA DONE            DAT2[25] = ''   # I2C BUS
#    DAT2[26] = ''   # REF LOCK DET         DAT2[27] = ''   # BUC LOCK DET

    # Reading HLD data file
    if (IPA == '192.168.1.101'):
        BUC = 'KuBUC-A'
        FLN1 = 'KuBUC-Av.csv'
        FLN2 = 'KuBUC-As.csv'
        FN3 = '/mnt/ssd/log/kubuc-a/KuBUC-A_'
    elif (IPA == '192.168.1.102'):
        BUC = 'KuBUC-B'
        FLN1 = 'KuBUC-Bv.csv'
        FLN2 = 'KuBUC-Bs.csv'
        FN3 = '/mnt/ssd/log/kubuc-b/KuBUC-B_'
    elif (IPA == '192.168.1.111'):
        BUC = 'CBUC-A'
        FLN1 = 'CBUC-Av.csv'
        FLN2 = 'CBUC-As.csv'
        FN3 = '/mnt/ssd/log/cbuc-a/CBUC-A_'
    elif (IPA == '192.168.1.112'):
        BUC = 'CBUC-B'
        FLN1 = 'CBUC-Bv.csv'
        FLN2 = 'CBUC-Bs.csv'
        FN3 = '/mnt/ssd/log/bbuc-b/CBUC-B_'

    fld = '/home/xs4/basis/req_relFiles/'
    FLN1 = fld + FLN1
    FLN2 = fld + FLN2

    # File Check-1
    with open(FLN1) as f:
        reader = csv.reader(f)
        BUC_V = [row for row in reader]
#    print(BUC_V[0][0],BUC_V[0][1],BUC_V[0][2],BUC_V[0][3],BUC_V[0][4],BUC_V[0][5],BUC_V[0][6],BUC_V[0][7],BUC_V[0][8],BUC_V[0][9],BUC_V[0][10],BUC_V[0][11],BUC_V[0][12],BUC_V[0][13],BUC_V[0][14],BUC_V[0][15],BUC_V[0][16],BUC_V[0][17],BUC_V[0][18],BUC_V[0][19],BUC_V[0][20],BUC_V[0][21])

    # File Check-2
    with open(FLN2) as f:
        reader = csv.reader(f)
        BUC_S = [row for row in reader]
#    print(BUC_S[0][0],BUC_S[0][1],BUC_S[0][2],BUC_S[0][3],BUC_S[0][4],BUC_S[0][5],BUC_S[0][6],BUC_S[0][7],BUC_S[0][8],BUC_S[0][9],BUC_S[0][10],BUC_S[0][11],BUC_S[0][12],BUC_S[0][13],BUC_S[0][14],BUC_S[0][15],BUC_S[0][16],BUC_S[0][17],BUC_S[0][18],BUC_S[0][19],BUC_S[0][20],BUC_S[0][21],BUC_S[0][22],BUC_S[0][23],BUC_S[0][24],BUC_S[0][25])

    DTN = lqms_dt.RTC_CHK()
    URL = 'http://' + IPA + '/status.htm'
    res = requests.get(URL,auth=('comtech','comtech'))
    content = res.content
    soup = BeautifulSoup(content, 'html.parser')

    print ('          ',DTN[1],'\033[1m\033[46m\033[37m\033[1m BUC \033[0m  LPod-BUC Ethernet Counter Monitor & Recorder                              lqms_buc.py Ver.' + VER)
    with open(FN2 + DTN[5] + '.log', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([DTN[0], DTN[1], BUC, 'BUC','Web Analysis', 'BUC Status'])

    # 01 24V-PS1
    BUC_VAL0 = soup.select('td')[9].string.replace(' Volts','')
    BUC_VAL0 = BUC_VAL0.lstrip()
    BUC_VAL0 = BUC_VAL0.rstrip()
    BUC_STA0 = soup.select('td')[10].string
#    print ('BUC Value [0] :', BUC_V[0][0], BUC_VAL0 , 'BUC State [0] :', BUC_S[0][0], BUC_STA0)
    if (BUC_V[0][0] != BUC_VAL0) or (BUC_S[0][0] != BUC_STA0) :
        with open(FN3 + DTN[5] + '.log', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([DTN[0], DTN[1], BUC, 'BUC', '24V PS1 VTG', BUC_VAL0, BUC_STA0])

    # 02 24V-PS2
    BUC_VAL1 = soup.select('td')[16].string.replace(' Volts','')
    BUC_VAL1 = BUC_VAL1.lstrip()
    BUC_VAL1 = BUC_VAL1.rstrip()
    BUC_STA1 = soup.select('td')[17].string
#    print ('BUC Value [1] :', BUC_V[0][1], BUC_VAL1 , 'BUC State [1] :', BUC_S[0][1], BUC_STA1)
    if (BUC_V[0][1] != BUC_VAL1) or (BUC_S[0][1] != BUC_STA1):
        with open(FN3 + DTN[5] + '.log', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([DTN[0], DTN[1], BUC, 'BUC', '24V PS2 VTG', BUC_VAL1, BUC_STA1])

    # 03 13.5V-PS
    BUC_VAL2 = soup.select('td')[23].string.replace(' Volts','')
    BUC_VAL2 = BUC_VAL2.lstrip()
    BUC_VAL2 = BUC_VAL2.rstrip()
    BUC_STA2 = soup.select('td')[24].string
#    print ('BUC Value [2] :', BUC_V[0][2], BUC_VAL2 , 'BUC State [2] :', BUC_S[0][2], BUC_STA2)
    if (BUC_V[0][2] != BUC_VAL2) or (BUC_S[0][2] != BUC_STA2):
        with open(FN3 + DTN[5] + '.log', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([DTN[0], DTN[1], BUC, 'BUC', '13.5V PS VTG', BUC_VAL2, BUC_STA2])

    # 04 10V-PS1
    BUC_VAL3 = soup.select('td')[30].string.replace(' Volts','')
    BUC_VAL3 = BUC_VAL3.lstrip()
    BUC_VAL3 = BUC_VAL3.rstrip()
    BUC_STA3 = soup.select('td')[31].string
#    print ('BUC Value [3] :', BUC_V[0][3], BUC_VAL3 , 'BUC State [3] :', BUC_S[0][3], BUC_STA3)
    if (BUC_V[0][3] != BUC_VAL3) or (BUC_S[0][3] != BUC_STA3):
        with open(FN3 + DTN[5] + '.log', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([DTN[0], DTN[1], BUC, 'BUC', '10V PS1 VTG', BUC_VAL3, BUC_STA3])

    # 05 10V-PS2
    #BUC_VAL4 = soup.select('td')[37].string.replace(' Volts','')
    #BUC_VAL4 = BUC_VAL4.lstrip()
    #BUC_VAL4 = BUC_VAL4.rstrip()
    #BUC_STA4 = soup.select('td')[38].string
    #print ('BUC Value [4] :', BUC_V[0][4], BUC_VAL4 , 'BUC State [4] :', BUC_S[0][4], BUC_STA4)
    #if (BUC_V[0][4] != BUC_VAL4) or (BUC_S[0][4] != BUC_STA4):
    #    with open(FN3 + DTN[5] + '.log', 'a') as f:
    #        writer = csv.writer(f)
    #        writer.writerow([DTN[0], DTN[1], BUC, 'BUC', '10V PS2 VTG', BUC_VAL4, BUC_STA4])

    # 06 RF10V-PS1
    BUC_VAL5 = soup.select('td')[44].string.replace(' Volts','')
    BUC_VAL5 = BUC_VAL5.lstrip()
    BUC_VAL5 = BUC_VAL5.rstrip()
    BUC_STA5 = soup.select('td')[45].string
#    print ('BUC Value [5] :', BUC_V[0][5], BUC_VAL5 , 'BUC State [5] :', BUC_S[0][5], BUC_STA5)
    if (BUC_V[0][5] != BUC_VAL5) or (BUC_S[0][5] != BUC_STA5):
        with open(FN3 + DTN[5] + '.log', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([DTN[0], DTN[1], BUC, 'BUC', 'RF10V PS 1VTG', BUC_VAL5, BUC_STA5])

    # 06 RF10V-PS2
    #BUC_VAL6 = soup.select('td')[51].string.replace(' Volts','')
    #BUC_VAL6 = BUC_VAL6.lstrip()
    #BUC_VAL6 = BUC_VAL6.rstrip()
    #BUC_STA6 = soup.select('td')[52].string
    #print ('BUC Value [6] :', BUC_V[0][6], BUC_VAL6 , 'BUC State [6] :', BUC_S[0][6], BUC_STA6)
    #if (BUC_V[0][6] != BUC_VAL6) or (BUC_S[0][6] != BUC_STA6):
    #    with open(FN3 + DTN[5] + '.log', 'a') as f:
    #        writer = csv.writer(f)
    #        writer.writerow([DTN[0], DTN[1], BUC, 'BUC', 'RF10V PS2 VTG', BUC_VAL6, BUC_STA6])

    # 07 7.8V-PS
    BUC_VAL7 = soup.select('td')[58].string.replace(' Volts','')
    BUC_VAL7 = BUC_VAL7.lstrip()
    BUC_VAL7 = BUC_VAL7.rstrip()
    BUC_STA7 = soup.select('td')[59].string
#    print ('BUC Value [7] :', BUC_V[0][7], BUC_VAL7 , 'BUC State [7] :', BUC_S[0][7], BUC_STA7)
    if (BUC_V[0][7] != BUC_VAL7) or (BUC_S[0][7] != BUC_STA7):
        with open(FN3 + DTN[5] + '.log', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([DTN[0], DTN[1], BUC, 'BUC', '7.8V PS VTG', BUC_VAL7, BUC_STA7])

    # 08 5.8V-PS
    BUC_VAL8 = soup.select('td')[65].string.replace(' Volts','')
    BUC_VAL8 = BUC_VAL8.lstrip()
    BUC_VAL8 = BUC_VAL8.rstrip()
    BUC_STA8 = soup.select('td')[66].string
#    print ('BUC Value [8] :', BUC_V[0][8], BUC_VAL8 , 'BUC State [8] :', BUC_S[0][8], BUC_STA8)
    if (BUC_V[0][8] != BUC_VAL8) or (BUC_S[0][8] != BUC_STA8):
        with open(FN3 + DTN[5] + '.log', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([DTN[0], DTN[1], BUC, 'BUC', '5.8V PS VTG', BUC_VAL8, BUC_STA8])

    # 09 2.5V-PS
    BUC_VAL9 = soup.select('td')[72].string.replace(' Volts','')
    BUC_VAL9 = BUC_VAL9.lstrip()
    BUC_VAL9 = BUC_VAL9.rstrip()
    BUC_STA9 = soup.select('td')[73].string
#    print ('BUC Value [9] :', BUC_V[0][9], BUC_VAL9 , 'BUC State [9] :', BUC_S[0][9], BUC_STA9)
    if (BUC_V[0][9] != BUC_VAL9) or (BUC_S[0][9] != BUC_STA9):
        with open(FN3 + DTN[5] + '.log', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([DTN[0], DTN[1], BUC, 'BUC', '2.5V PS VTG', BUC_VAL9, BUC_STA9])

    # 10 1.2V-PS
    BUC_VAL10 = soup.select('td')[79].string.replace(' Volts','')
    BUC_VAL10 = BUC_VAL10.lstrip()
    BUC_VAL10 = BUC_VAL10.rstrip()
    BUC_STA10 = soup.select('td')[80].string
#    print ('BUC Value [10] :', BUC_V[0][10], BUC_VAL10 , 'BUC State [10] :', BUC_S[0][10], BUC_STA10)
    if (BUC_V[0][10] != BUC_VAL10) or (BUC_S[0][10] != BUC_STA10):
        with open(FN3 + DTN[5] + '.log', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([DTN[0], DTN[1], BUC, 'BUC', '1.2V PS VTG', BUC_VAL10, BUC_STA10])

    # 12 -5.8V-PS
    BUC_VAL11 = soup.select('td')[86].string.replace(' Volts','')
    BUC_VAL11 = BUC_VAL11.lstrip()
    BUC_VAL11 = BUC_VAL11.rstrip()
    BUC_STA11 = soup.select('td')[87].string
#    print ('BUC Value [11] :', BUC_V[0][11], BUC_VAL11 , 'BUC State [11] :', BUC_S[0][11], BUC_STA11)
    if (BUC_V[0][11] != BUC_VAL11) or (BUC_S[0][11] != BUC_STA11):
        with open(FN3 + DTN[5] + '.log', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([DTN[0], DTN[1], BUC, 'BUC', '-5.8V PS VTG', BUC_VAL11, BUC_STA11])

    # 13 LNB-PS
    #BUC_VAL12 = soup.select('td')[93].string.replace(' Volts','')
    #BUC_VAL12 = BUC_VAL12.lstrip()
    #BUC_VAL12 = BUC_VAL12.rstrip()
    #BUC_STA12 = soup.select('td')[94].string
    #print ('BUC Value [12] :', BUC_V[0][12], BUC_VAL12 , 'BUC State [12] :', BUC_S[0][12], BUC_STA12)
    #if (BUC_V[0][12] != BUC_VAL12) or (BUC_S[0][12] != BUC_STA12):
    #    with open(FN3 + DTN[5] + '.log', 'a') as f:
    #        writer = csv.writer(f)
    #        writer.writerow([DTN[0], DTN[1], BUC, 'BUC', 'LNB PS VTG', BUC_VAL12, BUC_STA12])
    # 12 LNB-Cureent
    #BUC_VAL13 = soup.select('td')[100].string.replace(' Volts','')
    #BUC_VAL13 = BUC_VAL13.lstrip()
    #BUC_VAL13 = BUC_VAL13.rstrip()
    #BUC_STA13 = soup.select('td')[101].string
    #print ('BUC Value [13] :', BUC_V[0][13], BUC_VAL13 , 'BUC State [13] :', BUC_S[0][13], BUC_STA13)
    #if (BUC_V[0][13] != BUC_VAL13) or (BUC_S[0][13] != BUC_STA13):
    #    with open(FN3 + DTN[5] + '.log', 'a') as f:
    #        writer = csv.writer(f)
    #        writer.writerow([DTN[0], DTN[1], BUC, 'BUC', 'LNB CUR', BUC_VAL13, BUC_STA13])

    # 14 Forward Power
    BUC_VAL14 = soup.select('td')[13].string.replace(' dBm','')
    BUC_VAL14 = BUC_VAL14.lstrip()
    BUC_VAL14 = BUC_VAL14.rstrip()
    BUC_STA14 = soup.select('td')[14].string
#    print ('BUC Value [14] :', BUC_V[0][14], BUC_VAL14 , 'BUC State [14] :', BUC_S[0][14], BUC_STA14)
    if (BUC_V[0][14] != BUC_VAL14) or (BUC_S[0][14] != BUC_STA14):
        with open(FN3 + DTN[5] + '.log', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([DTN[0], DTN[1], BUC, 'BUC', 'FRD PWR', BUC_VAL14, BUC_STA14])
    
    # 15 Reverse Power
    #BUC_VAL15 = soup.select('td')[20].string
    #BUC_VAL15 = BUC_VAL15.lstrip()
    #BUC_VAL15 = BUC_VAL15.rstrip()
    #BUC_STA15 = soup.select('td')[21].string
    #print ('BUC Value [15] :', BUC_V[0][15], BUC_VAL15 , 'BUC State [15] :', BUC_S[0][15], BUC_STA15)
    #if (BUC_V[0][15] != BUC_VAL15) or (BUC_S[0][15] != BUC_STA15):
    #    with open(FN3 + DTN[5] + '.log', 'a') as f:
    #        writer = csv.writer(f)
    #        writer.writerow([DTN[0], DTN[1], BUC, 'BUC', 'REV PWR', BUC_VAL15, BUC_STA15])

    # 16 Redundant SW
    BUC_VAL16 = soup.select('td')[27].string
    BUC_VAL16 = BUC_VAL16.lstrip()
    BUC_VAL16 = BUC_VAL16.rstrip()
    BUC_STA16 = soup.select('td')[28].string
#    print ('BUC Value [16] :', BUC_V[0][16], BUC_VAL16 , 'BUC State [16] :', BUC_S[0][16], BUC_STA16)
    if (BUC_V[0][16] != BUC_VAL16) or (BUC_S[0][16] != BUC_STA16):
        with open(FN3 + DTN[5] + '.log', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([DTN[0], DTN[1], BUC, 'BUC', 'RED SW', BUC_VAL16, BUC_STA16])

    # 17 Redundant Link
    BUC_STA17 = soup.select('td')[35].string
#    print ('BUC State [17] :', BUC_S[0][17], BUC_STA17)
    if (BUC_S[0][17] != BUC_STA17):
        with open(FN3 + DTN[5] + '.log', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([DTN[0], DTN[1], BUC, 'BUC', 'RED Link', BUC_STA17])

    # 18 FAN1 Speed
    BUC_VAL18 = soup.select('td')[41].string.replace(' %','')
    BUC_VAL18 = BUC_VAL18.lstrip()
    BUC_VAL18 = BUC_VAL18.rstrip()
    BUC_STA18 = soup.select('td')[42].string
#    print ('BUC Value [18] :', BUC_V[0][18], BUC_VAL18 , 'BUC State [18] :', BUC_S[0][18], BUC_STA18)
    if (BUC_V[0][18] != BUC_VAL18) or (BUC_S[0][18] != BUC_STA18):
        with open(FN3 + DTN[5] + '.log', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([DTN[0], DTN[1], BUC, 'BUC', 'RED Link', BUC_VAL18, BUC_STA18])

    # 19 FAN2 Speed
    #BUC_VAL19 = soup.select('td')[48].string.replace(' %','')
    #BUC_VAL19 = BUC_VAL19.lstrip()
    #BUC_VAL19 = BUC_VAL19.rstrip()
    #BUC_STA19 = soup.select('td')[49].string
    #print ('BUC Value [19] :', BUC_V[0][19], BUC_VAL19 , 'BUC State [19] :', BUC_S[0][19], BUC_STA19)
    #if (BUC_V[0][19] != BUC_VAL19) or (BUC_S[0][19] != BUC_STA19):
    #    with open(FN3 + DTN[5] + '.log', 'a') as f:
    #        writer = csv.writer(f)
    #        writer.writerow([DTN[0], DTN[1], BUC, 'BUC', 'RED Link', BUC_VAL19, BUC_STA19])

    # 20 FAN3 Speed
    #BUC_VAL20 = soup.select('td')[55].string.replace(' %','')
    #BUC_VAL20 = BUC_VAL20.lstrip()
    #BUC_VAL20 = BUC_VAL20.rstrip()
    #BUC_STA20 = soup.select('td')[56].string
    #print ('BUC Value [20] :', BUC_V[0][20], BUC_VAL20 , 'BUC State [20] :', BUC_S[0][20], BUC_STA20)
    #if (BUC_V[0][20] != BUC_VAL20) or (BUC_S[0][20] != BUC_STA20):
    #    with open(FN3 + DTN[5] + '.log', 'a') as f:
    #        writer = csv.writer(f)
    #        writer.writerow([DTN[0], DTN[1], BUC, 'BUC', 'RED Link', BUC_VAL20, BUC_STA20])

    # 21 Apmlifier Temperature
    BUC_VAL21 = soup.select('td')[62].string.replace(' Volts','')
    BUC_VAL21 = BUC_VAL21.lstrip()
    BUC_VAL21 = BUC_VAL21.rstrip()
    BUC_STA21 = soup.select('td')[63].string
#    print ('BUC Value [21] :', BUC_V[0][21], BUC_VAL21 , 'BUC State [21] :', BUC_S[0][21], BUC_STA21)
    if (BUC_V[0][21] != BUC_VAL21) or (BUC_S[0][21] != BUC_STA21):
        with open(FN3 + DTN[5] + '.log', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([DTN[0], DTN[1], BUC, 'BUC', 'RED Link', BUC_VAL21, BUC_STA21])

    # 22 Over Temperature
    BUC_STA22 = soup.select('td')[70].string
#    print ('BUC State [22] :', BUC_S[0][22], BUC_STA22)
    if (BUC_S[0][22] != BUC_STA22):
        with open(FN3 + DTN[5] + '.log', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([DTN[0], DTN[1], BUC, 'BUC', 'Over TEMP', '---', BUC_STA22])

    # 23 Flash Checksum
    BUC_STA23 = soup.select('td')[77].string
#    print ('BUC State [23] :', BUC_S[0][23], BUC_STA23)
    if (BUC_S[0][23] != BUC_STA23):
        with open(FN3 + DTN[5] + '.log', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([DTN[0], DTN[1], BUC, 'BUC', 'Flash Check', '---', BUC_STA23])

    # 24 FPGA Done
    BUC_STA24 = soup.select('td')[84].string
#    print ('BUC State [24] :', BUC_S[0][24], BUC_STA24)
    if (BUC_S[0][24] != BUC_STA24):
        with open(FN3 + DTN[5] + '.log', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([DTN[0], DTN[1], BUC, 'BUC', 'FPGA', '---', BUC_STA24])

    # 25 i2C-BUS
    BUC_STA25 = soup.select('td')[91].string
#    print ('BUC State [25] :', BUC_S[0][25], BUC_STA25)
    if (BUC_S[0][25] != BUC_STA25):
        with open(FN3 + DTN[5] + '.log', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([DTN[0], DTN[1], BUC, 'BUC', 'i2C BUS', '---', BUC_STA25])

    # 26 Reference Lock
    BUC_STA26 = soup.select('td')[98].string
#    print ('BUC State [26] :', BUC_S[0][26], BUC_STA26)
    if (BUC_S[0][26] != BUC_STA26):
        with open(FN3 + DTN[5] + '.log', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([DTN[0], DTN[1], BUC, 'BUC', 'REF', '---', BUC_STA26])

    # 27 BUC Lock
    BUC_STA27 = soup.select('td')[105].string
#    print ('BUC State [27] :', BUC_S[0][27], BUC_STA27)
    if (BUC_S[0][27] != BUC_STA27):
        with open(FN3 + DTN[5] + '.log', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([DTN[0], DTN[1], BUC, 'BUC', 'BUC Lock', '---', BUC_STA27])

    BUC_VAL4 = '---'
    BUC_VAL6 = '---'
    BUC_VAL12 = '---'
    BUC_VAL13 = '---'
    BUC_VAL15 = '---'
    BUC_VAL17 = '---'
    BUC_VAL19 = '---'
    BUC_VAL20 = '---'
#    print(BUC_VAL0,BUC_VAL1,BUC_VAL2,BUC_VAL3,BUC_VAL4,BUC_VAL5,BUC_VAL6,BUC_VAL7,BUC_VAL8,BUC_VAL9,BUC_VAL10,BUC_VAL11,BUC_VAL12,BUC_VAL13,BUC_VAL14,BUC_VAL15,BUC_VAL16,BUC_VAL17,BUC_VAL18,BUC_VAL19,BUC_VAL20,BUC_VAL21)
    BUC_STA4 = '---'
    BUC_STA6 = '---'
    BUC_STA12 = '---'
    BUC_STA13 = '---'
    BUC_STA15 = '---'
    BUC_STA19 = '---'
    BUC_STA20 = '---'
#    print(BUC_STA0,BUC_STA1,BUC_STA2,BUC_STA3,BUC_STA4,BUC_STA5,BUC_STA6,BUC_STA7,BUC_STA8,BUC_STA9,BUC_STA10,BUC_STA11,BUC_STA12,BUC_STA13,BUC_STA14,BUC_STA15,BUC_STA16,BUC_STA17,BUC_STA18,BUC_STA19,BUC_STA20,BUC_STA21,BUC_STA22,BUC_STA23,BUC_STA24,BUC_STA25)

    # File Check-1
    with open(FLN1, 'w') as f:
        writer = csv.writer(f)
        writer.writerow([BUC_VAL0,BUC_VAL1,BUC_VAL2,BUC_VAL3,BUC_VAL4,BUC_VAL5,BUC_VAL6,BUC_VAL7,BUC_VAL8,BUC_VAL9,BUC_VAL10,BUC_VAL11,BUC_VAL12,BUC_VAL13,BUC_VAL14,BUC_VAL15,BUC_VAL16,BUC_VAL17,BUC_VAL18,BUC_VAL19,BUC_VAL20,BUC_VAL21])

    # File Check-2
    with open(FLN2, 'w') as f:
        writer = csv.writer(f)
        writer.writerow([BUC_STA0,BUC_STA1,BUC_STA2,BUC_STA3,BUC_STA4,BUC_STA5,BUC_STA6,BUC_STA7,BUC_STA8,BUC_STA9,BUC_STA10,BUC_STA11,BUC_STA12,BUC_STA13,BUC_STA14,BUC_STA15,BUC_STA16,BUC_STA17,BUC_STA18,BUC_STA19,BUC_STA20,BUC_STA21,BUC_STA22,BUC_STA23,BUC_STA24,BUC_STA25,BUC_STA26,BUC_STA27])
    DTN = lqms_dt.RTC_CHK()
#    print ('     ' , DTN[1] , 'Complete : LPod-BUC Ethernet Status Monitor')


    if (BUC == 'KuBUC-A'):
        print ('          ', DTN[1], '\33[1m\033[46m\033[37m' + ' BUC ' + '\033[0m' + '\033[32m\033[1m  Ku-Band BUC-A Forward Power : ' + BUC_VAL14 + ' (dBm)\033[0m                                 lqms_buc.py Ver.' + VER)
        lqms_plt3.ST(BUC_VAL14,BUC)
    elif (BUC == 'KuBUC-B'):
        print ('          ', DTN[1], '\33[1m\033[46m\033[37m' + ' BUC ' + '\033[0m' + '\033[32m\033[1m  Ku-Band BUC-B Forward Power : ' + BUC_VAL14 + ' (dBm)\033[0m                                 lqms_buc.py Ver.' + VER)
        lqms_plt3.ST(BUC_VAL14,BUC)
    elif (BUC == 'CBUC-A'):
        print ('          ', DTN[1], '\33[1m\033[46m\033[37m' + ' BUC ' + '\033[0m' + '\033[32m\033[1m   C-Band BUC-A Forward Power : ' + BUC_VAL14 + ' (dBm)\033[0m                                 lqms_buc.py Ver.' + VER)
        lqms_plt3.ST(BUC_VAL14,BUC)
    elif (BUC == 'CBUC-B'):
        print ('          ', DTN[1], '\33[1m\033[46m\033[37m' + ' BUC ' + '\033[0m' + '\033[32m\033[1m   C-Band BUC-B Forward Power : ' + BUC_VAL14 + ' (dBm)\033[0m                                 lqms_buc.py Ver.' + VER)
        lqms_plt3.ST(BUC_VAL14,BUC)

