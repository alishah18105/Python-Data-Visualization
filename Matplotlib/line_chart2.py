import matplotlib.pyplot as plt

x= ["Mon", "Tues", "Wed", "Thurs", "Fri"]
y = [10, 15, 7, 20,12]

plt.plot(x,y)

plt.title("Bakery Sales Of This Week")
plt.xlabel("Days")
plt.ylabel("Number of Sales")

plt.show()