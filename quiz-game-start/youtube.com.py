from pytube import YouTube

import os

print(f"Here is the current directory from the IDE environment: {os.getcwd()}")

thePath = os.getcwd()

downloadPath = "/Users/erudite/Downloads"

if thePath != downloadPath:
    os.chdir(downloadPath)
    print(f"Changing to the Download directory from the laptop directory: {os.getcwd()}")
    # print(os.listdir())
    folder = input("What folder you looking for:? ").lower()

    print(os.getcwd())
    myPath = os.getcwd()
    myDir = os.listdir(myPath)

    # print(myDir)

    if os.path.isdir(folder):
        print(f"{folder} already exist")

    else:
        print(f"{folder} does not exits...Creating {folder} folder on {os.getcwd()}.")
        os.mkdir(folder)
        # print(f"{os.path.join(downloadPath, folder)}")

    # To delete folder or not

    choice = input("Do you have any folder you want to delete:?, 'y' for Yes and 'n' No: ").lower()
    if choice == 'y':

        knowFolderName = input(
            "Do you know the name of folder you want to delete:? 'y' for Yes and 'n' for No, 'm' for change to the new folder directory ").lower()
        if knowFolderName == 'y':
            print(
                f"Please note this action is irreversible, the following action will delete the {folder} folder in this directory {os.getcwd()} ")
            folderName = input("Type in the name of folder you want to delete:? ").lower()

            if folderName in os.listdir(os.getcwd()):
                # os.removedirs(folderName)
                os.rmdir(folderName)
                print(f"{folderName} successfully deleted/remove from {os.getcwd()} directory.")

        elif knowFolderName == 'n':

            print(f"Below are the directories/folders in the {os.getcwd()}")
            for _ in os.listdir(os.getcwd()):
                if os.path.isdir(os.path.join(downloadPath, _)):
                    print(_)

            remFile = input("Type the name of folder you want to delete:? ").lower()

            for check in myDir:
                if remFile in check:
                    ans = input(f"Are you sure you want to delete {remFile} folder: 'y' for yes and 'n' no ").lower()
                    if ans == 'y':
                        os.rmdir(remFile)
                        print(f"{remFile} folder/directory successful deleted")

                    elif ans == 'n':

                        print(f"{remFile} directory not deleted")

                    else:
                        print("Please choose 'y' yes or 'n' no")

        elif knowFolderName == 'm':

            os.path.isdir(folder)
            print("Changing to the new folder directory")
            os.chdir(os.path.join(downloadPath, folder))
            print(os.getcwd())

        else:
            print("no options selected")

    elif choice == 'n':
        print("No folder to delete")
        os.path.isdir(folder)
        print("Changing to the new folder directory")
        os.chdir(os.path.join(downloadPath, folder))
        print(os.getcwd())

        urlLink = input("Please type or paste the 'URL' here: ").lower()

        youtube = YouTube(urlLink)

        youtube.streams.filter(adaptive=True)
        Resolution = youtube.streams.get_highest_resolution()

        print(Resolution)



    # if os.path.isdir(folder):
    #     print("Change to the new folder directory")
    #     os.chdir(os.path.join(downloadPath, folder))
    #     print(os.getcwd())

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
