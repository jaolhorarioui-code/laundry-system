PRICE_PER_KG = 50.0

def calculate_total_fee(weight):
    total_fee = weight * PRICE_PER_KG
    print("\n--- BILLING DETAILS ---")
    print(f"Weight: {weight:.2f} kg")
    print(f"Price per kg: PHP {PRICE_PER_KG:.2f}")
    print(f"Total Fee: PHP {total_fee:.2f}")

    return total_fee


def handle_payment(total_fee):
    print("\n--- CUSTOMER PAYMENT ---")

    while True:
        method = input("Payment Method (Cash/Card/Digital): ").strip()

        if method:
            break

        print("Please enter a payment method.")

    amount_paid = 0.0

    while amount_paid < total_fee:
        balance = total_fee - amount_paid
        print(f"Remaining Balance: PHP {balance:.2f}")

        try:
            payment = float(
                input("Enter Amount to Pay: PHP ")
            )

            if payment <= 0:
                print("Payment must be greater than zero.")
                continue

            amount_paid += payment

        except ValueError:
            print("Please enter a valid amount.")

    change = amount_paid - total_fee

    print("Payment completed successfully.")
    print(f"Change: PHP {change:.2f}")

    return {
        "method": method,
        "total_paid": amount_paid,
        "change": change
    }
