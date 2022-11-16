import re, requests

def getCIK():
    URL = 'http://www.sec.gov/cgi-bin/browse-edgar?CIK={}&Find=Search&owner=exclude&action=getcompany'
    CIK_RE = re.compile(r'.*CIK=(\d{10}).*')    
    cik_dict = {}
    ticker = str(input("Enter the ticker: ")).upper()
    f = requests.get(URL.format(ticker), stream = True)
    results = CIK_RE.findall(f.text)
    
    if len(results):
        results[0] = int(re.sub('\.[0]*', '.', results[0]))
        cik_dict[str(ticker).upper()] = str(results[0])
        
    return cik_dict[ticker]

getCIK()


'''
def getCIKs(TICKERS):
    URL = 'http://www.sec.gov/cgi-bin/browse-edgar?CIK={}&Find=Search&owner=exclude&action=getcompany'
    CIK_RE = re.compile(r'.*CIK=(\d{10}).*')    
    cik_dict = {}
    for ticker in TICKERS:
        f = requests.get(URL.format(ticker), stream = True)
        results = CIK_RE.findall(f.text)
        if len(results):
            results[0] = int(re.sub('\.[0]*', '.', results[0]))
            cik_dict[str(ticker).upper()] = str(results[0])
    f = open('cik_dict', 'w')   
    print(cik_dict)
    f.close()

getCIKs(['wmt','amzn','nflx'])
# returns:
# {'WMT': '104169', 'AMZN': '1018724', 'NFLX': '1065280'}
'''
