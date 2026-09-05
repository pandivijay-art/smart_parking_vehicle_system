print("=================================")
print("    Smart Parking Management     ")
print("           System                ")
print("=================================")
Vehicle_number=input("Enter Your Vehicle_Number:")
print()
print(" Avaialble Vehicle Type Details:")
print("           1.Bike               ")
print("           2.Car                ")
print("           3.Auto               ")
Vehicle_type=int(input("Enter Your Vehicle Type:"))

if Vehicle_type == 1:
    print("Your Vehicle Type is BIKE.")
elif Vehicle_type == 2:
    print("Your Vehicle Type is CAR.")
elif Vehicle_type == 3:
    print("Your Vehicle Type is AUTO.")
else:
    print("Invalid Type,Please choose 1 to 3")
print()
print("Available Parking Type Details")
print("       1.Normal parking       ")
print("       2.Premium Parking      ")
parking_type=int(input("Select your Parking Type :"))

if parking_type == 1:
    print("Your Parking Type is , NORMAL.")
elif parking_type == 2:
    print("Your Parking type is, PREMIUM.")
else:
    print("Invalid Parking Number","Your Choice Between 1 or 2")
print()
print()
print("=================================")
print("    SMART PARKING RATE CHART     ")
print("=================================")
print("Vehicle   1-2 Hrs  3-5Hrs   6+Hrs ")
print("---------------------------------")
print("Bike       ₹20      ₹40      ₹60 ")
print("Car        ₹40      ₹80      ₹120 ")
print("Auto       ₹30      ₹60      ₹90  ")
print("---------------------------------- ")
print("   Normal Parking : Basic Rate     ")
print("   Premium Parking : + ₹50 Extra   ")
print()
print()
if parking_type == 1:
    if Vehicle_type == 1:
        print("=================================")
        print("  YOUR VEHICLE TYPE IS BIKE.     ")
        print("=================================")
        Duration = int(input("Enter Parking Duration(In Hours)"))
        if Duration == 1 or Duration == 2:
            print("Your Parking Fee: ₹20")
        elif Duration == 3 or Duration == 4 or Duration == 5 :
            print("Your Parking Fee : ₹40")
        elif Duration >= 6:
            print("Your Parking Fee : ₹60")
        else:
            print("Invalid Hours")
    
    if Vehicle_type == 2:
        print("=================================")
        print("  YOUR VEHICLE TYPE IS CAR.     ")
        print("=================================")
        Duration = int(input("Enter Parking Duration(In Hours)"))
        if Duration == 1 or Duration == 2:
            print("Your Parking Fee: ₹40")
        elif Duration == 3 or Duration == 4 or Duration == 5 :
            print("Your Parking Fee : ₹80")
        elif Duration >= 6 :
            print("Your Parking Fee : ₹120")
        else:
            print("Invalid Hours")
    
    if Vehicle_type == 3:
        print("=================================")
        print("  YOUR VEHICLE TYPE IS AUTO.     ")
        print("=================================")
        Duration = int(input("Enter Parking Duration(In Hours)"))
        if Duration == 1 or Duration == 2:
            print("Your Parking Fee : ₹30")
        elif Duration == 3 or Duration == 4 or Duration == 5 :
            print("Your Parking Fee  : ₹60")
        elif Duration >= 6 :
            print("Your Parking Fee : ₹90")
        else:
            print("Invalid Hours")

else:
    print("Invalid  Vehicle Type! Please select a Valid Option (1 -3)")

bike_parking_fee1= 20
bike_parking_fee2= 40
bike_parking_fee3= 60

car_parking_fee1= 40
car_parking_fee2= 80
car_parking_fee3= 120

auto_parking_fee1= 30
auto_parking_fee2= 60
auto_parking_fee3= 90



if parking_type == 2:
    if Vehicle_type == 1:
        print("=================================")
        print("  YOUR VEHICLE TYPE IS BIKE.     ")
        print("=================================")
        Duration = int(input("Enter Parking Duration(In Hours)"))
        if Duration == 1 or Duration == 2:
            premium_fee= bike_parking_fee1 + 50; 
            print("Your Parking Fee:","₹",premium_fee)
            bike_premium_fee1=premium_fee    
        elif Duration == 3 or Duration == 4 or Duration == 5 :
            premium_fee= bike_parking_fee2 + 50; 
            print("Your Parking Fee:","₹",premium_fee)
            bike_premium_fee2=premium_fee
        elif Duration >= 6:
            premium_fee= bike_parking_fee3 + 50; 
            print("Your Parking Fee:","₹",premium_fee)
            bike_premium_fee3=premium_fee
        else:
            print("Invalid Hours")
    
    if Vehicle_type == 2:
        print("=================================")
        print("  YOUR VEHICLE TYPE IS CAR.     ")
        print("=================================")
        Duration = int(input("Enter Parking Duration(In Hours)"))
        if Duration == 1 or Duration == 2:
            premium_fee= car_parking_fee1 + 50; 
            print("Your Parking Fee:","₹",premium_fee)
            car_premium_fee1=premium_fee
        elif Duration == 3 or Duration == 4 or Duration == 5 :
            premium_fee= car_parking_fee2 + 50; 
            print("Your Parking Fee:","₹",premium_fee)
            car_premium_fee2=premium_fee
        elif Duration >= 6 :
            premium_fee= car_parking_fee3 + 50; 
            print("Your Parking Fee:","₹",premium_fee)
            car_premium_fee3=premium_fee
        else:
            print("Invalid Hours")
    
    if Vehicle_type == 3:
        print("=================================")
        print("  YOUR VEHICLE TYPE IS AUTO.     ")
        print("=================================")
        Duration = int(input("Enter Parking Duration(In Hours)"))
        if Duration == 1 or Duration == 2:
            premium_fee= auto_parking_fee1 + 50; 
            print("Your Parking Fee:","₹",premium_fee)
            auto_premium_fee1=premium_fee
        elif Duration == 3 or Duration == 4 or Duration == 5 :
            premium_fee= auto_parking_fee2 + 50; 
            print("Your Parking Fee:","₹",premium_fee)
            auto_premium_fee2=premium_fee
        elif Duration >= 6 :
            premium_fee= auto_parking_fee3 + 50; 
            print("Your Parking Fee:","₹",premium_fee)
            auto_premium_fee3=premium_fee
        else:
            print("Invalid Hours")

else:
    print("Invalid  Vehicle Type! Please select a Valid Option (1 -3)")

discount=int(input("Do You Have a Discount Cart?"))

if discount == 1:
    


