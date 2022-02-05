from pytube import YouTube

import os

print(os.getcwd())

thePath = os.getcwd()

downloadPath = "/Users/erudite/Downloads"

if thePath != downloadPath:
    os.chdir(downloadPath)
    print(os.getcwd())
    # print(os.listdir())
    folder = input("What folder you looking for:? ").lower()

    print(os.getcwd())
    myPath = os.getcwd()
    myDir = os.listdir(myPath)

    # print(myDir)

    if os.path.isdir(folder):
        print(f"{folder} already exist")

    else:
        os.mkdir(folder)
        # print(f"{os.path.join(downloadPath, folder)}")

    knowFolderName = input("Do you know the name of folder you want to delete:? 'y' for Yes and 'n' for No ").lower()
    if knowFolderName == 'y':
        folderName = input("Type in the name of folder you want to delete:?").lower()
        print("Please note the action is irreversible, the following action will delete all folder in this directory ")
        if folderName in os.listdir(os.getcwd()):
            # os.removedirs(folderName)
            os.rmdir(folderName)

    elif knowFolderName == 'n':
        for _ in os.listdir(os.getcwd()):
            if os.path.isdir(os.path.join(downloadPath, _)):
                print(_)
    else:
        print("no options selected")

    # print(os.listdir(os.getcwd()))

    remFile = input("Type the name of folder you want to delete:? ").lower()
    for check in myDir:
        if remFile == check:
            ans = input(f"Are you sure you want to delete the {remFile}: 'y' for yes and 'n' no ").lower()
            if ans == 'y':
                os.rmdir(remFile)
                print(f"{remFile} directory successful deleted")

            elif ans == 'n':

                print(f"{remFile} directory not deleted")

            else:
                print("Please choose 'y' yes or 'n' no")

    if os.path.isdir(folder):
        os.chdir(os.path.join(downloadPath, folder))
        print(os.getcwd())



    # fullDir = os.path.join(downloadPath, folder)
    # print(fullDir)

    # print(myDir)
    # for chckFile in myDir:
    #     try:
    #         if folder not in chckFile:
    #             os.mkdir(f"{folder}")
    #             print(f"{folder} created successful")
    #
    #
    #     except FileExistsError:
    #         print(f"{folder} already exits")
    #         # if folder not in os.getcwd():
    #         # print(f"{folder} does not exit")
    #         # print(f"Creating {folder} directory on {os.getcwd()}")
    #         # os.mkdir(folder)
    #         # print(f"{folder} created successfully")
    #     # except FileExistsError:
    #
    #     # # else:
    #     #     print("Folder already exit")
    # # option = input("Do you want to delete the folder 'y' yes and 'n' no: ").lower()
    # #     if option == 'y':
    # #         os.rmdir(folder)
    # #         print(f"The {folder} folder/directory is now deleted")
    # #     else:
    # #         print("folder kept")
