def calculate_discount(price, discount_percent):
   
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price

# Prompt the user to enter the original price and discount percentage
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Calculate the final price
    final_price = calculate_discount(original_price, discount_percentage)

    # Print the result
    if final_price < original_price:
        print(f"The final price after applying a discount of {discount_percentage}% is: {final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: {original_price:.2f}")
except ValueError:
    print("Please enter valid numerical values for the price and discount percentage.")
