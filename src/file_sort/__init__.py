import os

def main() -> None:
    print("Hello from file-sort!")

    home_dir = "/home/simon/"
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
    
    files = os.listdir(downloads)
    
    #just a check to make sure its doing what I expect
    for file in files:
        print(file)

    for file in files:
        for dir, exts in target_dirs.items():
            move_file(dir, exts, file)
        
def move_file(target_dir, extensions, file):
    for ext in extensions:
        if ext in file:
            mv_file = "mv /home/simon/Downloads/" + file + " " + target_dir
            os.system(mv_file)
            print(file + " succesfully moved to " + target_dir)

