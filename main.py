# # 1
# my_tuple = (5, 10, 15, 20)
#
# print(f"Tuple uzunligi: {len(my_tuple)}")
# print(f"3 elemt: {my_tuple[3]}")
# if 15 in my_tuple:
#     print("bor")
# else:
#     print("yq")
# # 2
# # Tuple
# colors = ('red', 'blue', 'green')
#
# colors_list = list(colors)
#
# colors_list.append('yellow')
#
# colors_list.remove('blue')
#
# colors_list.sort()
#
# print(colors_list)
# # 3
# nubers = (3, 7, 2, 9, 4)
#
# summ = sum(nubers)
#
# if summ % 2 == 0:
#     result = "juft"
# else:
#     result = "toq"
# print("Yig‘indi:", summ)
# print("Yig‘indi", result, "son.")
# # 4
# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
#
# a = tuple1 + tuple2
# print(a)
# print(f"sum: {sum(a)}")
# print(a[-1])
# # 5
# values = (12, 5, 8, 19, 3, 15)
# print(values)
#
# print(f"eng katta: {max(values)}")
# print(f"eng kichik: {min(values)}")
#
# print(f"farq: {max(values) - min(values)}")
# # 6
# words = ("apple", "banana", "cherry", "data")
# print(words)
#
# a = sorted(words,reverse=True)
# print(a)
# print(f"bir va oxirgi e: {a[0]}, {[-1]}")
# # 7
# data = (10, 20, 30, 40, 50)
# print(data)
#
# if 30 in data:
#     print("bor")
# else:
#     print("yo")
#
# print(f"30 index: {data.index(30)}")
# # 8
# nums = (1, 2, 3, 4, 5, 6, 7, 8)
# print(nums)
#
# a = tuple()
# s = nums[1::2]
# print(s)
# print(f"sum: {sum(s)}")
# print(s)
# # 9
# fruits = ("apple", "kiwi", "banana", "pear")
# print(fruits)
#
# fruits = list(fruits)
# print(type(fruits))
#
# fruits.sort()
# print(fruits)
#
# fruits = tuple(fruits)
# print(fruits)
# # 10
# numbers = (-3, 5, -7, 2, -1, 8)
# print(numbers)
#
# numbers_list = list(numbers)
#
# for i in range(len(numbers_list)):
#     if numbers_list[i] < 0:
#         numbers_list[i] = 0
#
# new_numbers = tuple(numbers_list)
# print(new_numbers)
# # 11
# s = (2, 4, 6, 8)
# print(s)
#
# s = list(s)
#
# for i in range(len(s)):
#     s[i] *= 2
#
# s = tuple(s)
# print(s)
# # 12
# r_t = (10, 20, 30, 40, 50, 60, 70)
# print(r_t)
#
# a = r_t[2:5]
# print(a)
#
# print(f"sum: {sum(a)}")
#
# print(a)
