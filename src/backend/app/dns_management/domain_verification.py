# Path: src/backend/app/dns_management/domain_verification.py

from .domain_api import DomainRegistrarAPI

class DomainVerification:
    @staticmethod
    def create_verification_txt_record(domain):
        # Generate and set a unique TXT record for domain verification
        verification_code = "verify-{}".format(domain)
        response = DomainRegistrarAPI.create_txt_record(domain, verification_code)
        return response
