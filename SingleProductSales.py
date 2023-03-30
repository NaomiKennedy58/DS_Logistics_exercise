import csv

with open('actual_sales.csv') as sales_Data:
    show_data = csv.DictReader(sales_Data)

    items_sold = []
    units_sold = []

    # row = next(show_data)

    
    for row in show_data:
        if row['warehouse'] == 'Omega':
            id_number = row['product_id']
            if id_number in items_sold and row['quantity']:
                index = items_sold.index(id_number)
                units_sold[index] += float(row['quantity'])
            elif row['quantity']:
                q = [float(row['quantity'])]
                items_sold.append(id_number)
                units_sold = units_sold + q
    # print(id_number)
    # print(items_sold)
    # print(units_sold)

with open('simplified_sales.csv', 'w') as file:
    writer = csv.writer(file)

    # writer.writerows(items_sold)

    writer.writerow(['product_id', 'units_sold'])

    for i in range(len(items_sold)):
        writer.writerow([items_sold[i], units_sold[i]])

    # for row in show_data:
    #     id_number = row['product_id']
    #     if id_number=="11068092.0":
    #         units_sold += float(row['quantity'])
    # print(units_sold)