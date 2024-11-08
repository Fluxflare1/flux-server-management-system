from .domain_registrar_api import DomainRegistrarAPI

class DomainManager:
    def __init__(self):
        self.api = DomainRegistrarAPI()

    def register_domain(self, domain_name, client_id):
        try:
            response = self.api.register_domain(domain_name)
            # Save domain registration details to the database
            # Replace with actual database code
            print(f"Domain {domain_name} registered for client {client_id}")
            return response
        except Exception as e:
            print(f"Error registering domain: {e}")
            raise

    def update_dns_record(self, domain_name, record_type, value):
        try:
            response = self.api.update_dns_record(domain_name, record_type, value)
            return response
        except Exception as e:
            print(f"Error updating DNS record for {domain_name}: {e}")
            raise

    def check_domain_status(self, domain_name):
        try:
            status = self.api.get_domain_status(domain_name)
            return status
        except Exception as e:
            print(f"Error checking status for domain {domain_name}: {e}")
            raise
