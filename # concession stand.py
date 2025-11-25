# concession stand 

menu={"popcorn":600,
      "soda":300,
      "candy":200,
      "fries":400,
      "hotdog":500,
      "briyani":700,
      "burger":800,
      }
cart=[]
total=0
print("----------------MENU----------------")
for key,value in menu.items():
    print(f"{key:}: Rs{value}")
    
print("------------------------------------")

while True:
    food=input("Select the food item(q to quit): ").lower()
    if food=="q":
        break
    
    elif menu.get(food) is not None:
            
            cart.append(food)
print()

for items in cart:
    print(items,end=", ")
    total+=menu[items]

print(f"\nYour total bill is: Rs{total}")

