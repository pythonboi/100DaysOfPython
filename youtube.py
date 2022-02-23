from pytube import YouTube

import os

print(f"Here is the current directory from the IDE environment: {os.getcwd()}")

thePath = os.getcwd()

# downloadPath = "/Users/erudite/Downloads"

PcPath = r"C:\Users\admin\Downloads"

if thePath != PcPath:
    os.chdir(PcPath)
    print(f"Changing to the Download directory from the laptop directory: {os.getcwd()}")
    # print(os.listdir())
    folder = input("What folder you looking for:? ").title()

    print(os.getcwd())
    myPath = os.getcwd()
    myDir = os.listdir(myPath)

    # print(myDir)

    if os.path.isdir(folder):
        print(f"{folder} already exist")

    else:
        print(f"{folder} does not exits...Creating {folder} folder on {os.getcwd()}.")
        os.mkdir(folder)
        # print(f"{os.path.join(PcPath, folder)}")

    # To delete folder or not

    choice = input("Do you have any folder you want to delete:?, 'y' for Yes and 'n' No: ").lower()
    if choice == 'y':

        knowFolderName = input(
            "Do you know the name of folder you want to delete:? 'y' for Yes and 'n' for No,"
            " 'm' for change to the new folder directory ").lower()
        if knowFolderName == 'y':
            print(
                f"Please note this action is irreversible, the following action will delete the {folder} folder in this directory {os.getcwd()} ")
            folderName = input("Type in the name of folder you want to delete:? ").lower()
            print(os.listdir)

            if folderName in os.listdir(os.getcwd()):
                # os.removedirs(folderName)
                os.rmdir(folderName)
                print(f"{folderName} successfully deleted/remove from {os.getcwd()} directory.")

        elif knowFolderName == 'n':

            print(f"Below are the directories/folders in the {os.getcwd()}")
            for _ in os.listdir(os.getcwd()):
                if os.path.isdir(os.path.join(PcPath, _)):
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
            os.chdir(os.path.join(PcPath, folder))
            print(os.getcwd())

        else:
            print("no options selected")

    elif choice == 'n':
        print("No folder to delete")
        os.path.isdir(folder)
        print("Changing to the new folder directory")
        os.chdir(os.path.join(PcPath, folder))
        print(os.getcwd())

        urlLink = input("Please type or paste the 'URL' here: ")

        youtube = YouTube(urlLink)

        fl = youtube.streams.filter(adaptive=True)
        Resolution = youtube.streams.get_highest_resolution()

        # print(fl)

        for n in fl:
            high = 0
            getStream = n
            for mn in getStream:
                if mn 
            print(getStream)


