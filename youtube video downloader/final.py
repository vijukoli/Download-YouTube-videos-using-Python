
from pytube import YouTube

url = input("Enter Your URl")

video = YouTube(url)

print("**********Video Title*************")

print(video.title)

print("*********Tumbnail Image************")

print(video.thumbnail_url)

print("*********Download video**************")

for stream in video.streams: 
 
   print(stream)

my_video = my_video.streams.first()

my_video.download()