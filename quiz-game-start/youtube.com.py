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
        print(f"{os.path.join(downloadPath, folder)}")

    remFile = input("What folder/file you want to delete:? ").lower()
    for check in myDir:
        if remFile == check:
            ans = input(f"Are you sure you want to delete the {remFile}: 'y' for yes and 'n' no ").lower()
            if ans == 'y':
                os.rmdir(remFile)
                print(f"{remFile} directory successful deleted")

            elif ans == 'n':

                print(f"{remFile} directory not deleted")


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
