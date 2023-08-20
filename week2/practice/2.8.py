print("Travelling from City A to City B")

Time= int(input("Enter the amount of time u wanna get there in: "))
Longer= int(input("Define longer amount of time: "))
if (Time >= Longer):
    Price= int(input("Enter budget: "))
    Higher= int(input("Define pricey: "))
    if (Price >= Higher):
        print("Coach")
    else:
        print("Train")

else:
    Price= int(input("Enter budget: "))
    Higher= int(input("Define pricey: "))
    if (Price <= Higher):
        print("Red Eye Flight")
    else:
        print("Daytime Flight")

print("You've arrived!")