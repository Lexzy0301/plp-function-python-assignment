# def calculate_Discount (price, discount_percent):
if discount_percent >= 20:
   discounted_price = price - (price * discount_percent / 100)
   return (discounted_price)
else:
    return (price)


price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))
final_price = calculate_discount(price, discount_percent)c
# Print the result
if discount_percent >= 20:
    print("Final price after discount:", final_price)
else:
    print("No discount applied. Price remains:", final_price)
