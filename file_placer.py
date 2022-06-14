import shutil, re, os
# from CreateFolder import Folder
from pytube import YouTube

currentDirectory = os.getcwd()
print(currentDirectory)

chgeDirectory = input("Please Copy the directory you want to change to: ")

folderSide = []
fileSide = []
getfileList = ' '
newfileExt = []
newSet = set()
fullPath = ''
# getExistingDir = ''

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
                print(f"{uniqFile} already exists ")

        for vryFile in lstDir:
            # print(vryFile)

            if os.path.isfile(vryFile):
                fullPath = os.path.join(chgeDirectory, vryFile)
                # print(f"{fullPath},  read this first")

            for chkFolder in folderSide:
                # print(chkFolder)
                getExistingDir = os.path.join(chgeDirectory, chkFolder)

                try:

                    for word in newSet:

                        if word in fullPath and word in getExistingDir:
                            print(shutil.move(fullPath, getExistingDir))

                        elif os.path.isfile(vryFile) and vryFile in getExistingDir:
                            print(f"{vryFile}, I am printing this")

                        # elif vryFile in getExistingDir:
                        #     print(f"{vryFile} already exists in directory")
                except shutil.Error:
                    print("file already exits")

        # print("No folder created")

