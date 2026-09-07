import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [1,20,15,40,35]

fig, ax = plt.subplots(1,2,figsize=(10,5)) #row, column, figsize=(width, height)

ax[0].plot(x,y, color='purple')
ax[0].set_title("Line Chart")

ax[1].bar(x,y, color='orange')
ax[1].set_title("Bar Chart")

fig.suptitle("Line Chart and Bar Chart", fontsize=16)
plt.tight_layout()
plt.show()

