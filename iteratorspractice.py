# iterators practice

import math

ast = "*"

x = [2, 4, 6, 8, 10, 12]
y = []
    
# for v in x :
#     y = 2*math.sin(v)


y = (2*math.sin(v) for v in x)



print(x,list(y))

print(
*map(lambda n: '.'*n,
filter(lambda n: not bool(n%3),
range(10))),
sep=' ')
