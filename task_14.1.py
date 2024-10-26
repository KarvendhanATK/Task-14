import requests
import json
class CountryInfo:
    def __init__(self, url):
        self.url = url
        self.data = self.fetch_data()
    
    def fetch_data(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return None
    def display_countries_and_currencies(self):
        """Displays the names of countries, their currencies, symbols."""
        if not self.data:
            print("No data available.")
            return
        print("Countries, Currencies, and Symbols:")
        for country in self.data:
            country_name = country.get('name', {}).get('common', 'Unknown')
            currencies = country.get('currencies', {})
            for currency_code, currency_info in currencies.items():
                currency_name = currency_info.get('name', 'Unknown')
                currency_symbol = currency_info.get('symbol', 'N/A')
                print(f"Country: {country_name}, Currency: {currency_name}, Symbol: {currency_symbol}")

    def countries_with_currency(self, currency_name):
        """Displays countries that have a specified currency."""
        if not self.data:
            print("No data available.")
            return
        
        print(f"\nCountries with currency '{currency_name}':")
        found = False
        for country in self.data:
            currencies = country.get('currencies', {})
            for currency_code, currency_info in currencies.items():
                if currency_info.get('name') == currency_name:
                    country_name = country.get('name', {}).get('common', 'Unknown')
                    print(country_name)
                    found = True
        if not found:
            print(f"No countries found with currency '{currency_name}'.")

# URL 
url = "https://restcountries.com/v3.1/all"

# Create CountryInfo class
country_info = CountryInfo(url)

# Display countries and their currencies
country_info.display_countries_and_currencies()

# Display countries with USD (Dollar)
country_info.countries_with_currency('United States Dollar')

# Display countries with EUR (Euro)
country_info.countries_with_currency('Euro')
