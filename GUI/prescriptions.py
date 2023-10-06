import csv

# define csv header to use to read/write/display prescriptions
FIELDNAMES = ["product_name","in_stock","price"]

def read_prescriptions(filename):
    prescriptions_dict = {}
    with open(filename, mode='r', newline='', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            prescriptions_dict[row["product_name"]] = row
    return prescriptions_dict
