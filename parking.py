print("=================================")
print("    Smart Parking Management     ")
print("           System                ")
print("=================================")
Vehicle_number=input("Enter Your Vehicle_Number:")
print()
valid_slot=False
valid_duration=False
print(" Avaialble Vehicle Type Details:")
print("           1.Bike               ")
print("           2.Car                ")
print("           3.Auto               ")
Vehicle_type=int(input("Enter Your Vehicle Type:"))

if Vehicle_type == 1:
    print("Your Vehicle Type is BIKE.")
    user_vehicle_type="Bike"
    valid_vehicle=True
elif Vehicle_type == 2:
    print("Your Vehicle Type is CAR.")
    user_vehicle_type="Car"
    valid_vehicle=True
elif Vehicle_type == 3:
    print("Your Vehicle Type is AUTO.")
    user_vehicle_type="Auto"
    valid_vehicle=True
else:
    print("Invalid Type,Please choose 1 to 3")
    valid_vehicle=False
    
print()
print("Available Parking Type Details")
print("       1.Normal parking       ")
print("       2.Premium Parking      ")
parking_type=int(input("Select your Parking Type :"))

if parking_type == 1:
    print("Your Parking Type is , NORMAL.")
    user_parking_type="Normal"
    valid_parking=True
elif parking_type == 2:
    print("Your Parking type is, PREMIUM.")
    user_parking_type="Premium"
    valid_parking=True
else:
    print("Invalid Parking Number","Your Choice Between 1 or 2")
    valid_parking=False
    
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
        if Duration <=0:
            print("Invalid Duration! please enter a positive Number")
        elif Duration == 1 or Duration == 2:
            print("Your Parking Fee: ₹20")
            valid_duration=True
            parking_fee=20
        elif Duration == 3 or Duration == 4 or Duration == 5 :
            print("Your Parking Fee : ₹40")
            parking_fee=40
            valid_duration=True
        elif Duration >= 6:
            print("Your Parking Fee : ₹60")
            parking_fee=60
            valid_duration=True
        else:
            print("Invalid Hours")
    
    elif Vehicle_type == 2:
        print("=================================")
        print("  YOUR VEHICLE TYPE IS CAR.     ")
        print("=================================")
        Duration = int(input("Enter Parking Duration(In Hours)"))
        if Duration <=0:
            print("Invalid Duration! please enter a positive Number")
        elif Duration == 1 or Duration == 2:
            print("Your Parking Fee: ₹40")
            parking_fee=40
            valid_duration=True
        elif Duration == 3 or Duration == 4 or Duration == 5 :
            print("Your Parking Fee : ₹80")
            parking_fee=80
            valid_duration=True
        elif Duration >= 6 :
            print("Your Parking Fee : ₹120")
            parking_fee=120
            valid_duration=True
        else:
            print("Invalid Hours")
    
    elif Vehicle_type == 3:
        print("=================================")
        print("  YOUR VEHICLE TYPE IS AUTO.     ")
        print("=================================")
        Duration = int(input("Enter Parking Duration(In Hours)"))
        if Duration <=0:
            print("Invalid Duration! please enter a positive Number")
        elif Duration == 1 or Duration == 2:
            print("Your Parking Fee : ₹30")
            parking_fee=30
            valid_duration=True
        elif Duration == 3 or Duration == 4 or Duration == 5 :
            print("Your Parking Fee  : ₹60")
            parking_fee=60
            valid_duration=True
        elif Duration >= 6 :
            print("Your Parking Fee : ₹90")
            parking_fee=90
            valid_duration=True
        else:
            print("Invalid Hours")

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
        if Duration <=0:
            print("Invalid Duration! please enter a positive Number")
        elif Duration == 1 or Duration == 2:
            premium_fee= bike_parking_fee1 + 50
            print("Your Parking Fee:","₹",premium_fee)
            bike_premium_fee1=premium_fee   
            parking_fee=premium_fee
            valid_duration=True
        elif Duration == 3 or Duration == 4 or Duration == 5 :
            premium_fee= bike_parking_fee2 + 50
            print("Your Parking Fee:","₹",premium_fee)
            bike_premium_fee2=premium_fee
            parking_fee=premium_fee
            valid_duration=True
        elif Duration >= 6:
            premium_fee= bike_parking_fee3 + 50
            print("Your Parking Fee:","₹",premium_fee)
            bike_premium_fee3=premium_fee
            parking_fee=premium_fee
            valid_duration=True
        else:
            print("Invalid Hours")
    
    elif Vehicle_type == 2:
        print("=================================")
        print("  YOUR VEHICLE TYPE IS CAR.     ")
        print("=================================")
        Duration = int(input("Enter Parking Duration(In Hours)"))
        if Duration <=0:
            print("Invalid Duration! please enter a positive Number")
        elif Duration == 1 or Duration == 2:
            premium_fee= car_parking_fee1 + 50 
            print("Your Parking Fee:","₹",premium_fee)
            car_premium_fee1=premium_fee
            parking_fee=premium_fee
            valid_duration=True
        elif Duration == 3 or Duration == 4 or Duration == 5 :
            premium_fee= car_parking_fee2 + 50 
            print("Your Parking Fee:","₹",premium_fee)
            car_premium_fee2=premium_fee
            parking_fee=premium_fee
            valid_duration=True
        elif Duration >= 6 :
            premium_fee= car_parking_fee3 + 50
            print("Your Parking Fee:","₹",premium_fee)
            car_premium_fee3=premium_fee
            parking_fee=premium_fee
            valid_duration=True
        else:
            print("Invalid Hours")
    
    elif Vehicle_type == 3:
        print("=================================")
        print("  YOUR VEHICLE TYPE IS AUTO.     ")
        print("=================================")
        Duration = int(input("Enter Parking Duration(In Hours)"))
        if Duration <=0:
            print("Invalid Duration! please enter a positive Number")
        elif Duration == 1 or Duration == 2:
            premium_fee= auto_parking_fee1 + 50
            print("Your Parking Fee:","₹",premium_fee)
            auto_premium_fee1=premium_fee
            parking_fee=premium_fee
            valid_duration=True
        elif Duration == 3 or Duration == 4 or Duration == 5 :
            premium_fee= auto_parking_fee2 + 50 
            print("Your Parking Fee:","₹",premium_fee)
            auto_premium_fee2=premium_fee
            parking_fee=premium_fee
            valid_duration=True
        elif Duration >= 6 :
            premium_fee= auto_parking_fee3 + 50 
            print("Your Parking Fee:","₹",premium_fee)
            auto_premium_fee3=premium_fee
            parking_fee=premium_fee
            valid_duration=True
        else:
            print("Invalid Hours")
