class ParkingSystem:
    def __init__(self, capacity):
        self.capacity = capacity
        self.parking_lot = {}

    def park(self, vehicle_number):
        if len(self.parking_lot) >= self.capacity:
            print("Parking lot is full.")
        else:
            if vehicle_number in self.parking_lot:
                print("Vehicle already parked.")
            else:
                self.parking_lot[vehicle_number] = True
                print("Vehicle parked successfully.")

    def retrieve(self, vehicle_number):
        if vehicle_number in self.parking_lot:
            del self.parking_lot[vehicle_number]
            print("Vehicle retrieved successfully.")
        else:
            print("Vehicle not found in the parking lot.")

    def check_availability(self):
        available_spaces = self.capacity - len(self.parking_lot)
        print(f"Available parking spaces: {available_spaces}/{self.capacity}")


# Create a parking system with a capacity of 5
parking_system = ParkingSystem(5)

# Park vehicles
parking_system.park("ABC123")  # Vehicle parked successfully.
parking_system.park("XYZ789")  # Vehicle parked successfully.
parking_system.park("DEF456")  # Vehicle parked successfully.

# Retrieve a vehicle
parking_system.retrieve("XYZ789")  # Vehicle retrieved successfully.

# Park a vehicle when the parking lot is full
parking_system.park("GHI789")  # Parking lot is full.

# Check parking availability
parking_system.check_availability()  # Available parking spaces: 2/5
