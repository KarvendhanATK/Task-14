import requests
from collections import Counter, defaultdict

# URL for Open Brewery DB API
states = ["Alaska", "Maine", "New York"]
base_url = "https://api.openbrewerydb.org/breweries"

# Function for breweries by state
def fetch_breweries(state):
    response = requests.get(f"{base_url}?by_state={state}&per_page=50")
    response.raise_for_status()
    return response.json()

# 1. List names of all breweries in each state
breweries_by_state = {state: fetch_breweries(state) for state in states}
brewery_names = {state: [brewery["name"] for brewery in breweries] for state, breweries in breweries_by_state.items()}
print("Brewery Names by State:")
for state, names in brewery_names.items():
    print(f"{state}: {names}")

# 2. Count number of breweries in each state
brewery_counts = {state: len(breweries) for state, breweries in breweries_by_state.items()}
print("\nBrewery Counts by State:")
print(brewery_counts)

# 3. Count types of breweries in individual cities for each state
brewery_types_by_city = defaultdict(lambda: defaultdict(int))
for state, breweries in breweries_by_state.items():
    for brewery in breweries:
        city = brewery["city"]
        brewery_type = brewery["brewery_type"]
        brewery_types_by_city[state][city] += 1

print("\nBrewery Types by City:")
for state, cities in brewery_types_by_city.items():
    print(f"{state}:")
    for city, count in cities.items():
        print(f"  {city}: {count} breweries")

# 4. Count and list breweries with websites in each state
breweries_with_websites = {state: [brewery for brewery in breweries if brewery["website_url"]] for state, breweries in breweries_by_state.items()}
brewery_website_counts = {state: len(breweries) for state, breweries in breweries_with_websites.items()}

print("\nBreweries with Websites by State:")
for state, count in brewery_website_counts.items():
    print(f"{state}: {count} breweries with websites")
