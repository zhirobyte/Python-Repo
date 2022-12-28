import requests

# Open the file containing the list of URLs
with open('url_list.txt', 'r') as f:
    # Read each line in the file (each line is a URL)
    for url in f:
        # Strip leading/trailing whitespace and newline characters from the URL
        url = url.strip()
        
        # Make a GET request to the URL
        response = requests.get(url)
        
        # Check if the response is a valid one (2xx status code)
        if response.status_code // 100 == 2:
            # Check if the phrase "page not found" appears in the response content
            if "page not found" in response.text.lower():
                print(f'{url} is NOT a valid URL')
            else:
                print(f'{url} is a valid URL')
        else:
            print(f'{url} is NOT a valid URL')
