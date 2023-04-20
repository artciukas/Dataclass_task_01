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
    
    

@dataclass
class Products:
    products = []

    def add_product(self, product: Product) -> None:
        self.products.append(product)


    def print_list(self):
        for product in self.products:
            print(f"{product.product_id}, {product.name}, {product.price}, {product.quantity}")
        


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

product.print_list()
# print(product.products)