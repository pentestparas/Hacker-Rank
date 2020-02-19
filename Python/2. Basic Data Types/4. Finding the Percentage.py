n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
query_score=student_marks[query_name]
avg=sum(query_score)/3
print("%.2f"% avg)