import requests

class DomainRegistrarAPI:
    def __init__(self):
        self.api_url = "https://api.domainregistrar.com"
        self.api_key = "YOUR_API_KEY"

    def register_domain(self, domain_name):
        response = requests.post(f"{self.api_url}/register", json={"domain": domain_name}, headers={"Authorization": self.api_key})
        response.raise_for_status()
        return response.json()

    def update_dns_record(self, domain_name, record_type, value):
        response = requests.put(f"{self.api_url}/dns/update", json={"domain": domain_name, "type": record_type, "value": value}, headers={"Authorization": self.api_key})
        response.raise_for_status()
        return response.json()

    def get_domain_status(self, domain_name):
        response = requests.get(f"{self.api_url}/status/{domain_name}", headers={"Authorization": self.api_key})
        response.raise_for_status()
        return response.json()
