import os
print os.environ

def set():
    mingw_path = 'C:\\Program Files\\mingw-w64\\x86_64-6.3.0-posix-seh-rt_v5-rev1\\mingw64\\bin'
    os.environ['PATH'] = mingw_path + ';' + os.environ['PATH']
set()
print os.environ
# import xgboost