num_days=int(input("Please enter how many days you want to track your expenese"))
expenses=[]
for i in range (num_days):
    expense=float(input(f"Please enter how much expense day{i+1}="))
    expenses.append(expense)
    print(expenses)
    