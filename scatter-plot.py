import matplotlib.pyplot as plt

# Data for heights and weights
heights = [160, 165, 170, 175, 180, 185, 190, 195, 200, 205]
weights = [60, 65, 70, 75, 80, 85, 90, 95, 100, 105]

# Creating the scatter plot
plt.scatter(heights, weights)
plt.xlabel('Height')
plt.ylabel('Weight')
plt.title('Height vs Weight')

# Saving the plot
plt.savefig('scatter-plot.png')