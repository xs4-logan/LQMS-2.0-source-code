#####
# CDM-570AL-IP / EBN Command Version 0.0.1
# 2022.08.23 Yoshiaki Sato[Technobiz]
#####
import lqms_dt
import lqms_plt2

import csv
from decimal import Decimal, ROUND_HALF_UP
import serial
from time import sleep
import time
import os
import re

VER = '0.0.1'
FN1 = '/mnt/ssd/log/error/err_'
FN2 = '/mnt/ssd/log/facl/sys_'

DEF_TRK = ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
TRK = ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
DEF_UPC = ['','','','','','','','','','','','','','','','','','','','','','','','','']
UPCp = ['','','','','','','','','','','','','','','','','','','','','','','','','']
DEF_STA = ['','','','','','','','','','','','','','','','','','','','','']
STA = ['','','','','','','','','','','','','','','','','','','','','']

##### CHECKSUM Calculate #####
def TK(ADD,RxDAT):
    DTN = lqms_dt.RTC_CHK()
    TRK[0] = RxDAT[0:2]             # STx
    TRK[1] = RxDAT[2:4]             # DATA Length
    TRK[2] = RxDAT[4:6]             # UPC Unit Address
    TRK[3] = RxDAT[6:8]             # Message instruction
    TRK[4] = RxDAT[8:10]            # Information
    TRK[5] = RxDAT[10:32]           # Video Center Frequency ['xxxxxxxxxxx' = 'XX.XXXXXXXXX'(GHz)]
    TRK[6] = RxDAT[32:48]           # Frequency SPAN ['xxxxxxxx' = 'XX.XXXXXX'(MHz)]
    TRK[7] = RxDAT[48:56]           # Video Reference Level ['-xxx' = '-XXX' (dB)]
    TRK[8] = RxDAT[56:58]           # Band width Resolution ['1':1(KHz) , '6':6(KHz)]
    TRK[9] = RxDAT[58:60]           # 10dB Pad ON/OFF ['1':ON , '0':OFF]
    TRK[10] = RxDAT[60:62]          # Sweep rate index (0-7) ['0':2.5KHz/s , '1':5.0KHz/s , '2':10KHz/s , '3':20KHz/s , '4':40KHz/s , '5':80KHz/s , '6':120KHz/s , '7':240KHz/s]
    TRK[11] = RxDAT[62:64]          # Sweep width index (0-4) ['0':+/-20KHz , '1':+/-50KHz , '2':+/-100KHz , '3':+/-200KHz , '4':+/-500KHz]
    TRK[12] = RxDAT[64:66]          # Log dB/V ['0':0.5dB/V , '1':1dB/V , '2':2dB/V , '3':5dB/V , '4':10dB/V]
    TRK[13] = RxDAT[66:72]          # Log OFFSET
    TRK[14] = RxDAT[72:74]          # ASB ON/OFF ['1':ON , '0':OFF]
    TRK[15] = RxDAT[74:84]          # DC Output  ['-xxxx' = '-XX.XX' (V)]
    TRK[16] = RxDAT[84:94]          # Rx Level ['-xxxx' = '-XXX.X' (dBm)]
    TRK[17] = RxDAT[94:116]         # Frequency ['xxxxxxxxxxx' = 'XX.XXXXXXXXX' (GHz)]
    TRK[18] = RxDAT[116:126]        # Gain ['+xxxx' = '+XXX.X' (dB)]
    TRK[19] = RxDAT[126:128]        # Not Use
    TRK[20] = RxDAT[128:130]        # 10MHz ON/OFF ['1':ON , '0':OFF]
    TRK[21] = RxDAT[130:132]        # DC Feed ON/OFF ['1':ON , '0':OFF]
    TRK[22] = RxDAT[132:134]        # SHF Local ON/OFF ['1':ON , '0':OFF]
    TRK[23] = RxDAT[134:156]        # SHF Frequency ['xxxxxxxxxxx' = 'XX.XXXXXXXXX' (GHz)]
    TRK[24] = RxDAT[156:158]        # Spectrum Inversion ['1':ON , '0':OFF]
    TRK[25] = RxDAT[158:160]        # Tracking Out of Lock ['1':Fault , '0':Normal]
    TRK[26] = RxDAT[160:162]        # 2nd Local Fault ['1':Fault , '0':Normal]
    TRK[27] = RxDAT[162:196]        # Time and Date
    TRK[28] = RxDAT[196:198]        # Checksum
    TRK[29] = RxDAT[198:200]        # ETx

    if (TRK[2] == '31') : # C-Band UPC
        DEF_FL = 'C_UPC_DEF_TRK.csv'
        UPC_N = 'C-Band'
        DEF_FL = '/home/xs4/basis/req_relFiles/' + DEF_FL
        FNL = '/mnt/ssd/log/c-upc/c-upc'
        print ('          ',DTN[1],'\033[1m\033[42m\033[37m\033[1m UPC \033[0m  C-Band UPC Tracking Receiver Status Query                                 lqms_upc.py Ver.' + VER)
    elif (TRK[2] == '32') : # Ku-Band UPC
        DEF_FL = 'Ku_UPC_DEF_TRK.csv'
        UPC_N = 'Ku-Band'
        DEF_FL = '/home/xs4/basis/req_relFiles/' + DEF_FL
        FNL = '/mnt/ssd/log/ku-upc/ku-upc'
        print ('          ',DTN[1],'\033[1m\033[42m\033[37m\033[1m UPC \033[0m  Ku-Band UPC Tracking Receiver Status Query                                lqms_upc.py Ver.' + VER)

    # File Check
    is_file = os.path.isfile(DEF_FL)
    c=0
    if is_file:
        with open(DEF_FL) as f:
            reader = csv.reader(f)
            DEF_TRK = [row for row in reader]

    if (TRK[4] == '4b' or TRK[4] == '4B'):
        if (TRK[5] != DEF_TRK[0][5]):
            TMP_LST = re.split('(..)',TRK[5])[1::2]
            L = len(TMP_LST)
            videoFreq = ''
            for Co in range(0,L):
                DC = int(TMP_LST[Co],16)
                videoFreq = videoFreq + (chr(DC))
            videoFreq =  str('{:.9f}'.format((float(videoFreq)/1000000000)))
