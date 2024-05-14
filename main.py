import csv
import argparse
import os
from customer_module import CustomerModule
from sales_module import SalesModule

# Initialize modules
# Initialize CustomerModule and SalesModule instances
customer_module = CustomerModule()
sales_module = SalesModule()

"""Displays a menu with options for the user to load/save data, 
add/delete records, search records, and generate reports.
"""
# Function to display the menu and handle user input
def display_menu():
    print('1. Load customer and sales records')
    print('2. Save customer records to CSV')
    print('3. Save sales records to CSV')
    print('4. Add a new customer')
    print('5. Add a new sales record')
    print('6. Search customers')
    print('7. Search sales records')
    print('8. Display sales records for a customer')
    print('9. Delete a sales record')
    print('10. Delete a customer and their sales records')
    print('11. Exit')
    print('12. Display monthly sales values and number of sales')
    print('13. Display monthly sales values and number of sales for a given customer')
    print('14. Display monthly sales values and number of sales for a given postcode')

    choice = input('Enter your choice: ')
    return choice


"""Main entry point for the program.

Loads customer and sales data from the provided file paths if given. 
Then displays a menu and handles user input in a loop until the user exits.
"""
def main(customers_file_path=None, sales_file_path=None):
    if customers_file_path and sales_file_path:
        customer_module.load_customers(customers_file_path)
        sales_module.load_sales(sales_file_path)

        """Displays a menu and handles user input in a loop to allow
    loading/saving data, adding/deleting records, searching, and generating reports.
    
    The menu options call functions in the CustomerModule and SalesModule 
    to perform the requested actions on the customer and sales data.
    
    Exits the loop when the user selects the exit option."""
while True:
        choice = display_menu()
        if choice == '1':
            customers_file_path = input('Enter customer records file path: ')
            sales_file_path = input('Enter sales records file path: ')
            customer_module.load_customers(customers_file_path)
            sales_module.load_sales(sales_file_path)
        elif choice == '2':
            file_path = input('Enter file path to save customer records: ')
            customer_module.save_customers_to_csv(file_path)
        elif choice == '3':
            file_path = input('Enter file path to save sales records: ')
            sales_module.save_sales_to_csv(file_path)
        elif choice == '4':
            customer_module.add_new_customer()
        elif choice == '5':
            sales_module.add_new_sales_record(customer_module.customers)
        elif choice == '6':
            search_query = input('Enter search string for customers: ')
            customer_module.search_customers(search_query)
        elif choice == '7':
            search_query = input('Enter search string for sales records: ')
            sales_module.search_sales_records(search_query)
        elif choice == '8':
            cust_id = input('Enter customer ID to display sales records: ')
            sales_module.display_sales_for_customer(cust_id)
        elif choice == '9':
            trans_id = input('Enter transaction ID to delete sales record: ')
            sales_module.delete_sales_record(trans_id)
        elif choice == '10':
            cust_id = input('Enter customer ID to delete customer and their sales records: ')
            customer_module.delete_customer(cust_id)
            sales_module.delete_sales_for_customer(cust_id)
        elif choice == '11':
            print('Exiting the program.')
            break
        else:
            print('Invalid choice. Please try again.')

# Command-line arguments handling
"""Parse command-line arguments and call main() to run the program.

This allows running the program with different input files by specifying them 
on the command line. Default to no input files if none provided.
"""
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Manage sales records.')
    parser.add_argument('customers_file', nargs='?', help='Customer records CSV file path')
    parser.add_argument('sales_file', nargs='?', help='Sales records CSV file path')
    args = parser.parse_args()

    main(args.customers_file, args.sales_file)
