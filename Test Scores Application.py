print("Test Scores application\n")

total_score = 0

scoreExam1 = float(input("Enter Exam 1 score: "))
total_score += scoreExam1

scoreExam2 = float(input("Enter Exam 2 score: "))
total_score += scoreExam2

scoreFinalExam = float(input("Enter Final Exam score: "))
total_score += scoreFinalExam

average_score = total_score / 3
avergae_score = round(average_score , 1)

print()

print("Your Scores:" , scoreExam1 , scoreExam2 , scoreFinalExam)
print("Total score:" , total_score)
print("Average Score:" , average_score)
