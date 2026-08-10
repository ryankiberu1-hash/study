list = [10,23,30]
print(list[0])
print(list[2])
list.append(40)
list.reverse()
print(list)
print(len(list))
list.sort()          # sorts the list in ascending order
print("Sorted list:", list)
list.pop()           # removes the last element
print("After pop:", list)
