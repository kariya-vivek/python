import pylab as plt

# Data
labels = ["a", "b", "c", "d"]
sizes = [3, 8, 12, 10]
colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99"]  # Custom colors
explode = [0.1, 0, 0.1, 0]  # Explode slices 'a' and 'c'

# Pie chart
plt.pie(
    sizes,
    labels=labels,
    colors=colors,
    explode=explode,
    autopct='%1.1f%%',     # Show percentages
    shadow=True,           # Add shadow
    startangle=140,        # Rotate start angle
    wedgeprops={'width': 0.5}  # Donut-style width
)

plt.title("Enhanced Pie Chart")
plt.axis('equal')  # Equal aspect ratio ensures pie is drawn as a circle
plt.show()
