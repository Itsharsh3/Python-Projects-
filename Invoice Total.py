programName = "Invoice Total"
developerName = "Harsh Patel"

print(f"Program name: {programName}\n"
      f"Developer: {developerName}\n"
      f"\n")


customer_type = input("Enter customer type (r/w): ")
invoice_total = float(input("Enter invoice total: "))

if customer_type == "r" or customer_type == "R":
    if invoice_total >= 500:
        discount_percent = .25
    elif invoice_total >= 250 and invoice_total < 500:
        discount_percent = .2
    elif invoice_total >= 100 and invoice_total < 250:
        discount_percent = .1
    else:
        discount_percent = 0        
elif customer_type == "w" or customer_type == "W":
    if invoice_total >= 500:
        discount_percent = .5
    else:
        discount_percent = .4
else:
    discount_percent = 0

discount_amount = round(invoice_total * discount_percent, 2)
final_invoice_total = round(invoice_total - discount_amount, 2)

print()
print("Invoice total:", invoice_total)
print("Discount percent:", discount_percent)
print("Discount amount:", discount_amount)
print("Final invoice total:", final_invoice_total)
