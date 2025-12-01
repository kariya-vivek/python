import pylab as plt

x = [1, 2, 3, 4, 5]
y = [2, 5, 7, 1, 6]

plt.plot(x, y, 'o--b',
         markersize=10,
         markerfacecolor='yellow',
         markeredgecolor='red',
         markeredgewidth=2,
         linewidth=2)

plt.grid(True)
plt.xlabel("X Axis Label")
plt.ylabel("Y Axis Label")
plt.xlim(0, 6)
plt.ylim(0, 10)
plt.title("Demo Plot with All Features")
plt.show()
