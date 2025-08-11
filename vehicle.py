from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    @abstractmethod
    def start_engine(self) -> str:
        pass

    @abstractmethod
    def stop_engine(self) -> str:
        pass

    def vehicle_info(self):
        return f"{self.year} {self.brand} {self.model}"

class Car(Vehicle):
    def start_engine(self):
        return f"{self.vehicle_info()} engine started with a key."

    def stop_engine(self):
        return f"{self.vehicle_info()} engine stopped."

class Truck(Vehicle):
    def start_engine(self):
        return f"{self.vehicle_info()} engine started with a heavy-duty switch."

    def stop_engine(self):
        return f"{self.vehicle_info()} engine shut down."

class ElectricMixin(Vehicle):
    def charge_battery(self):
        return f"{self.vehicle_info()} battery charging..."

class ElectricCar(Car, ElectricMixin):
    def start_engine(self):
        return f"{self.vehicle_info()} silently powers on."

    def stop_engine(self):
        return f"{self.vehicle_info()} powers off."
    
class Bus(Vehicle):
    def start_engine(self):
        return f"{self.vehicle_info()} engine started with a button."

    def stop_engine(self):
        return f"{self.vehicle_info()} engine stopped."

class Motorcycle(Vehicle):
    def start_engine(self):
        return f"{self.vehicle_info()} engine started with a kick."

    def stop_engine(self):
        return f"{self.vehicle_info()} engine turned off."  
          
class FleetManager:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles.append(vehicle)  

    def remove_vehicle(self, vehicle: Vehicle):
        if vehicle in self.vehicles:
            self.vehicles.remove(vehicle)
        else:
            raise ValueError("Vehicle not found in fleet.")

    def type_list(self):
        for vehicle in self.vehicles:
            print(f"- {vehicle.vehicle_info()} - vehicle type: {type(vehicle).__name__}") 

    def start_all_engines(self):
        for vehicle in self.vehicles:
            print(vehicle.start_engine())           