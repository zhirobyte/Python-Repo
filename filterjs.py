import re
import requests

# List the input files
input_files = ['ins1.txt', 'ins2.txt', 'ins3.txt']

# Iterate through the input files
for input_file in input_files:
    # Open the current input file and read its contents into a list
    with open(input_file, 'r') as f:
        lines = f.readlines()

    # Iterate through the list of URLs
    for line in lines:
        # Download the JavaScript file from the URL
        response = requests.get(line)
        contents = response.text

        # Use a regular expression to find all URLs
        urls = re.findall(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', contents)

        # Print the URLs
        for url in urls:
            print(url)