#            print ('          ',DTN[1],'Video Frequency : ' + videoFreq + ' (GHz)')
            with open(FNL + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], UPC_N, 'Video Frequency', videoFreq + ' (GHz)'])

        if (TRK[6] != DEF_TRK[0][6]):
            TMP_LST = re.split('(..)',TRK[6])[1::2]
            L = len(TMP_LST)
            freqSpan = ''
            for Co in range(0,L):
                DC = int(TMP_LST[Co],16)
                freqSpan = freqSpan + (chr(DC))
            freqSpan =  str('{:.6f}'.format((float(freqSpan)/1000000)))
#            print ('          ',DTN[1],'Frequency Span : ' + freqSpan + ' (MHz)')
            with open(FNL + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], UPC_N, 'Frequency Span', freqSpan + ' (MHz)'])

        if (TRK[7] != DEF_TRK[0][7]):
            TMP_LST = re.split('(..)',TRK[7])[1::2]
            L = len(TMP_LST)
            refLevel = ''
            for Co in range(0,L):
                DC = int(TMP_LST[Co],16)
                refLevel = refLevel + (chr(DC))
            refLevel =  str(int(refLevel))
#            print ('          ',DTN[1],'Reference Level : ' + refLevel + ' (dB)')
            with open(FNL + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], UPC_N, 'Reference Level', refLevel + ' (dB)'])

        if (TRK[8] != DEF_TRK[0][8]):
            TMP_LST = re.split('(..)',TRK[8])[1::2]
            DC = int(TMP_LST[0],16)
            DCC = chr(DC)
            BWRES = ''
            if (DCC == '1'):
#                print ('          ',DTN[1],'Bandwidth RES : 1KHz')
                BWRES = '1KHz'
            elif (DCC == '6'):
#                print ('          ',DTN[1],'Bandwidth RES : 6KHz')
                BWRES = '1KHz'
            with open(FNL + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], UPC_N, 'Bandwidth RES : ' + BWRES])

        if (TRK[9] != DEF_TRK[0][9]):
            TMP_LST = re.split('(..)',TRK[9])[1::2]
            DC = int(TMP_LST[0],16)
            DCC = chr(DC)
            PAD = ''
            if (DCC == '1'):
#                print ('          ',DTN[1],'10dB Pad : ON')
                PAD = 'ON'
            elif (DCC == '0'):
#                print ('          ',DTN[1],'10dB Pad : OFF')
                PAD = 'OFF'
            with open(FNL + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], UPC_N, '10dB PAD : ' + PAD])

        if (TRK[10] != DEF_TRK[0][10]):
            TMP_LST = re.split('(..)',TRK[10])[1::2]
            DC = int(TMP_LST[0],16)
            DCC = chr(DC)
            SWRT = ''
            if (DCC == '0'):
#                print ('          ',DTN[1],'Sweep Rate : 2.5KHz/s')
                SWRT = '2.5KHz/s'
            elif (DCC == '1'):
#                print ('          ',DTN[1],'Sweep Rate : 5.0KHz/s')
                SWRT = '5.0KHz/s'
            elif (DCC == '2'):
#                print ('          ',DTN[1],'Sweep Rate : 10.0KHz/s')
                SWRT = '10.0KHz/s'
            elif (DCC == '3'):
#                print ('          ',DTN[1],'Sweep Rate : 20.0KHz/s')
                SWRT = '20.0KHz/s'
            elif (DCC == '4'):
#                print ('          ',DTN[1],'Sweep Rate : 40.0KHz/s')
                SWRT = '40.0KHz/s'
            elif (DCC == '5'):
#                print ('          ',DTN[1],'Sweep Rate : 80.0KHz/s')
                SWRT = '80.0KHz/s'
            elif (DCC == '6'):
#                print ('          ',DTN[1],'Sweep Rate : 120.0KHz/s')
                SWRT = '120.0KHz/s'
            elif (DCC == '7'):
#                print ('          ',DTN[1],'Sweep Rate : 240.0KHz/s')
                SWRT = '240.0KHz/s'
            with open(FNL + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], UPC_N, 'Sweep Rate : ' + SWRT])

        if (TRK[11] != DEF_TRK[0][11]):
            TMP_LST = re.split('(..)',TRK[11])[1::2]
            DC = int(TMP_LST[0],16)
            DCC = chr(DC)
            SWW = ''
            if (DCC == '0'):
#                print ('          ',DTN[1],'Sweep Width : +/- 20KHz')
                SWW = '+/- 20KHz'
            elif (DCC == '1'):
#                print ('          ',DTN[1],'Sweep Width : +/- 50KHz')
                SWW = '+/- 50KHz'
            elif (DCC == '2'):
#                print ('          ',DTN[1],'Sweep Width : +/- 100KHz')
                SWW = '+/- 100KHz'
            elif (DCC == '3'):
#                print ('          ',DTN[1],'Sweep Width : +/- 200KHz')
                SWW = '+/- 200KHz'
            elif (DCC == '4'):
#                print ('          ',DTN[1],'Sweep Width : +/- 500KHz')
                SWW = '+/- 500KHz'
            with open(FNL + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], UPC_N, 'Sweep Width : ' + SWW])

        if (TRK[12] != DEF_TRK[0][12]):
            TMP_LST = re.split('(..)',TRK[12])[1::2]
            DC = int(TMP_LST[0],16)
            DCC = chr(DC)
            LGV = ''
            if (DCC == '0'):
#                print ('          ',DTN[1],'Log dB/Volt : 0.5dB/V')
                LGV = '0.5dB/V'
            elif (DCC == '1'):
