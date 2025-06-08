import matplotlib.pyplot as plt

monthly.plot(x='month', y='amount', kind='bar')
plt.title('Monthly Sales')
plt.ylabel('Sales Amount')
plt.show()