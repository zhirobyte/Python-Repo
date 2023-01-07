# List the input files
input_files = ['urls1.txt', 'urls2.txt', 'urls3.txt']

# Open the output file
with open('hasil.txt', 'w') as outfile:
    # Iterate through the input files
    for input_file in input_files:
        # Open the current input file
        with open(input_file, 'r') as infile:
            # Read the contents of the input file into a list
            lines = infile.readlines()

            # Iterate through the list of URLs
            for line in lines:
                # Check if the URL has the "?url=" parameter
                if "?url=" in line:
                    # If it does, write the URL to the output file
                    outfile.write(line)
