"""
YouTube Video/Audio Downloader :

This Python script allows users to download YouTube videos in various formats, including both video and audio.
It utilizes the pytube library to fetch video streams from a given YouTube link and provides options to download 
based on available formats.

Libraries Used:
- pytube: Python library for downloading YouTube videos.

Usage:

1. Ensure Python is installed on your system. 
2. Install the pytube library:
        open your terminal ----pip install pytube

"""

from pytube import YouTube

#...........youtube video/audio Downloader .............
try:
    link = input("Enter or paste your YouTube video link: ")
    youtube_1 = YouTube(link)
    
    # List all available formats
    videos = youtube_1.streams.all()
    vid = list(enumerate(videos))
    for i in vid:
        print(i)
    
    strm = int(input("Enter the Sl. No. of the format you want to download: "))
    videos[strm].download()
    print("Your file downloaded successfully.")
    
except Exception as e:
    print(f"An error occurred: {str(e)}")
