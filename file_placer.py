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
fullPath = os.path.join(chgeDirectory, getfileList)
getFilename = []
myAppend = []

dest = os.path.join(chgeDirectory, )
dest1 = os.path.abspath(chgeDirectory)
print(dest, dest1)

print(type(newSet))

if currentDirectory != chgeDirectory:
    os.chdir(chgeDirectory)
    print(os.getcwd())

    qNewFolder = input("Do you want to create a new Folder: (Y/N) ").lower()
    if qNewFolder == 'y':

        newFolder = input("Please Enter the name of the new Folder: ").title()

        if os.path.exists(chgeDirectory):
            # for v in chgeDirectory:
            #     print(v)

            lstDir = os.listdir(os.getcwd())
            for v in lstDir:
                getfileList += v

            # print(getfileList)
            # print(os.path.join(chgeDirectory, getfileList))
            # print(lstDir)
            print(len(lstDir), f"items in {chgeDirectory}")

        for check in lstDir:
            if os.path.isdir(check):
                folderSide.append(check)

            else:
                fileSide.append(check)

        print("Here is folder/directory section below: ")
        print("=======================================================================================================")

        # print(folderSide)
        # print(len(fileSide))
        print(fileSide)

        # Here is printing all the file in the directory
        # print(fileSide)
        # for v in folderSide:
        #     fullPath += os.path.join(chgeDirectory, v)

        if newFolder not in folderSide:
            os.mkdir(newFolder)

            print(f"{newFolder} folder created successful")
        else:
            print(f"{newFolder} folder already exits")
            # exit()

        # if os.path.exists(fullPath):
        #     print(fullPath)
        #     print("Yes")

        # Differentiate the file from the extension

        # Commenting this for issue that needs to be fix

        for f in fileSide:

            if os.path.isfile(f):
                splitFileExt = os.path.splitext(f)

                fileName = splitFileExt[0]
                fileExt = splitFileExt[1]

                # print(splitFileExt)

                # Using regular Expression to separate the file extension from the file name

                for ext in fileExt:
                    regExt = re.search(r'\.(\w+)', fileExt)
                newfileExt.append(regExt.group(1))

        # print(newfileExt)

        # Need to fix the issue above

        # Making the extension to be unique in the file

        for uni in newfileExt:
            newSet.add(uni.lower())

        print(newSet)

        print("Here is the second set side")
        print(len(newSet))

        # Creating the Folder from the file extension

        for uniqFile in newSet:
            try:
                if uniqFile in newSet:
                    os.mkdir(uniqFile)  # .title())
                    print(f"{uniqFile} created successfully")
            except FileExistsError:
                print(f"{uniqFile} already exists ")

    else:
        print("No folder created")

    for vryFile in lstDir:

        if os.path.isfile(vryFile):

            # getfile, getnewFileExt = os.path.splitext(vryFile)
            # getExtFilePath = os.path.join(chgeDirectory, getfile)
            # print(vryFile)
            fullPath = os.path.join(chgeDirectory, vryFile)
            print(fullPath)
            #print(len(fullPath))
            fileName, fileExt = os.path.splitext(vryFile)

            # print(getExtFilePath)

        for chkFolder in folderSide:
                # print(chkFolder)
            getExistingDir = os.path.join(chgeDirectory, chkFolder)

            for word in newSet:
                # print(word)
                if word in fullPath and word in getExistingDir:

                    print(shutil.copy2(fullPath, getExistingDir))


            #print(getExistingDir)

                # fileType = input("Please Enter the file format you want to copy: ").lower()
                #
                # if fullPath.endswith(fileType) and fileType == os.path.isdir(getExistingDir):
                #     shutil.copy2(fullPath, getExistingDir) # and fullPath.endswith(fileExt) == os.path.isdir(chkFolder):

                    # print(fileExt)
                    # shutil.copy(fullPath, getExistingDir)

                # if getExistingDir.endswith(getExtFilePath):
                #     shutil.copy(vryFile, getExistingDir)
                # print(vryFile)
                # pr and chkFolder in getnewFileExt:

                # os.chdir(os.path.join(chgeDirectory, chkFolder))
                # shutil.copy(getfile, getnewFileExt)

                # print(getExistingDir)

    # for vryFile in lstDir:
    #
    #     if os.path.isfile(vryFile):
    #
    #         getfile, getnewFileExt = os.path.splitext(vryFile)
    #         getExtFilePath = os.path.join(chgeDirectory, getfile)
    #         print(getExtFilePath)
    #
    #         for chkFolder in folderSide:
    #             # print(chkFolder)
    #             getExistingDir = os.path.join(chgeDirectory, chkFolder)
    #             # print(getExistingDir)
    #
    #             if getExistingDir.endswith(getExtFilePath):
    #                 shutil.copy(vryFile, getExistingDir)
    #                 # print(vryFile)
    #                 # pr and chkFolder in getnewFileExt:
    #
    #                 # os.chdir(os.path.join(chgeDirectory, chkFolder))
    #                 # shutil.copy(getfile, getnewFileExt)
    #
    #             # print(getExistingDir)

    #     if newGetSet in chkFolder:
    #         shutil.copyfile(getfile, getExistingDir)
    #         # myAppend.append("yes")
    #         # print("yes")
    #
    #     else:
    #         print("no")
    #
    # print(len(myAppend))

    # if newGetSet == chkFolder:
    #     print("yes")
    # else:
    #     print("No")

    # print(os.path.isdir(vryFile))
    # shutil.copyfile(getfile, vryFile)

    # print(getnewFileExt)
    # else:
    #     print("false")

    # for chkFolder in folderSide:
    #     getExistingDir = os.path.join(chgeDirectory, chkFolder)
    #     print(getExistingDir)

# for vryFile in fileSide:
#
#     if vryFile.endswith()
#     if vryFile.endswith('rdp'):
#         print(f"{vryFile}")
#         # shutil.copyfile()
#
#     pass

# urlLink = "https://www.youtube.com/watch?v=n3IYVthup9I"
#
# urlLink2 = "https://www.youtube.com/watch?v=PAMpNhx4maM"

urlLink3 = "https://www.youtube.com/watch?v=isRtFdu8sRs"
#
#
# mvFolder = shutil.move(chgeDirectory, )