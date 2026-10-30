def get_order_details():
    print("\n--- LAUNDRY ORDER DETAILS ---")

    

    while True:
        service_type = input("Enter Service Type: ").strip()

        if service_type:
            break

        print("Service type cannot be empty.")

    while True:
        pickup_date = input("Enter Pickup Date (YYYY-MM-DD): ").strip()

        if pickup_date:
            break

        print("Pickup date cannot be empty.")

    return {
        "service_type": service_type,
        "pickup_date": pickup_date
    }