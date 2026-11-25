import matplotlib.pyplot as plt

department = ["HR", "IT", "Sales", "Finance"]
salary = [25000, 40000, 30000, 35000]

plt.bar(department, salary)

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Salary")

plt.savefig("bar_chart.png")
plt.show()