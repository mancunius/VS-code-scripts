import os
from pathlib import Path

# Define all folders to process
folders_to_process = [
    Path("/Users/martinbaker/Documents/GitHub/AdFontes/"),
    Path("/Users/martinbaker/Dropbox/03_Professional/34_LaTeX/LaTeX_invoices"),
    Path("/Users/martinbaker/Documents/GitHub/ICEL-Graduale-Romanum"),
    Path("/Users/martinbaker/Documents/GitHub/2025-Abbots-Abbesses-Virgins")
]

# Define file extensions to delete
extensions_to_delete = [".log", ".gz", ".gtex", ".gaux", ".glog", ".aux", ".out", ".toc"]

def gather_files(folder_path: Path):
    """Return a list of matching files from this folder and all subfolders."""
    files = []
    if not folder_path.exists():
        print(f"⚠️ Folder not found: {folder_path}")
        return files

    for extension in extensions_to_delete:
        for file_path in folder_path.rglob(f"*{extension}"):
            if file_path.is_file():
                files.append(file_path)

    return files


# ---- MAIN WORK FLOW ----
all_files = []

for folder in folders_to_process:
    print(f"🔍 Scanning {folder} ...")
    files = gather_files(folder)
    all_files.extend(files)

# If no files, exit safely
if not all_files:
    print("✨ No matching files found. Nothing to delete.")
    exit(0)

# List files
print("\nThe following files will be deleted:\n")
for f in all_files:
    print(f"  {f}")

print(f"\nTotal: {len(all_files)} files\n")

# Ask for confirmation
answer = input("❓ Delete all listed files? (y/N): ").strip().lower()

if answer != "y":
    print("🚫 Deletion cancelled. No files were removed.")
    exit(0)

# Proceed with deletion
print("\n🗑️ Deleting files...\n")
deleted = 0

for file_path in all_files:
    try:
        file_path.unlink()
        print(f"Deleted: {file_path}")
        deleted += 1
    except Exception as e:
        print(f"❌ Could not delete {file_path}: {e}")

print(f"\n✅ Done. {deleted} files deleted.")

'''This script cleans up auxiliary files (like .log, .aux, etc.) from specified LaTeX project directories. It scans the directories, lists the files to be deleted, asks for user confirmation, and then deletes the files if confirmed.'''