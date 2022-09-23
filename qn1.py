"""
QUESTION: 

COMPANY : WIPRO

"""

n= int(input())
lis = list(input())
m = []
p = int(input())

for i in lis:
    if i!=" ":
        m.append(i)

visited = [False for i in range(n)]
cnt = []
for i in range(n):
    if (visited[i] == True):
        continue

    count = 1
    for j in range(i + 1, n, 1):
        if (m[i] == m[j]):
            visited[j] = True
            count += 1
         
    cnt.append(count)
c=0
for i in cnt:
    if i==p:
        c+=1
print(c)
