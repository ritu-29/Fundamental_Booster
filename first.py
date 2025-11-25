name = input("Please Enter your name : ")
age = int(input("Please Enter your age : "))
height = float(input("Please Enter your height in meters : "))  
fav_no = int(input("Please Enter your favourite number : "))

print("Thank you ! Here is the information we collected:")

print("Name:",name, "(Type :",type(name), "Memory Address :",id(name),")")
print("Age:" ,age, "(Type :" ,type(age), "Memory Address:",id(age),")")
print("Height:" ,height, "(Type :" ,type(height), "Memory Address:",id(height),")")
print("Fav_no:" ,fav_no, "(Type :" ,type(fav_no), "Memory Address:",id(fav_no),")")

b_date = 2025 - age
print("Your birth year is approximately:",b_date)

print("Thank you for using the personal Data Collector. Goodbye!")