import pytube

# Paste the YouTube video URL here
url = input("Enter url video")

# Create a PyTube object with the YouTube video URL
video = pytube.YouTube(url)

# Get the highest resolution video stream
stream = video.streams.get_highest_resolution()

# Download the video to your computer
stream.download()