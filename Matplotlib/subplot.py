import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [1,20,15,40,35]

plt.subplot(1,2,1) #row, column, index
plt.plot(x,y)
plt.title("Line Chart")

plt.subplot(1,2,2) #row, column, index
plt.bar(x,y)
plt.title("Bar Chart")

plt.tight_layout()

plt.show()