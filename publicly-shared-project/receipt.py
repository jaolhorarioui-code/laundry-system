def generate_receipt(customer,weight, order, total_fee, payment):
    print("\n" + "=" * 40)
    print("          LAUNDRY RECEIPT")
    print("=" * 40)

    print(f"Customer Name : {customer['name']}")
    print(f"Contact       : {customer['contact']}")
    print(f"Address       : {customer['address']}")
    print("-" * 40)

    print(f"Service       : {order['service_type']}")
    print(f"Weight        : {weight:.2f} kg")
    print(f"Pickup Date   : {order['pickup_date']}")
    print("-" * 40)

    print(f"Total Fee     : PHP {total_fee:.2f}")
    print(f"Payment Method: {payment['method']}")
    print(f"Amount Paid   : PHP {payment['total_paid']:.2f}")
    print(f"Change        : PHP {payment['change']:.2f}")

    print("=" * 40)
  