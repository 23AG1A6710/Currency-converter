import requests

# Your API key
API_KEY = "4b1fea5a44cd4133e7fdd596"

# Base currency (you can change this later)
base_currency = "USD"

# API endpoint
url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base_currency}"

# Fetch data
response = requests.get(url)
data = response.json()

# User input
amount = float(input("Enter amount: "))
to_currency = input("Enter target currency (e.g. INR, EUR, GBP): ").upper()

# Conversion
if to_currency in data['conversion_rates']:
    converted = amount * data['conversion_rates'][to_currency]
    print(f"{amount} {base_currency} = {converted:.2f} {to_currency}")
else:
    print("Currency not found!")