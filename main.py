from pytubefix import YouTube
import requests

print("Welcome to YouTube Downloader this service made by Rauf Fathi Govashin."
      " There are 2 services:\n"
      "[1] YouTube video downloader\n"
      "[2] YouTube thumbnail downloader")

a = input("Select Service: ")

if a == "1":
    url = input("Enter YouTube URL: ")
    path = ""
    YouTube(url).streams.get_highest_resolution().download(path)
    print("Video downloaded successfully!")

elif a == "2":
    url = input("Enter YouTube URL: ")
    yt = YouTube(url)

    thumbnail_url = yt.thumbnail_url
    response = requests.get(thumbnail_url)

    with open("thumbnail.jpg", "wb") as f:
        f.write(response.content)

    print("Thumbnail downloaded successfully! (thumbnail.jpg)")

else:
    print("Invalid input!")
