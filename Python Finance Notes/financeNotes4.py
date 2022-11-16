import requests
import pandas as pd
from bs4 import BeautifulSoup

"""
Section One: Define the Parameters of the Search
"""

"""
Parameters:
action: (required) By default should be set to getcompany
CIK: (required)
type: (optional) Allows filtering the type of form. For example, if set to 10-k only the 10-k filings are returned.
dateb: (optional) Will only return the filings before a given date. The format is as follows: YYYYMMDD
datea: (optional) Will only return the filings after a given date. The format is as follows: YYYYMMDD
owner: (required) Is set to 'exclude' by default and specifies ownership. You may also set it to 'include' and 'only'.
start: (optional) Is the starting index of the results. For example, if I have 100 results but want to start at 45 of 100, I would pass 45.
state: (optional) The company's state
filenum: (optional) The filing number
sic: (optional) The company's SEC (Standard Industry Classification) identifier
output: (optional) Defines returned data structure as either xml (atom) or normal html
count: (optional) The number of results you want to see with your request, the max is 100 and if not set it will default to 40.
"""

# define our endpoint
endpoint = r"https://www.sec.gov/cgi-bin/browse-edgar"

# define our parameters
param_dict = {'action':'getcompany',
              'CIK':'789019',
              'type':'10-k',
              'dateb':'20190101',
              'owner':'exclude',
              'start':'',
              'output':'atom',
              'count':'100'}

# request the url, and then parse the response
response = requests.get(url = endpoint, params = param_dict)
soup = BeautifulSoup(response.content,'html.parser')

# Let the user know it was successful.
print('Request Successful')
print(response.url)

"""
Side Note: Doing a simple company name search
"""
'''
# base URL for the SEC EDGAR browser


# define your parameters dictionary
param_dict = {'action':'getcompany',
              'company':'Goldman Sachs',
              'owner':'exclude'}

# request the url, and then parse the response
response = requests.get(url = endpoint, params = param_dict)
soup = BeautifulSoup(response.content,'html.parser')

# Let the user know it was successful
print('Request Successful')
print(response.url)
'''
"""
Section Two: Parse the Response for the Document Details
"""

# find the document table with our data
doc_table = soup.find_all('table',class_='tableFile2')

# define a base url that will be used for link building.
base_url_sec = r"https://www.sec.gov"

master_list = []

# loop through each row in the table
for row in doc_table[0].find_all('tr'):

    # find all the columns
    cols = row.find_all('td')

    # if there are no columns move on to the next row.
    if len(cols) != 0:

        # grab the text
        filing_type = cols[0].text.strip()
        filing_data = cols[3].text.strip()
        filing_numb = cols[4].text.strip()

        # find the links
        filing_doct_href = cols[1].find('a', {'href':True, 'id':'documentsbutton'})
        filing_int_href = cols[1].find('a', {'href':True, 'id':'interactiveDataBtn'})
        filing_num_href = cols[4].find('a')

        # grab the first href
        if filing_doc_href != None:
            filing_doc_link = base_url_sec + filing_doc_href['href']
        else:
            filing_doc_link = 'no link'

        # grab the second href
        if filing_int_href != None:
            filing_int_link = base_url_sec + filing_int_href['href']
        else:
            filing_int_link = 'no link'

        # grab the third href
        if filing_num_href != None:
            filing_num_link = base_url_sec + filing_num_href['href']
        else:
            filing_num_link = 'no link'

        # create and store data in the dictionary
        file_dict = {}
        file_dict['file_type'] = filing_type
        file_dict['file_number'] = filing_numb
        file_dict['file_date'] = filing_date
        file_dict['links'] = {}
        file_dict['links']['documents'] = filing_doc_link
        file_dict['links']['interactive_data'] = filing_int_link
        file_dict['links']['filing_number'] = filing_num_link

        # let the user know it's working
        print('-'*100)
        print("Filing Type: " + filing_type)
        print("Filing Date: " + filing_date)
        print("Filing Number: " + filing_numb)
        print("Document Link: " + filing_doc_link)
        print("Filing Number Link: " + filing_num_link)
        print("Interactive Data Link: " + filing_int_link)

        # append dictionary to master list
        master_list.append(file_dict)

"""
Section Three: Parsing the Master List
"""

