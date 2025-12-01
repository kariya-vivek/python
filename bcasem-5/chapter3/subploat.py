import pylab as plt

# Common x values
x = [1, 2, 3, 4, 5]

plt.figure()

# Subplot 1
y = [1, 2, 3, 4, 5]
plt.subplot(2, 3, 1)
plt.plot(x, y)
plt.title("Plot 1")

# Subplot 2
y = [2, 4, 6, 8, 10]
plt.subplot(2, 3, 2)
plt.plot(x, y)
plt.title("Plot 2")

# Subplot 3
y = [5, 4, 3, 2, 1]
plt.subplot(2, 3, 3)
plt.plot(x, y)
plt.title("Plot 3")

# Subplot 4
y = [1, 3, 5, 7, 9]
plt.subplot(2, 3, 4)
plt.plot(x, y)
plt.title("Plot 4")

# Subplot 5
y = [0, 1, 0, 1, 0]
plt.subplot(2, 3, 5)
plt.plot(x, y)
plt.title("Plot 5")

# Subplot 6
y = [10, 8, 6, 4, 2]
plt.subplot(2, 3, 6)
plt.plot(x, y)
plt.title("Plot 6")

# Add a super title for the whole figure
plt.suptitle("My 2×3 Subplot Grid", fontsize=16)

plt.show()
