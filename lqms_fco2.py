#####
# log File Compression and Organization2
#      for EBN Logfile
# 2022.08.23 Yoshiaki Sato[Technobiz]
#####
import lqms_dt
import os
import zipfile
from operator import itemgetter
from time import sleep

# ＥＢＮログの処理
def ST(MD):
    if (MD == '192.168.1.11'):
        os.chdir('/mnt/ssd/log/mda1/eth/')
    elif (MD == '192.168.1.12'):
        os.chdir('/mnt/ssd/log/mda2/eth/')
    elif (MD == '192.168.1.21'):
        os.chdir('/mnt/ssd/log/mdb1/eth/')
    elif (MD == '192.168.1.22'):
        os.chdir('/mnt/ssd/log/mdb2/eth/')
    elif (MD == '192.168.1.23'):
        os.chdir('/mnt/ssd/log/mdc1/eth/')
    elif (MD == '192.168.1.24'):
        os.chdir('/mnt/ssd/log/mdc2/eth/')
    elif (MD == '192.168.1.25'):
        os.chdir('/mnt/ssd/log/mde1/eth/')
    elif (MD == '192.168.1.26'):
        os.chdir('/mnt/ssd/log/mde2/eth/')
    elif (MD == '192.168.1.13'):
        os.chdir('/mnt/ssd/log/mdf1/eth/')
    elif (MD == '192.168.1.14'):
        os.chdir('/mnt/ssd/log/mdf2/eth/')

    # rtcログの処理１
    filelists = []
    for file in os.listdir():
        base, ext = os.path.splitext(file)
        if ext == '.log':
            filelists.append([file, os.path.getctime(file)])
    filelists.sort(key=itemgetter(1), reverse=True)
    MAX_CNT = 7
    for i,file in enumerate(filelists):
        if i > MAX_CNT - 1:
            name = os.path.splitext(os.path.basename(file[0]))[0] + '.zip'
            with zipfile.ZipFile(name, "w", zipfile.ZIP_DEFLATED) as zf:
                zf.write(file[0]) 
                sleep(0.1)
            os.remove(file[0])

    # zipファイルの削除
    filelists = []
    for file in os.listdir():
        base, ext = os.path.splitext(file)
        if ext == '.zip':
            filelists.append([file, os.path.getctime(file)])
    filelists.sort(key=itemgetter(0), reverse=True)
    MAX_CNT = 30
    for i,file in enumerate(filelists):
        if i > MAX_CNT - 1:
            name = os.path.splitext(os.path.basename(file[0]))[0] + '.zip'
            os.remove(file[0])

    if (MD == '192.168.1.11'):
        os.chdir('/mnt/ssd/log/mda1/rtc/')
    elif (MD == '192.168.1.12'):
        os.chdir('/mnt/ssd/log/mda2/rtc/')
    elif (MD == '192.168.1.21'):
        os.chdir('/mnt/ssd/log/mdb1/rtc/')
    elif (MD == '192.168.1.22'):
        os.chdir('/mnt/ssd/log/mdb2/rtc/')
    elif (MD == '192.168.1.23'):
        os.chdir('/mnt/ssd/log/mdc1/rtc/')
    elif (MD == '192.168.1.24'):
        os.chdir('/mnt/ssd/log/mdc2/rtc/')
    elif (MD == '192.168.1.25'):
        os.chdir('/mnt/ssd/log/mde1/rtc/')
    elif (MD == '192.168.1.26'):
        os.chdir('/mnt/ssd/log/mde2/rtc/')
    elif (MD == '192.168.1.13'):
        os.chdir('/mnt/ssd/log/mdf1/rtc/')
    elif (MD == '192.168.1.14'):
        os.chdir('/mnt/ssd/log/mdf2/rtc/')

    # システムログの処理２
    filelists = []
    for file in os.listdir():
        base, ext = os.path.splitext(file)
        if ext == '.log':
            filelists.append([file, os.path.getctime(file)])
    filelists.sort(key=itemgetter(1), reverse=True)
    MAX_CNT = 7
    for i,file in enumerate(filelists):
        if i > MAX_CNT - 1:
            name = os.path.splitext(os.path.basename(file[0]))[0] + '.zip'
            with zipfile.ZipFile(name, "w", zipfile.ZIP_DEFLATED) as zf:
                zf.write(file[0]) 
                sleep(0.1)
            os.remove(file[0])

    # zipファイルの削除
    filelists = []
    for file in os.listdir():
        base, ext = os.path.splitext(file)
        if ext == '.zip':
            filelists.append([file, os.path.getctime(file)])
    filelists.sort(key=itemgetter(0), reverse=True)
    MAX_CNT = 30
    for i,file in enumerate(filelists):
        if i > MAX_CNT - 1:
            name = os.path.splitext(os.path.basename(file[0]))[0] + '.zip'
            os.remove(file[0])

