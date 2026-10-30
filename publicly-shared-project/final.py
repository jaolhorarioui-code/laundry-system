import time
def process_laundry_order():
    print("\n--- LAUNDRY PROCESSING ---")

    stages = ["Washing", "Drying", "Folding"]

    for stage in stages:
        print(f"{stage} is in progress...")
        time.sleep(1)

    while True:
        status = input(
            "Is the laundry ready? (yes/no): "
        ).strip().lower()

        if status == "yes":
            print("Laundry is ready for pickup!")
            break

        elif status == "no":
            print("Continue processing the laundry.")

        else:
            print("Please enter yes or no.")


def notify_and_pickup():
    print("\n--- CUSTOMER NOTIFICATION ---")
    print("Your laundry is ready for pickup!")

    while True:
        status = input(
            "Has the customer picked up the laundry? (yes/no): "
        ).strip().lower()

        if status == "yes":
            print("Order Status: COMPLETED")
            break

        elif status == "no":
            print("Order Status: READY FOR PICKUP")
            print("Waiting for customer pickup...")

        else:
            print("Please enter yes or no.")
