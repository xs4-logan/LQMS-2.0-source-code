#####
# CDM-570AL-IP / per_port_stat.htm scraper
# 2022.05.27 Yoshiaki Sato[Technobiz]
#####
import datetime

def RTC_CHK():
	DTN = datetime.datetime.now()
	TDY = DTN.strftime('%y/%m/%d')
	TOD = DTN.strftime('%H:%M:%S')
	FN = DTN.strftime('%y%m%d')
	hr = int(DTN.strftime('%H'))
	mn = int(DTN.strftime('%M'))
	sc = int(DTN.strftime('%S'))

	return (TDY , TOD , hr , mn , sc, FN)