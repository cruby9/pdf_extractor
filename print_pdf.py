import csv
import tkinter as tk
import re
from tkinter import filedialog
from tkinter import messagebox
import PyPDF2

# Create a Tkinter root window
root = tk.Tk()

# Hide the root window
root.withdraw()

# Open the file browser window to select the PDF
file_path = filedialog.askopenfilename()

# Open the PDF file in binary mode
with open(file_path, "rb") as f:
    # Create a PDF object
    pdf = PyPDF2.PdfReader(f)

    # Extract the text from the PDF
    text = ""
    for page in pdf.pages:
        text += page.extract_text()
print(f"PDF text: {text}")

# Open the file browser window to select the search terms CSV file
csv_file_path = filedialog.askopenfilename()

# Read the search terms from the CSV file
search_terms = []
with open(csv_file_path, 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        search_terms.append(row[0])
print(search_terms)

# Set the minimum number of characters to extract
min_chars = 10

for term in search_terms:
    # Use regex to find all matches for the term in the text object
    matches = re.finditer(term, text)
    extracted_values = []
    for match in matches:
        # Get the start and end indices of the match
        start_index = match.end()
        # Set the end index to the start index plus the minimum number of characters
        end_index = start_index + min_chars
        # Extract the text from the original string using the start and end indices
        extracted_text = text[start_index:end_index]
        # Append the extracted text to the list of extracted values
        extracted_values.append(extracted_text)
    # If no match is found, append an empty string
    if not extracted_values:
        extracted_values.append("")
print(f"Extracted values: {extracted_values}")



# Open the file browser window to select the output directory
directory = filedialog.askdirectory()

# Construct the full file path for the CSV file
csv_file_path = f"{directory}\\output.csv"

# Write the extracted values to the CSV file
with open(csv_file_path, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(extracted_values)