#                print ('          ',DTN[1],'Log dB/Volt : 1.0dB/V')
                LGV = '1.0dB/V'
            elif (DCC == '2'):
#                print ('          ',DTN[1],'Log dB/Volt : 2.0dB/V')
                LGV = '2.0dB/V'
            elif (DCC == '3'):
#                print ('          ',DTN[1],'Log dB/Volt : 5.0dB/V')
                LGV = '5.0dB/V'
            elif (DCC == '4'):
#                print ('          ',DTN[1],'Log dB/Volt : 10.0dB/V')
                LGV = '10.0dB/V'
            with open(FNL + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], UPC_N, 'Log dB/Volt : ' + LGV])

        if (TRK[13] != DEF_TRK[0][13]):
            TMP_LST = re.split('(..)',TRK[13])[1::2]
            L = len(TMP_LST)
            LGO = ''
            for Co in range(0,L):
                DC = int(TMP_LST[Co],16)
                LGO = LGO + (chr(DC))
            LGO =  str(int(LGO))
#            print ('          ',DTN[1],'LOG OFFSET : ' + LGO)
            with open(FNL + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], UPC_N, 'LOG OFFSET', LGO ])

        if (TRK[14] != DEF_TRK[0][14]):
            TMP_LST = re.split('(..)',TRK[14])[1::2]
            DC = int(TMP_LST[0],16)
            DCC = chr(DC)
            ASB = ''
            if (DCC == '1'):
#                print ('          ',DTN[1],'ASB : ON')
                ASB = 'ON'
            elif (DCC == '0'):
#                print ('          ',DTN[1],'ASB : OFF')
                ASB = 'OFF'
            with open(FNL + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], UPC_N, 'ASB : ' + ASB])

        if (TRK[15] != DEF_TRK[0][15]):
            TMP_LST = re.split('(..)',TRK[15])[1::2]
            L = len(TMP_LST)
            DCO = ''
            for Co in range(0,L):
                DC = int(TMP_LST[Co],16)
                DCO = DCO + (chr(DC))
            DCO =  str('{:.6f}'.format((float(DCO)/100)))
#            print ('          ',DTN[1],'DC Output : ' + DCO + ' (V)')
            with open(FNL + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], UPC_N, 'DC Output', DCO + ' (V)'])

        if (TRK[16] != DEF_TRK[0][16]):
            TMP_LST = re.split('(..)',TRK[16])[1::2]
            L = len(TMP_LST)
            RXL = ''
            for Co in range(0,L):
                DC = int(TMP_LST[Co],16)
                RXL = RXL + (chr(DC))
            RXL =  str('{:.6f}'.format((float(RXL)/10)))
#            print ('          ',DTN[1],'Rx Level : ' + RXL + ' (dBm)')
            with open(FNL + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], UPC_N, 'Rx Level', RXL + ' (dBm)'])

        if (TRK[17] != DEF_TRK[0][17]):
            TMP_LST = re.split('(..)',TRK[17])[1::2]
            L = len(TMP_LST)
            Freq = ''
            for Co in range(0,L):
                DC = int(TMP_LST[Co],16)
                Freq = Freq + (chr(DC))
            Freq =  str('{:.9f}'.format((float(Freq)/1000000000)))
#            print ('          ',DTN[1],'Frequency : ' + Freq + ' (GHz)')
            with open(FNL + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], UPC_N, 'Frequency', Freq + ' (GHz)'])

        if (TRK[18] != DEF_TRK[0][18]):
            TMP_LST = re.split('(..)',TRK[18])[1::2]
            L = len(TMP_LST)
            GAIN = ''
            for Co in range(0,L):
                DC = int(TMP_LST[Co],16)
                GAIN = GAIN + (chr(DC))
            GAIN =  str('{:.2f}'.format((float(GAIN)/10)))
#            print ('          ',DTN[1],'GAIN : ' + GAIN + ' (dB)')
            with open(FNL + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], UPC_N, 'GAIN', GAIN + ' (dB)'])

        if (TRK[20] != DEF_TRK[0][20]):
            TMP_LST = re.split('(..)',TRK[20])[1::2]
            DC = int(TMP_LST[0],16)
            DCC = chr(DC)
            MHz = ''
            if (DCC == '1'):
#                print ('          ',DTN[1],'10MHz : ON')
                MHz = 'ON'
            elif (DCC == '0'):
#                print ('          ',DTN[1],'10MHz : OFF')
                MHz = 'OFF'
            with open(FNL + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], UPC_N, '10MHz : ' + MHz])

        if (TRK[21] != DEF_TRK[0][21]):
            TMP_LST = re.split('(..)',TRK[21])[1::2]
            DC = int(TMP_LST[0],16)
            DCF = chr(DC)
            MHz = ''
            if (DCF == '1'):
#                print ('          ',DTN[1],'DC Bias Feed : ON')
                MHz = 'ON'
            elif (DCF == '0'):
#                print ('          ',DTN[1],'DC Bias Feed : OFF')
                MHz = 'OFF'
            with open(FNL + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], UPC_N, 'DC Bias Feed : ' + DCF])

        if (TRK[22] != DEF_TRK[0][22]):
            TMP_LST = re.split('(..)',TRK[22])[1::2]
            DC = int(TMP_LST[0],16)
            DCF = chr(DC)
            SHL = ''
            if (DCF == '1'):
#                print ('          ',DTN[1],'SHF LOCAL : ON')
                SHL = 'ON'
            elif (DCF == '0'):
#                print ('          ',DTN[1],'SHF LOCAL : OFF')
                SHL = 'OFF'
            with open(FNL + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], UPC_N, 'SHF LOCAL : ' + SHL])

        if (TRK[23] != DEF_TRK[0][23]):
            TMP_LST = re.split('(..)',TRK[23])[1::2]
            L = len(TMP_LST)
            SHF = ''
            for Co in range(0,L):
                DC = int(TMP_LST[Co],16)
                SHF = SHF + (chr(DC))
            SHF =  str('{:.9f}'.format((float(SHF)/1000000000)))
