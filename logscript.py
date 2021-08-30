#!/bin/python3

import shutil # for copyfile
import os   # for getfiles and check size
import sys # for cli arguments

#logscript.py mylog.txt 10 5

if(len(sys.argv) < 4):
    print("You lose arguments? try again")
    exit(1)

file_name = sys.argv[1]
limit_size = int(sys.argv[2])
logsnumber = int(sys.argv[3])

if(os.path.isfile(file_name) == True):
    logfile_size = os.stat(file_name).st_size
    logfile_size = logfile_size / 1024

    if(logfile_size >= limit_size):
        if(logsnumber > 0 ):
            for current_file_num in range(logsnumber, 1, -1):
                src = file_name +"_" + str(current_file_num-1)
                dst = file_name +"_" + str(current_file_num)
                if(os.path.isfile(src) == True):
                    shutil.copy(src, dst)
                    print("Copied: " + src + " to " + dst)
            shutil.copyfile(file_name, file_name + "_1")
            print(" Copied: " + file_name + "  to" + file_name + "_1")
        myfile = open(file_name, 'w')
        myfile.close()







