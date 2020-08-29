from openpyxl import load_workbook
import csv

wb = load_workbook(filename = 'Budget2020.xlsx')
sheet_ranges = wb['Totals']

def main():
  csv_file = sys.argv[1]
  with open(csv_file, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in csv_reader:
      print(', '.join(row))

main()

# print(sheet_ranges['C4'].value)