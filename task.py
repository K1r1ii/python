sum_p = int(input())
#все 3-значные числа имеющие заданную сумму цифр

for i in range(100, 999+1):
    sum_n = 0
    i_s = str(i)
    for j in i_s:
        sum_n += int(j)
    if sum_n == sum_p:
        print(i)