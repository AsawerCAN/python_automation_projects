from pytube import YouTube
import os
try:
    # Ask the user to input the YouTube URL
    url = input("Enter Youtube Url: ")
    
    yt = YouTube(url)
    
    print("Title:", yt.title)
    print("Views:", yt.views)

    # Get the highest resolution stream
    yd = yt.streams.get_highest_resolution()
    
    # Download the video to the current directory
    yd.download('') # enter path to where video is downloaded
    
    print("Download complete.")
except Exception as e:
    print("An error occurred:", str(e))