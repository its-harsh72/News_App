import json
data = [
  {
    "Compliance Name": "Debtor Ageing and Bank Statements for all operating accounts to be submitted quarterly by 20th day of every month of previous quarter.”",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "Bank Statement",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing and Bank Statements for all operating accounts to be submitted quarterly by 20th day of every month of previous quarter.”",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "Debtor Ageing",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 20 th of every quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Signed copy of debtor ageing to be provided by 20 th of every quarter.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted quarterly by 20th day of every month of previous quarter.”",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging & Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "Bank Statement",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 25th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statement",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "MIS",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "MIS Statement",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statement",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR-3B Statement",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debts Position",
    "": "",
    "Standardization Name": "Debts Position",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR 3B statement",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock Statement",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Month on month company financial MIS",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "MIS Statement",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "MoM MIS including profit & loss and Balance Sheet- Monthly by 25th of next month.",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 25th of every quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging & Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "Bank Statement",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted quarterly by 25th day of the following month of each quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 25th of every quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 20th of every quarter end.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Month-to-month company financial MIS of the company to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 10th of every month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Month on month company financial MIS to be submitted by 25th of every month (this should include stock and debtor figures as well).",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing to be submitted by 25th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 20th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Statutory Compliance Certificate",
    "": "",
    "Standardization Name": "Statutory Certificate",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR-3B Statements",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Clarity on the debtors ageing as of Oct’23 and July’23",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GST and EPFO to be paid in full till Nov’23 and Dec’23 respectively.",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "EPFO",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "RBI Annexure",
    "": "",
    "Standardization Name": "RBI Annexure",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Audited Financial Tax Report",
    "": "",
    "Standardization Name": "Audited Financial Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Audited Financial Balance Sheet FY 22-23",
    "": "",
    "Standardization Name": "Audited Financial Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "RBI Annexure",
    "": "",
    "Standardization Name": "RBI Annexure",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Financials (along with profit and loss, balance sheet and schedules) of the Borrower to be submitted by 20th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 25th of every quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 20th day of the month for previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock Statements",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statement",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "MIS Statement",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statement",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Month on month company financial MIS",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing to be submitted",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR-3B Statement",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "M-O-M sales & purchase happening through the portal in a report format.",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Month on month company financial MIS",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing to be submitted",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Month on month company financial MIS",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "M-O-M sales & purchase happening through the portal in a report format.",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock statements to be submitted",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debts Position",
    "": "",
    "Standardization Name": "Debts Position",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "MIS Statement",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debts Position",
    "": "",
    "Standardization Name": "Debts Position",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "RBI Annexure",
    "": "",
    "Standardization Name": "RBI Annexure",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing to be submitted",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtors Ageing",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statement of all accounts",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock statements to be submitted",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Month on month company financial MIS",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statement",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR-3B Statement",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debts Position",
    "": "",
    "Standardization Name": "Debts Position",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock Statement",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Month on month company financial MIS",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock statements to be submitted",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "RBI Annexure",
    "": "",
    "Standardization Name": "RBI Annexure",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debts Position",
    "": "",
    "Standardization Name": "Debts Position",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "MIS Statement",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debts Position",
    "": "",
    "Standardization Name": "Debts Position",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock statements to be submitted",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statement of all accounts",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debts position",
    "": "",
    "Standardization Name": "Debts Position",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statement of all accounts",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statement of all accounts",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "RBI Annexure",
    "": "",
    "Standardization Name": "RBI Annexure",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "ITR, computation Form 3CEB",
    "": "",
    "Standardization Name": "ITR",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Month on month company financial MIS",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statement",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Month on month company financial MIS",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock statement for all operating accounts to be submitted by 25th of next month every quarter",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GST returns to be shared by 25th of next month for every quarter",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 25th of next month every quarter",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing for all operating accounts to be submitted by 25th of next month every quarter",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 25th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 10th day of every month (starting from Aug’23)",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "The Anchor/Borrower shall provide Month on Month MIS to be submitted on or before the 25th day of subsequent month",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statement of all accounts by 10th of next month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statement",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock Statement",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debt table for all operating accounts to be submitted by 25th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "Debts Position",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statement",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statement",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock statement for all operating accounts to be submitted by 25th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR 3B in pdf or json file (or consent to Credable to access GST details online) 29AAICS8142E1Z5 for all operating accounts to be submitted by 25th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging (in excel) for all operating accounts to be submitted by 25th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statement",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Monthly Debtor Ageing for all operating accounts to be submitted on or before the 25th day of each month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Monthly Bank statements for all operating accounts to be submitted on or before the 25th day of each month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stamp Duty Reimbursement",
    "": "",
    "Standardization Name": "Stamp Duty",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Month on month company financial MIS to be submitted by 25th of every month (this should include stock and debtor figures as well).",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Month on month company financial MIS to be submitted by 25th of every month (this should include stock and debtor figures as well).",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing to be submitted by 25th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing to be submitted by 25th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR3B (Returns)- Monthly by 25th of next month.",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtors ageing (excel)- Monthly by 25th of next month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 25th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging & Bank statements for all operating accounts to be submitted monthly by 25th of next month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "Bank Statement",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debt position in our format (excel)- Monthly by 25th of next month.",
    "": "",
    "Standardization Name": "Debts Position",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 25th day of the following month of previous quarter",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted quarterly by 25th of following month for previous quarter",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 25th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 25th of next month starting August’23.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 25th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 25th of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 25th day of the following month for the previous monthly.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debt position of the Borrower to be submitted by 25th day of the following month for the immediately preceding calendar month.",
    "": "",
    "Standardization Name": "Debts Position",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging for all operating accounts to be submitted by 25th of next month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 25th of next month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR3B of all GSTINs to be obtained quarterly by 25th of next month.",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock Statement to be submitted by 25th of next month every quarter",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 25th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 25th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statement to be submitted by 25th day of the following month for the previous quarter, in a form and manner acceptable to the Lender",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 20th day of the following month for the previous quarter",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock statement to be submitted by 25th day of the following month for the previous quarter, in a form and manner acceptable to the Lender",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "SOA of all the loan accounts to be submitted on 20th of every month to check the repayment tracks",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements returns for all operating accounts to be submitted by 25th of next month every quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every quarte",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 25th of next month every quarter",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Monthly project tracker - execution, billing and collections to be taken monthly. As on date debt position to be submitted by 25th of next month",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 25th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock Statement for all operating accounts to be submitted by 25th of next month.",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtors ageing to be submitted by 25th day of the following month for the immediately preceding calendar month. in form and manner acceptable to the Lender.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR3B returns, to be submitted by 25th day of the following month for the immediately preceding calendar month. in form and manner acceptable to the Lender.",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debt position, to be submitted by 25th day of the following month for the immediately preceding calendar month. in form and manner acceptable to the Lender.",
    "": "",
    "Standardization Name": "Debts Position",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock statement ageing to be submitted by 25th day of the following month for the immediately preceding calendar month. in form and manner acceptable to the Lender.",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statement to be submitted by 25th day of the following month for the immediately preceding calendar month. in form and manner acceptable to the Lender.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "MoM MIS including profit and loss and balance sheet, to be submitted by 25th day of the following month for the immediately preceding calendar month. in form and manner acceptable to the Lender.",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging for all operating accounts to be submitted by 10th of every month",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements analysis to be done for G5K Petro Products Pvt Ltd after getting the provisional financials for FY 23.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 25th of next month every quarter",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 25th of every quarter",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 25th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted quarterly by 25th of following month for previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Month-to-month company financial MIS of the company to be submitted by 25th of every month.",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 25th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 20th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor statements of proposed end clients to be submitted monthly",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock Statement every month",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debt Position for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debts Position",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 25th of every quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debt Position for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debts Position",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "MoM MIS including profit and loss and Balance sheet to be submitted by 25th day of the following month for the previous monthly.",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 25th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "The Anchor/Borrower shall provide Month on Month MIS to be submitted on or before the 25th day of subsequent month",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "monthly review of existing loan portfolio",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "monthly Debtor Ageing for all operating accounts to be submitted on or before the 25th day of each month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "monthly Bank statements for all operating accounts to be submitted on or before the 25th day of each month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing to be submitted by 25th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Month on month company financial MIS to be submitted by 25th of every month (this should include stock and debtor figures as well).",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "The Borrower shall submit Month on Month MIS on a monthly basis to the Lender.",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 10th day of the following month for previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for ICICI bank account (where major revenue is booked) to be submitted by 25th of every month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging to be submitted by 25th of every month",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Monthly MIS including details of encumbered and unencumbered cash position of Bijak to be called for and credit to analyze the same",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted quarterly by 25th of following month for previous quarter",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock statements to be submitted by 10th of every month",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging to be submitted by 10th of every month",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging to be submitted by 25th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted quarterly by 25th month for previous quarter",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted quarterly by 25th of following month for previous quarter",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted quarterly by 25th of previous quarter",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 20th day of following month of the previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 25th day of previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 25th day of the following month for the previous quarter",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Month on Month consolidated MIS to be provided by the Borrower by 25th day of the following month.",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing & Every month borrower to share receivable details of these end clients with CredAble by 10 th of next month",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 25th of every quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock statements to be submitted to the Lender on or before the 10th day of every quarter",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts submitted by 15th day of every month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "MOM financial MIS to be submitted by 15th day of every month",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging & Bank statements for all operating accounts to be submitted by 20th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "Bank Statement",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging & Bank statements for all operating accounts to be submitted by 20th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "Bank Statement",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements submitted quarterly by 10th day of the following month of each quarter",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging to be submitted by 15th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 20th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 25th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging for all operating accounts to be submitted by 25th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 25 th of every quarter starting from Jun’23 Quarter by 25th Jul’23",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging & Bank statements for all operating accounts to be submitted by 20th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "Bank Statement",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging to be submitted by 10th of every month",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Monthly MIS of invoices raised by the borrower for Flipkart and RK worldinfocom to be shared",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Quarterly Bank Statement to be taken from the client",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for the previous month for all the operating accounts by 10th of the current month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 10th of every month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements to be provided within 10 days of following quarter end.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of the end of each quarter for the Tenure",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Monthly debtor Aging for all operating accounts to be submitted on or before the 10th of every subsequent calendar month",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Monthly Bank statements for all operating accounts to be submitted on or before the 10th of every subsequent calendar month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 20th of every quarter",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock statement for all operating accounts to be submitted by 10th of every month (starting from Jul’23).",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 10th of every month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock Statement",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging & Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "Bank Statement",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing to be submitted by 10th day of every quarter",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements updated till previous month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank and Debtor Ageing statement for all operating accounts to be submitted every quarter by 25th day of the subsequent month of the previous quarter from the date of signing of this Agreement”.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "Debtor Ageing",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Have we received Bank statements for the previous month for all the operating accounts by 10th of the current month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing to be submitted by the 10th of every month.",
    "": "",
    "Standardization Name": "Debts Position",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Have we received Bank statements for the previous month for all the operating accounts by 10th of the current month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debt position to be submitted by 25th day of the following month for the previous monthly.",
    "": "",
    "Standardization Name": "Debts Position",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statement to be submitted by 25th day of the following month for the immediately preceding calendar month. in form and manner acceptable to the Lender.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th day of following month for the previous quarter",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Every month new purchase orders to be verified along with the development.",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Cashflows to be monitored regularly and if reduction in cashflows then we will have to \ncheck the facility again and ask for more end clients.",
    "": "",
    "Standardization Name": "Cashflow monitoring",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 25th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Drawings approval, project completion status should be checked monthly starting from \nAug23",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 25th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR3B returns, to be submitted by 25th day of the following month for the immediately preceding calendar month. in form and manner acceptable to the Lender.",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock statement ageing to be submitted by 25th day of the following month for the immediately preceding calendar month. in form and manner acceptable to the Lender.",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtors ageing to be submitted by 25th day of the following month for the immediately preceding calendar month. in form and manner acceptable to the Lender.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debt position, to be submitted by 25th day of the following month for the immediately preceding calendar month. in form and manner acceptable to the Lender.",
    "": "",
    "Standardization Name": "Debts Position",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 25th of next month every quarter",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "MoM MIS including profit and loss and balance sheet, to be submitted by 25th day of the following month for the immediately preceding calendar month",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 25th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR3B returns of the following month for the previous quarter on 25th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 25th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock statement returns of the following month for the previous quarter on 25th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debt position returns of the following month for the previous quarter on 25th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "Debts Position",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing returns of the following month for the previous quarter on 25th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 20th day of the following month for the previous quarter",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing to be submitted by 20th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 25th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "The Borrower shall provide GST 3B returns on a quarterly basis to the Lender.",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 25th of every quarter",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted quarterly by 25th of following month for previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock statements to be submitted by 10th of every month",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging to be submitted by 25th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted quarterly by 25th of following month for previous quarter",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted quarterly by 25th month for previous quarter",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging to be submitted by 10th of every month",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted quarterly by 25th of previous quarter",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 25th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Borrower to provide bank statement of its account maintained with the Bank of India.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging  for all operating accounts to be submitted by 25th of every quarter.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock Statement every monthly (for march its will be received on April'23)",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "The Borrower shall submit Month on Month MIS on a monthly basis to the Lender.",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 25th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing and Bank Statements to be submitted by 10th day of the following month for previous quarter.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "Bank Statement",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 10th day of the following month for previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Month-to-month company financial MIS of the company to be submitted by 25th of every month.",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Financial MIS for all operating accounts to be submitted by 25th of every quarter",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 20th day of following month of the previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 25th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debt Position for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debts Position",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging  for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging & Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "Bank Statement",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing to be submitted by 25th day of the following month for the previous quarter",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Month on Month consolidated MIS to be provided by the Borrower by 25th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statement Analysis to be completed and credit to give noting on same",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing and Bank Statements for all operating accounts to be submitted by 25th of every quarter.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "Bank Statement",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Every month borrower to share receivable details of these end clients with CredAble by 10 th of next month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 25th of every quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts submitted by 15th day of every month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Detailed MIS for Purchase Order to vendor financing tranches to be provided by Client on monthly basis",
    "": "",
    "Standardization Name": "Debts Position",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted on or before the 10th day of end of each calendar quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging to be submitted by 10th of every month",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "monthly Debtor Ageing & Bank statements for all operating accounts to be submitted on or before the 10th day of end of each calendar quarter.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "Bank Statement",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing to be submitted by 25th of each next month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements fBank statements for all operating accounts to be submitted quarterly by 10th of following month for the previous quarter",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "monthly MIS for rental payments/receipts, any changes in contractual terms for proposed clients, or any debt raised by Borrower to be submitted on or before by 10th of every subsequent calendar month.",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 25th day of the following month for the previous quarter",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging to be submitted by 15th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "MOM financial MIS to be submitted by 15th day of every month",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements submitted quarterly by 10th day of the following month of each quarter",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging & Bank statements for all operating accounts to be submitted by 20th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "Bank Statement",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 20th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging & Bank statements for all operating accounts to be submitted by 20th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "Bank Statement",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing to be submitted quarterly by 25th day of the following month of each quarter.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted quarterly by 25th day of the following month of each quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Month On Month MIS (including profit and loss, Balance Sheet) to be provided by 20th of every quarter end",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Signed provisional financials, debtors ageing as on latest date to be provided",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Revised debtors ageing as on 31.12.21 to be taken prior to disbursement.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing & Bank statements to be provided within 7 days of the month end.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "Bank Statement",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing & Bank statements to be provided within 7 days of the month end.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "Bank Statement",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "quarterly party wise debtor ageing and Bank statements to be provided within 10 days of following quarter end.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "Bank Statement",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for the previous month for all the operating accounts by 10th of the current month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "monthly MIS for rental payments/receipts, any changes in contractual terms for proposed clients, or any debt raised by borrower to be provided by 10th of every month.",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 10th of every month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging & Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "Bank Statement",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank and Debtor Ageing statement for all operating accounts to be submitted every quarter by 25th day of the subsequent month of the previous quarter from the date of signing of this Agreement”.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "Bank Statement",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Submission of monthly debtor ageing report",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 25th of every quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "monthly Bank statements for all operating accounts to be submitted on or before the 10th of every subsequent calendar month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing to be submitted by 10th of every month of the next quarter.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Month-to-month company financial MIS of the company to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging & Bank statements for all operating accounts to be submitted by 10th of the end of each quarter for the Tenure",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "Bank Statement",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing to be submitted by 10th of every month",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "monthly Debtor Aging and Bank statements for all operating accounts to be submitted by the Borrower to the Lender by the 10th of every subsequent calendar month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "Bank Statement",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "monthly financial MIS to be submitted by 25th of each next month.",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statement Analysis to be provided for Financial Year 2021-22.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "quarterly party wise debtor ageing and Bank statements to be provided.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "Bank Statement",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "monthly MIS along with Balance Sheet, Profit & Loss and Cash flow by 10 days of the month end.",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging & Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "Bank Statement",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Month on month MIS along with Balance Sheet, Profit & loss and Cash flow to be provided for Feb-2022",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "monthly MIS for rental payments/receipts, any changes in contractual terms for proposed clients, or any debt raised by Borrower to be provided by 10th of every quarter.",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Month-to-month company financial MIS of the company to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "quarterly Debtor Ag Ageing and Bank statements for all operating accounts to be submitted by the Borrower to the Lender by the 10th of every subsequent calendar month for every quarter",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "Bank Statement",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "monthly Debtor Aging and Bank statements for all operating accounts to be submitted by the Borrower to the Lender by the 10th of every subsequent calendar month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "Bank Statement",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 10th of every month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 10th of every month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements to be provided within 7 days of the month end.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing & Bank statements for all operating accounts to be submitted, by 25th day of the following month, for the previous quarter”",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "Bank Statement",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Submission of bank statements by 10th of following month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Submission of bank statements by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Have we received Bank statements for the previous month for all the operating accounts by 10th of the current month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 15th of every quarterly.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Have we received Bank statements for the previous month for all the operating accounts by 10th of the current month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Have we received Bank statements for the previous month for all the operating accounts by 10th of the current month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted every quarter by 10th of the next month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging  for all operating accounts to be submitted by 25th of next month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Monthly project tracker - execution, billing and collections to be taken monthly. As on date debt position to be submitted by 25th of next month",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "The Borrower shall provide quarterly update on tax refund, in form and manner acceptable to the Lender",
    "": "",
    "Standardization Name": "ITR",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements  returns for all operating accounts to be submitted by 25th of next month every quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging returns for all operating accounts to be submitted by 25th of next month every quarter.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR3B returns for all operating accounts to be submitted by 25th of next month every quarter.",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debt position of the Borrower to be submitted by 25th day of the following month for the immediately preceding calendar month.",
    "": "",
    "Standardization Name": "Debts Position",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 25th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 25th of next month every quarter",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "MIS Statement",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted on or before the 10th day of end of each calendar quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Monthly Debtor Ageing for all operating accounts to be submitted on or before the 10th day of end of each calendar quarter.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statement",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debt Position",
    "": "",
    "Standardization Name": "Debt Position",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statement",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR-3B",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Undertaking from borrower to maintain Quasi Equity till end of the facility.",
    "": "",
    "Standardization Name": "Quasi Equity",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statement",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR-3B",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Month on Month MIS",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR-3B",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statement",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Volume Data M-o-M",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debt Position",
    "": "",
    "Standardization Name": "Debt Position",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statement",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR-3B",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Month on Month MIS",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock Statement",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock Statement",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR-3B",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debt Position",
    "": "",
    "Standardization Name": "Debt Position",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statement",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Month on Month MIS",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statement to be submitted by 25th day of the following month for the immediately preceding calendar month. in form and manner acceptable to the Lender.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th day of following month for the previous quarter",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging to be submitted by 25th of every month",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Month-to-month company financial MIS of the company to be submitted by 25th of every month.",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock Statement to be submitted by 25th of next month every quarter",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR-3B Statement",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging (in excel) for all operating accounts to be submitted by 25th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted monthly ICICI Bank 109251000593 Axis Bank 923030009934965",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statement",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 25th of next month every quarter",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GST returns to be shared by 25th of next month for every quarter",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Month on month company financial MIS",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statement",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR 3B statement",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statement of all accounts",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock statements to be submitted",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statement of all accounts",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "M-O-M sales & purchase happening through the portal in a report format.",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "M-O-M sales & purchase happening through the portal in a report format.",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR-3B Statement",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debts position",
    "": "",
    "Standardization Name": "Debts Position",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Monthly MIS including details of encumbered and unencumbered cash position of Bijak to be called for and credit to analyze the same",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for ICICI bank account (where major revenue is booked) to be submitted by 25th of every month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 25th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Monthly MIS and the portfolio details to be provided",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 25th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR 3B in pdf or json file (or consent to Credable to access GST details online) 29AAICS8142E1Z5 for all operating accounts to be submitted by 25th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock statement",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debt table for all operating accounts to be submitted by 25th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "Debts Position",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR-3B Statement",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statement",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Month on Month MIS",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR-3B Statement",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock statement",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statement",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR-3B Statement",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock Statement",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "ITR, computation Form 3CEB",
    "": "",
    "Standardization Name": "ITR",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Month on month company financial MIS",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statement of all accounts",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statement of all accounts",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Month on month company financial MIS",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debts Position",
    "": "",
    "Standardization Name": "Debts Position",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statement of all accounts",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR-3B Statement",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Month on month company financial MIS",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock statement",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statement",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "bank statement",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Month on month company financial MIS",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statement of all accounts",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debts Position",
    "": "",
    "Standardization Name": "Debts Position",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR-3B Statement",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Month on month company financial MIS",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statement of all accounts",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statement of all accounts",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR-3B Statement",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "MIS Statement",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock Statements",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statement",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR-3B Statements",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR-3B Statements",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statement for Recurring",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "MIS",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR-3B Statments",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 25th day of the following month for the previous monthly.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statement of all accounts",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR-3B Statement",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debts Position",
    "": "",
    "Standardization Name": "Debts Position",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR-3B Statement",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statement of all accounts",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debts Position",
    "": "",
    "Standardization Name": "Debts Position",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR-3B Statments",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statement of all accounts",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statement",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statement of all accounts",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR-3B Statement",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR-3B Statement",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statement of all accounts",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statement of all accounts",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR-3B Statement",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statement",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR-3B Statement",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtors Ageing",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debts Position",
    "": "",
    "Standardization Name": "Debts Position",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "MIS Statement",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "MIS Statement",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR-3B Statement",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "The Borrower shall provide quarterly update on tax refund, in form and manner acceptable to the Lender",
    "": "",
    "Standardization Name": "ITR",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR3B of all GSTINs to be obtained quarterly by 25th of next month.",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 25th of next month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statement",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "MIS Statement",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock statement",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock Statement",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR-3B Statement",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Month on month company financial MIS",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR-3B Statement",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR-3B Statement",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statement of all accounts",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debts Position",
    "": "",
    "Standardization Name": "Debts Position",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statement of all accounts",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR-3B Statement",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statement of all accounts",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Month on month company financial MIS",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock statements to be submitted",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statement",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR-3B Statement",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Month on month company financial MIS",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statement",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock Statement",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR-3B Statements",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statement of all accounts",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statement",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR-3B Statements",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "MIS Statement",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statement",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "MIS Statement",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR-3B Statement",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Monthly project tracker - execution, billing and collections to be taken monthly. As on date debt position to be submitted by 25th of next month",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statement for Recurring",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "MIS Statement",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR-3B Statements",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "MIS Statement",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Cashflows to be monitored regularly and if reduction in cashflows then we will have to check the facility again and ask for more end clients.",
    "": "",
    "Standardization Name": "Cashflow monitoring",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stamp Duty Reimbursement",
    "": "",
    "Standardization Name": "Stamp Duty",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Month on Month ( MoM) MIS for all operating accounts to be submitted by 25 day of the following month for the previous quarte",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 25 day of the following month for the previous quarte",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 25th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "SOA of all the loan accounts to be submitted on 20th of every month to check the repayment tracks",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 25th of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 25th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Monthly Financial MIS to be provided by 20th of every quarter",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debt position of the Borrower to be submitted by 25th day of the following month for the immediately preceding calendar month.",
    "": "",
    "Standardization Name": "Debts Position",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statement",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR-3B Statements",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "MIS Statement",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 25th of next month every quarter",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statement",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR-3B Statements",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statement",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock Statements",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statement",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "The Anchor/Borrower shall provide Month on Month MIS to be submitted on or before the 25th day of subsequent month",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Monthly Bank statements for all operating accounts to be submitted on or before the 25th day of each month.",
    "": "",
    "Standardization Name": "On Cilient",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "MIS",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statement of all accounts by 10th of next month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "MIS",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statement of all accounts by 10th of next month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Consolidated MoM MIS including profit & loss, Balance Sheet to be submitted by 25th of next quarterly",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR3B (Returns)- Monthly by 25th of next month.",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtors ageing (excel)- Monthly by 25th of next month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debt position in our format (excel)- Monthly by 25th of next month.",
    "": "",
    "Standardization Name": "Debts Position",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "MoM MIS including profit & loss and Balance Sheet- Monthly by 25th of next month.",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "MoM MIS including profit & loss and Balance Sheet (excel) by 25th of following month for previous quarter.",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted quarterly by 25th of following month for previous quarter",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 25th day of the following month of previous quarter",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 25th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Month on Month ( MoM) MIS by 25 day of the following month for the previous quarter",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 25th of next month starting Augustâ23.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock statement",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging for all operating accounts to be submitted by 25th of next month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 25th of next month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging returns for all operating accounts to be submitted by 25th of next month every quarter.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR3B returns, to be submitted by 25th day of the following month for the immediately preceding calendar month. in form and manner acceptable to the Lender.",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtors ageing to be submitted by 25th day of the following month for the immediately preceding calendar month. in form and manner acceptable to the Lender.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debt position, to be submitted by 25th day of the following month for the immediately preceding calendar month. in form and manner acceptable to the Lender.",
    "": "",
    "Standardization Name": "Debts Position",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "MoM MIS including profit and loss and balance sheet, to be submitted by 25th day of the following month for the immediately preceding calendar month. in form and manner acceptable to the Lender.",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR3B returns, to be submitted by 25th day of the following month for the immediately preceding calendar month. in form and manner acceptable to the Lender.",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted quarterly by 25th of following month for previous quarter",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging to be submitted by 25th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted quarterly by 25th of following month for previous quarter",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock statement",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging for all operating accounts to be submitted by 10th of every month",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debt Position for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debts Position",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debt Position for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debts Position",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "MoM MIS including profit and loss and Balance sheet to be submitted by 25th day of the following month for the previous monthly.",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements returns for all operating accounts to be submitted by 25th of next month every quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Monthly project tracker - execution, billing and collections to be taken monthly. As on date debt position to be submitted by 25th of next month",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR3B of all GSTINs to be obtained quarterly by 25th of next month.",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debt position of the Borrower to be submitted by 25th day of the following month for the immediately preceding calendar month.",
    "": "",
    "Standardization Name": "Debts Position",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtors ageing to be submitted by 25th day of the following month for the immediately preceding calendar month. in form and manner acceptable to the Lender.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 20th day of the following month for the previous quarter",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "MoM MIS including profit and loss and balance sheet, to be submitted by 25th day of the following month for the immediately preceding calendar month",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 25th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR3B returns of the following month for the previous quarter on 25th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debt position returns of the following month for the previous quarter on 25th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "Debts Position",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 20th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Financials (along with profit and loss, balance sheet and schedules) of the Borrower to be submitted by 20th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "The Borrower shall submit Month on Month MIS on a monthly basis to the Lender.",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Month-to-month company financial MIS of the company to be submitted by 25th of every month.",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging to be submitted by 25th of every month",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "monthly MIS including details of encumbered and unencumbered cash position of Bijak to be called for and credit to analyze the same",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted on or before the 10th day of end of each calendar quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statement Analysis to be provided for Financial Year 2021-22.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock Statement",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging & Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "Bank Statement",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "monthly Debtor Aging and Bank statements for all operating accounts to be submitted by the Borrower to the Lender by the 10th of every subsequent calendar month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "Bank Statement",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "monthly MIS along with Balance Sheet, Profit & Loss and Cash flow by 10 days of the month end.",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every quarte",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 25th of next month every quarter",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statement to be submitted by 25th day of the following month for the immediately preceding calendar month. in form and manner acceptable to the Lender.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock statement",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 25th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statement to be submitted by 25th day of the following month for the previous quarter, in a form and manner acceptable to the Lender",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debt position, to be submitted by 25th day of the following month for the immediately preceding calendar month. in form and manner acceptable to the Lender.",
    "": "",
    "Standardization Name": "Debts Position",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock statement",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock statement",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "The Borrower shall provide GST 3B returns on a quarterly basis to the Lender.",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 25th of every quarter",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted quarterly by 25th of following month for previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 25th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging  for all operating accounts to be submitted by 25th of every quarter.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Financial MIS for all operating accounts to be submitted by 25th of every quarter",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Month on Month MIS including profit and loss and Balance Sheet to be submitted on a monthly basis by the 25th day of the following month for the immediately preceding calendar month.",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for ICICI bank account (where major revenue is booked) to be submitted by 25th of every month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock statement",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging to be submitted by 10th of every month",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging & Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "Bank Statement",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted quarterly by 25th of previous quarter",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging & Bank statements for all operating accounts to be submitted by 20th of every quarter.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "Bank Statement",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements analysis to be done for G5K Petro Products Pvt Ltd after getting the provisional financials for FY 23.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 20th day of following month of the previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging  for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging  for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "DP Statement to be called monthly and the same to be monitored",
    "": "",
    "Standardization Name": "Debts Position",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 25th day of previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 25th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 25th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statement to be submitted by 25th day of the following month for the previous quarter, in a form and manner acceptable to the Lender",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 25th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock statement",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 20th day of the following month for the previous quarter",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 25th of every quarter",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 25th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted quarterly by 25th of following month for previous quarter",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging to be submitted by 10th of every month",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging to be submitted by 25th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Every month borrower to share receivable details of these end clients with CredAble by 10 th of next month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted quarterly by 25th month for previous quarter",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 25th of every quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted quarterly by 25th of following month for previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "The Borrower shall submit Month on Month MIS on a monthly basis to the Lender.",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock statement",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 20th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted quarterly by 25th of previous quarter",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging to be submitted by 15th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 20th day of following month of the previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 25th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 25th of every quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Monthly MIS of invoices raised by the borrower for Flipkart and RK worldinfocom to be shared",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debt Position for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debts Position",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock statement",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 20th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debt Position for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debts Position",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Agingto be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements  returns for all operating accounts to be submitted by 25th of next month every quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "monthly MIS of invoices raised by the borrower for Flipkart and RK worldinfocom to be shared",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted quarterly by 25th of following month for previous quarter",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor statements of proposed end clients to be submitted monthly",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts submitted by 15th day of every month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "MOM financial MIS to be submitted by 15th day of every month",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 20th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Financial MIS for all operating accounts to be submitted by 25th of every quarter",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock statement",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements to be submitted to the Lender on or before the 10th day of every quarter",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 25th of every quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements submitted quarterly by 10th day of the following month of each quarter",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging & Bank statements for all operating accounts to be submitted by 20th of every quarter.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "Bank Statement",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 25th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 20th of every quarter end.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements submitted quarterly by 10th day of the following month of each quarter",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 25 th of every quarter starting from Junâ23 Quarter by 25th Julâ23",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging for all operating accounts to be submitted by 25th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted quarterly by 25th day of the following month of each quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging to be submitted by 10th of every month",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging & Bank statements for all operating accounts to be submitted by 10th of the end of each quarter for the Tenure",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "Bank Statement",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "MOM financial MIS to be submitted by 15th day of every month",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging & Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "Bank Statement",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging & Bank statements for all operating accounts to be submitted by 10th of the end of each quarter for the Tenure",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "Bank Statement",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Detailed MIS for Purchase Order to vendor financing tranches to be provided by Client on monthly basis",
    "": "",
    "Standardization Name": "Debts Position",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debt position and GSTR3B returns to be submitted on a monthly  basis by the 25th day of the following month for the immediately  preceding calendar month",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts submitted by 15th day of every month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging to be submitted by 15th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Month on Month consolidated MIS to be provided by the Borrower by 25th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Month on month MIS along with Balance Sheet, Profit & loss and Cash flow to be provided for Feb-2022",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Month-to-month company financial MIS of the company to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "The Borrower will provide to the Lender, MIS till 30th September 2022 on or before the date of signing of the Agreement",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 10th of every month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of the end of each quarter for the Tenure",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Quarterly Bank Statement to be taken from the client",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging & Bank statements for all operating accounts to be submitted by 20th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "Bank Statement",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 20th of every quarter end.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted on or before the 10th day of end of each calendar quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 25th day of previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted quarterly by 25th day of the following month of each quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "monthly Bank statements for all operating accounts to be submitted on or before the 10th of every subsequent calendar month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock statement",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "monthly MIS for rental payments/receipts, any changes in contractual terms for proposed clients, or any debt raised by Borrower to be provided by 10th of every quarter.",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Revised debtors ageing as on 31.12.21 to be taken prior to disbursement.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 20th of every quarter",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "monthly MIS for rental payments/receipts, any changes in contractual terms for proposed clients, or any debt raised by Borrower to be submitted on or before by 10th of every subsequent calendar month.",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing for all operating accounts to be submitted by 25th day of the following month for the immediately preceding calendar month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted every quarter by 10th of the next month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "monthly review of existing loan portfolio",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Month On Month MIS (including profit and loss, Balance Sheet) to be provided by 20th of every quarter end",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Monthly Bank statements for all operating accounts to be submitted on or before the 10th of every subsequent calendar month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging & Bank statements for all operating accounts to be submitted by 20th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "Bank Statement",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "monthly financial MIS to be submitted by 25th of each next month.",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 20th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing to be submitted by 25th of each next month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging to be submitted by 10th of every month",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements to be provided within 10 days of following quarter end.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 10th of every month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging & Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "Bank Statement",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for the previous month for all the operating accounts by 10th of the current month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Month On Month MIS (including profit and loss, Balance Sheet) to be provided by 20th of every quarter end",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Have we received Bank statements for the previous month for all the operating accounts by 10th of the current month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "The Anchor/Borrower shall provide Month on Month MIS to be submitted on or before the 25th day of subsequent month",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Agingto be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Anchor/Corporate to provide quarterly MIS reports with all required data points for business runway evaluation by the Lender, in a form and manner acceptable to the Lender to be submitted by 25th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Month-to-month company financial MIS of the company to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 20 th of every quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 10th of every month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Month-to-month company financial MIS of the company to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 10th of every month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 25th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Signed provisional financials, debtors ageing as on latest date to be provided",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock statement",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Monthly debtor Aging for all operating accounts to be submitted on or before the 10th of every subsequent calendar month",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statement in e-statement - quarterly by 25th of next month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "MoM MIS including profit and loss and Balance sheet to be submitted by 25th day of the following month for the previous monthly.",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging & Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "Bank Statement",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for the previous month for all the operating accounts by 10th of the current month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing to be submitted by 10th of every month",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Have we received Bank statements for the previous month for all the operating accounts by 10th of the current month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank and Debtor Ageing statement for all operating accounts to be submitted every quarter by 25th day of the subsequent month of the previous quarter from the date of signing of this Agreementâ.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "Bank Statement",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging  for all operating accounts to be submitted by 25th of next month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Stock statement for all operating accounts to be submitted by 10th of every month (starting from Julâ23).",
    "": "",
    "Standardization Name": "Stock Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 15th of every quarterly.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Aging & Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "Bank Statement",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR 3B returns, to be submitted by 25th day of the following month for the previous monthly.",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Every month new purchase orders to be verified along with the development.",
    "": "",
    "Standardization Name": "Purchase Order",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank and Debtor Ageing statement for all operating accounts to be submitted every quarter by 25th day of the subsequent month of the previous quarter from the date of signing of this Agreementâ.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "Bank Statement",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of the end of each quarter for the Tenure",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debt position to be submitted by 25th day of the following month for the previous monthly.",
    "": "",
    "Standardization Name": "Debts Position",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements for all operating accounts to be submitted by 10th of every month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 25th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 25th day of the following month for the previous monthly.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 25th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 20th of every quarter",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statement of all accounts by 10th of next month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statement of all accounts by 10th of next month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "MIS",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "GSTR3B returns for all operating accounts to be submitted by 25th of next month every quarter.",
    "": "",
    "Standardization Name": "GSTR-3B Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "quarterly Debtor Ag Ageing and Bank statements for all operating accounts to be submitted by the Borrower to the Lender by the 10th of every subsequent calendar month for every quarter",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "Bank Statement",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Drawings approval, project completion status should be checked monthly starting from AugÂ23",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "monthly Debtor Aging and Bank statements for all operating accounts to be submitted by the Borrower to the Lender by the 10th of every subsequent calendar month.",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "Bank Statement",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Have we received Bank statements for the previous month for all the operating accounts by 10th of the current month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Have we received Bank statements for the previous month for all the operating accounts by 10th of the current month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "monthly MIS for rental payments/receipts, any changes in contractual terms for proposed clients, or any debt raised by borrower to be provided by 10th of every month.",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank statements of all the operating accounts until May 2022, to be submitted by the Borrower.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 25th day of the following month for the previous quarter.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Bank Statements for all operating accounts to be submitted by 10th of every month",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "Debtor Ageing & Bank statements for all operating accounts to be submitted, by 25th day of the following month, for the previous quarterâ",
    "": "",
    "Standardization Name": "Debtor Ageing",
    "Standardization Name__1": "Bank Statement",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "MIS",
    "": "",
    "Standardization Name": "MIS Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  },
  {
    "Compliance Name": "monthly Bank statements for all operating accounts to be submitted on or before the 25th day of each month.",
    "": "",
    "Standardization Name": "Bank Statement",
    "Standardization Name__1": "",
    "Due Month": "",
    "Due Date": "",
    "Status": "To do"
  }
]






converted_dict = {}

for item in data:
    compliance_name = item["Compliance Name"]
    standardization_name = item["Standardization Name"]
    standardization_name_1 = item["Standardization Name__1"]
    
    if standardization_name_1:
        converted_dict[compliance_name] = (standardization_name, standardization_name_1)
    else:
        converted_dict[compliance_name] = standardization_name

print(json.dumps(converted_dict, indent=4))