# import libraries
import requests # to be able to access webpages
from bs4 import BeautifulSoup # to be able to parse HTML
import urllib
import pandas as pd

cik_num = '/' + input("What is the company CIK number? ") + '/'

def get_filings(cik_num):
    # define our base url
    base_url = r"https://www.sec.gov/Archives/edgar/data"

    # Let's create a filing url
    filing_url = base_url + cik_num + "/index.json"

    # Let's request the url
    content = requests.get(filing_url)
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
            if document['type'] == '10-k': # this if statement keeps image files from being returned
                doc_name = document['name']
                document_url = base_url + cik_num + filing_num + '/' + doc_name
                print(document_url)
get_filings(cik_num)
