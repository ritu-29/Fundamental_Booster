# Personal Data Collector -- README

This project is a simple Python program that collects basic personal
information from the user and displays useful details such as data type
and memory address.

------------------------------------------------------------------------

## 📌 Features of the Python Script

### 1. **User Input**

The program asks the user to enter: - Name (string) - Age (integer) -
Height in meters (float) - Favourite number (integer)

------------------------------------------------------------------------

## 🧠 Type Casting (Simple Explanation)

Python's `input()` function always returns a **string**.\
To use numbers in calculations, we convert them into the correct type:

-   `int()` → converts to integer\
-   `float()` → converts to decimal value

Example from the script:

``` python
age = int(input("Please Enter your age : "))
height = float(input("Please Enter your height in meters : "))
fav_no = int(input("Please Enter your favourite number : "))
```

This ensures age, height, and favourite number are used correctly as
numbers.

------------------------------------------------------------------------

## 🧠 Memory Address (Simple Explanation)

Every value stored in Python has a unique **memory location**.\
Using `id(value)` tells us **where the value is stored in memory**.

Example:

``` python
id(age)
```

This returns a unique number showing the internal memory location of the
variable.

------------------------------------------------------------------------

## 🔢 Birth Year Calculation

The program calculates birth year using:

    b_date = 2025 - age

### Short Explanation:

2.  The age entered by the user is subtracted from the current
    year (2025) to estimate the birth year.\
3.  This gives an approximate birth year, assuming the user already had
    their birthday this year.

------------------------------------------------------------------------

## 🧩 Complete Python Code

``` python
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
```

------------------------------------------------------------------------

## 📥 Download the README File

The README.md file has been generated for download below.
