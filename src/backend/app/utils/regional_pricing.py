class RegionalPricing:
    def __init__(self, region):
        self.region = region
        self.regional_multipliers = {
            "North America": 1.0,
            "Europe": 1.1,  # Example: add 10% for Europe
            "Asia": 0.9,    # Example: discount 10% for Asia
            "Africa": 0.85, # Example: discount 15% for Africa
        }

    def get_adjusted_price(self, base_price):
        multiplier = self.regional_multipliers.get(self.region, 1.0)  # Default to 1.0 if not found
        return round(base_price * multiplier, 2)
