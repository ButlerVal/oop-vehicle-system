import vehicle

def main():
    # Create instances of each vehicle type
    car = vehicle.Car("Toyota", "Corolla", 2020)
    truck = vehicle.Truck("Ford", "F-150", 2019)
    electric_car = vehicle.ElectricCar("Tesla", "Model S", 2021)

    # Start and stop engines for each vehicle
    print(car.start_engine())
    print(car.stop_engine())
    
    print(truck.start_engine())
    print(truck.stop_engine())
    
    print(electric_car.start_engine())
    print(electric_car.stop_engine())
    
    # Charge the electric car's battery
    print(electric_car.charge_battery())

    manager = vehicle.FleetManager()

    manager.add_vehicle(car)
    manager.add_vehicle(truck)  
    manager.add_vehicle(electric_car)
    manager.type_list()
    manager.start_all_engines()

if __name__ == "__main__":
    main()    