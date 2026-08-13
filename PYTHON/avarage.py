# def average(numbers):
#     total = sum(numbers)
#     count = len(numbers)
#     # average_value = total / count
#     # return average_value
#     if count ==0:
#         return 0
#     return total / count

# list = [1, 2, 3, 4, 510, 28]
# avg = average(list)
# print(avg)
def average(numbers):
    total = 0
    for num in numbers:
        total += num
        count = len(numbers)
    if count == 0:
        return 0
    return total / count
list = [1, 2, 3, 4, 5]
avg = average(list)
print(avg)