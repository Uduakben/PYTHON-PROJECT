student_scores = input("Input a list of student heights").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = 0
for scores in student_scores:
    if scores > highest_score:
        highest_score = scores
print(highest_score)

# #for loop with range
# for number in range(1, 11, 3):
#     print(number)
# student_scores = input("Input a list of students heights").split()
# for number in range(0, len(student_scores)):
#     student_scores[number] = int(student_scores[number])
# print(student_scores)
