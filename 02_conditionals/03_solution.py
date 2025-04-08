score  =101

if score>=100:
    print("Invalid Score: ")
    exit()

if score>=90:
    grade="A"
elif score>=80:
    grade="B"
elif score >=70:
    grade="C"
else:
    grade="Fail"

print(grade)                