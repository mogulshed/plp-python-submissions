def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    else:
        return price

# Get user input
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

final_price = calculate_discount(price, discount_percent)

if final_price != price:
    print(f"Final price after discount: {final_price:.2f}")
else:
    print(f"No discount applied.price remains: {final_price:.2f}")
    