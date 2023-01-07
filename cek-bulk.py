import requests

# Define the ANSI escape code for green text
GREEN = '\033[92m'

# Reset the text color to the default
RESET = '\033[0m'

# Open the file containing the list of URLs
with open('mtr.txt', 'r') as f:
    # Read each line in the file (each line is a URL)
    for url in f:
        # Strip leading/trailing whitespace and newline characters from the URL
        url = url.strip()
        
        # Make a GET request to the URL
        response = requests.get(url)
        
        # Check if the response is a valid one (2xx status code) and if the phrase "page not found" does not appear in the response content
        if response.status_code // 100 == 2 and "page not found" not in response.text.lower():
            # Print the URL in green text
            print(f'{GREEN}{url}{RESET} 200 OK')
