list = [1, 2, 3, 4, 5, 2, 6, 7, 8, 9, 1,4,5,7]
# def find_duplicates(numbers):
#     duplicates = []
#     for num in numbers:
#         if numbers.count(num) > 1 and num not in duplicates:
#             duplicates.append(num)
#     return duplicates
def find_duplicates(numbers):
    duplicates = []
    seen = []
    for num in numbers:
        if num in seen and num not in duplicates:
            duplicates.append(num)
        else:
            seen.append(num)
    return duplicates
duplicates = find_duplicates(list)
print(duplicates)