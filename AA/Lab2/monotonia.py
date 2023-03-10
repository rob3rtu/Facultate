n = int(input())
point = [int(i) for i in input().split()]

points = [point]
lefter = point
right = point
top = point
bottom = point
l = 0
r = 0
t = 0
b = 0

for i in range(1,n):
    point = [int(i) for i in input().split()]
    points.append(point)

    if point[0] < lefter[0]:
        lefter = point
        l = i

    if point[0] > right[0]:
        right = point
        r = i

    if point[1] < bottom[1]:
        bottom = point
        b = i

    if point[1] > top[1]:
        top = point
        t = i

points.append(points[0])

xMonoton = True
yMonoton = True

i = b + 1
while i % n != t:
    if points[i % n][1] < points[i % n - 1][1]:
        yMonoton = False
        break

    i += 1

if yMonoton:
    i = b - 1
    while i != t:
        if i == -1:
            i = n - 1
        if i == t:
            break
        
        if points[i][1] < points[i + 1][1]:
            yMonoton = False
            break

        i -= 1

i = l + 1
while i % n != r:
    if points[i % n][0] < points[i % n - 1][0]:
        xMonoton = False
        break

    i += 1

if xMonoton:
    i = l - 1
    while i != r:
        if i == -1:
            i = n - 1
        if i == r:
            break
        
        if points[i][0] < points[i + 1][0]:
            xMonoton = False
            break

        i -= 1

if xMonoton:
    print("YES")
else:
    print("NO")

if yMonoton:
    print("YES")
else:
    print("NO")