# Loop through to get the links from the dictionary
for report in master_list[0:2]:

    print('-'*100)
    print(report['links']['documents'])
    print(report['links']['filing_number'])
    print(report['links']['interactive_data'])

"""
Section Four: Parsing the XML version
"""

# base URL for the SEC EDGAR browser
endpoint = r"https://www.sec.gov/cgi-bin/browse-edgar"

# define our parameters dictionary
param_dict = {'action':'getcompany',
              'CIK':'789019',
              'type':'10-k',
              'dateb':'20190101',
              'owner':'exclude',
              'start':'',
              'output':'atom',
              'count':'100'}

# request the url, and then parse the response.
response = requests.get(url = endpoint, params = param_dict)
soup = BeautifulSoup(response.content,'lxml.parser')

# Let the user know it was successful
print('Request Successful')
print(response.url)

"""
"""

# find all the entry tags
entries = soup.find_all('entry')

# initialize our list for storage
master_list_xml = []

# loop through each found entry, remember this is only the first two
for entry in entries[0:2]:

    # grab the accession number so we can create a key value
    accession_num = entry.find('accession-nunber').text # there is a typo for "number" in EDGAR

    # create a new dictionary
    entry_dict = {}
    entry_dict[accession_num] = {}

    # store the category info
    category_info = entry.find('category')
    entry_dict[accession_num]['category'] = {}
    entry_dict[accession_num]['category']['label'] = category_info['label']
    entry_dict[accession_num]['category']['scheme'] = category_info['scheme']
    entry_dict[accession_num]['category']['term'] = category_info['term']

    # store the file info
    entry_dict[accession_num]['file_info'] = {}
    entry_dict[accession_num]['file_info']['act'] = entry.find('act').text
    entry_dict[accession_num]['file_info']['file_number'] = entry.find('file-number').text
    entry_dict[accession_num]['file_info']['file_number_href'] = entry.find('file-number-href').text
    entry_dict[accession_num]['file_info']['filing_date'] = entry.find('filing-date').text
    entry_dict[accession_num]['file_info']['filing_href'] = entry.find('filing-href').text
    entry_dict[accession_num]['file_info']['filing_type'] = entry.find('filing-type').text
    entry_dict[accession_num]['file_info']['form_number'] = entry.find('film-number').text
    entry_dict[accession_num]['file_info']['form_name'] = entry.find('form-name').text
    entry_dict[accession_num]['file_info']['file_size'] = entry.find('size').text

    # store extra info
    entry_dict[accession_num]['request_info'] = {}
    entry_dict[accession_num]['request_info']['link'] = entry.find('link')['href']
    entry_dict[accession_num]['request_info']['title'] = entry.find('title').text
    entry_dict[accession_num]['request_info']['last_updated'] = entry.find('updated').text

    # store in the master list
    master_list_xml.append(entry_dict)

    print('-'*100)
    print(entry.find('form-name').text)
    print(entry.find('file-number').text)
    print(entry.find('file-number-href').text)
    print(entry.find('link')['href'])
"""
Now that we have all the entries stored in our dictionary, let's grab the
first item and see what the output looks like for the category section.
"""

import pprint
pprint.pprint(master_list_xml[0]['0001265107-18-000013']['category'])

"""
Parsing the next page
"""
# base URL for the SEC EDGAR browser
endpoint = r"https://www.sec.gov/cgi-bin/browse-edgar"

# define our parameters dictionary
param_dict = {'action':'getcompany',
              'CIK':'789019',
              'dateb':'20190101',
              'owner':'exclude',
              'start':'',
              'output':'atom',
              'count':'100'}

# request the url, and then parse the response.
response = requests.get(url = endpoint, params = param_dict)
soup = BeautifulSoup(response.content,'lmxl')

# find the link that will take us to the next page
links = soup.find_all('link', {'rel':'next'})

# while there is still a next page
while soup.find_all('link', {'rel':'next'}) != []:

    # grab the link
    next_page_link = links[0]['href']

    print('-'*100)
    print(next_page_link)

    # request the next page
    response = requests.get(url = next_page_link)
    soup = BeautifulSoup(response.content,'lxml.parser')

    # see if there is a next link
    links = soup.find_all('link', {'rel':'next'})
