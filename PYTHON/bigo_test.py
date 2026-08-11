import time

def find_duplicates_slow(nums):
    duplicates = []
    for num in nums:
        if nums.count(num) > 1 and num not in duplicates:
            duplicates.append(num)
    return duplicates

def find_duplicates_fast(nums):
    seen = set()
    duplicates = set()
    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)

data = list(range(10000)) + list(range(5000))  # 5000 duplicates

start = time.time()
find_duplicates_slow(data)
print("slow version:", time.time() - start," seconds")

start = time.time()
find_duplicates_fast(data)
print("fast version:", time.time() - start," seconds")