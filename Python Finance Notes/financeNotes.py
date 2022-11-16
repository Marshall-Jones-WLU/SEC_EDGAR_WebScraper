"""
Notes from Python Finance episode 1 on Sigma Coding YouTube Channel
How to retrieve a filing from SEC's edgar database:
"""
# import Libraries
import requests
from bs4 import BeautifulSoup

# define our base url
base_url = r"https://www.sec.gov/Archives/edgar/data"

# define a CIK number to do a company search (Goldman Sachs in this example)
cik_num = '/886982/'

# Let's create a filing url
filing_url = base_ural + cik_num + "/index.json"

# Let's request the url
content = requests.get(filing_url)
decoded_content = content.json()

# go and grab a single filing number
filing_number = decoded_content['directory']['item'][0]['name']

# define our filing number url
filing_url = base_url + cik_num + filing_number + "/index.json"

# Let's request the url
content = requests.get(filing_url)
document_content = content.json()

# get the document names
for document in document_content['directory']['item']:

    if document['type'] != 'image2.gif':
        doc_name = document['name']
        document_url = base_url + cik_num + filing_number + '/' + doc_name
        print(document_url)

"""
To get multiple filings:
"""

# define our base url
base_url = r"https://www.sec.gov/Archives/edgar/data"

# define a CIK number to do a company search (Goldman Sachs in this example)
cik_num = '/886982/'

# Let's create a filing url
filing_url = base_ural + cik_num + "/index.json"

# Let's request the url
content = requests.get(filings_url)
decoded_content = content.json()

# get multiple filings
for filing in decoded_content['directory']['item']:

    # define each filing number
    filing_num = filing['name']

    # define our filing number url
    filing_url = base_url + cik_num + filing_num + "/index.json"

    # Let's request the url
    content = requests.get(filing_url)
    document_content = content.json()

    # get the document names
    for document in document_content['directory']['item']:
        doc_name = document['name']
        document_url = base_url + cik_num + filing_num + '/' + doc_name
        print(document_url)
