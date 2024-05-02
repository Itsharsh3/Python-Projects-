programName = "Calculate Letter Grade"
developerName = "Harsh Patel"

print(f"Program: {programName}\n"
      f"Developer: {developerName}\n"
      f"\n")

score = float(input("Enter test score: "))

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
