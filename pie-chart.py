import matplotlib.pyplot as plt

# Data to plot
labels = 'Apple', 'Samsung', 'Huawei', 'Others'
sizes = [30, 25, 20, 25]
colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen']

# Plotting the pie chart
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.

# Adding a legend
plt.legend(labels, loc="best")

# Saving the pie chart
plt.savefig('pie-chart.png')

plt.show()
