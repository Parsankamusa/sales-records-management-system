Main Module Documentation
The main module provides the core logic to run the customer/sales record management program.

Overview
The key functions are:

display_menu() - Shows menu options and gets user input
main() - Main program logic
Usage
Run python main.py to start the program. Can optionally pass CSV file paths to load initial data.

python main.py customers.csv sales.csv

Functions
display_menu()
Shows a menu prompt and gets user selection.

Logic:

Print menu options
Get and return user input choice
Example Output:

1. Load records
2. Add customer
3. Quit

Enter your choice: 



main()
Main program logic.

Parameters:

customers_file_path - Optional path to customer CSV file
sales_file_path - Optional path to sales CSV file
Logic:

Initialize CustomerModule and SalesModule
If file paths provided, load initial data
Loop:
Show menu and get choice
Perform action based on choice
Exit on 'Quit'
Example Usage:

customer_mod = CustomerModule()
sales_mod = SalesModule()

main('customers.csv', 'sales.csv')



This loads the data, shows the menu, and processes actions until the user quits.

Imports
The main modules imports:

csv - for reading/writing CSV files
argparse - for parsing command line arguments
customer_module, sales_module - the modules containing the program logic
Command Line Arguments
Can specify customer/sales CSV files when running:

python main.py customers.csv sales.csv

Customer Module Documentation
Overview
The CustomerModule class in customer_module.py provides functionality to manage customer and sales records in Python.

It can load records from a CSV file, add new customers and sales through a CLI, save records back to CSV, and analyze monthly sales performance.

Usage
To use the module:

Create an instance of CustomerModule

Load customer/sales data from a CSV file using load_customers_and_sales()

Add new customers with add_new_customer()

Add new sales records with add_new_sales_record()

Save updated data to CSV with save_customers_and_sales_to_csv()

Analyze monthly sales with analyze_monthly_sales()

Methods
__init__()
Initializes the class instance:

Sets up dtype for records array
Initializes empty records array
Sets starting counters for IDs
Defines month name list
load_customers_and_sales()
Loads customer and sales data from a CSV file.

Parameters:

file_path: Path to CSV file
Logic:

Open file and create CSV reader
Skip header row
Append each row to records array
save_customers_and_sales_to_csv()
Saves customer and sales records to a CSV file.

Parameters:

file_path: Path to write CSV file
Logic:

Open file and create CSV writer
Write header row
Write each customer record (excluding sales details)
add_new_customer()
Adds a new customer by prompting user for details.

Logic:

Prompt for name, postcode, phone number
Generate new customer ID
Append new record to array
Print new customer ID
add_new_sales_record()
Adds new sales record for a customer.

Parameters:

cust_id: ID of customer
Logic:

Prompt for sales date, category, value
Generate new transaction ID
Find matching cust_id in records
Append new sales data to this record
Print new transaction ID
analyze_monthly_sales()
Analyzes sales performance by month.

Logic:

Filter records for sales
Convert dates to datetimes
Total and count sales for each month
Return monthly totals
Data Structures
records: NumPy structured array to store customer and sales data
months: List of month names for analyzing sales
Key Attributes
next_cust_id: Counter for generating customer IDs
next_trans_id: Counter for generating transaction IDs