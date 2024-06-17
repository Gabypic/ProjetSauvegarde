import subprocess
import datetime

SOURCE = "/home/bots/projetsauvegarde/toSave"
DEST = "/home/bots/projetsauvegarde/saves"
SERVER = "bots@185.132.47.110"

rsync_command = f"rsync -avz --delete -e 'ssh -i /chemin/vers/votre/clé/privée/id_rsa' {SOURCE} {SERVER}:{DEST}"
result_rsync = subprocess.run(rsync_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if result_rsync.returncode == 0:
    print("Rsync - Sauvegarde réussie")
else:
    print("Rsync - Échec de la sauvegarde")
    print(result_rsync.stderr.decode('utf-8'))

now = datetime.datetime.now().strftime("%m-%d-%Y-%H-%M-%S")
borg_command = f"borg create --stats --progress -e 'ssh -i /chemin/vers/votre/clé/privée/id_rsa' {SERVER}:/home/bots/projetsauvegarde/backup::{now} {SOURCE}"
result_borg = subprocess.run(borg_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if result_borg.returncode == 0:
    print("Borg - Sauvegarde réussie")
else:
    print("Borg - Échec de la sauvegarde")
    print(result_borg.stderr.decode('utf-8'))
