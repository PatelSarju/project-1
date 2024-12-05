principal_amount=int(input("Enter the principal amount:"))
interest_rate=float(input("Enter the interest rate:"))
number_of_times=int(input("Enter the number of times interest is compounded per year:"))
number_of_years=int(input("For how many year you're borrowed the money:"))

# for convert the percentage into decimal
interest_rate=interest_rate/100

accumulated_value = principal_amount * (1+interest_rate/number_of_times)**(number_of_times*number_of_years)
interest_value=accumulated_value-principal_amount

print(f"Your interest value is {interest_value}!")
print(f"Your total payable amount is {accumulated_value}!")