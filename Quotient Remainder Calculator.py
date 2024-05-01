print("Quotient and Remainder Calculator - Easily Find Quotient and Remainder")

print()

divident = float(input("Please enter a divident: "))
divisor = float(input("Please enter a divisor: "))
divResult = divident / divisor
quotientResult = divident // divisor
remainderResult = divident % divisor

print()

print("Result:" , divResult)
print("Quotient:" , int (quotientResult))
print("Remainder:" , int(remainderResult))
