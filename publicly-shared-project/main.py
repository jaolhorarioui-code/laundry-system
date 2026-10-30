print("LAUNDRY MANAGEMENT SYSTEM")
from process import get_customer_details
from manage import get_order_details
from kilo import  calculate_total_fee, handle_payment
from receipt import  generate_receipt
from final import process_laundry_order,notify_and_pickup            


customer=get_customer_details()
order=get_order_details()
weight=float(input("Enter weight:"))
total_fee=calculate_total_fee(weight)
payment=handle_payment(total_fee)
process_laundry_order()
notify_and_pickup()
generate_receipt(customer,weight, order, total_fee, payment)