import re

# File path to your uploaded file
file_path = "bitcoinwallet (2).txt"

# Read the file content
with open(file_path, "r") as file:
    content = file.read()

# Regex to extract Bitcoin addresses
addresses = re.findall(r'\b1[1-9A-HJ-NP-Za-km-z]{26,35}\b', content)

# Print each address in a new line
for address in addresses:
    print(address)
