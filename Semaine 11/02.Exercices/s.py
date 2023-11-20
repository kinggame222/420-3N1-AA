import requests
from bs4 import BeautifulSoup

# Make a request to the website
response = requests.get('https://rustoria.co/clans/QC%20TAKEOVER')

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all 'table' elements
tables = soup.find_all('div')


if len(tables) > 0:
    # Print the text from each table
    for table in tables:
        print(table.get_text())


# Print the text from each table
for table in tables:
    print(table.get_text())