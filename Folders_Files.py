import os, shutil

path = r"C:\Users\admin"

# subDirectory = input("Please enter the directory you want to create the new folder: ").title().lower()

# Check if users want to create a new directory on different directory

print(f"You are currently on {os.getcwd()}")

option = input("Do you want to create your new folder on existing folder:? 'y' for Yes and 'n' No,"
               " 'l' to list all folders in the current directory ").lower()

if option == 'y':

    try:

        selectFolder = input("Which directory do you want to create your new folder on:? ").title()

        newDir = os.path.join(path, selectFolder)

        os.chdir(newDir)
        newFolder = input("Enter the name of your new folder:? ").title()
        os.mkdir(newFolder)
        print(f"{newFolder} created successful.")
        print(f"You are now in {os.getcwd()} directory")

    except FileExistsError:
        print("Folder already exists")

        # if os.path.isdir(newFolder):
        #     createFile = input(f"Do you have a file you want to create in this {os.getcwd()} directory 'y' Yes and 'n' No ").title()
        #     if createFile == 'y':
        #         with open

        fCopy = input("Do you want to copy any file to the new folder:? 'y' Yes and 'n' No ").lower()

        os.chdir(os.path.join(newDir, newFolder))

        print(os.getcwd())

        if fCopy == 'y':
            source = input(r"Please copy and paste your source directory here: ")
            target = input(r"Please copy and paste your target directory here ")

            try:

                shutil.copy(source, target)

                if os.path.isfile(target):
                    filePrefix = os.path.basename(target)

                    print(f"{filePrefix} copied successful")
            except FileExistsError:
                print(f"{filePrefix} already exits")

        elif fCopy == 'n':
            print("no file to copy")

# if os.getcwd() == path:
#     newDir = os.path.join(path, subDirectory)
#     os.chdir(newDir)
