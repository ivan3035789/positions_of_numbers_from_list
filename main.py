input_list = [int(i) for i in input().split()]
num = int(input())
position = []
lenght1 = len(input_list) - 1
if num in input_list:
    for i in range(0, lenght1 + 1):
        if input_list[i] == num:
            position.append(i)
    lenght2 = len(position) - 1
    for j in range(0, lenght2 + 1):
        print(position[j], end=' ')
else:
    print('Отсутствует')