#            print ('          ',DTN[1],'SHF Frequency : ' + SHF + ' (GHz)')
            with open(FNL + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], UPC_N, 'SHF Frequency', SHF + ' (GHz)'])

        if (TRK[24] != DEF_TRK[0][24]):
            TMP_LST = re.split('(..)',TRK[24])[1::2]
            DC = int(TMP_LST[0],16)
            DCF = chr(DC)
            SPI = ''
            if (DCF == '1'):
#                print ('          ',DTN[1],'SHF Spectrum Inversion : ON')
                SPI = 'ON'
            elif (DCF == '0'):
#                print ('          ',DTN[1],'SHF Spectrum Inversion : OFF')
                SPI = 'OFF'
            with open(FNL + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], UPC_N, 'SHF Spectrum Inversion  : ' + SPI])

        if (TRK[25] != DEF_TRK[0][25]):
            TMP_LST = re.split('(..)',TRK[25])[1::2]
            DC = int(TMP_LST[0],16)
            DCF = chr(DC)
            TKO = ''
            if (DCF == '1'):
#                print ('          ',DTN[1],'Tracking Out of lock : ON')
                TKO = 'Tracking'
            elif (DCF == '0'):
#                print ('          ',DTN[1],'Tracking Out of lock : OFF')
                TKO = 'Fault'
            with open(FNL + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], UPC_N, 'Tracking Out of lock : ' + TKO])

        if (TRK[26] != DEF_TRK[0][26]):
            TMP_LST = re.split('(..)',TRK[26])[1::2]
            DC = int(TMP_LST[0],16)
            DCF = chr(DC)
            LOC = ''
            if (DCF == '1'):
#                print ('          ',DTN[1],'2nd Local Fault : ON')
                LOC = 'Normal'
            elif (DCF == '0'):
#                print ('          ',DTN[1],'2nd Local Fault : OFF')
                LOC = 'Fault'
            with open(FNL + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], UPC_N, '2nd Local Fault : ' + LOC])

        with open(DEF_FL, 'w') as f:
            writer = csv.writer(f)
            writer.writerow([TRK[0], TRK[1], TRK[2], TRK[3], TRK[4], TRK[5], TRK[6], TRK[7], TRK[8], TRK[9], TRK[10], TRK[11], TRK[12], TRK[13], TRK[14], 
                    TRK[15], TRK[16], TRK[17], TRK[18], TRK[19], TRK[20], TRK[21], TRK[22], TRK[23], TRK[24], TRK[25], TRK[26], TRK[27], TRK[28], TRK[29] ])

    return()

def UPC(ADD,RxDAT):
    DTN = lqms_dt.RTC_CHK()
    SBL = ''
    #print (RxDAT)
    UPCp[0] = RxDAT[0:2]         # STx
    UPCp[1] = RxDAT[2:4]         # Rx Data Length
    UPCp[2] = RxDAT[4:6]         # UPC Unit Address
    UPCp[3] = RxDAT[6:8]         # Message
    UPCp[4] = RxDAT[8:10]         # Information
    UPCp[5] = RxDAT[10:12]         # Clear sky Calibrated
    UPCp[6] = RxDAT[12:14]         # Ext-Channels Calibrated
    UPCp[7] = RxDAT[14:16]         # Mode
    UPCp[8] = RxDAT[16:26]        # Clearsky beacom Level
    UPCp[9] = RxDAT[26:36]       # Clearsky offset
    UPCp[10] = RxDAT[36:46]      # Sampled Beacon Level
    UPCp[11] = RxDAT[46:52]      # Compensation Range 
    UPCp[12] = RxDAT[52:58]      # Compensation Radio
    UPCp[13] = RxDAT[58:60]      # Step Size
    UPCp[14] = RxDAT[60:62]      # Slew rate
    UPCp[15] = RxDAT[62:68]      # Sample Period
    UPCp[16] = RxDAT[68:74]      # Attenuation
    UPCp[17] = RxDAT[74:76]      # Scintillation Enabled?
    UPCp[18] = RxDAT[76:82]      # Hysteresis
    UPCp[19] = RxDAT[82:84]      # Clear sky Level too low
    UPCp[20] = RxDAT[84:86]      # Compensation range Exceeded
    UPCp[21] = RxDAT[86:88]      # Missing External Channels
    UPCp[22] = RxDAT[88:122]      # Time and Date
    UPCp[23] = RxDAT[122:124]      # Check Sum
    UPCp[24] = RxDAT[124:126]      # ETx

    if (UPCp[2] == '31') : # C-Band UPC
        DEF_FL = 'C_UPC_DEF_UPC.csv'
        UPC_N = 'C-Band'
        DEF_FL = '/home/xs4/basis/req_relFiles/' + DEF_FL
        FNL = '/mnt/ssd/log/c-upc/c-upc'
        print ('          ',DTN[1],'\033[1m\033[42m\033[37m\033[1m UPC \033[0m  C-Band UPC Status Query                                                   lqms_upc.py Ver.' + VER)
    elif (UPCp[2] == '32') : # Ku-Band UPC
        DEF_FL = 'Ku_UPC_DEF_UPC.csv'
        UPC_N = 'Ku-Band'
        DEF_FL = '/home/xs4/basis/req_relFiles/' + DEF_FL
        FNL = '/mnt/ssd/log/ku-upc/ku-upc'
        print ('          ',DTN[1],'\033[1m\033[42m\033[37m\033[1m UPC \033[0m  Ku-Band UPC Status Query                                                  lqms_upc.py Ver.' + VER)

    # File Check
    is_file = os.path.isfile(DEF_FL)
    c=0
    if is_file:
        with open(DEF_FL) as f:
            reader = csv.reader(f)
            DEF_UPC = [row for row in reader]

    if (UPCp[4] == '55'):
        if (UPCp[5] != DEF_UPC[0][5]):
            TMP_LST = re.split('(..)',UPCp[5])[1::2]
            DC = int(TMP_LST[0],16)
            DCC = chr(DC)
            CSC = ''
            if (DCC == '1'):
