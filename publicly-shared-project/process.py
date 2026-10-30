def get_customer_details():
    print("\n--- CUSTOMER DETAILS ---")

    while True:
        name = input("Enter Name: ").strip()
        contact = input("Enter Contact Number: ").strip()
        address = input("Enter Address: ").strip()

        if name and contact and address:
            print("Customer details accepted.")

            return {
                "name": name,
                "contact": contact,
                "address": address }

        print("Error: Please fill in all fields.")