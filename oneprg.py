import matplotlib.pyplot as plt
months = ["jan","feb","mar","apr","may"]
sales = [250,270,260,300,210]
plt.plot(months,sales, color="blue",marker="o",linewidth=2)
plt.title("MONTHLY SALES REPORT")
plt.xlabel("MONTH")
plt.ylabel("SALES")
plt.savefig("MONTHLY SALES REPORT")
plt.show()