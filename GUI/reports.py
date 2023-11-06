import csv
import os

def generate_financial_report():
    log_path = os.path.join('logs', 'log.csv')
    total_revenue = 0

    with open(log_path, mode='r', newline='', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if row[1] == 'fill_rx':
                price = float(row[2].split('$')[1])
                total_revenue += price

    print(f'Total revenue from filled prescriptions: ${total_revenue}')
