import os
import subprocess
import datetime

SOURCE = "/home/gaby/Desktop/to_save"
DEST = "./saves"
SERVER = "gaby@10.0.2.15"

rsync_command = f"rsync -avz --delete {SOURCE} {SERVER}:{DEST}"
result = subprocess.run(rsync_command, shell=True)

now = datetime.datetime.now().strftime('%Y-%m-%d')
borg_command = f"borg create --stats --progress {SERVER}:/home/gaby/Desktop/ProjetSauvegarde/server/backup::{now} {SOURCE}"
result = subprocess.run(borg_command, shell=True)

if result.returncode == 0:
    print("Sauvegarde réussie")
else:
    print("Échec de la sauvegarde")
