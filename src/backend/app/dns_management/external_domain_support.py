# Path: src/backend/app/dns_management/external_domain_support.py

from .domain_api import DomainRegistrarAPI  # Reuse API if necessary

class ExternalDomainSupport:
    def __init__(self, domain_name):
        self.domain_name = domain_name

    def verify_domain_ownership(self):
        # Code to verify ownership via TXT record
        verification_code = "verify-{}".format(self.domain_name)
        response = DomainRegistrarAPI.check_txt_record(self.domain_name, verification_code)
        return response
