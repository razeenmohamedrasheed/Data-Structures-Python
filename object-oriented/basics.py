class Car:
    def __init__(self,model,year,color,for_sale,price):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
        self.price = price

    def carDetails(self):
        return f"the brand is {self.model} from {self.year} with color {self.color} is rs {self.price} and is for sale {self.for_sale}"

car1 = Car("Honda Brio", 2020, "Red", True, 500000)
car2 = Car("Toyota Corolla", 2018, "Blue", False, 750000)
car3 = Car("Ford Mustang", 2021, "Black", True, 3000000)
car4 = Car("Hyundai i20", 2019, "White", True, 650000)
car5 = Car("Mercedes-Benz C-Class", 2022, "Silver", False, 4500000)

print(car1.carDetails())
print(car2.carDetails())
print(car3.carDetails())
print(car4.carDetails())
print(car5.carDetails())