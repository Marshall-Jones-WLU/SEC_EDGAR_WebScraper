'''
Author: Marshall Jones
Filename: Stocks_main

Description:
The user inputs the ticker symbol of a company. It then finds that
company's SEC Edgar CIK number. It then finds the Accession number of the company's most recently
published 10-k filing (the type of filing and number of most recently released). From
there, the get_filing_summary() function returns the summary of the filing in xml format. The
parse_filing_summary() function parses the filing summary and creates a list of all the different
reports, or sections of the filing. The grab_financial_statements() function finds the financial
statements that we want from the list of sections of the filing, and then returns a smaller list
of just the financial statement data that we want (currently the Balance Sheet, Income Statement,
Statement of Cash Flows, and Statement of Stockholders' Equity, but more can be added).

The scrape_financial_statements() function takes the data from each financial statement and organizes
it into a structure with column headers, section headers (on each row), and their associated data.
Then, there is another function for each statement that uses the pandas library to put the data into
a data frame, which can be viewed in an excel file. A new worksheet is saved for each of these
financial statements. These functions are called make_balSheet_df(), make_income_df(), make_cashFlow_df(),
and make_equity_df()
'''
#import sys
#sys.path.append('/Users/marshalljones/Desktop/Stock Analysis')

#print(sys.path)

# import libraries
from Stock_Analysis import Company, Analysis

class STONK(object):
    
    def __init__(self):
        self.ticker = str(input("Enter the ticker: ")).upper()
        self.docType = '10-K'

    def generate_csv(self):
        comp = Company()
        self.CIK = comp.get_CIK(self.ticker)
        filingListSoup = comp.get_filingList(self.CIK, self.docType)
        self.info_dict = comp.get_info(self.CIK, self.docType)

        ACC, filingDate = comp.get_ACC(filingListSoup)
        print(self.info_dict['CIK'])
        xml_summary, self.counter = comp.get_summary(self.info_dict, ACC, filingDate, self.docType)
        master_reports, counter, ACC, filingDate, xml_summary = comp.parse_summary(xml_summary, self.CIK, ACC, self.filingDate)
        statements_url, reportOrder = comp.grab_reports(master_reports)
        statements_data = comp.scrape_reports(statements_url, reportOrder)

        footnote = comp.footnote_check()
        if footnote == True:
            comp.footnote_remove()
            comp.footnote_store()

        balSheet_df, footnoteDict = comp.make_balSheet_df(statements_data, reportOrder)
        income_df, footnoteDict = comp.make_income_df(statements_data, reportOrder, footnoteDict)
        cashFlow_df, footnoteDict = comp.make_cashFlow_df(statements_data, reportOrder, footnoteDict)
        equity_df, footnoteDict = comp.make_equity_df(statements_data, reportOrder, footnoteDict)

        dirPath = self.dirPath
        Analysis.analysis(balSheet_df, income_df, cashFlow_df, self.infoDict, dirPath, filingDate, self.ticker)

    def compare_multiple(self):
        pass

    def compare_industry(self):
        pass

    def verticle_analysis(self):
        pass




def main():
   """Program Entry Point"""
   go = STONK()
   go.generate_csv()

if __name__ == "__main__":
    main()








"""
"""
