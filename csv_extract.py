import csv
import tkinter as tk
from tkinter import filedialog

def extract_data(search_term, input_file, search_file, output_file):
  # Open the search file in read mode
  with open(search_file, 'r') as search_csv_file:
    # Create a CSV reader
    search_csv_reader = csv.reader(search_csv_file)
    
    # Extract the search terms from the first column of the search file
    search_terms = [row[0] for row in search_csv_reader]
    
  # Open the input file in read mode
  with open(input_file, 'r') as csv_in_file:
    # Create a CSV reader
    csv_reader = csv.reader(csv_in_file)
    
    # Open the output file in write mode
    with open(output_file, 'w', newline='') as csv_out_file:
      # Create a CSV writer
      csv_writer = csv.writer(csv_out_file)
      
      # Iterate over the rows in the input file
      for row in csv_reader:
        # Check if the search term is in the list of search terms
        if row[0] in search_terms:
          # If it is, write the row with the data you want to extract to the output file
          # Add a check to make sure the row has at least three elements
          if len(row) > 2:
            csv_writer.writerow([row[0], row[1], row[2]])

# Create a GUI window
root = tk.Tk()
root.withdraw()

# Ask the user to select the input and output files using a file browser window
input_file = filedialog.askopenfilename(title='Select the input CSV file')
search_file = filedialog.askopenfilename(title='Select the search CSV file')
output_file = filedialog.asksaveasfilename(title='Select the output CSV file')

# Extract the data
extract_data('apple', input_file, search_file, output_file)

