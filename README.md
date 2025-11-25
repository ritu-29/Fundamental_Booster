# Personal Data Collector (Python Program)

This project is a simple interactive Python program that collects user
information such as name, age, height, and favourite number.\
It then displays the details along with their **data types**, **type
casting behavior**, and **memory addresses (id values)**.

------------------------------------------------------------------------

## 📌 Features

-   Takes user input for:
    -   Name\
    -   Age\
    -   Height\
    -   Favourite Number\
-   Prints:
    -   Value\
    -   Data Type\
    -   Memory Address (`id()`)\
-   Calculates the approximate birth year.

------------------------------------------------------------------------

## 🧠 Type Casting Explanation

### **What is Type Casting?**

Type casting means **converting one datatype into another datatype**.

In this program: - `age` and `fav_no` are converted (cast) to
**integers** using `int()` - `height` is converted to **float** using
`float()` - `name` stays a **string** (no casting)

### **Why Type Casting is needed here?**

When a user types something in input(), Python receives it as **string**
by default.

Example:

    input("Enter age: ")

If user enters `25`, Python stores it as `"25"` (string).

To perform math operations (like birth year calculation), we convert it
using:

    age = int(input("Please Enter your age: "))
    height = float(input("Please Enter your height in meters: "))

------------------------------------------------------------------------

## 🧩 Memory Address Explanation

### **What is Memory Address?**

Every value stored in Python is saved somewhere in your computer's
memory.\
`id(variable)` gives the **unique memory address** where the value is
stored.

Example:

    x = 10
    print(id(x))

If two variables hold the same value:

    a = 10
    b = 10
    print(id(a), id(b))

Python optimizes memory, so **both may have the same address**.

This program prints memory addresses for: - Name\
- Age\
- Height\
- Favourite Number

So you can understand how Python stores data internally.

------------------------------------------------------------------------

## 🗂 Folder Structure

    project/
    │── first.py
    │── README.md

------------------------------------------------------------------------

## ▶️ How to Run

1.  Make sure Python is installed.
2.  Run the program:

```{=html}
<!-- -->
```
    python first.py

------------------------------------------------------------------------

## 📝 Example Input/Output

    Please Enter your name : Alice
    Please Enter your age : 25
    Please Enter your height in meters : 1.60
    Please Enter your favourite number : 7

    Thank you ! Here is the information we collected:
    Name: Alice (Type : <class 'str'> Memory Address : 140...)
    Age: 25 (Type : <class 'int'> Memory Address: 140...)
    Height: 1.6 (Type : <class 'float'> Memory Address: 140...)
    Fav_no: 7 (Type : <class 'int'> Memory Address: 140...)
    Your birth year is approximately: 2000
    Thank you for using the personal Data Collector. Goodbye!

------------------------------------------------------------------------

## 📦 Requirements

-   Python 3.6 or above

------------------------------------------------------------------------

## 📄 License

MIT License

------------------------------------------------------------------------

## 👤 Author

Created by Rituu Poonjani
