import os
import hashlib
import time

# Set the directory to monitor
DIR_TO_MONITOR = "/path/to/directory"

# Initialize the dictionary of file hashes
file_hashes = {}

# Function to calculate the hash of a file
def hash_file(file_path):
    hasher = hashlib.sha256()
    with open(file_path, "rb") as f:
        while True:
            chunk = f.read(4096)
            if not chunk:
                break
            hasher.update(chunk)
    return hasher.hexdigest()

# Function to check if a file has changed
def check_file(file_path):
    if os.path.exists(file_path):
        file_hash = hash_file(file_path)
        if file_path in file_hashes:
            if file_hash != file_hashes[file_path]:
                print(f"File {file_path} has changed!")
                file_hashes[file_path] = file_hash
        else:
            print(f"New file {file_path} detected.")
            file_hashes[file_path] = file_hash
    elif file_path in file_hashes:
        print(f"File {file_path} has been deleted.")
        del file_hashes[file_path]

# Main loop to monitor the directory
while True:
    for root, dirs, files in os.walk(DIR_TO_MONITOR):
        for file in files:
            file_path = os.path.join(root, file)
            check_file(file_path)
    time.sleep(60)
