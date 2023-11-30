import csv
import os
import tkinter as tk
from datetime import datetime
from tkinter import messagebox

def generate_financial_report():
    log_path = os.path.join('GUI', 'log.csv')
    finance_path = os.path.join('logs', 'finance.csv')
    total_revenue = 0

    with open(log_path, mode='r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        finance_rows = [row for row in reader if row[2] == 'fill_rx']

    with open(finance_path, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(finance_rows)

    for row in finance_rows:
        if len(row) >= 3 and '$' in row[4]:
            qty_price = row[4].split(' ')
            qty = int(qty_price[0].split('x')[0])
            price = float(qty_price[4].split('$')[1])
            total_revenue += price * qty
    
    messagebox.showinfo("Total Revenue", f"Total revenue from filled prescriptions: ${total_revenue}")


def generate_inventory_report(start_date, end_date):
    log_path = os.path.join('GUI', 'inventory.csv')
    report_path = os.path.join('logs', 'inventory_report.csv')

    # Function to parse date in MM/DD/YYYY format
    def parse_date(date_str):
        return datetime.strptime(date_str, '%m/%d/%Y')

    start_date = parse_date(start_date)
    end_date = parse_date(end_date)

    inventory_rows = []

    with open(log_path, mode='r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        next(reader, None)  # Skip the header row
        for row in reader:
            if len(row) >= 5:
                row_date = parse_date(row[3])
                if start_date <= row_date <= end_date:
                    inventory_rows.append(row)

    with open(report_path, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['ID_number', 'product_name', 'in_stock', 'date_added', 'date_expires', 'is_expired', 'price'])
        writer.writerows(inventory_rows)

    messagebox.showinfo("Inventory Report Generated", f"Inventory report for the period {start_date.strftime('%m/%d/%Y')} to {end_date.strftime('%m/%d/%Y')} has been generated and saved to {report_path}.")