import matplotlib.pyplot as plt

# Data
ages = [22, 25, 27, 22, 24, 26, 28, 30, 20, 23, 29, 31, 21, 25, 27, 26, 28, 22, 24, 30, 23, 29, 31, 20, 21, 27, 28, 22, 24, 26]

# Creating histogram
plt.hist(ages, bins=range(20, 33, 2), edgecolor='black')

# Labeling axes and title
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution')

# Saving the plot
plt.savefig('histogram.png')