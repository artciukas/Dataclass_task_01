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

    def total_cost(self):
        return self.price * self.quantity
    
    def object_list(self):
        pass

@dataclass
class Products(Product):
    products: List[Product]

    def print_list(self):
        return print(self.products)


product_one = Product(product_id=1, name='Phone', price=150.0, quantity=5)
product_two = Product(product_id=2, name='Tv', price=250.0, quantity=7)

Products.print_list()