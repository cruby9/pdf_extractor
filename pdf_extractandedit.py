import tkinter as tk
from tkinter import filedialog
import csv
import pytesseract
from pdf2image import convert_from_path
from tkinter import ttk

# Create a Tkinter root window
root = tk.Tk()

# Hide the root window
root.withdraw()

# Open the file browser window to select the PDF
file_path = filedialog.askopenfilename()

# Convert the PDF to a sequence of images
images = convert_from_path(file_path)

# Initialize an empty string
text = ""

# Iterate over the images
for image in images:
    # Extract the text from the image
    text += pytesseract.image_to_string(image)

# Split the text into lines
lines = text.split("\n")

# Get a sorted list of unique expressions
expressions = sorted(set(line.split(":")[0] for line in lines if ":" in line))

# Create a dialog window to select the expressions and columns
dialog = tk.Toplevel(root)
dialog.title("Select Expressions and Columns")

# Create a frame to hold the widgets
frame = ttk.Frame(dialog)
frame.pack(padx=10, pady=10)

# Create a scrollable frame to hold the list of widgets
scrollable_frame = ttk.Frame(frame)
scrollable_frame.pack(side="left", fill="both", expand=True)

# Create a canvas to hold the scrollable frame
canvas = tk.Canvas(scrollable_frame)
canvas.pack(side="left", fill="both", expand=True)

# Create a scrollbar to scroll the canvas
scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

# Set the canvas's scrollbar to the scrollbar
canvas.configure(yscrollcommand=scrollbar.set)

# Create a frame to hold the list of widgets
inner_frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=inner_frame, anchor="nw")

# Create a list of Checkbutton widgets for the expressions
checkbuttons = []
for expression in expressions:
    checkbutton = ttk.Checkbutton(inner_frame, text=expression, onvalue=True, offvalue=False)
    checkbutton.pack(anchor="w")
    checkbuttons.append(checkbutton)

# Create a Combobox widget for each expression to select the column
comboboxes = []
for i in range(len(expressions)):
    combobox = ttk.Combobox(inner_frame, state="readonly", values=list(range(1, len(expressions)+1)))
    combobox.current(i)
    combobox.pack(pady=5)
    comboboxes.append(combobox)

# Update the widget's height to show all the widgets
inner_frame.update_idletasks()

# Set the canvas's scrollregion to the size of the frame
canvas.configure(scrollregion=canvas.bbox("all"))

# Create an OK button to close the dialog
button = ttk.Button(dialog, text="OK", command=dialog.destroy)
button.pack(pady=10)

# Bind the "Return" key to the "OK" button's invoke method
dialog.bind("<Return>", lambda event: button.invoke())

# Wait for the dialog to be closed
root.wait_window(dialog)

# Get the selected columns
columns = [combobox.get() for combobox in comboboxes]

# Create a mapping of expressions to columns
expression_columns = {expression: int(column) - 1 for expression, column in zip(expressions, columns) if column}

# Set the default column for each expression
for i, expression in enumerate(expressions):
    if expression not in expression_columns:
        expression_columns[expression] = i

# Open the file browser window to select the directory to save the CSV file
directory = filedialog.askdirectory()

# Open the file browser window to select the name for the CSV file
csv_file_path = filedialog.asksaveasfilename(initialdir=directory, defaultextension=".csv")

# Write the text to a CSV file
with open(csv_file_path, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    for line in lines:
        row = [''] * len(expressions)
        for expression, i in expression_columns.items():
            # Split the line into two parts at the first occurrence of the expression
            parts = line.split(expression, 1)
            if len(parts) == 2:
                # Write the parts to the CSV file in the specified column
                row[i] = parts[1].strip()
        writer.writerow(row)
















