one_week_expenses = [1000, 2000, 100, 20, 40, 400, 1500]
total_no_of_days = len(one_week_expenses)
total = sum(one_week_expenses)
average = total / total_no_of_days
print(f"Total expenses is {total}")
print(f"Avg expenses is {average:.2f}")