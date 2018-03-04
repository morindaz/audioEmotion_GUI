# encoding:UTF-8
import re
import os
import subprocess
from os import listdir

FNULL = open(os.devnull, 'w')
def videoCompress(outdir):
    target_format = '.mp4'
    filelist = listdir(os.getcwd())
    #print filelist
    for item in filelist:
        p=re.compile(r'(.*)\.(MTS|mp4)', re.I)
        files=p.findall(item)
        #print 11111
        print(files)
        if len(files)>0:
            if os.path.isfile(item):
                videoname = files[0][0]
                suffix = files[0][1]
                videoname = re.sub(r'\W+','_',videoname)
                print(videoname)
                if (suffix == 'MTS'or suffix == 'MP4'or suffix == 'mp4') and videoname[0] == '_':
                    os.rename('.\\'+item, '.\\_'+videoname+'.'+suffix)
if __name__ == '__main__':
    ORIGIN_VIDEODIR = 'E:\\morindaz\\SYM'
    NEW_VIDEODIR ='E:\\morindaz\\SYM'
    os.chdir(ORIGIN_VIDEODIR)
    videoCompress(NEW_VIDEODIR)
