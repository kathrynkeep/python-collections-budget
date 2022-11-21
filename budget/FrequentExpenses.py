from . import Expense
import collections

expenses = Expense.Expenses()


read_expenses(expenses(data/spending_data.csv))

spending_categories = []

for expense in expenses.list
    spending_categories.append(expense.category)

spending_counter = collections.Counter(spending_categories)

most_common()
top5 = most_common(spending_counter(5))

ax.bar(categories, count)

ax.set_title('# of Purchases by Category')

plt.show()
