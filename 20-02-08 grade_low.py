grade = [23,85,45,90,78,75,99,80,95,79]

low = grade[0]

for x in range(10):
    if low > grade[x]:
        low = grade[x]
print('성적 최솟값은 :', low, '입니다')
