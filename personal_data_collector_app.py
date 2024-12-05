print("Welcome to the Interactive Personal Data Collector!\n")

current_year=2024
name=input("Please enter your name:")
age=int(input("Please enter your age:"))
height=float(input("Please enter your height:"))
number=int(input("Please enter your favourite number:"))

print("Thank you! Here is the information we collected:\n")

print(f"Name:{name} (Type: {type(name)}, Memory Address: {id(name)})")
print(f"Age:{age} (Type: {type(age)}, Memory Address: {id(age)})")
print(f"Height:{height} (Type: {type(height)}, Memory Address: {id(height)})")
print(f"Favourite Number:{number} (Type: {type(number)}, Memory Address: {id(number)})\n")

print(f"Your birth year is approximately : {current_year-age} (based on your age of {age})\n")

print("Thank you for using the Personal Data Collector. Goodbye!")