#                print ('          ',DTN[1],'Clear sky Calibrated : OK')
                CSC = 'OK'
            elif (DCC == '0'):
#                print ('          ',DTN[1],'Clear sky Calibrated : NO')
                CSC = 'NO'
            with open(FNL + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], UPC_N, 'Clear sky Calibrated : ' + CSC])

        if (UPCp[6] != DEF_UPC[0][6]):
            TMP_LST = re.split('(..)',UPCp[6])[1::2]
            DC = int(TMP_LST[0],16)
            DCC = chr(DC)
            ECC = ''
            if (DCC == '1'):
#                print ('          ',DTN[1],'External Channel Calibrated : OK')
                ECC = 'OK'
            elif (DCC == '0'):
#                print ('          ',DTN[1],'External Channel Calibrated : NO')
                ECC = 'NO'
            with open(FNL + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], UPC_N, 'External Channel Calibrated : ' + ECC])

        if (UPCp[7] != DEF_UPC[0][7]):
            TMP_LST = re.split('(..)',UPCp[7])[1::2]
            DC = int(TMP_LST[0],16)
            DCC = chr(DC)
            MD = ''
            if (DCC == '1'):
#                print ('          ',DTN[1],'Mode : Automatic')
                MD = 'Automatic'
            elif (DCC == '0'):
#                print ('          ',DTN[1],'Mode : Manual')
                MD = 'Manual'
            with open(FNL + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], UPC_N, 'Mode : ' + ECC])

        if (UPCp[8] != DEF_UPC[0][8]):
            TMP_LST = re.split('(..)',UPCp[8])[1::2]
            L = len(TMP_LST)
            CBL = ''
            for Co in range(0,L):
                DC = int(TMP_LST[Co],16)
                CBL = CBL + (chr(DC))
            CBL =  str('{:.1f}'.format((float(CBL)/10)))
#            print ('          ',DTN[1],'Clear sky Beacon Level : ' + CBL + ' (dB)')
            with open(FNL + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], UPC_N, 'Clear sky Beacon Level', CBL + ' (dB)'])

        if (UPCp[9] != DEF_UPC[0][9]):
            TMP_LST = re.split('(..)',UPCp[9])[1::2]
            L = len(TMP_LST)
            CSO = ''
            for Co in range(0,L):
                DC = int(TMP_LST[Co],16)
                CSO = CSO + (chr(DC))
            CSO =  str('{:.1f}'.format((float(CSO)/10)))
#            print ('          ',DTN[1],'Clear sky Offset : ' + CSO + ' (dB)')
            with open(FNL + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], UPC_N, 'Clear sky Offset', CSO + ' (dB)'])

        if (UPCp[10] != DEF_UPC[0][10]):
            TMP_LST = re.split('(..)',UPCp[10])[1::2]
            L = len(TMP_LST)
            SBL = ''
            for Co in range(0,L):
                DC = int(TMP_LST[Co],16)
                SBL = SBL + (chr(DC))
            SBL =  '-' + str('{:.1f}'.format((float(SBL)/10)))
#            print ('          ',DTN[1],'Sampled Beacon Level : ' + SBL + ' (dBm)')
            with open(FNL + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], UPC_N, 'Sampled Beacon Level', SBL + ' (dBm)'])

        if (UPCp[11] != DEF_UPC[0][11]):
            TMP_LST = re.split('(..)',UPCp[11])[1::2]
            L = len(TMP_LST)
            CPR = ''
            for Co in range(0,L):
                DC = int(TMP_LST[Co],16)
                CPR = CPR + (chr(DC))
            CPR =  str('{:.1f}'.format((float(CPR)/10)))
#            print ('          ',DTN[1],'Compensation Range : ' + CPR + ' (dBm)')
            with open(FNL + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], UPC_N, 'Compensation Range : ', CPR + ' (dB)'])

        if (UPCp[12] != DEF_UPC[0][12]):
            TMP_LST = re.split('(..)',UPCp[12])[1::2]
            L = len(TMP_LST)
            CR = ''
            for Co in range(0,L):
                DC = int(TMP_LST[Co],16)
                CR = CR + (chr(DC))
            CR =  str('{:.1f}'.format((float(CR)/10)))
#            print ('          ',DTN[1],'Compensation Ratio : ' + CR + ' (dBm)')
            with open(FNL + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], UPC_N, 'Compensation Ratio : ', CR + ' (dB)'])

        if (UPCp[13] != DEF_UPC[0][13]):
            TMP_LST = re.split('(..)',UPCp[13])[1::2]
            DC = int(TMP_LST[0],16)
            DCC = chr(DC)
            SSZ = ''
            if (DCC == '0'):
#                print ('          ',DTN[1],'Step Size : 0.1dB')
                SSZ = '0.1dB'
            elif (DCC == '1'):
#                print ('          ',DTN[1],'Step Size : 0.2dB')
                SSZ = '0.2dB'
            elif (DCC == '2'):
#                print ('          ',DTN[1],'Step Size : 0.5dB')
                SSZ = '0.5dB'
            elif (DCC == '3'):
#                print ('          ',DTN[1],'Step Size : 1.0dB')
                SSZ = '1.0dB'
            elif (DCC == '4'):
#                print ('          ',DTN[1],'Step Size : 2.0dB')
                SSZ = '2.0dB'
            with open(FNL + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], UPC_N, 'Step Size : ' + SSZ])

        if (UPCp[14] != DEF_UPC[0][14]):
            TMP_LST = re.split('(..)',UPCp[14])[1::2]
            DC = int(TMP_LST[0],16)
            DCC = chr(DC)
            SR = ''
            if (DCC == '0'):
#                print ('          ',DTN[1],'Slew Rate : 1dB/10s')
                SR = '1dB/10s'
            elif (DCC == '1'):
