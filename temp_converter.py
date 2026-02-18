try:
    temp_f = float(input("Enter temperature in Fahrenheit: "))
    temp_c = (temp_f - 32) * 5/9
    print(f"{temp_f}F is {temp_c:.2f}C")
except ValueError:
    print("Please enter a valid number.")
