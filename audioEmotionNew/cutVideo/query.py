# encoding:UTF-8
import re
import os
import subprocess
from os import listdir

def fileQuery(viddir,anndir):
    vidlist = listdir(viddir)
    cnt = 0
    for vid in vidlist:
        if vid.split('.')[-1] != 'MTS' and vid.split('.')[-1] != 'MP4':
            continue
        else:
            cnt += 1
            print(vid)
            annlist = listdir(anndir)
            for ann in annlist:
                if vid[:-4] == ann[:-6]:
                    print(vid[:-4])
    print(cnt)

if __name__ == '__main__':
    VID_DIR = 'E:\\morindaz\\SYM\\'
    ANNOT_DIR ='C:\\Users\\Mypc\\Desktop\\morindaz\\audioEmotionNew\\cutVideo\\front0807\\'
    os.chdir(VID_DIR)
    fileQuery(VID_DIR,ANNOT_DIR)
