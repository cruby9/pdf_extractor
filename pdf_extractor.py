# Import the required Module
import tabula
import csv
import tkinter as tk
from tkinter import filedialog

# Create a Tkinter root window
root = tk.Tk()

# Hide the root window
root.withdraw()

# Open the file browser window to select the PDF
file_path = filedialog.askopenfilename()

# Read a PDF File
df = tabula.read_pdf(file_path, pages='all')[0]

# Open the file browser window to select the output directory for the CSV file
output_directory = filedialog.askdirectory()

# Prompt the user to enter the name of the CSV file
csv_file_name = input("Enter the name of the CSV file (without the '.csv' extension): ")

# Construct the full file path for the CSV file
csv_file_path = f"{output_directory}\\{csv_file_name}.csv"

# Convert the PDF to a CSV file
tabula.convert_into(file_path, csv_file_path, output_format="csv", pages='all')

# Read the CSV file into a list of rows
rows = []
with open(csv_file_path, 'r', newline='') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        # Split the text in each cell into separate columns based on the number of spaces
        columns = [column for column in row[0].split("  ") if column]
        rows.append(columns)

# Write the modified rows to the CSV file
with open(csv_file_path, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    for row in rows:
        writer.writerow(row)

print(df)











