from pytube import YouTube
import time

#time
items = list(range(0, 57))
l = len(items)

#link question
linkquestion = input("Enter the link:  ")
yt = YouTube(linkquestion)

#details
print('---------------------------------------------------------------------------------')
print("Title: ",yt.title)
print("Views: ",yt.views)
print("Rating: ",yt.rating)
print('---------------------------------------------------------------------------------')

#Getting highest res.
ys = yt.streams.get_highest_resolution()

print('The download starts.')
time.sleep(1)
print('The download starts..')
time.sleep(1)
print('the downloads starts...')
time.sleep(1)
ys.download()
print('Your video is downloaded!')