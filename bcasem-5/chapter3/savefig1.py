import pylab as plt

y1 = [2, 3, 4]
y2 = [1, 1.5, 5]

plt.plot(y1)
plt.plot(y2)

plt.legend(["team1", "team2"], loc="best")  # Options: 'center', 'left', 'right', etc.
plt.savefig("plot.jpg");#by default png
plt.show()

