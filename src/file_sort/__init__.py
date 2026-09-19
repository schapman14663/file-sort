import os

def main() -> None:
    print("Hello from file-sort!")

    downloads = "/home/simon/Downloads/"
    
    files = os.listdir(downloads)

    for file in files:
        print(file)

    extensions = [
        ".txt",
        ".epub",
        ".pdf",
        ".iso",
        ".jpeg",
        ".mpeg",
    ]

    #pattern should be a filename split at the dot?
    #then moved to *relevant directory*
    #for file in downloads:
    #    case pattern:
    #        pass
