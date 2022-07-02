import os
import re
import shutil

# from CreateFolder import Folder

currentDirectory = os.getcwd()
print(currentDirectory)

chgeDirectory = input("Please Copy the directory you want to change to: ")

folderSide = []
fileSide = []
getfileList = ' '
newfileExt = []
newSet = set()
fullPath = ''
getFileName = ''

if currentDirectory != chgeDirectory:
    os.chdir(chgeDirectory)
    print(os.getcwd())

    qNewFolder = input("Do you want to create a new Folder: (Y/N) ").lower()
    if qNewFolder == 'y':

        newFolder = input("Please Enter the name of the new Folder: ").title()

        try:
            os.mkdir(newFolder)
            print(f"{newFolder} created successful")

        except FileExistsError:
            print(f"{newFolder} already exists")

    else:

        if os.path.exists(chgeDirectory):

            lstDir = os.listdir(os.getcwd())
            for v in lstDir:
                getfileList += v

            # Print the total number of existing directory

            print(len(lstDir), f"items in {chgeDirectory}")

        for check in lstDir:
            if os.path.isdir(check):
                folderSide.append(check)

            else:
                fileSide.append(check)

        # Differentiate the file from the extension

        for f in fileSide:

            if os.path.isfile(f):
                splitFileExt = os.path.splitext(f)

                fileName = splitFileExt[0]
                fileExt = splitFileExt[1]

                # Using regular Expression to separate the file extension from the file name

                for ext in fileExt:
                    regExt = re.search(r'\.(\w+)', fileExt)
                newfileExt.append(regExt.group(1))

        # Making the extension to be unique in the file

        for uni in newfileExt:
            newSet.add(uni.lower())

        # Creating the Folder from the file extension

        for uniqFile in newSet:
            try:
                if uniqFile in newSet:
                    os.mkdir(uniqFile)  # .title())
                    print(f"{uniqFile} created successfully")
            except FileExistsError:
                print(f"{uniqFile} folder already exists ")

        for vryFile in lstDir:

            if os.path.isfile(vryFile):
                fullPath = os.path.join(chgeDirectory, vryFile)

            for chkFolder in folderSide:

                getExistingDir = os.path.join(chgeDirectory, chkFolder)

                try:

                    for word in newSet:

                        if word in fullPath and word in getExistingDir:
                            print(shutil.move(fullPath, getExistingDir))

                except shutil.Error:
                    print(f"{vryFile} file already exits")

# A new code begins from here. The code above works well and adding new code below

# Checked if the file already exits in a folder


for fileCheck in lstDir:
    if os.path.isfile(fileCheck):
        getFileName += fileCheck

    for name in lstDir:
        dirPath = os.path.join(chgeDirectory, name)
        for roots, dirs, files in os.walk(dirPath):
            if getFileName in files:

                print(f"{getFileName} already exits in ", os.path.abspath(dirPath))
                print(f"Removing {getFileName} in ", os.getcwd())
                os.remove(getFileName)

