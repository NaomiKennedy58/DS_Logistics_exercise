import matplotlib.pyplot as plt
import numpy as np
 
 
# Creating dataset
np.random.seed(10)
data1 = np.random.normal(100, 20, 200)
data2 = np.random.normal(100, 20, 200)

Data = [data1, data2]
 
fig = plt.figure(figsize =(10, 7))

print(type(data1[0]))
print(type(data2[0]))
 
# Creating plot
plt.boxplot(Data)
plt.get_figlabels()
 
# show plot
plt.show()