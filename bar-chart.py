import matplotlib.pyplot as plt

# City names and their average temperatures
cities = ["New York", "Los Angeles", "London", "Tokyo"]
temperatures = [15, 20, 11, 16]

# Different colors for each bar
colors = ['blue', 'red', 'green', 'purple']

# Creating the bar chart
plt.figure(figsize=(10,6))
plt.bar(cities, temperatures, color=colors)
plt.title("Average Temperatures of Cities")
plt.xlabel("Cities")
plt.ylabel("Average Temperature (°C)")
plt.legend(cities)

# Saving the bar chart as a PNG file
plt.savefig("bar-chart.png")

# Optionally, display the bar chart
plt.show()
