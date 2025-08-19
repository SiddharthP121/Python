'''
 1. Write a Python script to read a CSV file with missing values and replace the
 missing values with a default value (e.g., "Unknown" or 0).
 Sample Data (missing_data.csv)
'''

import csv

with open('missing_data.csv', mode='r', newline='') as data:
    csv_data = csv.reader(data)
    header = next(csv_data)
    # rows = [row for row in csv_data]

    for row in csv_data:
        cleaned_row = []
        for index, value in enumerate(row):
            if value.strip():
                cleaned_row.append(value.strip())
            else:
                cleaned_row.append('0' if index == 1 else 'Unknown')
        print(cleaned_row)

# import csv

# def handle_missing_values(input_file, default_value):
#     with open(input_file, mode='r') as infile:
#         reader = csv.reader(infile)
#         rows = [row for row in reader]
    
#     # Replace missing values
#     updated_rows = []
#     for row in rows:
#         updated_row = [value if value != ' ' else default_value for value in row]
#         updated_rows.append(updated_row)
#         print(updated_row)
   
# handle_missing_values('missing_data.csv', 'Unknown')
        
    

