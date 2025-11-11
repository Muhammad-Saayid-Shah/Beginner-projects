#  Python Project 7: Fetch & Process API Data 

#  Problem Statement:
# Write a Python script that fetches live data from a public API, processes it, and saves it to a JSON file.

#  What You'll Learn:

# - Making GET requests with Python’s requests module
# - Handling API responses (JSON)
# - Parsing and saving API data

#  Python Code:

import requests
import json

# API endpoint (Example: Public API for Random Users)
url = "https://randomuser.me/api/?results=5"

# Fetch data from API
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    data = response.json()
    print("API Data Fetched Successfully!\n")

    # Print fetched data
    print(json.dumps(data, indent=4))

    # Process data (Extract only names and emails)
    users = []
    for user in data['results']:
        users.append({
            "name": f"{user['name']['first']} {user['name']['last']}",
            "email": user['email']
        })

    # Save processed data to JSON
    with open("users.json", "w") as f:
        json.dump(users, f, indent=4)

    print("\nProcessed user data saved to users.json")

else:
    print(f"Error: Unable to fetch data (Status Code: {response.status_code})")


#  How It Works:

# 1. Sends a GET request to a public API.
# 2. Parses the JSON response.
# 3. Extracts user names & emails.
# 4. Saves clean data into a local users.json file.

#  Try Modifying:

# - Change API to fetch weather, news, or cryptocurrency prices.
# - Use query parameters to customize data.
# - Automate periodic API calls and logging.

#  Use Cases:

#  Collecting data for dashboards
#  Building real-time apps
#  Automating daily reports




