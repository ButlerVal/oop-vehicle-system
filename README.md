        🚗 Vehicle Management System

A Python project showcasing Object-Oriented Programming (OOP) principles such as abstraction, inheritance, polymorphism, and multiple inheritance through a Vehicle base class and specialized subclasses, managed by a FleetManager.


📂 Project Structure
oop-vehicle-system/
├── vehicle.py   # Defines Vehicle, Car, Truck, ElectricCar, Bus, Motorcycle, ElectricMixin, and FleetManager classes

├── main.py      # Entry point with user input to demonstrate vehicle functionality

├── README.md    # Project documentation

🎯 Features

Abstract Base Class: Vehicle enforces a common interface for all vehicle types.
Subclasses: Car, Truck, Bus, Motorcycle, and ElectricCar with unique behaviors.
Multiple Inheritance: ElectricCar combines Car and ElectricMixin for battery-charging functionality.
Polymorphism: Shared methods (start_engine, stop_engine) behave differently per vehicle type.
FleetManager: Manages a collection of vehicles with add, remove, list, and engine-start capabilities.
User Input: main.py accepts user input for vehicle brand, model, and year.

🛠️ How to Run

Clone the repository:git clone https://github.com/ButlerVal/oop-vehicle-system.git
cd oop-vehicle-system


Run the project:python main.py


Enter vehicle details (brand, model, year) when prompted.

Example Output
Enter vehicle brand: Toyota
Enter vehicle model: Camry
Enter vehicle year: 2021
---Starting and Stopping Engines---
2021 Toyota Camry engine started with a key.
2021 Toyota Camry engine stopped.
2021 Toyota Camry engine started with a heavy-duty switch.
2021 Toyota Camry engine shut down.
2021 Toyota Camry silently powers on.
2021 Toyota Camry powers off.
2021 Toyota Camry engine started with a button.
2021 Toyota Camry engine stopped.
2021 Toyota Camry engine started with a kick.
2021 Toyota Camry engine turned off.
2021 Toyota Camry battery charging...
---Fleet Manager Vehicle List---
- 2021 Toyota Camry - vehicle type: Car
- 2021 Toyota Camry - vehicle type: Truck
- 2021 Toyota Camry - vehicle type: ElectricCar
- 2021 Toyota Camry - vehicle type: Bus
- 2021 Toyota Camry - vehicle type: Motorcycle
---Starting All Engines---
2021 Toyota Camry engine started with a key.
2021 Toyota Camry engine started with a heavy-duty switch.
2021 Toyota Camry silently powers on.
2021 Toyota Camry engine started with a button.
2021 Toyota Camry engine started with a kick.

📜 Class Overview

Vehicle: Abstract base class with start_engine, stop_engine, and vehicle_info methods.
Car: Standard vehicle with key-based engine start/stop.
Truck: Heavy-duty vehicle with switch-based engine start/stop.
Bus: Large vehicle with button-based engine start/stop.
Motorcycle: Two-wheeled vehicle with kick-based engine start/stop.
ElectricMixin: Adds battery-charging capability.
ElectricCar: Inherits from Car and ElectricMixin for electric vehicle behavior.
FleetManager: Manages vehicle collections with methods to add, remove, list, and start all vehicle engines.

💡 Future Enhancements

Add more vehicle types (e.g., HybridVehicle).
Implement data persistence using JSON or CSV.
Create a command-line interface (CLI) for interactive fleet management.
Develop a web or GUI interface for enhanced usability.

🏷️ Topics

Python
Object-Oriented Programming
Inheritance
Polymorphism
Abstract Classes
Multiple Inheritance

📄 License
This project is licensed under the MIT License — see the LICENSE file for details.