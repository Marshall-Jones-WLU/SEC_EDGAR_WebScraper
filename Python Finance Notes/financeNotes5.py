import requests
from bs4 import BeautifulSoup

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

# define our response
response = requests.get(url = endpoint, params = param_dict)

# print status code
print(response.status_code)
print(response.url)

soup = BeautifulSoup(response.content, 'lmxl')

