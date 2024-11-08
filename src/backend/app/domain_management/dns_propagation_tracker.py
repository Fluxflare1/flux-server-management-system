import dns.resolver

class DNSPropagationTracker:
    def __init__(self, domain_name, expected_ip):
        self.domain_name = domain_name
        self.expected_ip = expected_ip

    def check_propagation(self):
        try:
            result = dns.resolver.resolve(self.domain_name, 'A')
            for ipval in result:
                if ipval.to_text() == self.expected_ip:
                    print(f"{self.domain_name} has propagated successfully.")
                    return True
            print(f"{self.domain_name} not yet propagated.")
            return False
        except Exception as e:
            print(f"Error during DNS propagation check for {self.domain_name}: {e}")
            raise
