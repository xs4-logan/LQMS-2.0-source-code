#####
# log File Compression and Organization1
#      for EBN Logfile
# 2022.08.23 Yoshiaki Sato[Technobiz]
#####
import lqms_dt
import os
import zipfile
from operator import itemgetter
from time import sleep

# ＥＢＮログの処理
def ST1(MD):
    if (MD == '0001'):
        FILENAME = '/mnt/ssd/log/mda1/MDA1_'
    elif (MD == '0002'):
        FILENAME = '/mnt/ssd/log/mda2/MDA2_'
    elif (MD == '0003'):
        FILENAME = '/mnt/ssd/log/mdb1/MDB1_'
    elif (MD == '0004'):
        FILENAME = '/mnt/ssd/log/mdb2/MDB2_'
    elif (MD == '0005'):
        FILENAME = '/mnt/ssd/log/mdc1/MDC1_'
    elif (MD == '0006'):
        FILENAME = '/mnt/ssd/log/mdc2/MDC2_'
    elif (MD == '0007'):
        FILENAME = '/mnt/ssd/log/mde1/MDE1_'
    elif (MD == '0008'):
        FILENAME = '/mnt/ssd/log/mde2/MDE2_'
    elif (MD == '0009'):
        FILENAME = '/mnt/ssd/log/mdf1/MDF1_'
    elif (MD == '0010'):
        FILENAME = '/mnt/ssd/log/mdf2/MDF2_'

    F = os.path.getsize( FILENAME )
    if ( F > 1024000):
        Counter = len([f for f in os.listdir(dir) if f.endswith('.zip') and os.path.isfile(os.path.join(dir, f))])
        with zipfile.ZipFile( FILENAME + '.' + str(Counter) + ".zip",
                        "w",
                        compression=zipfile.ZIP_DEFLATED,
                        compresslevel=-1    ) as zf:
            zf.write( FILENAME + '.log')

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

def ST2(MD):
    if (MD == '0001'):
        FILENAME = '/mnt/ssd/log/mda1/MDA1_'
    elif (MD == '0002'):
        FILENAME = '/mnt/ssd/log/mda2/MDA2_'
    elif (MD == '0003'):
        FILENAME = '/mnt/ssd/log/mdb1/MDB1_'
    elif (MD == '0004'):
        FILENAME = '/mnt/ssd/log/mdb2/MDB2_'
    elif (MD == '0005'):
        FILENAME = '/mnt/ssd/log/mdc1/MDC1_'
    elif (MD == '0006'):
        FILENAME = '/mnt/ssd/log/mdc2/MDC2_'
    elif (MD == '0007'):
        FILENAME = '/mnt/ssd/log/mde1/MDE1_'
    elif (MD == '0008'):
        FILENAME = '/mnt/ssd/log/mde2/MDE2_'
    elif (MD == '0009'):
        FILENAME = '/mnt/ssd/log/mdf1/MDF1_'
    elif (MD == '0010'):
        FILENAME = '/mnt/ssd/log/mdf2/MDF2_'

    F = os.path.getsize( FILENAME )
    if ( F > 1024000):
        Counter = len([f for f in os.listdir(dir) if f.endswith('.zip') and os.path.isfile(os.path.join(dir, f))])
        with zipfile.ZipFile( FILENAME + '.' + str(Counter) + ".zip",
                        "w",
                        compression=zipfile.ZIP_DEFLATED,
                        compresslevel=-1    ) as zf:
            zf.write( FILENAME + '.log')

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



