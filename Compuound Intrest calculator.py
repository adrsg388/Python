Principal=0
Rate=0
Time=0

while Principal<=0:
    Principal=float(input("Enter your Principal Amount: "))
    if Principal<=0:
        print("Principal can't be zero:")

while Rate<=0:
    Rate=float(input("Enter your Intrest Rate: "))
    if Rate<=0:
        print("Interst Rate can't be zero:")

while Time<=0:
    Time=int(input("Enter your Time in year's: "))
    if Rate<=0:
        print("Time can't be zero:")

amount=Principal*((1+Rate/100))**Time
print(f"The Balance amount for {Time} year's is ${amount}")