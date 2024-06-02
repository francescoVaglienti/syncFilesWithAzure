'''
Small draft sketch on how to get started with syncing multiple folders to Azure Storage Account

TODO:

- Implement auto syncing
- Implement login check 
- Implement as CLI tool for easy of use
'''

import subprocess
def sync_folder_with_azcopy(local_folder, container_url):
    try:
        # Construct the AzCopy command
        command = ["azcopy", "sync", local_folder, container_url]
        result = subprocess.run(command, text=True)
        
        # Check if the command was successful
        if result.returncode == 0:
            print(f'Successfully synced {local_folder} to {container_url}')
        else:
            print(f'Failed to sync {local_folder} to {container_url}')
            print(f'Error: {result.stderr}')
    
    except Exception as ex:
        print(f'Exception during syncing {local_folder}: {ex}')

try:
    account_url = "https://<storage_account_name>.blob.core.windows.net"
    container_name = "<storage_contianer_name>"

    folders_to_backup = ["<path_folder_one>","<path_folder_two>"]

    # Sync each folder using AzCopy
    for folder in folders_to_backup:
        print(f"Syncing {folder} to Azure Blob Storage")
        local_folder = "/" + folder + "/"
        container_url = f"{account_url}/{container_name}/{folder}"
        sync_folder_with_azcopy(local_folder, container_url)

except Exception as ex:
    print('Exception:')
    print(ex)
