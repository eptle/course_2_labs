from random import randint, seed
import matplotlib.pyplot as plt
from math import sqrt, acos
from decimal import Decimal

seed()
set_of_points = list((randint(-20, 20), randint(-20, 20)) for i in range(50))

def angle(a, b, c): #три точки a,b,c, векторы AB и AC,  
    cos = 0
    if (sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2) * sqrt((c[0]-a[0])**2 + (c[1]-a[1])**2)) != 0:
        cos = (((b[0]-a[0])*(c[0]-a[0])) + ((b[1]-a[1])*(c[1]-a[1]))) / \
            (sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2) * sqrt((c[0]-a[0])**2 + (c[1]-a[1])**2))
    return acos(round(cos, 3))

def graham(dataset):
    num_of_points = len(dataset)
    dataset.sort(key=lambda x: x[0])
    start = main_point = dataset[0]
    convex_hull = [main_point]
    a, b = main_point, (main_point[0], main_point[1]-10)
    remaining_points = dataset[1:]
    remaining_points.append(start)
    while True:
        remaining_points.sort(key=lambda c: angle(a, b, c), reverse=True)
        convex_hull.append(remaining_points[0])
        main_point = remaining_points.pop(0)
        a = main_point
        b = convex_hull[-2]
        #remaining_points.append()
        if main_point == convex_hull[0]:
            convex_hull.pop()
            break
      
    return convex_hull

convex_hull = graham(set_of_points)
print(convex_hull)
points = convex_hull + [convex_hull[0]]
x1 = [point[0] for point in points]
y1 = [point[1] for point in points]

x2 = [point[0] for point in set_of_points]
y2 = [point[1] for point in set_of_points]

plt.plot(x1, y1, color='red')
plt.scatter(x2, y2, color='red')

plt.show()