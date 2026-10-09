marks = [45, 78, 62, 89, 55, 92, 38, 76]
print ("highest mark is:", max(marks))
print("lowest mark is:", min(marks))
print("average mark is:", sum (marks)/len(marks))
print("how many students scored above average:", len([mark for mark in marks if mark > sum(marks)/len(marks)]))
marks.sort()
print("marks in ascending order:", marks)