score = [90,65,46,87,99,100]
number = 0
for s in score:
    number = number + 1
    if s >= 90:
        print("%d번 학생은 합격입니다"% number)
    else:
        print("%d번 학생은 불합격입니다"% number)

sum = 0
for n in range(1,11):
    sum = sum + n
print(sum)