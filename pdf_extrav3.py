import PyPDF2
import csv
import tkinter as tk
from tkinter import filedialog

# Create a Tkinter root window
root = tk.Tk()

# Hide the root window
root.withdraw()

# Open the file browser window to select the PDF
file_path = filedialog.askopenfilename()

# Open the PDF file
with open(file_path, "rb") as f:
    # Create a PDF object
    pdf = PyPDF2.PdfReader(f)

    # Extract the text from the PDF
    text = ""
    for page in pdf.pages:
        text += page.extract_text()

# Parse the layout of the PDF
layout = pdf.page_layout

# Extract the specific information you want from the layout
# This will depend on the specific format of the PDF and the information you want to extract
# You can use the layout object and the text object to navigate the PDF and extract the information you need

# Open the file browser window to select the output directory
directory = filedialog.askdirectory()

# Construct the full file path for the CSV file
csv_file_path = f"{directory}\\output.csv"

# Write the specific information you extracted to the CSV file
with open(csv_file_path, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([value1, value2, value3])


