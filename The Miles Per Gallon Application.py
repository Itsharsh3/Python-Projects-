print("The Miles Per Gallon Application")

miles_driven = float(input("Enter miles driven:"))
gallons_used = float(input("Enter gallons of gas used:"))
cost_per_gallon = float(input("Enter cost per gallon:"))
mpg = round(miles_driven / gallons_used, 1)
total_gas_cost = round(gallons_used * cost_per_gallon, 1)
cost_per_mile = round(total_gas_cost /miles_driven , 1)

print()

print("Miles Per Gallon:" , mpg)
print("Total Gas Cost:" , total_gas_cost)
print("cost_per_mile:" , cost_per_mile)
