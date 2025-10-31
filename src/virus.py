def start():
    chnapik_duration = 2*60+10
    
    import time
    timestamp = time.time()


    import os
    from multiprocessing import Process
    def music_func():
      os.system("start %USERPROFILE%/Music/youtube_com-watch-dQw4w9WgXcQ.mp3")
      time.sleep(chnapik_duration) 
    music = Process(target=music_func)
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

if __name__ == "__main__":
    start()
