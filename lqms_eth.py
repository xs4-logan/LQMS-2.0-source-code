#####soup
# Ethernet Packet Counter reader for LQMS-2.0E Version 0.2.4
# 2022.08.10 Yoshiaki Sato[Technobiz]
#####
import lqms_dt
import csv
from bs4 import BeautifulSoup
import requests
import os

VER = '0.2.4'
FN1 = '/mnt/ssd/log/error/err_'
FN2 = '/mnt/ssd/log/facl/sys_'

def ST(IPA):
    try :
        os.chdir('/home/xs4/basis/')
        DTN = lqms_dt.RTC_CHK()

        # Parameter of Outbound Packets [Counters]
        OBP_TOT_TRF = ''    # 01.Total Packet Received / Traffic Port
        OBP_UNI_TRF = ''    # 02.Unicast Packets Received / Traffic Port
        OBP_BRD_TRF = ''    # 03.Broadcast Packets Received / Traffic Port
        OBP_MLT_TRF = ''    # 04.Multicast Packets Received / Traffic Port
        OBP_TOT_WAN = ''    # 05.Total Packet Transmitted / WAN Port
        OBP_UNI_WAN = ''    # 06.Unicast Packets Transmitted / WAN Port
        OBP_BRD_WAN = ''    # 07.Broadcast Packets Transmitted / WAN Port
        OBP_MLT_WAN = ''    # 08.Multicast Packets Transmitted / WAN Port
        # Parameter of Outbound Packets [Speed]
        OBP_CDR_TRF = ''    # 09.Current Datarate / Traffic Port
        OBP_AVG_TRF = ''    # 10.Average Datarate / Traffic Port
        OBP_MAX_TRF = ''    # 11.MAX Datarate / Traffic Port
        OBP_CDR_WAN = ''    # 12.Current Datarate / WAN Port
        OBP_AVG_WAN = ''    # 13.Average Datarate / WAN Port
        OBP_MAX_WAN = ''    # 14.MAX Datarate / WAN Port

        # Parameter of Inbound Packets [Counters]
        IBP_TOT_WAN = ''    # 01.Total Packet Received / WAN Port
        IBP_UNI_WAN = ''    # 02.Unicast Packets Received / WAN Port
        IBP_BRD_WAN = ''    # 03.Broadcast Packets Received / WAN Port
        IBP_MLT_WAN = ''    # 04.Multicast Packets Received / WAN Port
        IBP_TOT_TRF = ''    # 05.Total Packet Transmitted / Traffic Port
        IBP_UNI_TRF = ''    # 06.Unicast Packets Transmitted / Traffic Port
        IBP_BRD_TRF = ''    # 07.Broadcast Packets Transmitted / Traffic Port
        IBP_MLT_TRF = ''    # 08.Multicast Packets Transmitted / Traffic Port
        # Parameter of Inbound Packets [Speed]
        IBP_CDR_WAN = ''    # 09.Current Datarate / WAN Port
        IBP_AVG_WAN = ''    # 10.Average Datarate / WAN Port
        IBP_MAX_WAN = ''    # 11.MAX Datarate / WAN Port
        IBP_CDR_TRF = ''    # 12.Current Datarate / Traffic Port
        IBP_AVG_TRF = ''    # 13.Average Datarate / Traffic Port
        IBP_MAX_TRF = ''    # 14.MAX Datarate / Traffic Port

        # Error Details in Outbound Packets
        OBP_ER01_TRF = ''   # 01.LAN FCS Error / Traffic Port
        OBP_ER02_TRF = ''   # 02.Alignment Error / Traffic Port
        OBP_ER03_TRF = ''   # 03.Undersize / Traffic Port
        OBP_ER04_TRF = ''   # 04.Fragments / Traffic Port
        OBP_ER05_TRF = ''   # 05.Jabber / Traffic Port
        OBP_ER06_TRF = ''   # 06.Oversize / Traffic Port
        OBP_ER07_TRF = ''   # 07.InDiscards / Traffic Port
        OBP_ER08_WAN = ''   # 08.Single Collision / WAN Port
        OBP_ER09_WAN = ''   # 09.Multiple Collision / WAN Port
        OBP_ER10_WAN = ''   # 10.Excessive Collistion / WAN Port 

        # Error Details in Inbound Packets
        IBP_ER01_WAN = ''   # 01.LAN FCS Error / WAN Port
        IBP_ER02_WAN = ''   # 02.Alignment Error / WAN Port
        IBP_ER03_WAN = ''   # 03.Undersize / WAN Port
        IBP_ER04_WAN = ''   # 04.Fragments / WAN Port
        IBP_ER05_WAN = ''   # 05.Jabber / WAN Port
        IBP_ER06_WAN = ''   # 06.Oversize / WAN Port
        IBP_ER07_WAN = ''   # 07.InDiscards / WAN Port
        IBP_ER08_TRF = ''   # 08.Single Collision / Traffic Port
        IBP_ER09_TRF = ''   # 09.Multiple Collision / Traffic Port
        IBP_ER10_TRF = ''   # 10.Excessive Collistion / Traffic Port 

        # Reading HLD data file
        if (IPA == '192.168.1.11'):
            MD = 'MDA1'
            MD2 = 'MODEM-A1'
            FLN1 = 'MDA1_OBP_TMP.csv'
            FLN2 = 'MDA1_IBP_TMP.csv'
            FLN3 = 'MDA1_ERR_TMP.csv'
            FN3 = '/mnt/ssd/log/mda1/MDA1_'
        elif (IPA == '192.168.1.12'):
            MD = 'MDA2'
            MD2 = 'MODEM-A2'
            FLN1 = 'MDA2_OBP_TMP.csv'
            FLN2 = 'MDA2_IBP_TMP.csv'
            FLN3 = 'MDA2_ERR_TMP.csv'
            FN3 = '/mnt/ssd/log/mda2/MDA2_'
        elif (IPA == '192.168.1.21'):
            MD = 'MDB1'
            MD2 = 'MODEM-B1'
            FLN1 = 'MDB1_OBP_TMP.csv'
            FLN2 = 'MDB1_IBP_TMP.csv'
            FLN3 = 'MDB1_ERR_TMP.csv'
            FN3 = '/mnt/ssd/log/mdb1/MDB1_'
        elif (IPA == '192.168.1.22'):
            MD = 'MDB2'
            MD2 = 'MODEM-B2'
            FLN1 = 'MDB2_OBP_TMP.csv'
            FLN2 = 'MDB2_IBP_TMP.csv'
            FLN3 = 'MDB2_ERR_TMP.csv'
            FN3 = '/mnt/ssd/log/mdb2/MDB2_'
        elif (IPA == '192.168.1.23'):
            MD = 'MDC1'
            MD2 = 'MODEM-C1'
            FLN1 = 'MDC1_OBP_TMP.csv'
            FLN2 = 'MDC1_IBP_TMP.csv'
            FLN3 = 'MDC1_ERR_TMP.csv'
            FN3 = '/mnt/ssd/log/mdc1/MDC1_'
        elif (IPA == '192.168.1.24'):
            MD = 'MDC2'
            MD2 = 'MODEM-C2'
            FLN1 = 'MDC2_OBP_TMP.csv'
            FLN2 = 'MDC2_IBP_TMP.csv'
            FLN3 = 'MDC2_ERR_TMP.csv'
            FN3 = '/mnt/ssd/log/mdc2/MDC2_'
        elif (IPA == '192.168.1.25'):
            MD = 'MDE1'
            MD2 = 'MODEM-E1'
            FLN1 = 'MDE1_OBP_TMP.csv'
            FLN2 = 'MDE1_IBP_TMP.csv'
            FLN3 = 'MDE1_ERR_TMP.csv'
            FN3 = '/mnt/ssd/log/mde1/MDE1_'
        elif (IPA == '192.168.1.26'):
            MD = 'MDE2'
            MD2 = 'MODEM-E2'
            FLN1 = 'MDE2_OBP_TMP.csv'
            FLN2 = 'MDE2_IBP_TMP.csv'
            FLN3 = 'MDE2_ERR_TMP.csv'
            FN3 = '/mnt/ssd/log/mde2/MDE2_'

        fld = '/home/xs4/basis/req_relFiles/'
        FLN1 = fld + FLN1
        FLN2 = fld + FLN2
        FLN3 = fld + FLN3

        # File Check-1
        with open(FLN1) as f:
            reader = csv.reader(f)
            OBP_1 = [row for row in reader]
        #print(OBP_1[0][0],OBP_1[0][1],OBP_1[0][2],OBP_1[0][3],OBP_1[0][4],OBP_1[0][5],OBP_1[0][6],OBP_1[0][7],OBP_1[0][8],OBP_1[0][9],OBP_1[0][10],OBP_1[0][11],OBP_1[0][12],OBP_1[0][13])
        # File Check-2
        with open(FLN2) as f:
            reader = csv.reader(f)
            IBP_1 = [row for row in reader]
        #print(IBP_1[0][0],IBP_1[0][1],IBP_1[0][2],IBP_1[0][3],IBP_1[0][4],IBP_1[0][5],IBP_1[0][6],IBP_1[0][7],IBP_1[0][8],IBP_1[0][9],IBP_1[0][10],IBP_1[0][11],IBP_1[0][12],IBP_1[0][13])
        # File Check-1
        with open(FLN3) as f:
            reader = csv.reader(f)
            ERR_1 = [row for row in reader]
        #print(ERR_1[0][0],ERR_1[0][1],ERR_1[0][2],ERR_1[0][3],ERR_1[0][4],ERR_1[0][5],ERR_1[0][6],ERR_1[0][7],ERR_1[0][8],ERR_1[0][9],ERR_1[0][10],ERR_1[0][11],ERR_1[0][12],ERR_1[0][13],ERR_1[0][14],ERR_1[0][15],ERR_1[0][16],ERR_1[0][17],ERR_1[0][18],ERR_1[0][19])

        DTN = lqms_dt.RTC_CHK()
        URL = 'http://' + IPA + ':8080/per_port_stat.htm'
        res = requests.get(URL,auth=('comtech','comtech'))
        content = res.content
        soup = BeautifulSoup(content, 'html.parser')

        print ('          ',DTN[1],'\033[1m\033[44m\033[37m\033[1m M/D \033[0m  Ethernet Counter Monitor & Recorder                                       lqms_eth.py Ver.' + VER)
        with open(FN2 + DTN[5] + '.log', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([DTN[0], DTN[1], MD, 'ETH','Web Analysis', 'Ethernet Statistics'])

        #Outbound Packets
        # 01.Total Packet Received @Traffic Port
        OBP_TOT_TRF = (soup.select('body td')[3].string).replace('\n','')
        if (OBP_1[0][0] != OBP_TOT_TRF):
            OBP_TOT_TRF = OBP_1[0][0]
            with open(FN3 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'ETH', 'Total Packets Received', OBP_TOT_TRF, '',  '@Traffic Input'])
        # 02.Unicast Packet Received @Traffic Port
        OBP_UNI_TRF = (soup.select('body td')[8].string).replace('\n','')
        if (OBP_1[0][1] != OBP_UNI_TRF):
            OBP_UNI_TRF = OBP_1[0][1]
            with open(FN3 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'ETH', 'Unicast Packets Received', OBP_UNI_TRF, '', '@Traffic Input'])
        # 03.Broadcast Packet Received @Traffic Port
        OBP_BRD_TRF = (soup.select('body td')[12].string).replace('\n','')
        if (OBP_1[0][2] != OBP_BRD_TRF):
            OBP_BRD_TRF = OBP_1[0][2]
            with open(FN3 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'ETH', 'Broadcast Packets Received', OBP_BRD_TRF, '', '@Traffic Input'])
        # 04.Multicast Packet Received @Traffic Port
        OBP_MLT_TRF = (soup.select('body td')[16].string).replace('\n','')
        if (OBP_1[0][3] != OBP_MLT_TRF):
            OBP_MLT_TRF = OBP_1[0][3]
            with open(FN3 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'ETH', 'Multicast Packets Received', OBP_MLT_TRF, '', '@Traffic Input'])
        # 05.Total Packet Transmitted @WAN Port
        OBP_TOT_WAN = (soup.select('body td')[58].string).replace('\n','')
        if (OBP_1[0][4] != OBP_TOT_WAN):
            OBP_TOT_WAN = OBP_1[0][4]
            with open(FN3 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'ETH', 'Total Packets Transmitted', OBP_TOT_WAN, '', '@WAN Output'])
        # 06.Unicast Packet Transmitted @WAN Port
        OBP_UNI_WAN = (soup.select('body td')[63].string).replace('\n','')
        if (OBP_1[0][5] != OBP_UNI_WAN):
            OBP_UNI_WAN = OBP_1[0][5]
            with open(FN3 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'ETH', 'Unicast Packets Transmitted', OBP_UNI_WAN, '', '@WAN Output'])
        # 07.Broadcast Packet Transmitted @WAN Port
        OBP_BRD_WAN = (soup.select('body td')[67].string).replace('\n','')
        if (OBP_1[0][6] != OBP_BRD_WAN):
            OBP_BRD_WAN = OBP_1[0][6]
            with open(FN3 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'ETH', 'Broadcast Packets Transmitted', OBP_BRD_WAN, '', '@WAN Output'])
        # 08.Broadcast Packet Transmitted @WAN Port
        OBP_MLT_WAN = (soup.select('body td')[71].string).replace('\n','')
        if (OBP_1[0][7] != OBP_MLT_WAN):
            OBP_MLT_WAN = OBP_1[0][7]
            with open(FN3 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'ETH', 'Multicast Packets Transmitted', OBP_MLT_WAN, '', '@WAN Output'])
        # 09.Current Datarate  @Traffic Port
        OBP_CDR_TRF = (soup.select('body td')[32].string).replace('\n','')
        if (OBP_1[0][8] != OBP_CDR_TRF):
            OBP_CDR_TRF = OBP_1[0][8]
            with open(FN3 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'ETH', 'Current Datarate', OBP_CDR_TRF, '', '@Traffic Port Input'])
        # 10.Average Datarate  @Traffic Port
        OBP_AVG_TRF = (soup.select('body td')[36].string).replace('\n','')
        if (OBP_1[0][9] != OBP_AVG_TRF):
            OBP_AVG_TRF = OBP_1[0][9]
            with open(FN3 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'ETH', 'Average Datarate', OBP_AVG_TRF, '', '@Traffic Port Input' ])
        # 11.MAX Datarate  @Traffic Port
        OBP_MAX_TRF = (soup.select('body td')[40].string).replace('\n','')
        if (OBP_1[0][10] != OBP_MAX_TRF):
            OBP_MAX_TRF = OBP_1[0][10]
            with open(FN3 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'ETH', 'MAX Datarate', OBP_MAX_TRF, '', '@Traffic Port Input'])
        # 12.Current Datarate  @WAN Port
        OBP_CDR_WAN = (soup.select('body td')[83].string).replace('\n','')
        if (OBP_1[0][11] != OBP_CDR_WAN):
            OBP_CDR_WAN = OBP_1[0][11]
            with open(FN3 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'ETH', 'Current Datarate', OBP_CDR_WAN, '', '@WAN Port Output' ])
        # 13.Average Datarate  @WAN Port
        OBP_AVG_WAN = (soup.select('body td')[87].string).replace('\n','')
        if (OBP_1[0][12] != OBP_AVG_WAN):
            OBP_AVG_WAN = OBP_1[0][12]
            with open(FN3 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'ETH', 'Average Datarate', OBP_AVG_WAN, '', '@WAN Port Output'])
        # 14.MAX Datarate  @WAN Port
        OBP_MAX_WAN = (soup.select('body td')[91].string).replace('\n','')
        if (OBP_1[0][13] != OBP_MAX_WAN):
            OBP_MAX_WAN = OBP_1[0][13]
            with open(FN3 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'ETH', 'MAX Datarate', OBP_MAX_WAN, '', '@WAN Port Output'])

        with open(FLN1, 'w') as f:
            writer = csv.writer(f)
            writer.writerow([OBP_TOT_TRF,OBP_UNI_TRF,OBP_BRD_TRF,OBP_MLT_TRF,OBP_TOT_WAN,OBP_UNI_WAN,OBP_BRD_WAN,OBP_MLT_WAN,OBP_CDR_TRF,OBP_AVG_TRF,OBP_MAX_TRF,OBP_CDR_WAN,OBP_AVG_WAN,OBP_MAX_WAN])
        DTN = lqms_dt.RTC_CHK()
        print ('          ',DTN[1],'\033[1m\033[44m\033[37m\033[1m M/D \033[0m  Finished processing for Outbound Packets.                                 lqms_eth.py Ver.' + VER)

        #Inbound Packets
        # 01.Total Packet Transmitted @Traffic Port
        IBP_TOT_TRF = (soup.select('body td')[56].string).replace('\n','')
        if (IBP_1[0][0] != IBP_TOT_TRF):
            IBP_TOT_TRF = IBP_1[0][0]
            with open(FN3 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'ETH', 'Total Packets Transmitted', IBP_TOT_TRF, '', '@Traffic Output' ])
        # 02.Unicast Packet Transmitted @Traffic Port
        IBP_UNI_TRF = (soup.select('body td')[61].string).replace('\n','')
        if (IBP_1[0][1] != IBP_UNI_TRF):
            IBP_UNI_TRF = IBP_1[0][1]
            with open(FN3 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'ETH', 'Unicast Packets Transmitted', IBP_UNI_TRF, '', '@Traffic Output' ])
        # 03.Broadcast Packet Transmitted @Traffic Port
        IBP_BRD_TRF = (soup.select('body td')[65].string).replace('\n','')
        if (IBP_1[0][2] != IBP_BRD_TRF):
            IBP_BRD_TRF = IBP_1[0][2]
            with open(FN3 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'ETH', 'Broadcast Packets Transmitted', IBP_BRD_TRF, '', '@Traffic Output'])
        # 04.Multicast Packet Transmitted @Traffic Port
        IBP_MLT_TRF = (soup.select('body td')[69].string).replace('\n','')
        if (IBP_1[0][3] != IBP_MLT_TRF):
            IBP_MLT_TRF = IBP_1[0][3]
            with open(FN3 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'ETH', 'Multicast Packets Transmitted', IBP_MLT_TRF, '', '@Traffic Output'])
        # 05.Total Packet Received @WAN Port
        IBP_TOT_WAN = (soup.select('body td')[5].string).replace('\n','')
        if (IBP_1[0][4] != IBP_TOT_WAN):
            IBP_TOT_WAN = IBP_1[0][4]
            with open(FN3 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'ETH', 'Total Packets Received', IBP_TOT_WAN, '', '@WAN Input'])
        # 06.Unicast Packet Received @WAN Port
        IBP_UNI_WAN = (soup.select('body td')[10].string).replace('\n','')
        if (IBP_1[0][5] != IBP_UNI_WAN):
            IBP_UNI_WAN = IBP_1[0][5]
            with open(FN3 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'ETH', 'Unicast Packets Received', IBP_UNI_WAN, '', '@WAN Input'])
        # 07.Broadcast Packet Received @WAN Port
        IBP_BRD_WAN = (soup.select('body td')[14].string).replace('\n','')
        if (IBP_1[0][6] != IBP_BRD_WAN):
            IBP_BRD_WAN = IBP_1[0][6]
            with open(FN3 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'ETH', 'Broadcast Packets Received', IBP_BRD_WAN, '', '@WAN Input'])
        # 08.Multicast Packet Received @WAN Port
        IBP_MLT_WAN = (soup.select('body td')[18].string).replace('\n','')
        if (IBP_1[0][7] != IBP_MLT_WAN):
            IBP_MLT_WAN = IBP_1[0][7]
            with open(FN3 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'ETH', 'Multicast Packets Received', IBP_MLT_WAN, '', '@WAN Input'])
        # 09.Current Datarate  @Traffic Port
        IBP_CDR_TRF = (soup.select('body td')[81].string).replace('\n','')
        if (IBP_1[0][8] != IBP_CDR_TRF):
            IBP_CDR_TRF = IBP_1[0][8]
            with open(FN3 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'ETH', 'Current Datarate', IBP_CDR_TRF, '', '@Traffic Port Output'])
        # 10.Average Datarate  @Traffic Port
        IBP_AVG_TRF = (soup.select('body td')[85].string).replace('\n','')
        if (IBP_1[0][9] != IBP_AVG_TRF):
            IBP_AVG_TRF = IBP_1[0][9]
            with open(FN3 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'ETH', 'Average Datarate', IBP_AVG_TRF, '', '@Traffic Port Output'])
        # 11.MAX Datarate  @Traffic Port
        IBP_MAX_TRF = (soup.select('body td')[89].string).replace('\n','')
        if (IBP_1[0][10] != IBP_MAX_TRF):
            IBP_MAX_TRF = IBP_1[0][10]
            with open(FN3 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'ETH', 'MAX Datarate', IBP_MAX_TRF, '', '@Traffic Port Output'])
        # 12.Current Datarate  @WAN Port
        IBP_CDR_WAN = (soup.select('body td')[34].string).replace('\n','')
        if (IBP_1[0][11] != IBP_CDR_WAN):
            IBP_CDR_WAN = IBP_1[0][11]
            with open(FN3 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'ETH', 'Current Datarate', IBP_CDR_WAN, '', '@WAN Port Input'])
        # 13.Average Datarate  @WAN Port
        IBP_AVG_WAN = (soup.select('body td')[38].string).replace('\n','')
        if (IBP_1[0][12] != IBP_AVG_WAN):
            IBP_AVG_WAN = IBP_1[0][12]
            with open(FN3 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'ETH', 'Average Datarate', IBP_AVG_WAN, '', '@WAN Port Input'])
        # 14.MAX Datarate  @WAN Port
        IBP_MAX_WAN = (soup.select('body td')[42].string).replace('\n','')
        if (IBP_1[0][13] != IBP_MAX_WAN):
            IBP_MAX_WAN = IBP_1[0][13]
            with open(FN3 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'ETH', 'MAX Datarate', IBP_MAX_WAN, '', '@WAN Port Input' ])

        with open(FLN2, 'w') as f:
            writer = csv.writer(f)
            writer.writerow([IBP_TOT_TRF,IBP_UNI_TRF,IBP_BRD_TRF,IBP_MLT_TRF,IBP_TOT_WAN,IBP_UNI_WAN,IBP_BRD_WAN,IBP_MLT_WAN,IBP_CDR_TRF,IBP_AVG_TRF,IBP_MAX_TRF,IBP_CDR_WAN,IBP_AVG_WAN,IBP_MAX_WAN])
        DTN = lqms_dt.RTC_CHK()
        print ('          ',DTN[1],'\033[1m\033[44m\033[37m\033[1m M/D \033[0m  Finished processing for Inbound Packets.                                  lqms_eth.py Ver.' + VER)

        #Error Packets Outbound
        # 01.LAN FCS Error  @Traffic Port
        OBP_ER01_TRF = (soup.select('td')[105].string).replace('\n','')
        if (ERR_1[0][0] != OBP_ER01_TRF):
            OBP_ER01_TRF = ERR_1[0][0]
            with open(FN3 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'ERP', 'LAN FCS Error', OBP_ER01_TRF, '', '@Traffic Port Input'])
        # 02.Alignment Error  @Traffic Port
        OBP_ER02_TRF = (soup.select('td')[109].string).replace('\n','')
        if (ERR_1[0][1] != OBP_ER02_TRF):
            OBP_ER02_TRF = ERR_1[0][1]
            with open(FN3 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'ERP', 'Alignment Error', OBP_ER02_TRF, '', '@Traffic Port Input'])
        # 03.Undersize Error  @Traffic Port
        OBP_ER03_TRF = (soup.select('td')[113].string).replace('\n','')
        if (ERR_1[0][2] != OBP_ER03_TRF):
            OBP_ER03_TRF = ERR_1[0][2]
            with open(FN3 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'ERP', 'Undersize Error', OBP_ER03_TRF, '', '@Traffic Port Input'])
        # 04.Flagment Error  @Traffic Port
        OBP_ER04_TRF = (soup.select('td')[117].string).replace('\n','')
        if (ERR_1[0][3] != OBP_ER04_TRF):
            OBP_ER04_TRF = ERR_1[0][3]
            with open(FN3 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'ERP', 'Flagments Error', OBP_ER04_TRF, '', '@Traffic Port Input'])
        # 05.Jabber Error  @Traffic Port
        OBP_ER05_TRF = (soup.select('td')[121].string).replace('\n','')
        if (ERR_1[0][4] != OBP_ER05_TRF):
            OBP_ER05_TRF = ERR_1[0][4]
            with open(FN3 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'ERP', 'Jabber Error', OBP_ER05_TRF, '', '@Traffic Port Input'])
        # 06.Oversize Error  @Traffic Port
        OBP_ER06_TRF = (soup.select('td')[125].string).replace('\n','')
        if (ERR_1[0][5] != OBP_ER06_TRF):
            OBP_ER06_TRF = ERR_1[0][5]
            with open(FN3 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'ERP', 'Oversize Error', OBP_ER06_TRF, '', '@Traffic Port Input'])
        # 07.Indiscards Error  @Traffic Port
        OBP_ER07_TRF = (soup.select('td')[129].string).replace('\n','')
        if (ERR_1[0][6] != OBP_ER07_TRF):
            OBP_ER07_TRF = ERR_1[0][6]
            with open(FN3 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'ERP', 'Indiscards Error', OBP_ER07_TRF, '', '@Traffic Port Input'])
        # 08.Single Collision  @WAN Port
        OBP_ER08_WAN = (soup.select('td')[135].string).replace('\n','')
        if (ERR_1[0][7] != OBP_ER08_WAN):
            OBP_ER08_WAN = ERR_1[0][7]
            with open(FN3 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'ERP', 'Single Collision', OBP_ER08_WAN, '', '@WAN Port Output'])
        # 09.Multiple Collision  @WAN Port
        OBP_ER09_WAN = (soup.select('td')[139].string).replace('\n','')
        if (ERR_1[0][8] != OBP_ER09_WAN):
            OBP_ER09_WAN = ERR_1[0][8]
            with open(FN3 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'ERP', 'Multiple Collision', OBP_ER09_WAN, '', '@WAN Port Output'])
        # 10.Excessive Collision  @WAN Port
        OBP_ER10_WAN = (soup.select('td')[143].string).replace('\n','')
        if (ERR_1[0][9] != OBP_ER10_WAN):
            OBP_ER10_WAN = ERR_1[0][9]
            with open(FN3 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'ERP', 'Excessive Collision', OBP_ER10_WAN, '', '@WAN Port Output'])

        #Error Packets Inbound
        # 01.LAN FCS Error  @Traffic Port
        IBP_ER01_WAN = (soup.select('td')[107].string).replace('\n','')
        if (ERR_1[0][10] != IBP_ER01_WAN):
            IBP_ER01_WAN = ERR_1[0][10]
            with open(FN3 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'ERP', 'LAN FCS Error', IBP_ER01_WAN, '', '@WAN Port Input'])
        # 02.Alignment Error  @WAN Port
        IBP_ER02_WAN = (soup.select('td')[111].string).replace('\n','')
        if (ERR_1[0][11] != IBP_ER02_WAN):
            IBP_ER02_WAN = ERR_1[0][11]
            with open(FN3 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'ERP', 'Alignment Error', IBP_ER02_WAN, '', '@WAN Port Input'])
        # 03.Undersize Error  @WAN Port
        IBP_ER03_WAN = (soup.select('td')[115].string).replace('\n','')
        if (ERR_1[0][12] != IBP_ER03_WAN):
            IBP_ER03_WAN = ERR_1[0][12]
            with open(FN3 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'ERP', 'Undersize Error', IBP_ER03_WAN, '', '@WAN Port Input'])
        # 04.Flagment Error  @WAN Port
        IBP_ER04_WAN = (soup.select('td')[119].string).replace('\n','')
        if (ERR_1[0][13] != IBP_ER04_WAN):
            IBP_ER04_WAN = ERR_1[0][13]
            with open(FN3 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'ERP', 'Flagments Error', IBP_ER04_WAN, '', '@WAN Port Input'])
        # 05.Jabber Error  @WAN Port
        IBP_ER05_WAN = (soup.select('td')[123].string).replace('\n','')
        if (ERR_1[0][14] != IBP_ER05_WAN):
            IBP_ER05_WAN = ERR_1[0][14]
            with open(FN3 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'ERP', 'Jabber Error', IBP_ER05_WAN, '', '@WAN Port Input'])
        # 06.Oversize Error  @WAN Port
        IBP_ER06_WAN = (soup.select('td')[127].string).replace('\n','')
        if (ERR_1[0][15] != IBP_ER06_WAN):
            IBP_ER06_WAN = ERR_1[0][15]
            with open(FN3 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'ERP', 'Oversize Error', IBP_ER06_WAN, '', '@WAN Port Input'])
        # 07.Indiscards Error  @WAN Port
        IBP_ER07_WAN = (soup.select('td')[131].string).replace('\n','')
        if (ERR_1[0][16] != IBP_ER07_WAN):
            IBP_ER07_WAN = ERR_1[0][16]
            with open(FN3 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'ERP', 'Indiscards Error', IBP_ER07_WAN, '', '@WAN Port Input'])
        # 08.Single Collision  @Traffic Port
        IBP_ER08_TRF = (soup.select('td')[133].string).replace('\n','')
        if (ERR_1[0][17] != IBP_ER08_TRF):
            IBP_ER08_TRF = ERR_1[0][17]
            with open(FN3 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'ERP', 'Single Collision', IBP_ER08_TRF, '', '@Traffic Port Output'])
        # 09.Multiple Collision  @Traffic Port
        IBP_ER09_TRF = (soup.select('td')[137].string).replace('\n','')
        if (ERR_1[0][18] != IBP_ER09_TRF):
            IBP_ER09_TRF = ERR_1[0][18]
            with open(FN3 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'ERP', 'Multiple Collision', IBP_ER09_TRF, '', '@Traffic Port Output'])
        # 10.Excessive Collision  @Traffic Port
        IBP_ER10_TRF = (soup.select('td')[141].string).replace('\n','')
        if (ERR_1[0][19] != IBP_ER10_TRF):
            IBP_ER10_TRF = ERR_1[0][19]
            with open(FN3 + DTN[5] + '.log', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([DTN[0], DTN[1], MD, 'ERP', 'Excessive Collision', IBP_ER10_TRF, '', '@Traffic Port Output'])

        with open(FLN3 , 'w') as f:
            writer = csv.writer(f)
            writer.writerow([OBP_ER01_TRF,OBP_ER02_TRF,OBP_ER03_TRF,OBP_ER04_TRF,OBP_ER05_TRF,OBP_ER06_TRF,OBP_ER07_TRF,OBP_ER08_WAN,OBP_ER09_WAN,OBP_ER10_WAN,IBP_ER01_WAN,IBP_ER02_WAN,IBP_ER03_WAN,IBP_ER04_WAN,IBP_ER05_WAN,IBP_ER06_WAN,IBP_ER07_WAN,IBP_ER08_TRF,IBP_ER09_TRF,IBP_ER10_TRF])
        DTN = lqms_dt.RTC_CHK()
        print ('          ',DTN[1],'\033[1m\033[44m\033[37m\033[1m M/D \033[0m  Finished processing for Error Detail.                                     lqms_eth.py Ver.' + VER)

    except:
        print ('          ',DTN[1], '\33[1m\033[44m\033[37m' + ' M/D ' + '\033[0m' + '    \033[1m\033[41m\033[37m FAULT \033[0m \033[1m\033[31m' + MD2 + ' Something Error in Ethernet Counter Scraping Process.' + '\033[0m          lqms_rtc.py Ver.' + VER)
