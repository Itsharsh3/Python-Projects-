programName = "Calculate Letter Grade"
developerName = "Harsh Patel"
instruction = "Enter \"exit\" to end the program"

print(f"Program: {programName}\n"
      f"Developer: {developerName}\n"
      f"Instruction: {instruction}"
      f"\n")

while True:
    str_score = input("Enter test score: ")

    if str_score.lower() == "exit":
        break
    
    score = float(str_score)

    if score < 0:
        print("A test score must be greater than or equal to zero. Try again.\n")
        continue
    
    if score >= 90:
        letterGrade = "A"
    elif score >= 80 and score < 90:
        letterGrade = "B"
    elif score >= 70 and score < 80:
        letterGrade = "C"
    elif score >= 60 and score < 70:
        letterGrade = "D"
    else:
        letterGrade = "F"

    print()
    print("The score you entered is:", score)
    print("The letter grade is:", letterGrade)
    print()

print("Okay, bye!")
