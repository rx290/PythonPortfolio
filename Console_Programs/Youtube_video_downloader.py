# Install pytube for this program to run
# pip install pytube
# I won't be creating a requirement file for small dependencies.

from pytube import YouTube

# fetching youtube link
video_link = input("Please copy paste your video url here: ")

# parsing youtube link
y_t = YouTube(video_link)
y_t.streams.first().download(filename="Download sample")
