name = input("enter student name: ")
sub1 = int(input("enter ur sub1 marks: "))
sub2 = int(input("enter ur sub2 marks: "))
sub3 = int(input("enter ur sub3 marks: "))
total_marks = sub1 + sub2 + sub3
percentage = (total_marks / 300) * 100
if percentage >= 75 :
  print(f"{name} : total={total_marks} percentage = {percentage} grade = A")
elif percentage >= 60 :
  print(f"{name} : total={total_marks} percentage = {percentage} grade = B")
elif percentage >= 40 :
  print(f"{name} : total={total_marks} percentage = {percentage} grade = C")
elif percentage <= 40 :
  print(f"{name} : total={total_marks} percentage = {percentage} grade = D")
