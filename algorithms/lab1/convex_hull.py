from random import randint, seed
import matplotlib.pyplot as plt
from math import sqrt, acos

seed()
set_of_points = list((randint(-20, 20), randint(-20, 20)) for i in range(50))


def angle(a, b, c):
    '''ищет угол по трем точкам между векторами AB и AC''' 
    cos = 0
    mult_of_lens = (sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2) * sqrt((c[0]-a[0])**2 + (c[1]-a[1])**2))
    if mult_of_lens != 0:
        cos = (((b[0]-a[0])*(c[0]-a[0])) + ((b[1]-a[1])*(c[1]-a[1]))) / mult_of_lens
    return acos(round(cos, 7))


def gift_wrapping_algorithm(set_of_points):
    if len(set_of_points) <= 3:
        return set_of_points
    
    set_of_points.sort(key=lambda x: x[0])  # сортируем все точки по иксу
    main_point = set_of_points[0]  # последняя найденная точка МВО
    convex_hull = [main_point]
    a, b = main_point, (main_point[0], main_point[1]-10)
    remaining_points = list(set_of_points)
    while True:
        remaining_points.sort(key=lambda c: angle(a, b, c), reverse=True)

        if len(convex_hull) == 1 and remaining_points[0] == convex_hull[0]:
            remaining_points[0], remaining_points[1] = remaining_points[1], remaining_points[0]

        convex_hull.append(remaining_points[0])
        main_point = remaining_points.pop(0)
        a = main_point
        b = convex_hull[-2]
        if main_point == convex_hull[0]:
            convex_hull.pop()
            break
      
    return convex_hull


if __name__ == '__main__':
    convex_hull = gift_wrapping_algorithm(set_of_points)
    print(convex_hull)
    print(set_of_points)
    points = convex_hull + [convex_hull[0]]

    plt.plot(*zip(*points), color='red')
    plt.scatter(*zip(*set_of_points), color='red')

    plt.show()