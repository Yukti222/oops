
class Vehicle:
    def __init__(self, number_plate, brand_name):
        self.number_plate = number_plate
        self.brand_name = brand_name
        # Note: 'vehicle_type' ki zaroorat nahi kyunki class ka naam hi type bata raha hai.

class Motorcycle(Vehicle):
    def __init__(self, number_plate, brand_name, no_of_hours):
        # Parent class (Vehicle) ki properties ko inherit karne ke liye
        super().__init__(number_plate, brand_name)
        
        self.no_of_hours = no_of_hours
        # Yahan aap apna charge calculate karne ka logic likh sakte hain
        self.charge = self.no_of_hours * 10 

    def show_receipt(self):
        print(f"Motorcycle Parking Charge: Rs {self.charge}")

class Car(Vehicle):
    def __init__(self, number_plate, brand_name, no_of_hours):
        super().__init__(number_plate, brand_name)
        
        self.no_of_hours = no_of_hours
        # Yahan aap apna charge calculate karne ka logic likh sakte hain
        self.charge = self.no_of_hours * 20 

    def show_receipt(self):
        print(f"Car Parking Charge: Rs {self.charge}")




def main():
    print("--- Parking Toll System ---")
    
    # 1. User se base input lein
    v_type = input("What is the type of vehicle? (Type 'Car' or 'Motorcycle'): ")
    plate = input("Enter number plate: ")
    brand = input("Enter brand name: ")

    # 2. Condition check karein aur us hisaab se Object banayein
    if v_type == "Motorcycle":
        hours = int(input("How many hours do you want to park your motorcycle?: "))
        
        # Motorcycle class ka Object ban raha hai yahan:
        my_vehicle = Motorcycle(plate, brand, hours) 
        my_vehicle.show_receipt()

    elif v_type == "Car":
        hours = int(input("How many hours do you want to park your car?: "))
        
        # Car class ka Object ban raha hai yahan:
        my_vehicle = Car(plate, brand, hours)
        my_vehicle.show_receipt()

    else:
        print("Invalid Vehicle Type! Please enter Car or Motorcycle.")

# Python mein main program ko run karne ka standard tareeqa
if __name__ == "__main__":
    main()
