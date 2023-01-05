# Import the required Module
import tabula
import tkinter as tk
from tkinter import filedialog
# Open the file browser window to select the PDF
file_path = filedialog.askopenfilename()
# Read a PDF File
df = tabula.read_pdf(file_path, pages='all')[0]
# convert PDF into CSV
tabula.convert_into(file_path, "iplmatch.csv", output_format="csv", pages='all')
print(df)