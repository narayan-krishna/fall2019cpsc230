#Krishna Narayan
#2327205
#narayan@chapman.edu
#CPSC 230 section 08
#Assignment 1

def total_price():
    #takes user input of the purchase price and sales tax rate
    purchase_price = float(input("price of purchase: "))
    sales_tax = float(input("sales tax rate: "))/100 #divides by one hundred
    #due to necessary conversion of percentage into decimal

    #returns the purchase price plus the amount owed from sales tax
    if purchase_price >= 0 and sales_tax >= 0:
        return("the total price is around "+ str((purchase_price + (purchase_price * (sales_tax)))) + " in dollars")
    else:
        return("please input valid values")

print(total_price())
