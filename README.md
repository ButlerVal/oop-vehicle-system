# OOP Vehicle System

This project demonstrates core object-oriented programming concepts such as **inheritance**, **abstraction**, and **polymorphism** through a simple vehicle management system. It is designed for learning and experimenting with OOP principles in Python.

## Overview

- All vehicle types inherit from a common abstract base class (`Vehicle`).
- Each subclass overrides abstract methods to provide unique behaviors.
- Instances are created and managed in `main.py`, with a `main()` function called under the `if __name__ == "__main__":` block.
- The system is modular and easily extensible for new vehicle types or features.

## Usage

1. Clone the repository and navigate to the project folder.
2. Run the program using:
   ```
   python main.py
   ```
3. The script will create vehicle instances, add them to a fleet, and demonstrate engine operations and type listings.

## Class Breakdown

- **Vehicle (ABC)**: Abstract base class with common attributes (`brand`, `model`, `year`) and abstract methods for engine operations.
- **Car**: Inherits from `Vehicle`, implements engine start/stop with key.
- **Truck**: Inherits from `Vehicle`, implements heavy-duty engine operations.
- **Bus**: Inherits from `Vehicle`, engine operations via button.
- **Motorcycle**: Inherits from `Vehicle`, engine operations via kick.
- **ElectricMixin**: Provides battery charging functionality.
- **ElectricCar**: Combines `Car` and `ElectricMixin` for electric-specific behavior.
- **FleetManager**: Manages a collection of vehicles, supports adding, removing, listing, and batch engine operations.

## Future Feature Ideas

- Add support for saving/loading fleet data to/from files.
- Implement maintenance tracking for each vehicle.
- Add user interaction via command-line or GUI.
- Integrate vehicle statistics (e.g., mileage, fuel type).
- Expand with more vehicle types (e.g., Bicycle, Scooter).
- Add unit tests for all classes and methods.

---
This project is a solid foundation for exploring and expanding OOP