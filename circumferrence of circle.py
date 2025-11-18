import math

radius=float(input("Enter the raius of the circle:  "))
Area =  math.pi *pow( radius,2)
circumfuresnce=2*math.pi*radius
print(f"The circumferrence of the circle is: ", {round(circumfuresnce,2)})
print(f"The area of the circle is: ", {round(Area,2)})