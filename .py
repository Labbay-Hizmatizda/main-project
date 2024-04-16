rating = 2
star = ''

for s in range(rating):
    
    star += '🌕'

n = 5 - rating
for s in range(n):
    star += '🌑'
print(star)