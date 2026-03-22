import os, tempfile, shutil
from datetime import date
from git import Repo

ROOT = "C:/Python"
LIVE_REPO_PATH = ROOT
ARCHIVE_REMOTE = "git@github.com:RajKamalDas/PythonGraveyard.git"
LOG_FILE = "Projects/GitCommitter/ListOfFiles.txt"


# ---------- Utils ----------


def should_ignore(path):
    return path.startswith(".") or "/." in path or "-P-" in path


def scan_files():
    files = set()
    for root, _, filenames in os.walk(ROOT):
        for f in filenames:
            full = os.path.join(root, f)
            rel = os.path.relpath(full, ROOT).replace("\\", "/")
            if not should_ignore(rel):
                files.add(rel)
    return files


def read_old():
    if not os.path.exists(LOG_FILE):
        return set()
    with open(LOG_FILE) as f:
        return set(line.strip() for line in f)


def write_new(files):
    with open(LOG_FILE, "w") as f:
        for file in sorted(files):
            f.write(file + "\n")


def safe_delete(path):
    import time

    for _ in range(5):
        try:
            shutil.rmtree(path)
            return
        except PermissionError:
            time.sleep(0.5)


# ---------- Archive Logic ----------


def archive_deleted(repoA, deleted_files):
    if not deleted_files:
        return

    commit = repoA.head.commit
    temp_dir = tempfile.mkdtemp()

    try:
        repoB = Repo.clone_from(ARCHIVE_REMOTE, temp_dir, no_checkout=True)

        added = []

        for file in deleted_files:
            try:
                blob = commit.tree / file
                content = blob.data_stream.read()

                dest = os.path.join(temp_dir, file)
                os.makedirs(os.path.dirname(dest), exist_ok=True)

                with open(dest, "wb") as f:
                    f.write(content)

                added.append(file)

            except KeyError:
                continue  # file never committed before

        if added:
            repoB.index.add(added)
            repoB.index.commit(f"[{date.today()}] My you RIP")
            repoB.git.branch("-M", "main")
            repoB.remote("origin").push(refspec="main:main")

    finally:
        safe_delete(temp_dir)


# ---------- Live Repo Sync ----------


def sync_live(repoA):
    # Add/update new + modified
    repoA.git.add(A=True)

    if repoA.is_dirty(untracked_files=True):
        repoA.index.commit(f"[{date.today()}] The Dragon gets Gold Shipment.")
        repoA.remote("origin").push()


# ---------- Main ----------


def main():
    repoA = Repo(LIVE_REPO_PATH)

    old_files = read_old()
    new_files = scan_files()

    deleted = old_files - new_files

    print("Scanned.")

    # Step 1: Archive from history BEFORE modifying repoA
    archive_deleted(repoA, deleted)
    print("Archived.")

    # Step 2: Sync live repo
    sync_live(repoA)
    print("Live updated.")

    # Step 3: Update memory LAST
    write_new(new_files)

    print("Done.")


if __name__ == "__main__":
    main()
