import os
import shutil
import subprocess
from datetime import date

from LogAllFiles import LogAllFiles  # ← your function


# ===== CONFIG =====
LIVE_REPO = "C:/Python"
ARCHIVE_REPO = "C:/PythonGrave"  # Repo B (ABSOLUTE PATH)
TRACK_FILE = "C:/Python/Projects/GitCommitter/ListOfFiles.txt"
# ==================


def run_git(cmd, cwd):
    subprocess.run(cmd, cwd=cwd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)


def read_old_files():
    if not os.path.exists(TRACK_FILE):
        return set()
    with open(TRACK_FILE, "r", encoding="utf-8") as f:
        return set(line.strip() for line in f if line.strip())


def write_new_files(files):
    os.makedirs(os.path.dirname(TRACK_FILE), exist_ok=True)
    with open(TRACK_FILE, "w", encoding="utf-8") as f:
        for file in sorted(files):
            f.write(file + "\n")


def archive_deleted_files(deleted):
    for path in deleted:
        src = path.lstrip("./")
        dst = os.path.join(ARCHIVE_REPO, src)

        if os.path.exists(src):
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(src, dst)


def main():
    old_files = read_old_files()
    new_files = LogAllFiles()

    deleted_files = old_files - new_files

    # --- Archive deletes ---
    if deleted_files:
        archive_deleted_files(deleted_files)
        msg = f"Automated [{date.today()}] : {len(deleted_files)} deleted files Archived."
        for file in deleted_files:
            run_git(f"git add {file}", ARCHIVE_REPO)
        run_git(f'git commit -m "{msg}"', ARCHIVE_REPO)
        run_git(f'git push', ARCHIVE_REPO)

    # --- Update memory ---
    write_new_files(new_files)

    # --- Commit live repo ---
    live_msg = f"[{date.today()}] Automated Commit."
    for file in new_files:
        run_git(f"git add {file}", LIVE_REPO)
    run_git(f'git commit -m "{live_msg}"', LIVE_REPO)
    run_git(f"git push", LIVE_REPO)


if __name__ == "__main__":
    main()
