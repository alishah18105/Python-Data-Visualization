import matplotlib.pyplot as plt

provinces = ["Punjab", "Sindh", "KPK", "Balochistan"]
population = [127330000, 55640000, 40640000, 14560000]

plt.pie(population, labels=provinces, autopct='%1.1f%%', colors=["yellow", "lightblue", "lightgreen", "lightcoral", "lightskyblue"])
plt.show()