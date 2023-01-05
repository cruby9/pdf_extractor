import tkinter as tk
from tkinter import filedialog
import csv
import pytesseract
from pdf2image import convert_from_path

# Create a Tkinter root window
root = tk.Tk()

# Hide the root window
root.withdraw()

# Open the file browser window
file_path = filedialog.askopenfilename()

# Convert the PDF to a sequence of images
images = convert_from_path(file_path)

# Initialize an empty string
text = ""

# Iterate over the images
for image in images:
    # Extract the text from the image
    text += pytesseract.image_to_string(image)

# Open the file browser window
directory = filedialog.askdirectory()

# Construct the full file path for the CSV file
csv_file_path = f"{directory}\\text.csv"

# Write the text to a CSV file
with open(csv_file_path, 'a', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([text])









