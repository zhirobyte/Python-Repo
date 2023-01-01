import requests
import re

# Prompt the user for the URL of the website to scrape
url = input("Enter the URL of the website to scrape: ")

# Open a file to write the results to
with open("js_files.txt", "w") as output_file:
  # Send a request to the website and retrieve the HTML
  response = requests.get(url)
  html = response.text

  # Use a regular expression to find all JavaScript files in the HTML
  js_files = re.findall(r"<script src=[^>]+", html)

  # Iterate through the list of JavaScript files
  for js_file in js_files:
    # Extract the URL of the JavaScript file
    js_url = re.search(r"https?://[^']+", js_file).group()

    # Send a request to the JavaScript file and retrieve the content
    js_response = requests.get(js_url)
    js_content = js_response.text

    # Check if the "admin" context is present in the JavaScript file
    if "admin" in js_content:
      # Write the URL of the JavaScript file to the output file
      output_file.write(js_url + "\n")
