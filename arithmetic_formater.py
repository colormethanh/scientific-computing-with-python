"""
Link: https://replit.com/@ThanhNguyen117/boilerplate-arithmetic-formatter-3#arithmetic_arranger.py
"""


import operator

inputs = ["32 + 698", "3801 + 2", "45 + 43", "123 + 49"]

op = {'+': operator.add,
      '-': operator.sub}

prblm_lst = []  # list of problems

# orangize each problem into the prblm_lst
for i in inputs:
    com = i.split(" ")

    prblm = {'num_1': com[0], 'num_2': com[2], 'oprnt': com[1], }
    prblm_lst.append(prblm)


# checking if input is valid
if len(prblm_lst) > 5:  # checking if too many problems error
    print("Error: Too many problems")

for i in prblm_lst:  # checking for multiple valid criteria
    if i['oprnt'] not in op:  # checking for operator error
        print("Error: Operator must be '+' or '-' ")

    if len(i['num_1']) > 4 or len(i['num_2']) > 4:  # checking for legnt error
        print("Error: Numbers cannot be more than 4 digits")

    if not i['num_1'].isdecimal() or not i['num_2'].isdecimal():  # checking for operand error
        print("Error: Numbers must only contain digits.")
        exit()


for i in prblm_lst:  # calculation the solution of the problems
    s = op[i['oprnt']](int(i['num_1']), int(i['num_2']))
    i['sol'] = str(s)


# Formatting Data
lines = []
for n in range(4):
    lst = []
    lines.append(lst)


seperator = " " * 4
cnt = 0
for i in prblm_lst:

    longest = len(i['num_1']) if len(i['num_1']) > len(i['num_2']) else len(i['num_2'])
    lnth_1 = len(i['num_1'])
    lnth_2 = len(i['num_2'])

    l1 = (' ' * (longest - lnth_1 + 2)) + i['num_1']
    lines[0].append(l1)

    l2 = i['oprnt'] + ' ' * (longest - lnth_2 + 1) + i['num_2']
    lines[1].append(l2)

    l3 = '-' * (longest + 2)
    lines[2].append(l3)

    l4 = ' ' * (longest - len(i['sol']) + 2) + i['sol']
    lines[3].append(l4)

    if cnt != len(prblm_lst) - 1:
        lines[0].append(seperator)
        lines[1].append(seperator)
        lines[2].append(seperator)
        lines[3].append(seperator)
    else:
        continue
    cnt += 1


print("".join(lines[0]) + '\n' +
      "".join(lines[1]) + '\n' +
      "".join(lines[2]) + '\n' +
      "".join(lines[3])
      )
