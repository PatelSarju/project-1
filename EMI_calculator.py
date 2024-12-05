product_price=int(input("Enter the product price:"))
annual_interest_rate=float(input("Enter the interest rate (in %):"))
year_duration=float(input("Enter the duration in year:"))

monthly_duration=12*year_duration
monthly_interest_rate=(annual_interest_rate/100)/12

EMI= product_price * monthly_interest_rate * (1+monthly_interest_rate)**monthly_duration / ((1+monthly_interest_rate)**monthly_duration-1)

print(f"\nYour Monthly EMI value is {EMI}!")