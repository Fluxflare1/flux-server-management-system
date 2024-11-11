from abc import ABC, abstractmethod

class CloudProvider(ABC):
    @abstractmethod
    def start_instance(self, instance_id):
        pass

    @abstractmethod
    def stop_instance(self, instance_id):
        pass

    @abstractmethod
    def list_instances(self):
        pass

    # Add new abstract methods as needed
