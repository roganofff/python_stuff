num = int(input("Enter a num of value: "))
arr_ternary_num = list()
alphabet = {0: "A", 1: "O", 2: "Y"}

rem = num - 1
while rem > 0:
    arr_ternary_num.append(rem % 3)
    rem //= 3
    
print(arr_ternary_num)