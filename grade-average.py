def calcAverage():
	total = 0
	for grade in range(1, 6):
		grades = int(input("Enter a test grade: "))
		total += grades
	average = total/grade
	print(average)
	determineGrade(average)


def determineGrade(average):
	if average >= 90:
		print("A")
	elif average >= 80:
		print("B")
	elif average >= 70:
		print("C")
	elif average >= 60:
		print("D")
	elif average < 60:
		print("F")

calcAverage()
