import subprocess

# Ask for the YouTube URL
url = input('Enter the share URL, excluding everything after the question mark (https://youtu.be/...):\n> ')

# Run command to rip and download
result = subprocess.run([
    "yt-dlp", 
    "-x", 
    "--audio-format", "mp3", 
    "--extractor-args", "youtube:player_client=default,-android_sdkless", 
    url
], text=True)