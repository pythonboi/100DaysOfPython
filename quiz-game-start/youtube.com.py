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
    # for name in os.getcwd():
    # print(os.listdir())

    try:

        if folder not in os.getcwd():
            # if folder not in os.getcwd():
            print(f"{folder} does not exit")
            print(f"Creating {folder} directory on {os.getcwd()}")
            os.mkdir(folder)
            print(f"{folder} created successfully")
    except FileExistsError:
        # else:
        print("Folder already exit")
        option = input("Do you want to delete the folder 'y' yes and 'n' no: ").lower()
        if option == 'y':
            os.rmdir(folder)
            print(f"The {folder} folder/directory is now deleted")
        else:
            print("folder kept")
