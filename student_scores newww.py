student_scores = input("Please input a list of stucent scores").split()
for x in range(0, len(student_scores)):
    student_scores[x] = int(student_scores[x])
print(student_scores)

highest_Score = 0

for scores in student_scores:
    if scores > highest_Score:
        highest_Score = scores
print(scores)
