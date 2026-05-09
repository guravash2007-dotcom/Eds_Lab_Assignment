def cal():
	n = int(input().strip())
	mrks = list(map(int,input().split()))
	if len(mrks) != n:
		print("Error")
		return 
	if any(m < 40 for m in mrks):
		print("Fail")
		return
	total = sum(mrks)
	percent= total/n
	if percent >75:
		grade= "Distinction"
	elif percent >= 60:
		grade = "First Division"
	elif percent >=50:
		grade = "Second Division"
	elif percent >= 40:
		grade = "Third Division"
	else:
		grade = "Fail"
	print(f"Aggregate Percentage: {percent:.2f}")
	print("Grade:",grade)
cal()