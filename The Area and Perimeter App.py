print("The Area and Perimeter App")
print()

length= float(input("Please enter the length:\t"))
width = float(input("Please enter the width:\t\t"))

area = length * width
perimeter = (2 * length) + (2 * width)
area = round(area, 2)
perimeter = round(perimeter, 2)
            
print()
print(f"Area = {area}")
print(f"Perimeter = {perimeter}")
print()
print("Bye!")


