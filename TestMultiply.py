# import numpy as np
import csv

with open('product_information.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    categories = []

    for row in csv_reader:
        area = row['division']
        if area not in categories:
            categories.append(area)
    
    print(categories)