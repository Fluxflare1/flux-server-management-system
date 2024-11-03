import subprocess

class BackupManager:
    def create_backup(self):
        # Logic to back up data
        subprocess.run(['backup-command', '--option'])

    def restore_backup(self, backup_id):
        # Logic to restore data from backup
        subprocess.run(['restore-command', backup_id])
