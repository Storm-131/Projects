# ---------------------------------------------------------*\
# Title: BMI-Calculator
# Author: T. Maus (2022)
# ---------------------------------------------------------*/
#!/usr/bin/env python3

print("Welcome to the BMI-Calculator!")

while (1):
    height = input("Enter your height in m: ").replace(",", ".")
    weight = input("Enter your weight in kg: ").replace(",", ".")

    try:
        bmi = float(weight) / (float(height) ** 2)
        print(f"\nYour BMI is {round(bmi, 2)}\n")

        check = input("Do you want to calculate another BMI (y/n)?: ")

        if (check == "y"):
            continue
        else:
            break

    except:
        print(type(height))
        print(type(weight))
        print("Wrong Input, try again!")
        continue

print("Thanks for using the BMI-Calculator!")

# -------------------------Notes-----------------------------------------------*\
# This is a simple BMI-Calculator to be run in a terminal
# -----------------------------------------------------------------------------*\
