"""
Create a dataclass named "Product" that has the following attributes:
    product_id: int
    name: str
    price: float
    quantity: int
The class should also have a method named "total_cost" that calculates and returns the total cost of the product, 
which is the price multiplied by the quantity.
Create a list of Product objects and write a function that takes this list as input and returns the product with the highest total cost.

Write a program that creates a list of 5 Product objects, prints out their attributes, and then calls the function to find the product with the highest total cost.
"""
from typing import List
from dataclasses import dataclass

@dataclass
class Product:

    product_id: int
    name: str
    price: float
    quantity: int


@dataclass
class Products:
    products = []
    
    def total_cost(self, product: Product):
        return product.price * product.quantity

    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def get_max(self):
        highest_cost = 0
        for product in self.products:
            if self.total_cost(product) > highest_cost:
                highest_cost = self.total_cost(product)
                highest_cost_product = product.name
            else:
                continue
        return f"highest cost = {highest_cost} name of the product = {highest_cost_product}"
    

    def print_list(self):
        for product in self.products:
            print(f"Id: {product.product_id}, name: {product.name}, price: {product.price}, quantity: {product.quantity}")
        


product_01 = Product(product_id=1, name='Phone', price=150.0, quantity=5)
product_02 = Product(product_id=2, name='Tv', price=250.0, quantity=7)
product_03 = Product(product_id=3, name='Keyboard', price=15.0, quantity=52)
product_04 = Product(product_id=4, name='Mouse', price=30.0, quantity=15)
product_05 = Product(product_id=5, name='Radio', price=50.0, quantity=19)
product_06 = Product(product_id=6, name='PC', price=1500.0, quantity=3)

product = Products()
product.add_product(product_01)
product.add_product(product_02)
product.add_product(product_03)
product.add_product(product_04)
product.add_product(product_05)
product.add_product(product_06)

print(product.total_cost(product_01))
print(product.get_max())
# product.print_list()
# print(product.products)