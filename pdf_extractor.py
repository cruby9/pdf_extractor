# Import the required modules
import pdfplumber
import tkinter as tk
import pandas as pd
from tkinter import filedialog

# Create a Tkinter root window
root = tk.Tk()

# Hide the root window
root.withdraw()

# Open the file browser window to select the PDF
file_path = filedialog.askopenfilename()

# Open the pdf file
with pdfplumber.open(file_path) as pdf:
    # Read the first page
    page = pdf.pages[0]
    # Extract the table
    table = page.extract_table()
    # Create a DataFrame from the table
    df = pd.DataFrame(table[1:], columns=table[0])
    # Open the file browser window to select the output directory for the Excel file
    output_directory = filedialog.askdirectory()
    # Prompt the user to enter the name of the Excel file
    excel_file_name = input("Enter the name of the Excel file (without the '.xlsx' extension): ")
    # Construct the full file path for the Excel file
    excel_file_path = f"{output_directory}\\{excel_file_name}.xlsx"
    df.to_excel(excel_file_path, index=False)

print(df)













