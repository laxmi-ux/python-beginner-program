
'''
Write a pyhton program to order the food in the swiggy display the menu for the user 
1.Dosa 
2.Idli
3.Pizza
4.Burgers
5.Chicken 
6.Briyani
7.Ice cream 
8.Place order
#calling to swiggy...
example : press 1 to order Dosa and so on 
if I press 4. you order been added to cart 
if i press 6. your order is been added to cart if i press 8 your order is placed. items : list your total amount.
'''

'''
Note: first he use function that contain menu 
      then make swiggy function in that he call menu function then give condtion and print the item with amount
      and also give item list,amount list  
      then at last call swiggy function and print item + amount
 
'''

def menu():
    print("Welcome to swiggy order your items:")
    print("press 1 for order : Dosa")
    print("press 2 for order : Idli")
    print("press 3 for order : Pizza")
    print("press 4 for order : Burgers")
    print("press 5 for order : Chicken")
    print("press 6 for order : Briyani")
    print("press 7 for order : Ice cream")
    print("press 8 for order : order")


items=[]
amount=[]

def swiggy():
    menu()
    n=int(input("Enter the order number: "))
    if(n>=1 and n<=8):
        if n==1:
            item="Dosa"
            items.append(item)
            amount.append(80)
            print(f"Your order item {items} is been added to the cart")
            swiggy()

        elif n==2:
            item="Idli"
            items.append(item)
            amount.append(40)
            print(f"Your order item {items} is been added to the cart")
            swiggy()

        elif n==3:
            item="Pizza"
            items.append(item)
            amount.append(100)
            print(f"Your order item {items} is been added to the cart")
            swiggy()

        elif n==4:
            item="Burger"
            items.append(item)
            amount.append(70)
            print(f"Your order item {items} is been added to the cart")
            swiggy()   

        elif n==5:
            item="Chicken"
            items.append(item)
            amount.append(120)
            print(f"Your order item {items} is been added to the cart")
            swiggy()   

        elif n==6:
            item="Briyani"
            items.append(item)
            amount.append(180)
            print(f"Your order item {items} is been added to the cart")
            swiggy() 

        elif n==7:
            item="Ice cream"
            items.append(item)
            amount.append(30)
            print(f"Your order item {items} is been added to the cart")
            swiggy()  

        else:
            print("Thanks for choosing swiggy")      

    else:
        print("Please select the correct order number:")
        swiggy()

  


swiggy()
print("Your ordered item are", items)
print("Your ordered total amount is", sum(amount))