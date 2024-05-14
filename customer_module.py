import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import csv

class CustomerModule:
    def __init__(self):
        """Initializes the CustomerModule class.
        
        Sets up the dtype for the records array to store customer data. Initializes records as an empty array. Sets starting values for cust_id and trans_id counters. Defines a list of month names.
        """
        dtype = [('cust_id', 'U10'), ('name', 'U50'), ('postcode', 'U10'), ('phone_number', 'U20'),
                 ('date', 'U10'), ('trans_id', 'U10'), ('category', 'U20'), ('value', 'f')]
        self.records = np.zeros(1, dtype=dtype)
        self.next_cust_id = 100000
        self.next_trans_id = 100000000
        self.months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


        """Loads customer and sales data from a CSV file.
            
            The CSV file must have customer ID, name, postcode, phone number, 
            and transaction date headers. This appends new records to 
            self.records, generating cust_id and trans_id values.
            """
    def load_customers_and_sales(self, file_path):
        with open(file_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                self.records = np.append(self.records, [(row[0], row[1], row[2], row[3], None, None, None, None)], axis=0)

    def save_customers_and_sales_to_csv(self, file_path):
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['cust_id', 'name', 'postcode', 'phone_number', 'date', 'trans_id', 'category', 'value'])
            for record in self.records:
                writer.writerow(record[:-3])  # Write customer details excluding sales details

        """Adds a new customer record.
    
    Prompts the user to enter the customer's name, postcode, and phone number. 
    Generates a new cust_id value. Appends a new record to self.records with 
    the entered details and generated cust_id. Prints the cust_id.
    """
    def add_new_customer(self):
        name = input("Enter the customer's name (required): ")
        postcode = input("Enter the customer's postcode (optional): ")
        phone_number = input("Enter the customer's phone number (optional): ")
        cust_id = str(self.next_cust_id)
        self.next_cust_id += 1
        self.records = np.append(self.records, [(cust_id, name, postcode, phone_number, None, None, None, None)], axis=0)
        print(f"Customer added with ID: {cust_id}")

    """Adds a new sales record.
    
        Prompts the user to enter the sales date, category, 
        and value for the given customer ID. Generates a new 
        trans_id value. Appends a new record to self.records 
        with the entered sales details, generated trans_id, 
        and matching cust_id. Prints the trans_id. If no 
        matching cust_id is found, prints an error.
        """
    def add_new_sales_record(self, cust_id):
        date = input("Enter sales date (optional): ")
        category = input("Enter sales category (optional): ")
        value = input("Enter sales value (optional): ")
        trans_id = str(self.next_trans_id)
        self.next_trans_id += 1
        for i, record in enumerate(self.records):
            if record[0] == cust_id:
                self.records[i] = (record[0], record[1], record[2], record[3], date, trans_id, category, value)
                print(f"Sales record added with ID: {trans_id}")
                return
        print("Customer ID not found.")


        """Analyzes monthly sales performance.
    
    Filters for sales records, converts dates to datetime, 
    totals sales by month, and counts number of sales by month.
    
    Returns:
        monthly_totals: Total sales value for each month.
        monthly_counts: Number of sales for each month.
    """
    def analyze_sales_performance(self):
        sales_data = self.records[self.records[:, 4]!='']  # Filter for sales records
        sales_dates = [datetime.strptime(date, '%Y-%m-%d') for date in sales_data[:, 4]]
        monthly_totals = np.zeros(12)
        monthly_counts = np.zeros(12)
        
        for date, value in zip(sales_dates, sales_data[:, 7].astype(float)):
            monthly_totals[date.month - 1] += value
            monthly_counts[date.month - 1] += 1
        
        return monthly_totals, monthly_counts

        """Plots monthly sales performance.
    
    Plots total sales value and number of sales for each month.
    """
    def plot_monthly_sales_values(self):
        monthly_totals, monthly_counts = self.analyze_sales_performance()
        plt.figure(figsize=(10, 6))
        plt.plot(monthly_totals, label='Monthly Total Sales')
        plt.plot(monthly_counts, label='Monthly Number of Sales')
        plt.title('Monthly Sales Performance')
        plt.xlabel('Month')
        plt.ylabel('Value/Count')
        plt.legend()
        plt.xticks(range(12), self.months)
        plt.show()

        """Analyzes monthly sales for a customer.
    
    Filters for the customer's sales records, converts dates to datetime,
    totals sales by month, and counts number of sales by month.
    
    Args:
      cust_id: ID of customer to analyze.
      
    Returns:
      monthly_totals: Total sales value for each month.
      monthly_counts: Number of sales for each month.  
    """
    def plot_sales_by_customer(self, cust_id):
        sales_data = self.records[(self.records[:, 0]==cust_id) & (self.records[:, 4]!='')]
        sales_dates = [datetime.strptime(date, '%Y-%m-%d') for date in sales_data[:, 4]]
        monthly_totals = np.zeros(12)
        monthly_counts = np.zeros(12)
        
        for date, value in zip(sales_dates, sales_data[:, 7].astype(float)):
            monthly_totals[date.month - 1] += value
            monthly_counts[date.month - 1] += 1
        
        plt.figure(figsize=(10, 6))
        plt.plot(monthly_totals, label=f'Total Sales for Customer {cust_id}')
        plt.plot(monthly_counts, label=f'Number of Sales for Customer {cust_id}')
        plt.title('Monthly Sales Performance for Customer')
        plt.xlabel('Month')
        plt.ylabel('Value/Count')
        plt.legend()
        plt.xticks(range(12), self.months)
        plt.show()

        """Plots monthly sales performance for a given postcode.
        
        Filters for sales records matching the given postcode, converts dates to 
        datetime, totals sales by month, and counts number of sales by month.
        
        Args:
          postcode: Postcode to analyze sales for.
          
        Returns:
          None. Directly plots the monthly sales performance.
        """
    def plot_sales_by_postcode(self, postcode):
        sales_data = self.records[(self.records[:, 2]==postcode) & (self.records[:, 4]!='')]
        sales_dates = [datetime.strptime(date, '%Y-%m-%d') for date in sales_data[:, 4]]
        monthly_totals = np.zeros(12)
        monthly_counts = np.zeros(12)
        
        for date, value in zip(sales_dates, sales_data[:, 7].astype(float)):
            monthly_totals[date.month - 1] += value
            monthly_counts[date.month - 1] += 1
        
        plt.figure(figsize=(10, 6))
        plt.plot(monthly_totals, label=f'Total Sales for Postcode {postcode}')
        plt.plot(monthly_counts, label=f'Number of Sales for Postcode {postcode}')
        plt.title('Monthly Sales Performance for Postcode')
        plt.xlabel('Month')
        plt.ylabel('Value/Count')
        plt.legend()
        plt.xticks(range(12), self.months)
        plt.show()