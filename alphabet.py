num = int(input("Enter a num of value: "))
ternary_num = list()
alphabet = {0: "A", 1: "O", 2: "Y"}

rem = num - 1
while rem > 0:
    ternary_num.append(rem % 3)
    rem //= 3

for i in range(0, len(ternary_num)):
    ternary_num[i] = alphabet[ternary_num[i]]
print(''.join(reversed(ternary_num)))