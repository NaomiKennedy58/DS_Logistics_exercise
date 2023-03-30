import csv

with open('expected_sales.csv') as sales_Data:
    show_data = csv.DictReader(sales_Data)

    items_sold = []
    predicted_units_sold = []
    
    for row in show_data:
        if row['warehouse'] == 'omega':
            id_number = row['product_id']
            q = [float(row['expected_sales'])]
            items_sold.append(id_number)
            predicted_units_sold = predicted_units_sold + q
            # if id_number in items_sold:
            #     index = items_sold.index(id_number)
            #     units_sold[index] += float(row['quantity'])
            # elif row['quantity']:

with open('predicted_sales.csv', 'w') as file:
    writer = csv.writer(file)

    writer.writerow(['product_id', 'expected_sales'])

    for i in range(len(items_sold)):
        writer.writerow([items_sold[i], predicted_units_sold[i]])