#                print ('          ',DTN[1],'Slew Rate : 1dB/20s')
                SR = '1dB/20s'
            elif (DCC == '2'):
#                print ('          ',DTN[1],'Slew Rate : 1dB/50s')
                SR = '1dB/50s'
            elif (DCC == '3'):
#                print ('          ',DTN[1],'Slew Rate : 1dB/100s')
                SR = '1dB/100s'
            with open(FNL + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], UPC_N, 'Slew Rate : ' + SR])

        if (UPCp[15] != DEF_UPC[0][15]):
            TMP_LST = re.split('(..)',UPCp[15])[1::2]
            L = len(TMP_LST)
            SP = ''
            for Co in range(0,L):
                DC = int(TMP_LST[Co],16)
                SP = SP + (chr(DC))
            SP =  str('{:.1f}'.format((float(SP)/10)))
#            print ('          ',DTN[1],'Sampling Period : ' + SP + ' (s)')
            with open(FNL + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], UPC_N, 'Sampling Period : ', SP + ' (s)'])

        if (UPCp[16] != DEF_UPC[0][16]):
            TMP_LST = re.split('(..)',UPCp[16])[1::2]
            L = len(TMP_LST)
            ATT = ''
            for Co in range(0,L):
                DC = int(TMP_LST[Co],16)
                ATT = ATT + (chr(DC))
            ATT =  str('{:.1f}'.format((float(ATT)/10)))
#            print ('          ',DTN[1],'Attenuation : ' + ATT + ' (dB)')
            with open(FNL + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], UPC_N, 'Attenuation : ', ATT + ' (dB)'])

        if (UPCp[17] != DEF_UPC[0][7]):
            TMP_LST = re.split('(..)',UPCp[17])[1::2]
            DC = int(TMP_LST[0],16)
            DCC = chr(DC)
            SCE = ''
            if (DCC == '1'):
#                print ('          ',DTN[1],'Scintillation Enabled : OK')
                SCE = 'OK'
            elif (DCC == '0'):
#                print ('          ',DTN[1],'Scintillation Enabled : NO')
                SCE = 'NO'
            with open(FNL + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], UPC_N, 'Scintillation Enabled : ' + SCE])

        if (UPCp[18] != DEF_UPC[0][18]):
            TMP_LST = re.split('(..)',UPCp[18])[1::2]
            L = len(TMP_LST)
            HYS = ''
            for Co in range(0,L):
                DC = int(TMP_LST[Co],16)
                HYS = HYS + (chr(DC))
            HYS =  str('{:.1f}'.format((float(HYS)/10)))
#            print ('          ',DTN[1],'Hysteresis : ' + HYS + ' (dB)')
            with open(FNL + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], UPC_N, 'Hysteresis : ', HYS + ' (dB)'])

        if (UPCp[19] != DEF_UPC[0][19]):
            TMP_LST = re.split('(..)',UPCp[19])[1::2]
            DC = int(TMP_LST[0],16)
            DCC = chr(DC)
            CLL = ''
            if (DCC == '1'):
#                print ('          ',DTN[1],'Clearsky Level too LOW : Fault')
                CLL = 'FAULT'
            elif (DCC == '0'):
#                print ('          ',DTN[1],'Clearsky Level too LOW : OK')
                CLL = 'OK'
            with open(FNL + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], UPC_N, 'Clearsky Level too LOW : ' + CLL])

        if (UPCp[20] != DEF_UPC[0][20]):
            TMP_LST = re.split('(..)',UPCp[20])[1::2]
            DC = int(TMP_LST[0],16)
            DCC = chr(DC)
            CRE = ''
            if (DCC == '1'):
#                print ('          ',DTN[1],'Compensation Range Exceeded : Fault')
                CRE = 'FAULT'
            elif (DCC == '0'):
#                print ('          ',DTN[1],'Compensation Range Exceeded : OK')
                CRE = 'OK'
            with open(FNL + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], UPC_N, 'Compensation Range Exceeded : ' + CRE])

        if (UPCp[21] != DEF_UPC[0][21]):
            TMP_LST = re.split('(..)',UPCp[21])[1::2]
            DC = int(TMP_LST[0],16)
            DCC = chr(DC)
            MSE = ''
            if (DCC == '1'):
#                print ('          ',DTN[1],'Missing External Channels Fault : FAULT')
                MSE = 'FAULT'
            elif (DCC == '0'):
#                print ('          ',DTN[1],'Missing External Channels Fault : NO')
                MSE = 'OK'
            with open(FNL + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], UPC_N, 'Missing External Channels Fault : ' + MSE])

        with open(DEF_FL, 'w') as f:
            writer = csv.writer(f)
            writer.writerow([UPCp[0], UPCp[1], UPCp[2], UPCp[3], UPCp[4], UPCp[5], UPCp[6], UPCp[7], UPCp[8], UPCp[9], UPCp[10], UPCp[11], UPCp[12], UPCp[13], UPCp[14], 
                    UPCp[15], UPCp[16], UPCp[17], UPCp[18], UPCp[19], UPCp[20], UPCp[21], UPCp[22], UPCp[23], UPCp[24] ])

        TMP_LST = re.split('(..)',UPCp[10])[1::2]
        L = len(TMP_LST)
        SBL = ''
        for Co in range(0,L):
            DC = int(TMP_LST[Co],16)
            SBL = SBL + (chr(DC))
        SBL =  '-' + str('{:.1f}'.format((float(SBL)/10)))
 
        if (UPCp[2] == '31') : # C-Band UPC
            print ('          ',DTN[1],'\033[1m\033[42m\033[37m\033[1m UPC \033[0m' + '\033[32m\033[1m  C-UPC Sampled Beacon Level : ' + SBL + ' (dBm) \033[0m' + '                                 lqms_upc.py Ver.' + VER)
        elif (UPCp[2] == '32') : # Ku-Band UPC
            print ('          ',DTN[1],'\033[1m\033[42m\033[37m\033[1m UPC \033[0m' + '\033[32m\033[1m  Ku-UPC Sampled Beacon Level :' + SBL + ' (dBm) \033[0m' + '                                 lqms_upc.py Ver.' + VER)
        lqms_plt2.ST(SBL,UPC_N)

    return()

