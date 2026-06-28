import subprocess

# Ask for the YouTube URL and save path
url = input('Enter the share URL, excluding everything after the question mark (https://youtu.be/...):\n> ')
save_path = input('Enter the complete download path, and finish with the filename:\n> ')

# Run command to rip and download
result = subprocess.run([
    "yt-dlp", 
    "-x", 
    "-o", save_path,
    "--audio-format", "mp3", 
    "--extractor-args", "youtube:player_client=default,-android_sdkless", 
    url
], text=True)