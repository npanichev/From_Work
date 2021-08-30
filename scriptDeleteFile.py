import os
import time

DAYS = 5
FOLDERS = ["C:\\Users\\n.panichev\\Desktop\\Лента\\тк-041"]
TOTAL_DELETED_SIZE = 0
TOTAL_DELETED_FILE = 0
TOTAL_DELETED_DIRS = 0

nowTime = time.time()
ageTime = nowTime - 60*60*24*DAYS

def delete_old_files(folder):
    global TOTAL_DELETED_FILE
    global TOTAL_DELETED_SIZE
    for path , dirs, files in os.walk(folder):
        for file in files:
            fileName = os.path.join(path, file)
            fileTime = os.path.getmtime(fileName)
            if fileTime < ageTime:
                sizeFile = os.path.getsize(fileName)
                TOTAL_DELETED_SIZE += sizeFile
                TOTAL_DELETED_FILE += 1
                print("Deleting file: " + str(fileName))
                os.remove(fileName)
def delete_empty_dir(folder):
    global TOTAL_DELETED_DIRS
    for path, dirs, files in os.walk(folder):
        if (not dirs) and (not files):
            TOTAL_DELETED_DIRS += 1
            print("Deleting EMPTY Dir: " + str(path))
            os.rmdir(path)


#----------MAIN----------------------
starttime = time.asctime()

for folder in FOLDERS:
    delete_old_files(folder)
    delete_empty_dir(folder)


finishtime = time.asctime()

print("-------------------------------")
print("START TIME: " + str(starttime))
print("Total Deleted Size: " + str(TOTAL_DELETED_SIZE/1024/1024) + "Mb")
print("Total Deleted files: " + str (TOTAL_DELETED_FILE))
print("Total Deleted Empty folders: " + str(TOTAL_DELETED_DIRS))
print("FINISH TIME: " + str(finishtime))

print("---------EOF-----------")

