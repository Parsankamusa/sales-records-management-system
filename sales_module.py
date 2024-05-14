import csv
from collections import defaultdict

class SalesModule:
    def __init__(self):
        self.sales = defaultdict(list)
        self.next_trans_id = 100000000

    def load_sales(self, file_path):
        with open(file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.sales[row['cust_id']].append(row)
# function to save the sales into the sales.csv file
    def save_sales_to_csv(self, file_path):
        with open(file_path, mode='w', newline='') as file:
            fieldnames = ['date', 'trans_id', 'cust_id', 'category', 'value']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for sales_records in self.sales.values():
                for sale_record in sales_records:
                    writer.writerow(sale_record)
# function to add the new sales 
    def add_new_sales_record(self, cust_id, date, category, value):
        if cust_id in self.sales:
            trans_id = str(self.next_trans_id)
            self.next_trans_id += 1
            new_sale = {
                'date': date,
                'trans_id': trans_id,
                'cust_id': cust_id,
                'category': category,
                'value': value
            }
            self.sales[cust_id].append(new_sale)
            print(f"Sales record added with Transaction ID: {trans_id}")
        else:
            print("Customer ID does not exist.")
# function to search the records
    def search_sales_records(self, search_query):
        search_query = search_query.lower()
        for sales_records in self.sales.values():
            for sale_record in sales_records:
                if (search_query in sale_record['date'].lower() or
                    search_query in sale_record['trans_id'] or
                    search_query in sale_record['cust_id'] or
                    search_query in sale_record['category'].lower() or
                    search_query in str(sale_record['value']).lower()):
                    print(f"Date: {sale_record['date']}, Transaction ID: {sale_record['trans_id']}, "
                          f"Customer ID: {sale_record['cust_id']}, Category: {sale_record['category']}, "
                          f"Value: {sale_record['value']}")
  # function to delete sales records
    def delete_sales_record(self, trans_id):
        for cust_id, sales_records in self.sales.items():
            for sale_record in sales_records:
                if sale_record['trans_id'] == trans_id:
                    sales_records.remove(sale_record)
                    print(f"Sales record with Transaction ID {trans_id} has been deleted.")
                    return
        print("Transaction ID not found.")

    def delete_sales_for_customer(self, cust_id):
        if cust_id in self.sales:
            del self.sales[cust_id]
            print(f"All sales records for Customer ID {cust_id} have been deleted.")
        else:
            print("Customer ID not found.")
