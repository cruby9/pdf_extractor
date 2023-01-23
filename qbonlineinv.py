import tabula
import openai_secret_manager

assert "quickbooks" in openai_secret_manager.get_services()
secrets = openai_secret_manager.get_secrets("quickbooks")

print(secrets)

# Read the CSV file
df = tabula.read_pdf(file_path, pages='all')[0]

# Extract the relevant data from the CSV file
data = []
for index, row in df.iterrows():
    invoice_number = row['Invoice Number']
    customer_name = row['Customer Name']
    item_name = row['Item Name']
    quantity = row['Quantity']
    price = row['Price']
    data.append({
        'invoice_number': invoice_number,
        'customer_name': customer_name,
        'item_name': item_name,
        'quantity': quantity,
        'price': price
    })

# Create a new invoice using the QuickBooks Online API
from quickbooks import QuickBooks
from quickbooks.objects import Invoice, Line, Customer

qb = QuickBooks(secrets["client_id"], secrets["client_secret"], secrets["refresh_token"], secrets["realm_id"], environment="sandbox")

invoice = Invoice()

# Set the customer name
customer = Customer.filter(DisplayName=data[0]['customer_name'], max_results=1, qb=qb)[0]
invoice.CustomerRef = customer.to_ref()

# Add line items to the invoice
for item in data:
    line_item = Line()
    line_item.Amount = item['price']
    line_item.Description = item['item_name']
    line_item.Quantity = item['quantity']
    invoice.Line.append(line_item)

invoice.save(qb=qb)

print("Invoice created with ID: %s and total amount: %s" % (invoice.Id, invoice.TotalAmt))
