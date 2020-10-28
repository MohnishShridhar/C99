import os
import shutil

source=input("Enter source folder name: ")
destination=input("Enter destination forlder name: ")

source=source+'/'
destination=destination+'/'

list_of_files=os.listdir(source)

for file in list_of_files:
    shutil.copy((source+file), destination)