import os
from pytube import YouTube

dirct = input("Please put the directory here: ")

if os.getcwd() != dirct:

    os.chdir(dirct)
    print(os.getcwd())

urlLink = input("Please paste your URL link here: ")

y = YouTube(urlLink)

adapt = y.streams.filter(adaptive=True)
print(adapt)

dwn = y.streams.get_highest_resolution()


dwn.download()

print(f"{dwn.title} download successfully and completed")
