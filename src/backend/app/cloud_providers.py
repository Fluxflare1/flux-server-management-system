class CloudProvider:
    """Abstract class for cloud provider integration."""
    def create_instance(self, config):
        raise NotImplementedError("Create instance method not implemented.")

    def manage_instance(self, instance_id):
        raise NotImplementedError("Manage instance method not implemented.")

    def billing(self, instance_id):
        raise NotImplementedError("Billing method not implemented.")


class AWSProvider(CloudProvider):
    def create_instance(self, config):
        # AWS instance creation logic
        return f"AWS instance created with config: {config}"

    def manage_instance(self, instance_id):
        # AWS instance management logic
        return f"Managing AWS instance {instance_id}"

    def billing(self, instance_id):
        # AWS billing logic
        return f"Billing for AWS instance {instance_id}"


class GCPProvider(CloudProvider):
    def create_instance(self, config):
        # GCP instance creation logic
        return f"GCP instance created with config: {config}"

    def manage_instance(self, instance_id):
        # GCP instance management logic
        return f"Managing GCP instance {instance_id}"

    def billing(self, instance_id):
        # GCP billing logic
        return f"Billing for GCP instance {instance_id}"


class AzureProvider(CloudProvider):
    def create_instance(self, config):
        # Azure instance creation logic
        return f"Azure instance created with config: {config}"

    def manage_instance(self, instance_id):
        # Azure instance management logic
        return f"Managing Azure instance {instance_id}"

    def billing(self, instance_id):
        # Azure billing logic
        return f"Billing for Azure instance {instance_id}"


class HostingManager:
    def __init__(self, provider_name):
        self.provider = self.get_provider(provider_name)

    def get_provider(self, provider_name):
        if provider_name == "aws":
            return AWSProvider()
        elif provider_name == "gcp":
            return GCPProvider()
        elif provider_name == "azure":
            return AzureProvider()
        else:
            raise ValueError("Unsupported provider")

    def create_instance(self, config):
        return self.provider.create_instance(config)

    def manage_instance(self, instance_id):
        return self.provider.manage_instance(instance_id)

    def billing(self, instance_id):
        return self.provider.billing(instance_id)
