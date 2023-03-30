import csv
import matplotlib.pyplot as plt
import numpy as np

with open('product_information.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    item_list = []
    categories = []

    for row in csv_reader:
        id_number = row['product_id']
        area = row['division']
        item_list.append(id_number)
        categories.append(area)

with open('percentage_errors.csv') as analysed_data:
    Data = csv.DictReader(analysed_data)

    items_sold = []
    errors = []

    for row in Data:
        id_number = row['product_id']
        e = row['percentage_error']
        items_sold.append(id_number)
        errors.append(e)

CoreBeauty = []
BeautyBrands = []
Ingenuity = []
Media = []
Nutrition = []
Clothing = []
Luxury = []
Packaging = []
Subscriptions = []
POD = []
Others = []

Divisions = ['Core Beauty', 'Beauty Brands', 'Ingenuity', 'Media Commerce', 'Nutrition', 'MP Clothing', 'Luxury', 'Packaging', 'Subscriptions', 'POD', 'Others']

for i in range(len(items_sold)):
    product = items_sold[i]
    if product in item_list:
        index = item_list.index(product)
        Area = categories[index]
        if Area=='Core Beauty':
            CoreBeauty.append(float(errors[i]))
        elif Area=='Beauty Brands':
            BeautyBrands.append(float(errors[i]))
        elif Area=='Ingenuity':
            Ingenuity.append(float(errors[i]))
        elif Area=='Media Commerce':
            Media.append(float(errors[i]))
        elif Area=='Nutrition':
            Nutrition.append(float(errors[i]))
        elif Area=='MP Clothing':
            Clothing.append(float(errors[i]))
        elif Area=='Luxury':
            Luxury.append(float(errors[i]))
        elif Area=='Packaging':
            Packaging.append(float(errors[i]))
        elif Area=='Subscriptions':
            Subscriptions.append(float(errors[i]))
        elif Area=='POD':
            POD.append(float(errors[i]))
        elif Area=='Others':
            Others.append(float(errors[i]))

sorted_errors = [CoreBeauty, BeautyBrands, Ingenuity, Media, Nutrition, Clothing, Luxury, Packaging, Subscriptions, POD, Others]
# sorted_errors = [np.array(errors) for errors in sorted_errors]

# print(type(CoreBeauty[0]))

fig, ax = plt.subplots()
for i, category in enumerate(Divisions):
    x = np.random.normal(i+1, 0.1, size=len(sorted_errors[i]))
    ax.scatter(x, sorted_errors[i], alpha=0.5)
ax.set_xticks(range(1, len(Divisions)+1))
ax.set_xticklabels(Divisions)
ax.set_xlabel('Division')
ax.set_ylabel('Percentage Error')
ax.set_ylim([0, 200])

# fig, ax = plt.subplots()
# fig = plt.figure(figsize =(10, 7))
# ax.boxplot(sorted_errors)
# ax.set_xticklabels(Divisions)
# ax.set_xlabel('Division')
# ax.set_ylabel('Percentage Error')
# ax.set_ylim([0, 200])

plt.show()