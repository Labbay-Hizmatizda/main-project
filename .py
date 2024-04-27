# rating = 0
# star = ''

# for s in range(rating):
    
#     star += '🌕'

# n = 5 - rating
# for s in range(n):
#     star += '🌑'
# print(star)

# m = 'XX-XXX-XX-XX'
# m = m.replace('-', '')
# print(m)


# class Solution:
# def findMin(nums):
#     n = len(nums)
#     l = 0
#     r = n - 1

#     while l < r:
#         m = (l + r) // 2
#         if nums[m] > nums[r]:
#             l = m + 1
#         else:
#             r = m

    # Возвращаем список, отсортированный по возрастанию
    # return sorted(nums[:l] + nums[l:])

# print(findMin([4,5,6,1,2,3]))

# import sys

# m = {1 : 3}
# print(sys.getsizeof(m))


# m = [4,5,6,1,2,3]
# print(sorted(m))

# m.sort()
# print(m)






import time

class DictStorage:
    def __init__(self):
        self.dictionary = {}

    def add_dictionary(self, key, dictionary):
        self.dictionary[key] = dictionary

    def get_dictionary_by_key(self, key):
        return self.dictionary.get(key)

    def clear_dictionaries(self):
        self.dictionary = {}

# Создаём экземпляр класса DictStorage
storage = DictStorage()

# Добавляем миллион словарей
start_time_add = time.time()

for i in range(1000000):
    storage.add_dictionary(i, {i: i})

end_time_add = time.time()
add_time = end_time_add - start_time_add
print("Время добавления миллиона словарей:", add_time, "секунд")

# Получаем словарь по ключу 900000
start_time_get = time.time()

key = 900000
dictionary_by_key = storage.get_dictionary_by_key(key)

end_time_get = time.time()
get_time = end_time_get - start_time_get
print(f"Словарь с ключом {key}:", dictionary_by_key)

print("Время получения словаря по ключу 900000:", get_time, "секунд")
