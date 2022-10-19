#####
# log File Compression and Organization
# 2022.08.23 Yoshiaki Sato[Technobiz]
#####
import lqms_dt
import os
import zipfile

import glob

dir = '/mnt/ssd/log/mdx1/ebn/'
F = os.path.getsize( dir + 'MDX1_EBN.log' )

if ( F > 1024000):
    Counter = len([f for f in os.listdir(dir) if f.endswith('.zip') and os.path.isfile(os.path.join(dir, f))])
    with zipfile.ZipFile( dir + "MDX1_EBN." + str(Counter) + ".zip",
                     "w",
                     compression=zipfile.ZIP_DEFLATED,
                     compresslevel=-1    ) as zf:
        zf.write(dir + "MDX1_EBN.log")
