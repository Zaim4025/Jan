    # def track_expenses():
    #     num_days=int(input("Please enter how many days you want to track your expenese"))
    #     expenses=[]
    #     for i in range (num_days):
    #         expense=float(input(f"Please enter how much expense day{i+1}="))
    #         expenses.append(expense)
    #         print(expenses)
    #         return expenses
    # track_expenses()
def celculator():        
    print("Welcome to my calculator.")
    print("Enter 1 to add.")
    print("Enter 2 to subtract.")
    print("Enter 3 to multipey.")
    print("Enter 4 to divid.") 
    user_input=int(input("Please enter your number."))
    def sum():
        first_number=int(input("Please enter first number."))
        second_number=int(input("Please enter second number."))
        add=first_number+second_number
        print(add)
    def subtract():
        first_number=int(input("Please enter first number."))
        second_number=int(input("Please enter second number."))
        subtract=first_number-second_number
        print(subtract)
    def multiply():
            first_number=int(input("PLease enter first number."))
            second_number=int(input("Please enter second number"))
            multiply=first_number*second_number
            print(multiply)
    def divid():
            first_number=int(input("Please enter first number."))
            second_number=int(input("Please enter second number."))
            divid=first_number/second_number
            print(divid)
    if user_input==1:
        sum()      
    elif  user_input==2:
        subtract() 
    elif user_input==3:
        multiply()
    elif  user_input==4:
        divid()  
    else:
        print("Wrong input!!!!")
celculator()              


                

                


        