import asyncio
import aiohttp

# Define the ANSI escape code for green text
GREEN = '\033[92m'

# Reset the text color to the default
RESET = '\033[0m'

async def check_url(url):
    # Make a GET request to the URL
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            # Check if the response is a valid one (2xx status code) and if the phrase "page not found" does not appear in the response content
            if response.status == 200 and "page not found" not in await response.text():
                # Print the URL in green text
                print(f'{GREEN}{url}{RESET} is a valid URL')

async def main():
    # Open the file containing the list of URLs
    with open('stn.txt', 'r') as f:
        # Read each line in the file (each line is a URL)
        tasks = []
        for url in f:
            # Strip leading/trailing whitespace and newline characters from the URL
            url = url.strip()
            
            # Create a task to check the URL asynchronously
            task = asyncio.create_task(check_url(url))
            tasks.append(task)
        
        # Wait for all tasks to complete
        await asyncio.gather(*tasks)

# Run the main function
asyncio.run(main())
