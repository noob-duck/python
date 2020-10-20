grade = [23,85,45,90,78,75,99,80,95,79]

max = grade[0]

for x in range(10):
    if max < grade[x]:
        max = grade[x]
print('성적 최댓값은 :', max, '입니다')
