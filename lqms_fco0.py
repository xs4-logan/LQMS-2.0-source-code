#####
# log File Compression and Organization0
# 2022.08.23 Yoshiaki Sato[Technobiz]
#####
import lqms_dt
import os
import zipfile
from operator import itemgetter
from time import sleep

def ST():
    # システムログの処理１
    os.chdir('/mnt/ssd/log/facl/')
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


    # システムログの処理２
    os.chdir('/mnt/ssd/log/error/')
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

