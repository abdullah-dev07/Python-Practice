class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model 

    def display_info(self):
        print(f"make of vehicle: {self.make} and model of vehicle: {self.model}")


class Car(Vehicle):
    def __init__(self, make, model, number_of_doors):
        super().__init__(make, model)
        self.number_of_doors = number_of_doors
        
    def display_info(self):
        print(f"make of car: {self.make} and model of car: {self.model}")
        print(f"number of doors of car: {self.number_of_doors}")


class Motorcycle(Vehicle):
    def __init__(self, make, model, engine_cc):
        super().__init__(make, model)
        self.engine_cc = engine_cc

    def display_info(self):
        print(f"make of motorcycle: {self.make} and model of motorcycle: {self.model}")
        print(f"Motorcycle engine: {self.engine_cc}")



car = Car("toyota", 2024, 4)

car.display_info()


bike = Motorcycle("honda",2023, "125 CC")
bike.display_info()