import requests
import os
import shutil
import zipfile

# GitHub repository URL
repo_url = "https://api.github.com/repos/PieMC-Dev/PieMC/releases/latest"

# Update folder path
update_folder = os.path.join(os.path.dirname(__file__), "update")

# Configuration file path to preserve
config_file_path = os.path.join(os.path.dirname(__file__), "piemc", "config.py")

# Get the latest version from the GitHub repository
response = requests.get(repo_url)
if response.status_code == 200:
    latest_release = response.json()
    latest_version = latest_release['tag_name']
    
    # Read the current version from the timestamp file
    timestamp_file = os.path.join(os.path.dirname(__file__), "timestamp.txt")
    if os.path.exists(timestamp_file):
        with open(timestamp_file, 'r') as file:
            current_version = file.read().strip()
    else:
        current_version = "0"  # Initial version if the timestamp file doesn't exist
    
    if current_version < latest_version:
        print("New version available:", latest_version)
        
        # Create the update folder
        if not os.path.exists(update_folder):
            os.makedirs(update_folder)
        
        # Download and save the update as a zip file
        asset_url = latest_release['zipball_url']
        response = requests.get(asset_url)
        if response.status_code == 200:
            zip_file_path = os.path.join(update_folder, "update.zip")
            with open(zip_file_path, 'wb') as file:
                file.write(response.content)
            print("Update file downloaded")
        else:
            print("Error downloading the update file")
        
        # Extract the update folder from the zip file
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            extracted_folder = None
            for file_info in zip_ref.infolist():
                if file_info.is_dir():
                    extracted_folder = file_info.filename
                    break
            if extracted_folder is None:
                print("Error extracting the update folder from the zip file")
                exit(1)
            zip_ref.extractall(update_folder)
        
        # Move the updated files to their respective folders, excluding config.py
        for root, dirs, files in os.walk(os.path.join(update_folder, extracted_folder)):
            for file in files:
                file_path = os.path.join(root, file)
                if file_path.endswith("piemc/config.py"):
                    # Preserve the configuration file
                    continue
                # Get the relative path of the updated file
                relative_path = os.path.relpath(file_path, os.path.join(update_folder, extracted_folder))
                destination_path = os.path.join(os.path.dirname(__file__), relative_path)
                
                # Move the file to the destination folder
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.move(file_path, destination_path)
                print("Updated file:", relative_path)
        
        # Update the timestamp file with the latest version
        with open(timestamp_file, 'w') as file:
            file.write(latest_version)
        
        print("Server updated to version:", latest_version)
        
        # Move the preserved configuration file to its original location
        if extracted_folder is not None and os.path.exists(os.path.join(update_folder, extracted_folder, "piemc/config.py")):
            shutil.move(os.path.join(update_folder, extracted_folder, "piemc/config.py"), config_file_path)
    
    else:
        print("The server is already up to date.")
    
else:
    print("Failed to retrieve repository information.")
