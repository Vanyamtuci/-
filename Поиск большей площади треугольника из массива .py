def maxS(arr):
    S = 0
    print(arr)
    arr.sort(reverse = True)
    print(arr)
    for x in arr[::-1]: # проверка на отриц. число начиная с меньшего
        if x <= 0:
            return "Невозможные значения в массиве: " + str(x) + "\n"
    for i in range(0, len(arr) - 2): # поиск наибольшего
        if arr[i] < (arr[i+1] + arr[i+2]):
            p = (arr[i] + arr[i+1] + arr[i+2]) / 2.0 
            S = (p * (p - arr[i]) * (p - arr[i+1]) * (p - arr[i+2])) ** 0.5
            bordes = map(str, [arr[i], arr[i+1], arr[i+2]])
            break
    if(S == 0):
        return "Треугольник создать невозможно\n"
    else:
        return "Максимальная площадь: " + str(round(S, 6)) + "\nстороны: " + ", ".join(bordes) + "\n"
  
def main():
    arr = [6, 1, 6, 5, 8, 4]
    a = maxS(arr)
    print(a)
    arr = [2, 20, 7, 55, 
            1, 33, 12, -4]
    a = maxS(arr)
    print(a)
    arr = [2, 20, 7, 55, 
            1, 33, 12, 4]
    a = maxS(arr)
    print(a)
    arr = [33, 6, 20, 1, 8,
            12, 5, 55, 4, 9]
    a = maxS(arr)
    print(a)

if __name__=='__main__':
    main()
