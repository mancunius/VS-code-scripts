import os
from pathlib import Path

# Toggle this:
DRY_RUN = False  # True = preview only, False = actually delete

# Define all folders to process
folders_to_process = [
    Path("/Users/martinbaker/Documents/GitHub/AdFontes/"),
    Path("/Users/martinbaker/Dropbox/03_Professional/34_LaTeX/LaTeX_invoices"),
    Path("/Users/martinbaker/Documents/GitHub/ICEL-Graduale-Romanum"),
    Path("/Users/martinbaker/Documents/GitHub/2025-Abbots-Abbesses-Virgins"),
    Path("/Users/martinbaker/Documents/GitHub/2026-Virgins"),
    Path("/Users/martinbaker/Dropbox/04_Music/480_Lilypond-scores/01-LaTex_compiler"),
    Path("/Users/martinbaker/Documents/GitHub/2026-LoH-card-inserts")
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

if DRY_RUN:
    print("🧪 DRY RUN enabled — no files were deleted.")
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

'''This script will scan the specified folders and their subfolders for files with the defined extensions and delete them. Toggle the DRY_RUN variable to preview the files that would be deleted without actually deleting them. Make sure to review the list of files before running with DRY_RUN set to False.'''