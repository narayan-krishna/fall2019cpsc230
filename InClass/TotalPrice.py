#Krishna Narayan
#2327205
#narayan@chapman.edu
#CPSC 230 section 08
#Assignment 1

def total_price():
    #takes user input of the purchase price and sales tax rate
    purchase_price = float(input("price of purchase: "))
    sales_tax = float(input("sales tax rate: "))/100

    # #finds the amount of dollars and cents by find location of decimal and
    # #separating the values appropriately
    purchase_price_str = str(purchase_price)
    decimal_location = purchase_price_str.find(".")
    dollars_str = purchase_price_str[:decimal_location]
    cents_str = purchase_price_str[(decimal_location + 1):]

    # #converting the total dollars and total cents back to floats for calculation
    dollars_value = float(dollars_str)
    cents_value = float(cents_str)
    #
    # #finding the purchase price in cents
    purchase_price_cents = ((dollars_value)*100) + cents_value
    # #finding the total price in cents
    total_price_cents = (purchase_price_cents + (purchase_price_cents*sales_tax))
    # #finding the amount of dollars from the total amount of cents
    total_price_dollars = (total_price_cents/100)
    #
    # #finds the cents via the decimal from the dollar calculation
    total_decimal_location = str(total_price_dollars).find(".")
    cents_total_str = str(total_price_dollars)[(decimal_location + 1):]

    # #formats to price values properly through series of if statements
    # #(ensures that there are only two decimal values, as to represent cents)
    if (len(cents_total_str) == 1):
        return((str(total_price_dollars)[:decimal_location + 2] + "0"))
    elif (len(cents_total_str) == 2):
        return(str(total_price_dollars))
    else:
        return(str(total_price_dollars)[:decimal_location] + "." + str(total_price_dollars)[decimal_location+1:decimal_location+3])

print(total_price())
