import csv
import math

with open('predicted_sales.csv') as prediction:
    guess_data = csv.DictReader(prediction)

    item_list = []
    guess_sales = []

    for row in guess_data:
        id_number = int(row['product_id'])
        expected_sales = 7*float(row['expected_sales'])
        item_list.append(id_number)
        guess_sales.append(expected_sales)
    # guess_sales = 7*guess_sales
    # print(type(item_list[0]))

with open('simplified_sales.csv') as sales:
    real_data = csv.DictReader(sales)

    items_sold = []
    Errors = []

    for row in real_data:
        if row['product_id']:
            n = float(row['product_id'])
            # print(type(n))
            id_number = math.ceil(n)
            # print(type(id_number))
            if id_number in item_list:
                items_sold.append(id_number)
                index = item_list.index(id_number)
                A = float(row['units_sold'])
                F = guess_sales[index]
                error = 100*abs((A - F)/A)
                Errors.append(error)

# print(item_list[0])
# print(error)

with open('percentage_errors.csv', 'w') as file:
    writer = csv.writer(file)

    writer.writerow(['product_id', 'percentage_error'])

    for i in range(len(items_sold)):
        writer.writerow([items_sold[i], Errors[i]])