import requests
from config.logging_config import log_error

class CurrencyConverter:
    def __init__(self, base_currency="USD"):
        self.api_url = "https://api.exchangerate-api.com/v4/latest/"
        self.base_currency = base_currency

    def get_conversion_rate(self, target_currency):
        try:
            response = requests.get(f"{self.api_url}{self.base_currency}")
            response.raise_for_status()
            data = response.json()
            return data["rates"].get(target_currency, 1)  # Fallback to 1 if not found
        except Exception as e:
            log_error(f"Currency conversion error: {e}")
            return 1  # Return 1 as a fallback if API fails

    def convert_price(self, amount, target_currency):
        rate = self.get_conversion_rate(target_currency)
        return round(amount * rate, 2)
