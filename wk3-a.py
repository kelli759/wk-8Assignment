def calculate_discount(price, discount_percent):
    """
    Args:
        price = The original price of the item.
        discount_percent (float) = The discount percentage.

    Returns:
        float: The final price after applying the discount.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


if __name__ == "__main__":
    # Enter the original price of an item
    price = float(input("Enter the original price of the item: kshs"))

    # Enter the discount percentage
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate the final price after applying the discount
    final_price = calculate_discount(price, discount_percent)

    # Print the final price after applying the discount, if no discount was applied print the original price
    print(f"The final price is: kshs{final_price:.2f}")
