def path_details(PATH):
    
    fileCount, dirCount = 0,0

    for root, dirs, files in os.walk(PATH):
        print(f"\nLooking in Root: {root}\n")
        for directories in dirs:
            dirCount += 1
        for Files in files:
            fileCount += 1

    print(f"Number of files = {fileCount}")
    print(f"Number of Directories = {dirCount}")
    
    total = dirCount + fileCount
    
    return f'\nTotal current directory details = {total}'

if __name__ == "__main__":
    import os
    PATH = os.path.abspath(os.getcwd())
    print(path_details(PATH))
