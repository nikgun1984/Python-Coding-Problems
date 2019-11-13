# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
#
# Suppose the following input is supplied to the program:
#
# 9
# Then, the output should be:
#
# 11106

input_str = input('Enter number')

num1 = int(input_str)
num2 = int(input_str*2)
num3 = int(input_str*3)
num4 = int(input_str*4)

print(num1+num2+num3+num4)