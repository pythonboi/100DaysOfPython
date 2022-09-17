# Import both the OS and YouTube Module
import os
from pytube import YouTube

# Print the current directory of the path
print(os.getcwd())

# Create a variable for raw string of the directory where to store the file/video
download_Dir = r"C:\Users\admin\Downloads"

# Check if the current directory is the directory to download the file

if os.getcwd() != download_Dir:
    # Change the directory to where the file/video will be downloaded to
    os.chdir(download_Dir)
    print(os.getcwd())

# Create variable for the URL link
urlLink = input("Please paste your URL link here: ")

# Instantiate the YouTube class to get the URL link
y = YouTube(urlLink)

# Create a variable to for the highest resolution
dwn = y.streams.get_highest_resolution()

# Download the video/file
dwn.download()

# Print the message of the successful download
print(f"{dwn.title} download successfully and completed")
