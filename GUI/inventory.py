import csv

# define csv header to use to read/write/display inventory
FIELDNAMES = ["ID_number", "product_name","in_stock","date_added","date_expires","is_expired"]

def read_inventory(filename : str)-> dict: 
    inventory_dict = {}
    with open(filename, mode='r', newline='', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            inventory_dict[row["ID_number"]] = row
    return inventory_dict


def write_inventory(filename : str, inventory_dict : dict)-> None: 
    with open(filename, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=FIELDNAMES)
        writer.writeheader()
        for value in inventory_dict.values():
            writer.writerow(value)

# # example of reading inventory from csv into dictionary
# inventory = read_inventory("inventory.csv")

# # example of adding product
# inventory["12"] = {"product_name" : "product12",
#                    "ID_number" : "12",
#                    "in_stock" : "15",
#                    "date_added" : "2023/9/27",
#                    "date_expires" : "2024/9/24",
#                    "is_expired" : "false"}

# # example of modifying product attribute
# inventory["1"]["in_stock"] = "17"

# # example of deleting product
# del(inventory["11"])

# # example of writing inventory to csv from dictionary
# write_inventory("products_output.csv", inventory)

# print("done")
