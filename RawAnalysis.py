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
        # if area!='Packaging' & area!='Others':
        categories.append(area)

with open('raw_errors.csv') as analysed_data:
    Data = csv.DictReader(analysed_data)

    items_sold = []
    errors = []

    for row in Data:
        id_number = row['product_id']
        e = row['error']
        items_sold.append(id_number)
        errors.append(e)

CoreBeauty = []
BeautyBrands = []
Ingenuity = []
Media = []
Nutrition = []
Clothing = []
Luxury = []
# Packaging = []
Subscriptions = []
POD = []
# Others = []

Divisions = ['Core Beauty', 'Beauty Brands', 'Ingenuity', 'Media Commerce', 'Nutrition', 'MP Clothing', 'Luxury', 'Subscriptions', 'POD']

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
        # elif Area=='Packaging':
        #     Packaging.append(float(errors[i]))
        elif Area=='Subscriptions':
            Subscriptions.append(float(errors[i]))
        elif Area=='POD':
            POD.append(float(errors[i]))
        # elif Area=='Others':
        #     Others.append(float(errors[i]))

sorted_errors = [CoreBeauty, BeautyBrands, Ingenuity, Media, Nutrition, Clothing, Luxury, Subscriptions, POD]

fig, ax = plt.subplots()
for i, category in enumerate(Divisions):
    x = np.random.normal(i+1, 0.1, size=len(sorted_errors[i]))
    ax.scatter(x, sorted_errors[i], alpha=0.5)
ax.set_xticks(range(1, len(Divisions)+1))
ax.set_xticklabels(Divisions)
ax.set_xlabel('Division', fontsize=20)
ax.set_ylabel('Predicted Minus Actual Sales', fontsize=20)
ax.set_ylim([-50, 50])
fig.suptitle('Accuracy of Sales Predictions Across Divisions', fontsize=25)

plt.show()