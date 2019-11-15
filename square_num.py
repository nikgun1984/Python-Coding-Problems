# Question:
# Use a list comprehension to square each odd number in a list. The list is input
# by a sequence of comma-separated numbers. Suppose the following input is supplied to the program:
#
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
#
# 1,9,25,49,81


def square_odd_nums(input_lst) -> str:
    new = [str(i ** 2) for i in input_lst if i % 2 != 0]

    return ','.join(new)


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(square_odd_nums(lst))


# Question:
# Write a program that computes the net amount of a bank account based a transaction log from console input.
# The transaction log format is shown as following:
#
# D 100
# W 200
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
#
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
#
# 500

def net_amount(account) -> int:
    net = 0
    for i in account.get('D'):
        net += i
    for j in account.get('W'):
        net -= j

    return net


account1 = {'D': [300, 300, 100], 'W': [200]}
total = net_amount(account1)
print(f'Total amount after all transactions is ${total}.')
