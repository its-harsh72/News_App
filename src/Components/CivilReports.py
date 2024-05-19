import re
import requests
import PyPDF2
import csv
from tkinter import filedialog
import tkinter as tk

def extract_text_from_pdf(url):
    response = requests.get(url)
    with open('downloaded_pdf.pdf', 'wb') as file:
        file.write(response.content)

    text = ""
    with open('downloaded_pdf.pdf', 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

def extract_company_name_and_rank(text):
    company_name = None
    rank = None
    # Look for the line containing "Search Criteria:"
    search_criteria_match = re.search(r'Search Criteria:\s*(.*?),', text)
    if search_criteria_match:
        company_name = search_criteria_match.group(1).strip()
    # Look for the line containing "Rank"
    rank_match = re.search(r'Rank\s+(\w+-\d+)', text)
    if rank_match:
        rank = rank_match.group(1)
    return company_name, rank

def find_numeric_values_and_amounts(text):
    matches = re.findall(r'(Total\s*-\s*#\d+)\s*₹([\d,]+)', text)
    return matches

def print_max_numeric_value_and_amount(numeric_values_and_amounts):
    if numeric_values_and_amounts:
        max_value = max(int(value[0].split('#')[-1]) for value in numeric_values_and_amounts)
        associated_amount = None
        for value in numeric_values_and_amounts:
            if int(value[0].split('#')[-1]) == max_value:
                associated_amount = "₹"+  value[1]
                break
        return "#" + str(max_value), associated_amount
    else:
        return "No numeric values found.", None

def find_total_after_enquiry_summary(text):
    # Search for the pattern "5. Enquiry Summary" followed by "Total"
    pattern = r'5\. Enquiry Summary.*?Total\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)'
    match = re.search(pattern, text, re.DOTALL)
    
    if match:
        total_values = [int(value) for value in match.groups()]
        first_value = total_values[0] if len(total_values) > 0 else None
        second_value = total_values[1] if len(total_values) > 1 else None
        third_value = total_values[2] if len(total_values) > 2 else None
        fourth_value = total_values[3] if len(total_values) > 3 else None
        Total_Value = first_value+second_value + third_value+fourth_value 
        if Total_Value is not None:
            print("Fourth value after '5. Enquiry Summary':", Total_Value)
        else:
            print("Fourth value not found after '5. Enquiry Summary'.")
    else:
        print("Total not found after '5. Enquiry Summary'.")
    return Total_Value
def find_non_zero_overdue(text):
    # Search for all occurrences of "Overdue:" followed by a non-zero value
    pattern = r'Overdue:\s*(?!0(?:\.0+)?$)(\d+(?:\.\d+)?)'
    matches = re.findall(pattern, text)
    
    if matches:
        non_zero_overdue_values = [float(match) for match in matches if float(match) != 0.0]
        if non_zero_overdue_values:
            latest_dpd = find_latest_dpd(text)
            return non_zero_overdue_values, latest_dpd
        else:
            return "No Overdue.", None
    else:
        return "No 'Overdue:' values found.", None


def find_latest_dpd(text):
    matches = re.findall(r'[01] DPD', text)
    latest_dpd = matches[-1] if matches else "No DPD found"
    return latest_dpd


pdf_url = "https://myamo.amoga.io/non_prod/credable/2024/5/17/tooljet/GIFTS_PLANET_PRIVATE_LIMITED_CIBIL_3Evbvtl.pdf"

text = extract_text_from_pdf(pdf_url)

company_name, rank = extract_company_name_and_rank(text)

numeric_values_and_amounts = find_numeric_values_and_amounts(text)

max_value, associated_amount = print_max_numeric_value_and_amount(numeric_values_and_amounts)

Total_Value = find_total_after_enquiry_summary(text)
print("Total_Value",Total_Value)

overdue_values, latest_dpd = find_non_zero_overdue(text)

root = tk.Tk()
root.withdraw()  


file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])


rows = [
        ["Company Name", "Rank", "Max Value", "Associated Amount (₹)", "Enquiry Summary'", "Overdue", "Latest DPD"],
        [company_name, rank, max_value, associated_amount, Total_Value, overdue_values, latest_dpd]
    ]


with open(file_path, mode='w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerows(rows)

print("CSV file generated successfully at:", file_path)
