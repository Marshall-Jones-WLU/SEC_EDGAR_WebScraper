#This code can be used for parsing xml records of SEC filings

'''All this code is good for gathering all the data on each report. I don't need all of this
for the time being though.

# loop through each entry
for entry in entries:

    # grab the accession number to create a key value
    accession_num = entry.find('accession-number').text
    
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
    entry_dict[accession_num]['file_info']['file_number_href'] = entry.find('file_number_href').text
    entry_dict[accession_num]['file_info']['filing_date'] = entry.find('filing_date').text
    entry_dict[accession_num]['file_info']['filing_href'] = entry.find('filing_href').text
    entry_dict[accession_num]['file_info']['filing_type'] = entry.find('filing_type').text
    entry_dict[accession_num]['file_info']['form_number'] = entry.find('form_number').text
    entry_dict[accession_num]['file_info']['form_name'] = entry.find('form_name').text
    entry_dict[accession_num]['file_info']['file_size'] = entry.find('file_size').text

    # store extra info
    entry_dict[accession_num]['request_info'] = {}
    entry_dict[accession_num]['request_info']['link'] = entry.find('link')['href']
    entry_dict[accession_num]['request_info']['title'] = entry.find('title').text
    entry_dict[accession_num]['request_info']['last_updated'] = entry.find('updated').text

    # store in the master list
    master_list_xml.append(entry_dict)'''
