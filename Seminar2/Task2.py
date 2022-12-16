# для натурального n создать последовательность 3n +1
# Для n = 6
# 4, 7, 10,13,16,19
n = int(input('Введите число: '))

# i = 0
# while i <= n and :
#     print(i*3 +1, end=' ')
#     i+=1

# ИЛИ
for i in range(1,n + 1):
    result = i *3 + 1
    print(result,end=' ')
