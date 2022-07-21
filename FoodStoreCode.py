# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 13:32:28 2022

@author: Eminfe
"""

class FoodStore():
    
    def __init__(self):
        
        self.item_quantity = {}
        self.item_price = {}
        
        
    def add_item(self, items):
        
        for (item , quantity, price) in items:
            if item not in self.item_quantity:
                self.item_quantity[item] = quantity
            else:
                self.item_quantity[item] += quantity
            self.item_price[item] = price
            
        
    @property
    def show_stock(self):
        return self.item_quantity
    
    @property
    def show_quantity_price(self):
        result = {}
        for item, quantity in self.item_quantity.items():
            result[item] = self.item_price[item] * quantity
        return result
    
    def purchase_item(self, items):
        
        for (item , quantity) in items:
            if item not in self.item_quantity or item not in self.item_price:
                raise ValueError(("Item `{}` not found in stock.\nPlease place purchase order again.".format(item)))
            
            if quantity > self.item_quantity[item]:
                raise ValueError(("Not enough stock found for item `{}`.\nPlease place purchase order again.".format(item)))
            
            self.item_quantity[item] -= quantity
               
        
if __name__=="__main__":
    
    fs = FoodStore()
    fs.add_item([('Bread', 20,  2), 
                 ('Muffins', 50, 3), 
                 ('Cake', 30, 2.5), 
                 ('Cookies', 100, 0.5)])
    
    print("\n....WELCOME.....\n")
    print("\n Price List (per item in PLN) \n  ----------------------\n Bread   - 2 \n Muffins - 3 \n Cake    -2.5 \n Cookies - 0.5 \n")
    print("\n *** Stock Available (in numbers)*** \n-----------------------------------\n")
    print(fs.show_stock)
    print("\n*** Stock Value of each item (in PLN) *** \n------------------------------------------\n")
    print(fs.show_quantity_price)
   
    input_text = "How many distinct items you are purchasing? \n"
    n_items =int(input(input_text))
    if n_items > 4:
        raise ValueError("Number of items cannot be greater than four.")
    pur_order = []
    for i in range(n_items):
        input_text = "Enter the item - "
        item = input(input_text + 'Bread / Muffins / Cake / Cookies \n')
        if item not in ('Bread','Muffins','Cake','Cookies'):
            raise ValueError("Order can be placed for only above four items.\n Please place order again.")
        input_text = "Enter the quantity \n"
        qty = int(input(input_text))        
        pur_order.append((item, qty))
        
    print("\n>>>>>>>>> YOUR ORDER <<<<<<<<< \n")
    print(pur_order)    
    print("\n ......Updating Stock......\n")
    fs.purchase_item((pur_order))
    print("\n*** Stock after purchase *** \n-----------------------------------\n")
    print(fs.show_stock)
    
    print("\n *** Stock value of each item after purchase *** \n------------------------------------------\n")
    print(fs.show_quantity_price)
    
