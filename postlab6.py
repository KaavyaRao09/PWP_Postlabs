
# num = 1
# while num <= 100:
#     print(num, end=" ")
#     num += 2  


# n = int(input("Enter a natural number: "))
# total = 0
# count = 1
# while count <= n:
#     total += count
#     count += 1
# print("The sum of natural numbers from 1 to", n, "is:", total)


# num = input("Enter a number: ")
# first_digit = int(num[0])
# last_digit = int(num[-1])
# print("First digit:", first_digit)
# print("Last digit:", last_digit)


# num = input("Enter a number: ")
# if len(num) == 1:
#     swapped = num
# else:
#     swapped = num[-1] + num[1:-1] + num[0]
# print("After swapping first and last digits:", swapped)


# num = input("Enter a number: ")
# product = 1
# for digit in num:
#     product *= int(digit)
# print("Product of digits:", product)


# num = input("Enter a number: ")
# reverse_num = num[::-1]
# print("Reversed number:", reverse_num)


def count_digits(number):
    count = 0
    while number != 0:
        number //= 10
        count += 1
    return count
num = int(input("Enter a number: "))
print("Number of digits:", count_digits(num))