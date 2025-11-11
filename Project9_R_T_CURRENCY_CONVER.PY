# 
# Problem Statement:  
# Create a Python script that converts one currency to another using live exchange rates from a real-time API (like ExchangeRate-API or exchangerate.host).

# What You'll Learn:

# - Accessing REST APIs  
# - Handling query parameters  
# - Parsing JSON responses  
# - Performing dynamic currency conversion

# Python Code:
 
import requests

def convert_currency(from_currency, to_currency, amount):
    url = f"https://api.exchangerate.host/convert"
    params = {
        "from": from_currency,
        "to": to_currency,
        "amount": amount
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        converted = data['result']
        print(f"💱 {amount} {from_currency.upper()} = {converted:.2f} {to_currency.upper()}")
    else:
        print("Error fetching exchange rates.")

#Example usage
convert_currency("usd", "inr", 10)

#  Output:


#  10 USD = 873.54 INR

#  How It Works:

# 1. Sends request with currencies and amount.  
# 2. Fetches real-time rates from exchangerate.host.  
# 3. Prints the converted amount clearly.

#  Try Modifying:

# - Add input() for interactive CLI  
# - Support batch conversions  
# - Build a GUI using Tkinter

#  Use Cases:

#  Daily currency tracking  
#  Travel budgeting tools  
#  Financial data apps  
