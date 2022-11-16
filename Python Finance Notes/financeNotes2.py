# import our Libraries
import requests
import urllib
from bs4 import BeautifulSoup

# Let's first make a function that will make the process of building a url easy
def make_url(base_url, comp):

    url = base_url

    # add each component to the base url
    for r in comp:
        url = '{}/{}'.format(url, r)

    return url

base_url = r"https://www.sec.gov/Archive/edgar/data"
components = ['886982','000156459019011378','0001564590-19-011378-index-headers.html']
make_url(base_url, components)

"""
"""

# base url for the daily index files
base_url = r"https://www.sec.gov/Archive/edgar/daily-index"

# create the daily index url for 2019
year_url = make_url(base_url,['2019','index.json'])

# Request the 2019 url
content = requests.get(year_url)
decoded_content = content.json()

# Loop through the dictionary
for item in decoded_content['directory']['item']:

    # get the name of the folder
    print('-'*100)
    print('Pulling url for quarter {}'.format(item['name']))

    # create the qtr url
    qtr_url = make_url(base_url,['2019',item['name'],'index.json'])

    print(qtr_url)

    # request the url and decode it.
    file_content = requests.get(qtr_url)
    decoded_content = file_content.json()

    print('-'*100)
    print('Pulling files')

    for file in decoded_content['directory']['item']:

        file_url = make_url(base_url, ['2019', item['name'], file['name']])
        print(file_url)

"""
"""

# define a master file url
file_url = r"https://www.sec.gov/Archive/edgar/daily-index/2019/QTR2/master.20190401.idx"

# make a request for that file
content = requests.get(file_url).content

# Let's write the content to a text file
with open('master_20190401.txt', 'wb') as f:
    f.write(content)

# Let's read the content in the text file
with open('master_20190401.txt', 'rb') as f:
    byte_data = f.read()

# decode the byte data
data = byte_data.decode('utf-8').split('  ')

# finding the starting index
for index, item in enumerate(data):

    if 'ftp://ftp.sec.gov/edgar/' in item:
        start_ind = index

# create a new list that removes the junk
data_format = data[start_ind + 1:]

master_data = []

# Loop through the data list
for index, item in enumerate(data_format):

    if index == 0:
        clean_item_data = item.replace('\n', '|').split('|')
        clean_item_data = clean_item_data[8:]
    else:
        clean_item_data = item.replace('\n', '|').split('|')

    for index, row in enumerate(clean_item_data):

        # when you find the txt. file
        if '.txt' in row:

            mini_list = clean_item_data[(index - 4): index + 1]

            if len(mini_list) != 0:
                mini_list[4] = "https://www.sec.gov/Archives/" + mini_list[4]
                master_data.append(mini_list)

master_data[:3]

"""
"""

# Loop through the master data set
for index, document in enumerate(master_data):

    # create a dictionary
    document_dict = {}
    document_dict['cik_number'] = document[0]
    document_dict['company_name'] = document[1]
    document_dict['form_id'] = document[2]
    document_dict['data'] = document[3]
    document_dict['file_url'] = document[4]

    master_data[index] = document_dict

"""
"""

for document_dict in master_data:

    if document_dict['form_id'] == '10-k':
        print(document_dict['company_name'])
        print(document_dict['file_url'])
