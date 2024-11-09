class Car:
    def __init__(self, make: str, model: str, year: int, price: float):
        self.make = make
        self.model = model
        self.year = year
        self.price = price

    def __str__(self):
        return f"{self.year} {self.make} {self.model} - ${self.price}"

class CarShowroom:
    def __init__(self):
        self.cars_for_sale = []

    def add_car(self, car: Car):
        self.cars_for_sale.append(car)

    def sell_car(self, car: Car):
        if car in self.cars_for_sale:
            self.cars_for_sale.remove(car)
            print(f"Car sold: {car}")
        else:
            print("Car not available for sale.")

    def __str__(self):
        if not self.cars_for_sale:
            return "No cars available for sale."
        return "Cars available for sale:\n" + "\n".join(str(car) for car in self.cars_for_sale)

# Приклад використання
showroom = CarShowroom()
car1 = Car("Toyota", "Camry", 2020, 24000)
car2 = Car("Honda", "Civic", 2018, 18000)

showroom.add_car(car1)
showroom.add_car(car2)

print(showroom)  # Показує доступні авто
showroom.sell_car(car1)  # Продає авто
print(showroom)  # Показує авто після продажу
