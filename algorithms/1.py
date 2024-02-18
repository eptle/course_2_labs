#алгоритм грэхема для МВО
arr = [[1, 1], [0, 0], [-3, 5], [4, 0], [3, -1], [1, 4], [-4, -1], [-1, -1], [-3, 2]]

def rotate(a, b, c):
    return (b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0])

def grahamscan(arr):
  n = len(arr) # число точек
  P = list(range(n)) # список номеров точек
  for i in range(1,n):
    if arr[P[i]][0]<arr[P[0]][0]: # если P[i]-ая точка лежит левее P[0]-ой точки
      P[i], P[0] = P[0], P[i] # меняем местами номера этих точек 
  for i in range(2,n): # сортировка вставкой
    j = i
    while j>1 and (rotate(arr[P[0]],arr[P[j-1]],arr[P[j]])<0): 
      P[j], P[j-1] = P[j-1], P[j]
      j -= 1
  S = [P[0],P[1]] # создаем стек
  for i in range(2,n):
    while rotate(arr[S[-2]],arr[S[-1]],arr[P[i]])<0:
      del S[-1] # pop(S)
    S.append(P[i]) # push(S,P[i])
  return S

print(grahamscan(arr))