import csv

with open('62b7c5a8248128210ccffd4d_2022-12-10T04_00_11.565Z_earning_report.csv', 'r') as file1:
  # Read the first CSV file
  csv1 = csv.reader(file1)
  
  # Open the second CSV file in read-only mode
  with open('62b7c5a8248128210ccffd4d_2022-12-10T04_00_11.565Z_earning_report.csv', 'r') as file2:
    # Read the second CSV file
    csv2 = csv.reader(file2)
    
    # Compare the rows in the two files
    for row1, row2 in zip(csv1, csv2):
      # If the rows are different, print the differences
      if row1 != row2:
        print('Row differences:')
        print(row1)
        print(row2)