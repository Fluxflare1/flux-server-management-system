import json

class DNSBackupRestore:
    def __init__(self, domain_name):
        self.domain_name = domain_name
        self.backup_file = f"backups/{self.domain_name}_dns_backup.json"

    def backup_dns_records(self, records):
        try:
            with open(self.backup_file, 'w') as file:
                json.dump(records, file)
            print(f"Backup for {self.domain_name} completed successfully.")
        except Exception as e:
            print(f"Error backing up DNS records: {e}")
            raise

    def restore_dns_records(self):
        try:
            with open(self.backup_file, 'r') as file:
                records = json.load(file)
                # Implement code to restore records using DomainRegistrarAPI
                print(f"Restored DNS records for {self.domain_name}.")
                return records
        except FileNotFoundError:
            print("Backup file not found.")
            raise
        except Exception as e:
            print(f"Error restoring DNS records: {e}")
            raise
