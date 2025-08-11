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
    
    
