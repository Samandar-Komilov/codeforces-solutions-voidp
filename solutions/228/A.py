ln = 4
lst = [None] * ln
cnt = 0

lst[0],lst[1],lst[2],lst[3] = map(int, input().split())

while (ln>1):
    n = lst.pop()
    if n in lst:
        cnt+=1
    ln-=1

print(cnt)