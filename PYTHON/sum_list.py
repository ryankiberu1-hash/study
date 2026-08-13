def sum_list(number):
    if len(number) ==0:
        return 0
    return number[0] + sum_list(number[1:])
print(sum_list([1,2,3,4,5]))