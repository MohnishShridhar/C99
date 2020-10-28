import os
import shutil

#Write the name of the directory here which needs to be sorted
path= input("Enter the name of the directory to be sorted: ")

#This will create a properly organised list with all the file names in the directory
list_of_files= os.listdir(path)

#This will go through each and every file
for file in list_of_files:
    name, ext=os.path.splitext(file)

    #This is going to store the extension type
    ext=ext[1:]

    #This forces the next iteration if it is a directory
    if ext=='':
        continue

    #this will move the file to the directory where the name is 'ext already exists'
    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file, path+'/'+ext+'/'+file)

    #this will create a new directory if the directory doesnt exist
    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file, path+'/'+ext+'/'+file)
