principal_amount=int(input("Enter the principal amount:"))
interest_rate=int(input("Enter the interest rate (in %):"))
number_of_years=int(input("For how many years you borrow the amount:"))

interest_rate=interest_rate/100

simple_interest_value=principal_amount*interest_rate*number_of_years

print(f"The interest value is {simple_interest_value}!")
print(f"Total payable amount is {principal_amount+simple_interest_value}!")