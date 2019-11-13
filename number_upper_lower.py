# Question:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
#
# Suppose the following input is supplied to the program:
#
# Hello world!
# Then, the output should be:
#
# UPPER CASE 1
# LOWER CASE 9


input_sentence = input('Enter sentence')

upper_let = 0
lower_let = 0

for a in input_sentence:
    if a.isupper():
        upper_let += 1
    if a.islower():
        lower_let += 1

print(f'UPPER CASE {upper_let}')
print(f'LOWER CASE {lower_let}')
