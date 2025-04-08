class Car:
    total_car = 0
    def __init__(self,brand,model):
        self.__brand= brand
        self.__model= model
        Car.total_car+=1
    
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def get_brand(self):
        return self.__brand
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @property
    def model(self):
        return self.__model

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size

    def fuel_type(self):
        return "Electric Charge"

class Battery:
    def battery_info(self):
        return "This is battery"


class Engine:
    def engine_info(self):
        return "Engine Info"

class ElecCar(Battery,Engine,Car):
    pass

my_new_tesla = ElecCar("Tesla","Model S")

print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())

# my_car= Car("Tata","Safari")
# my_car.model= "City"

# print(my_car.model)


# my_tesla=ElectricCar("Tesla","V4","85KWH")

# print(my_tesla.fuel_type())
# safari =  Car("Tata","Safari")

# safariThree =  Car("Tata","Nexon")
# print(safari.fuel_type())

# print(Car.total_car)

# print(my_tesla.__brand)
# print(my_tesla.get_brand())

# my_car = Car("Toyota","Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())


# my_new_car = Car("Tata","Safari")
# print(my_new_car.brand)
# print(my_new_car.model)