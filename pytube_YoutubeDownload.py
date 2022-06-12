import os
from pytube import YouTube

print(os.getcwd())

download_Dir = r"C:\Users\admin\Downloads"

# dirct = input("Please put the directory here: ")

if os.getcwd() != download_Dir:

    os.chdir(download_Dir)
    print(os.getcwd())

urlLink = input("Please paste your URL link here: ")

y = YouTube(urlLink)

adapt = y.streams.filter(adaptive=True)
# print(adapt)

dwn = y.streams.get_highest_resolution()

dwn.download()

print(f"{dwn.title} download successfully and completed")
