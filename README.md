# Food Store OOP (Python)
##STOCK MANAGEMENT IN FOOD STORE 
A program is required to show the following:
- Price list of items
- Initial stock availability
- Initial stock value of each item
- Purchase details
- Updated stock after purchase
- Updated stock value after purchase

Set the class as Foodstore.
Define the set of items’ quantity and price as dictionaries.
Set the hierarchy as: items, quantity and price.
Add the above list of items as initial stock – by calling a method to add the items’ name, quantity and price.
Display the initial stock and stock value after evaluation.
User will be prompted to provide purchase details.

User can enter the number of distinct items he is going to purchase, item name and quantity. Below validations are incorporated in the user inputs:
If the input number of purchase items is greater than 4, system will generate a ValueError – number of items cannot be greater than 4.
User can select items only from the above list of 4 items. If the input item name is different, system will generate ValueError – Order can be placed only for the above items.

Purchase order will be displayed.
System will update the stock by calling corresponding method. Below validations are incorporated:
If the ordered quantity is greater than stock balance of the ordered item, system will generate ValueError – Required quantity is not available.
Updated stock and stock value will be displayed after purchase.

