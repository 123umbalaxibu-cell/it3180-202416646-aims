def calculate_discount(total, percent):
    if not 0 <= percent <= 100:
        raise ValueError("Discount percent must be between 0 and 100")

    return total * (1 - percent / 100)