def ST(ADD,RxDAT):
    DTN = lqms_dt.RTC_CHK()
    STA[0] = RxDAT[0:2]         # STx
    STA[1] = RxDAT[2:4]         # Rx Data Length
    STA[2] = RxDAT[4:6]         # UPC Unit Address
    STA[3] = RxDAT[6:8]         # Message
    STA[4] = RxDAT[8:62]        # Type of Unit
    STA[5] = RxDAT[62:72]       # Serial No.
    STA[6] = RxDAT[72:86]       # F/W Version
    STA[7] = RxDAT[86:88]       # Summary Alarm
    STA[8] = RxDAT[88:90]       # DCPS + 5V
    STA[9] = RxDAT[90:92]       # DCPS +15V
    STA[10] = RxDAT[92:94]      # DCPS -15V
    STA[11] = RxDAT[94:96]      # Primary VTG
    STA[12] = RxDAT[96:98]      # Temperature
    STA[13] = RxDAT[98:100]      # Humidity
    STA[14] = RxDAT[100:102]      # External Reference
    STA[15] = RxDAT[102:104]      # 100MHz Fault
    STA[16] = RxDAT[104:106]      # Coaxial SW
    STA[17] = RxDAT[106:108]      # Internal Ethernet Module
    STA[18] = RxDAT[108:148]      # Time and Date
    STA[19] = RxDAT[148:150]      # Check sum
    STA[20] = RxDAT[150:152]      # ETx

    if (STA[2] == '31') : # C-Band STA
        DEF_FL = 'C_UPC_DEF_STA.csv'
        UPC_N = 'C-Band'
        DEF_FL = '/home/xs4/basis/req_relFiles/' + DEF_FL
        FNL = '/mnt/ssd/log/c-upc/c-upc'
        print ('          ',DTN[1],'\033[1m\033[42m\033[37m\033[1m UPC \033[0m  C-Band UPC Unit Status Query                                              lqms_upc.py Ver.' + VER)
    elif (STA[2] == '32') : # Ku-Band STA
        DEF_FL = 'Ku_UPC_DEF_STA.csv'
        UPC_N = 'Ku-Band'
        DEF_FL = '/home/xs4/basis/req_relFiles/' + DEF_FL
        FNL = '/mnt/ssd/log/ku-upc/ku-upc'
        print ('          ',DTN[1],'\033[1m\033[42m\033[37m\033[1m UPC \033[0m  Ku-Band UPC Unit Status Query                                             lqms_upc.py Ver.' + VER)

    # File Check
    is_file = os.path.isfile(DEF_FL)
    c=0
    if is_file:
        with open(DEF_FL) as f:
            reader = csv.reader(f)
            DEF_STA = [row for row in reader]


    if (STA[4] != DEF_STA[0][4]):
        TMP_LST = re.split('(..)',STA[4])[1::2]
        L = len(TMP_LST)
        TYP = ''
        for Co in range(0,L):
            DC = int(TMP_LST[Co],16)
            TYP = TYP + (chr(DC))
