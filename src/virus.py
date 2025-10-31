def start():
    chnapik_duration = 2*60+10
    
    import time
    timestamp = time.time()


    import os
    import threading
    music = threading.Thread(target=lambda: os.system("start '%USERPROFILE%/Music/youtube_com-watch-dQw4w9WgXcQ.mp3'".replace("/", "\\")))
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


    time_elapsed = time.time() - timestamp
    time.sleep(max(0, chnapik_duration - time_elapsed))

if __name__ == "__main__":
    start()
