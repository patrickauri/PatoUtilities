from pytube import YouTube

# Ask user which video to download from
videofound = False

print("*************************************")
print("*                                   *")
print("*         YouTube Video             *")
print("*        Audio Downloader           *")
print("*                                   *")
print("*            script by              *")
print("*           Patrick Auri            *")
print("*                                   *")
print("*************************************")
print("")

while videofound != True:
    video = input("Please enter a URL to download from: ")
    try:
        yt = YouTube(video)
        videofound = True
    except:
        print ("Error: Couldn't find a YouTube video at " + video)


# Ask user whether to download video or just audio
choice = ""
while choice == "":
    choiceinput = input("Do you want to download the video or only the audio? (A) (V): ").capitalize()
    if choiceinput == 'A':
        choice = 'A'
    if choiceinput == 'V':
        choice = 'V'

if choice == 'A':
    # Download Audio Only
    print('Downloading: ' + yt.title + ' by ' + yt.author + " (Audio Only)")
    yt.streams.get_audio_only().download()
    print(yt.title + " Successfully downloaded!")
if choice == 'V':
    # Download Video
    print('Downloading: ' + yt.title + ' by ' + yt.author)
    yt.streams.get_highest_resolution().download()
    print(yt.title + " Successfully downloaded!")


