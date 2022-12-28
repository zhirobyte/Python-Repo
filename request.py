import requests

# Prompt the user for the URL
url = input('Enter the URL: ')

# Prompt the user for the API key
api_key = input('Enter the API key: ')

# Set the headers for the request
headers = {'X-API-KEY': api_key}

# Send the GET request
response = requests.get(url, headers=headers)

# Print the status code of the response
print(response.status_code)

# Print the response content
print(response.text)
