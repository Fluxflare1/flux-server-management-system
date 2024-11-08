# Path: src/backend/app/dns_management/dns_propagation_tracker.py

import dns.resolver
import time

class DNSPropagationTracker:
    def __init__(self, domain, record_type, expected_value):
        self.domain = domain
        self.record_type = record_type
        self.expected_value = expected_value

    def track_propagation(self):
        while True:
            # Check if DNS records match expected values
            answers = dns.resolver.resolve(self.domain, self.record_type)
            if any(answer.to_text() == self.expected_value for answer in answers):
                print(f"DNS propagation complete for {self.domain}")
                break
            print("Waiting for DNS propagation...")
            time.sleep(300)  # Check every 5 minutes
