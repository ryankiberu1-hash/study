# student = {
#     "name": "RYAN",
#     "age": 20,
#     "grades": {"MATH": 85, "SCIENCE": 90, "ENGLISH": 78, "HISTORY": 92, "ART": 88}

# }
# student["city"] = "New York"
# def word_count(string):
#     count ={}
#     words = string.split()
#     for word in words:
#         count[word] = count.get(word, 0) + 1
#     return count
# print(word_count(student["name"]))
# def word_count(string):
#     count = {}
#     words = string.split()
#     for word in words:
#         count[word] = count.get(word, 0) + 1
#     return count

# # Gather only the string values from the dictionary
# text_values = []
# for value in student.values():
#     if isinstance(value, str):
#         text_values.append(value)

# combined_text = " ".join(text_values)
# print(word_count(combined_text))



# def word_count(text):
#     words = text.split()
#     counts = {}
#     for word in words:
#         if word in counts:
#             counts[word] += 1
#         else:
#             counts[word] = 1
#     return counts

# print(word_count("the cat sat on the mat"))