#        print ('          ',DTN[1],'Type of Unit : ' + TYP )
        with open(FNL + DTN[5] + '.log', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([DTN[0], DTN[1], UPC_N, 'Type of Unit', TYP ])
            
    if (STA[5] != DEF_STA[0][5]):
        TMP_LST = re.split('(..)',STA[5])[1::2]
        L = len(TMP_LST)
        SER = ''
        for Co in range(0,L):
            DC = int(TMP_LST[Co],16)
            SER = SER + (chr(DC))
#        print ('          ',DTN[1],'Serial No : ' + SER )
        with open(FNL + DTN[5] + '.log', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([DTN[0], DTN[1], UPC_N, 'Serial No', SER ])

    if (STA[6] != DEF_STA[0][6]):
        TMP_LST = re.split('(..)',STA[6])[1::2]
        L = len(TMP_LST)
        FWV = ''
        for Co in range(0,L):
            DC = int(TMP_LST[Co],16)
            FWV = FWV + (chr(DC))
#        print ('          ',DTN[1],'Firmware Version : ' + FWV )
        with open(FNL + DTN[5] + '.log', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([DTN[0], DTN[1], UPC_N, 'Firmware Version', FWV ])

    if (STA[7] != DEF_STA[0][7]):
        TMP_LST = re.split('(..)',STA[7])[1::2]
        DC = int(TMP_LST[0],16)
        DCC = chr(DC)
        SUA = ''
        if (DCC == '1'):
#            print ('          ',DTN[1],'Summary Alarm : FAULT')
            SUA = 'FAULT'
        elif (DCC == '0'):
#            print ('          ',DTN[1],'Summary Alarm : OK')
            SUA = 'OK'
        with open(FNL + DTN[5] + '.log', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([DTN[0], DTN[1], UPC_N, 'Summary Alarm : ' + SUA])

    if (STA[8] != DEF_STA[0][8]):
        TMP_LST = re.split('(..)',STA[8])[1::2]
        DC = int(TMP_LST[0],16)
        DCC = chr(DC)
        DC5 = ''
        if (DCC == '1'):
#            print ('          ',DTN[1],'DCPS + 5V Alarm : FAULT')
            DC5 = 'FAULT'
        elif (DCC == '0'):
#            print ('          ',DTN[1],'DCPS + 5V Alarm : OK')
            DC5 = 'OK'
        with open(FNL + DTN[5] + '.log', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([DTN[0], DTN[1], UPC_N, 'DCPS + 5V Alarm : ' + DC5])

    if (STA[9] != DEF_STA[0][9]):
        TMP_LST = re.split('(..)',STA[9])[1::2]
        DC = int(TMP_LST[0],16)
        DCC = chr(DC)
        DC15 = ''
        if (DCC == '1'):
#            print ('          ',DTN[1],'DCPS +15V Alarm : FAULT')
            DC15 = 'FAULT'
        elif (DCC == '0'):
#            print ('          ',DTN[1],'DCPS +15V Alarm : OK')
            DC15 = 'OK'
        with open(FNL + DTN[5] + '.log', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([DTN[0], DTN[1], UPC_N, 'DCPS +15V Alarm : ' + DC15])

    if (STA[10] != DEF_STA[0][10]):
        TMP_LST = re.split('(..)',STA[10])[1::2]
        DC = int(TMP_LST[0],16)
        DCC = chr(DC)
        DCM15 = ''
        if (DCC == '1'):
#            print ('          ',DTN[1],'DCPS -15V Alarm : FAULT')
            DCM15 = 'FAULT'
        elif (DCC == '0'):
#            print ('          ',DTN[1],'DCPS -15V Alarm : OK')
            DCM15 = 'OK'
        with open(FNL + DTN[5] + '.log', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([DTN[0], DTN[1], UPC_N, 'DCPS -15V Alarm : ' + DCM15])

    if (STA[11] != DEF_STA[0][11]):
        TMP_LST = re.split('(..)',STA[11])[1::2]
        DC = int(TMP_LST[0],16)
        DCC = chr(DC)
        DCP = ''
        if (DCC == '1'):
#            print ('          ',DTN[1],'Primary Voltage Alarm : FAULT')
            DCP = 'FAULT'
        elif (DCC == '0'):
#            print ('          ',DTN[1],'Primary Voltage Alarm : OK')
            DCP = 'OK'
        with open(FNL + DTN[5] + '.log', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([DTN[0], DTN[1], UPC_N, 'Primary Voltage Alarm : ' + DCP])

    if (STA[12] != DEF_STA[0][12]):
        TMP_LST = re.split('(..)',STA[12])[1::2]
        DC = int(TMP_LST[0],16)
        DCC = chr(DC)
        DCP = ''
        if (DCC == '1'):
#            print ('          ',DTN[1],'Primary Voltage Alarm : FAULT')
            DCP = 'FAULT'
        elif (DCC == '0'):
#            print ('          ',DTN[1],'Primary Voltage Alarm : OK')
            DCP = 'OK'
        with open(FNL + DTN[5] + '.log', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([DTN[0], DTN[1], UPC_N, 'Primary Voltage Alarm : ' + DCP])

    if (STA[13] != DEF_STA[0][13]):
        TMP_LST = re.split('(..)',STA[13])[1::2]
        DC = int(TMP_LST[0],16)
        DCC = chr(DC)
        HUM = ''
        if (DCC == '1'):
#            print ('          ',DTN[1],'Humidity Alarm : FAULT')
            HUM = 'FAULT'
        elif (DCC == '0'):
#            print ('          ',DTN[1],'Humidity Alarm : OK')
            HUM = 'OK'
        with open(FNL + DTN[5] + '.log', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([DTN[0], DTN[1], UPC_N, 'Humidity : ' + HUM])

    if (STA[14] != DEF_STA[0][14]):
        TMP_LST = re.split('(..)',STA[14])[1::2]
        DC = int(TMP_LST[0],16)
        DCC = chr(DC)
        EXR = ''
        if (DCC == '1'):
#            print ('          ',DTN[1],'External Reference : FAULT')
            EXR = 'FAULT'
        elif (DCC == '0'):
#            print ('          ',DTN[1],'External Reference : OK')
            EXR = 'OK'
        with open(FNL + DTN[5] + '.log', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([DTN[0], DTN[1], UPC_N, 'External Reference : ' + EXR])

    if (STA[15] != DEF_STA[0][15]):
        TMP_LST = re.split('(..)',STA[15])[1::2]
        DC = int(TMP_LST[0],16)
        DCC = chr(DC)
        M100 = ''
        if (DCC == '1'):
#            print ('          ',DTN[1],'100MHz Fault : FAULT')
            M100 = 'FAULT'
        elif (DCC == '0'):
#            print ('          ',DTN[1],'100MHz Fault : OK')
            M100 = 'OK'
        with open(FNL + DTN[5] + '.log', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([DTN[0], DTN[1], UPC_N, '100MHz Fault : ' + M100])

    if (STA[16] != DEF_STA[0][16]):
        TMP_LST = re.split('(..)',STA[16])[1::2]
        DC = int(TMP_LST[0],16)
        DCC = chr(DC)
        EXR = ''
        if (DCC == '1'):
#            print ('          ',DTN[1],'Coaxial SW Fault : FAULT')
            EXR = 'FAULT'
        elif (DCC == '0'):
#            print ('          ',DTN[1],'Coaxial SW Fault : OK')
            EXR = 'OK'
        with open(FNL + DTN[5] + '.log', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([DTN[0], DTN[1], UPC_N, 'Coaxial SW Fault : ' + EXR])

    if (STA[17] != DEF_STA[0][17]):
        TMP_LST = re.split('(..)',STA[17])[1::2]
        DC = int(TMP_LST[0],16)
        DCC = chr(DC)
        IEM = ''
        if (DCC == '1'):
#            print ('          ',DTN[1],'Internal Ethernet Module : FAULT')
            IEM = 'FAULT'
        elif (DCC == '0'):
#            print ('          ',DTN[1],'Internal Ethernet Module : OK')
            IEM = 'OK'
        with open(FNL + DTN[5] + '.log', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([DTN[0], DTN[1], UPC_N, 'Internal Ethernet Module : ' + IEM])

        with open(DEF_FL, 'w') as f:
            writer = csv.writer(f)
            writer.writerow([STA[0], STA[1], STA[2], STA[3], STA[4], STA[5], STA[6], STA[7], STA[8], STA[9], STA[10], STA[11], STA[12], STA[13], STA[14], 
                    STA[15], STA[16], STA[17], STA[18], STA[19], STA[20]])

    return()
