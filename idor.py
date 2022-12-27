import requests

# Prompt the user for the base URL
base_url = input('Enter the base URL: ')

# Prompt the user for the parameter name
param_name = input('Enter the parameter name: ')

# Prompt the user for the parameter values
param_values = input('Enter the parameter values (comma-separated): ')
param_values = param_values.split(',')

# Iterate over the parameter values
for param_value in param_values:
  # Construct the full URL with the parameter
  url = f'{base_url}?{param_name}={param_value}'

  # Send a GET request to the URL
  response = requests.get(url)

  # Check the status code of the response
  if response.status_code == 200:
    # If the status code is 200 (OK), check the response content
    content = response.text
    if 'private' in content:
      # If the word 'private' appears in the response content, print a warning
      print(f'Possible IDOR vulnerability found at {url}')
  else:
    # If the status code is not 200, print an error message
    print(f'Error {response.status_code} for {url}')
