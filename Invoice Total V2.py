from decimal import Decimal
from decimal import ROUND_HALF_UP
import locale as lc

programName = "Enhanced Invoice Total"
developerName = "Harsh Patel"
date = "March 6, 2024"
print(f"Program name: {programName}\n"
      f"Developer: {developerName}\n"
      f"\n")

customer_type = input("Enter customer type (r/w): ")
invoice_total = Decimal(input("Enter invoice total: "))

if customer_type == "r" or customer_type == "R":
    if invoice_total >= 500:
        discount_percent = Decimal(".25")
    elif invoice_total >= 250 and invoice_total < 500:
        discount_percent = Decimal(".2")
    elif invoice_total >= 100 and invoice_total < 250:
        discount_percent = Decimal(".1")
    else:
        discount_percent = Decimal("0")        
elif customer_type == "w" or customer_type == "W":
    if invoice_total >= 500:
        discount_percent = Decimal(".5")
    else:
        discount_percent = Decimal(".4")
else:
    discount_percent = Decimal("0") 

discount_amount = invoice_total * discount_percent
discoutn_amount = discount_amount.quantize(Decimal("1.00"), ROUND_HALF_UP)

final_invoice_total = invoice_total - discount_amount
final_invoice_total = final_invoice_total.quantize(Decimal("1.00"), ROUND_HALF_UP)

lc.setlocale(lc.LC_ALL, "us")

invoice_total = lc.currency(invoice_total, grouping=True)
discount_amount = lc.currency(discount_amount, grouping=True)
final_invoice_total = lc.currency(final_invoice_total, grouping=True)

print()
print(f"{'Invoice total:':30}" f"{invoice_total:>20}")
print(f"{'Discount percent:':30}" f"{discount_percent:20.1%}")
print(f"{'Discount amount:':30}" f"{discount_amount:>20}")
print(f"{'Final invoice total:':30}" f"{final_invoice_total:>20}")
