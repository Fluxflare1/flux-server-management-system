# Path: src/backend/app/dns_management/dns_backup.py

from .domain_api import DomainRegistrarAPI

class DNSBackup:
    def __init__(self, domain):
        self.domain = domain

    def backup_dns_records(self):
        records = DomainRegistrarAPI.get_all_dns_records(self.domain)
        with open(f"{self.domain}_dns_backup.json", "w") as file:
            json.dump(records, file)
        return "Backup complete"

    def restore_dns_records(self, backup_file):
        with open(backup_file, "r") as file:
            records = json.load(file)
        for record in records:
            DomainRegistrarAPI.create_dns_record(self.domain, record["type"], record["value"])
        return "DNS records restored"
