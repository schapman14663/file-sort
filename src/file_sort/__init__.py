import os
import subprocess

def main() -> None:
    print("Hello from file-sort!")

    home_dir = "/home/{user}/"
    docs_dir = home_dir + "Documents/"
    downloads = home_dir + "Downloads/"
    epubs_dir = home_dir + "Books/epubs/"
    music_dir = home_dir + "Music/"
    pdfs_dir = home_dir + "Books/pdfs/"
    pics_dir = home_dir + "Pictures/"
    vids_dir = home_dir + "Videos/"
    tarballs_dir = home_dir + "Tarballs/"
    distros_dir = home_dir + "Distros/"

    target_dirs = {
        docs_dir: [".txt", ".doc", ".docx"],
        epubs_dir: [".epub"],
        music_dir: [".mp3"],
        pdfs_dir: [".pdf"],
        pics_dir: [".jpeg", ".png", ".tiff"],
        vids_dir: [".mp4"],
        tarballs_dir: [".tar.gz"],
        distros_dir: [".iso"],
    }
    
    files = os.scandir(downloads)

    for file in files:
        
        if file.is_dir():
            print(f"Skipped Directory: {file.name}.")
            continue

        for dir, exts in target_dirs.items():
            move_file(downloads, dir, exts, file.name)
        
        result_files = os.listdir(downloads)
        if file in result_files:
            print(f"Unable to move {file}, consider updating sorting script")
            
        
def move_file(orgin_dir: str, target_dir: str, extensions: list[str], file: str):
    for ext in extensions:
        if ext in file:
            mv_file = "/home/{user}/Downloads/" + file 
            _ = subprocess.run(["mv", mv_file, target_dir])

            updated_files = os.listdir(orgin_dir)
            if file not in updated_files:
                print(file + " succesfully moved to " + target_dir)