print()
print()
print("=================================")
print("      AVAILABLE PARKING SLOT.    ")
print("=================================")
print("Bike       B01      B02     B03 ")
print("Car        C01      C02     C03  ")
print("Auto       A01      A02     A03  ")
print()
print()
if valid_vehicle == True:
    if Vehicle_type == 1:
        print("Available slots B01,B02,B03")
        parking_slot=input("Enter your Parking Slot:")
        slot=parking_slot.upper()
        if slot in ["B01","B02","B03"]:
            print("Bike slot Allocated")
            valid_slot=True
        else:
            print("Invalid Parking Slot")
            valid_slot=False
    elif Vehicle_type == 2:
        print("Available slots C01,C02,C03")
        parking_slot=input("Enter your Parking Slot:")
        slot=parking_slot.upper()
        if slot in ["C01","C02","C03"]:
            valid_slot=True
            print("Car slot Allocated")
        else:
            print("Invalid Parking Slot")
            valid_slot=False
    elif Vehicle_type == 3:
        print("Available slots A01,A02,A03")
        parking_slot=input("Enter your Parking Slot:") 
        slot=parking_slot.upper()
        if slot in ["A01","A02","A03"]:
            valid_slot=True
            print("Auto slot Allocated")
        else:
            print("Invalid Parking Slot")
            valid_slot=False

             
print()
print()
if (valid_parking == True) and (valid_vehicle == True) and (valid_slot == True) and (valid_duration == True):
    print("=================================")
    print("         PARKING RECEIPT.       ")
    print("=================================")
    print(f"Vehicle Number  : {Vehicle_number}")
    print(f"Vehicle Type    : {user_vehicle_type}")
    print(f"Parking Type    : {user_parking_type}")
    print(f"Duration(Hr)    : {Duration} Hr")
    print(f"Parking fee     : {parking_fee}")
    print(f"Parking slot    : {slot}")  
    print("----------------------------------")
    print(f"Final Amount    : {parking_fee} ")
    print("=================================")
    print("          Thank You.            " )
    print("=================================")

else:
    print("Invalid Details! Please Check Your Entered Details.")
    



    


