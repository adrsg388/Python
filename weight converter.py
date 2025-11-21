unit=input("Enter the unit lbs/kg: ")
weight=float(input("Enter the Weight: "))

if unit=="lbs":
    result = weight * 0.45
    print(f"Your Weight is {result} in kg")

elif unit == "kg":
    result = weight / 0.45
    print(f"Your Weight is {round(result,2)} in lbs")
else:
    print(f"Invalid unit")

