import csv
import os

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
            price = float(row[4].split('$')[1])
            total_revenue += price

    print(f'Total revenue from filled prescriptions: ${total_revenue}')
