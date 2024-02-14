#Create a function that takes two arguments: the original price and the discount percentage as integers and returns the final price after the discount.

def calculate_final_price(original_price, discount_percentage):
    # Calculate the discount amount
    discount_amount = original_price * discount_percentage / 100
    
    # Calculate the final price after the discount
    final_price = original_price - discount_amount
    
    return final_price

# Test the function with an example
original_price = 100
discount_percentage = 20
final_price = calculate_final_price(original_price, discount_percentage)
print(f"The final price after a {discount_percentage}% discount is: ${final_price}")
