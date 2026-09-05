import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [1500, 1000, 2000, 3000]

plt.plot(x,y, color='blue', marker='o', linestyle='dashed', linewidth=2)
plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales in USD")
plt.xticks(x,["Jan", "Feb", "Mar", "Apr"])
plt.legend(loc='upper left', labels=["Sales"])
plt.grid(color = 'gray', linestyle = "--", linewidth = 0.5)
plt.xlim(0,5)
plt.ylim(0,4000)
plt.show()