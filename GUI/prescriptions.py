import csv

# define csv header to use to read/write/display prescriptions
FIELDNAMES = ["product_name","in_stock","price"]

def read_prescriptions(filename):
    prescriptions_list = []
    with open(filename, mode='r', newline='', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            prescriptions_list.append(row)
    return prescriptions_list
