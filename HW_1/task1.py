# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

number = input("enter three-digit number: ")
print(f"sum of digits in number {number} is", sum([int(number[0]), int(number[1]), int(number[2])]))