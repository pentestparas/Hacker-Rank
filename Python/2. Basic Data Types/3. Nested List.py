grade=[]
for _ in range(int(input())):
    name = input()
    score = float(input())
    grade.append([name,score])

second_lowest_grade=(sorted(list(set(grades for name, grades in grade))))[1]

print('\n'.join([a for a, b in sorted(grade) if b == second_lowest_grade]))
