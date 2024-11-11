from utils.currency_conversion import CurrencyConverter
from utils.regional_pricing import RegionalPricing

class PricingService:
    def __init__(self, base_currency="USD"):
        self.converter = CurrencyConverter(base_currency=base_currency)

    def calculate_price(self, base_price, target_currency, region):
        # Step 1: Adjust price for region
        regional_pricing = RegionalPricing(region)
        adjusted_price = regional_pricing.get_adjusted_price(base_price)

        # Step 2: Convert to target currency
        final_price = self.converter.convert_price(adjusted_price, target_currency)
        return final_price
