import matplotlib.pyplot as plt

# Sales data for each month
months = range(1, 13)
sales = [150, 200, 250, 300, 350, 400, 300, 250, 200, 150, 100, 50]

# Creating the plot
plt.figure(figsize=(10, 6))
plt.plot(months, sales, marker='o')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)

# Saving the plot as PNG
plt.savefig('line-plot.png')

# Displaying the plot
plt.show()
