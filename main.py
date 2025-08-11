import vehicle

def main():
    # using user input to create vehicles
    brand = input("Enter vehicle brand: ")
    model = input("Enter vehicle model: ")
    try:
        year = int(input("Enter vehicle year: "))
    except ValueError:
        print("Invalid year. Setting to default 2020.")
        year = 2000
    
    # Create instances of each vehicle type
    car = vehicle.Car(brand, model, year)
    truck = vehicle.Truck(brand, model, year)
    electric_car = vehicle.ElectricCar(brand, model, year)
    bus = vehicle.Bus(brand, model, year)
    motorcycle = vehicle.Motorcycle(brand, model, year)

    # Start and stop engines for each vehicle
    print("---Starting and Stopping Engines---")
    print(car.start_engine())
    print(car.stop_engine())
    
    print(truck.start_engine())
    print(truck.stop_engine())
    
    print(electric_car.start_engine())
    print(electric_car.stop_engine())

    print(bus.start_engine())
    print(bus.stop_engine())    

    print(motorcycle.start_engine())
    print(motorcycle.stop_engine())
    
    # Charge the electric car's battery
    print(electric_car.charge_battery())

    manager = vehicle.FleetManager()

    print("\n---Fleet Manager Vehicle List---")
    manager.add_vehicle(car)
    manager.add_vehicle(truck)  
    manager.add_vehicle(electric_car)
    manager.add_vehicle(bus)
    manager.add_vehicle(motorcycle)
    manager.type_list()
    manager.start_all_engines()

if __name__ == "__main__":
    main()    