# rating = 2
# star = ''

# for s in range(rating):
    
#     star += '🌕'

# n = 5 - rating
# for s in range(n):
#     star += '🌑'
# # print(star)

# m = 'XX-XXX-XX-XX'
# m = m.replace('-', '')
# print(m)


# class Solution:
def findMin(nums):
    n = len(nums)
    l = 0
    r = n - 1

    while l < r:
        m = (l + r) // 2
        if nums[m] > nums[r]:
            l = m + 1
        else:
            r = m

    # Возвращаем список, отсортированный по возрастанию
    return sorted(nums[:l] + nums[l:])

print(findMin([4,5,6,1,2,3]))




m = [4,5,6,1,2,3]
print(sorted(m))

m.sort()
print(m)