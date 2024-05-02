programName = "Square Calculator"

print(f"Program: {programName}\n")

more = "y"

while more.lower() == "y":
    data = input("Enter an integer to square: ")
    num = int(data) 
    
    num_squared = num * num

    print(num, "squared is", num_squared, "\n")
    
    more = input("Continue? (y/n): ")
    print()

print("Okay, bye!")
