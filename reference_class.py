# map fn.
def sq(n):
    return n * n


L = [1, 2, 3]
newL = []
for i in L:
    newnum = i * i
    newL.append(newnum)

print(newL)

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for index, item in enumerate(L):
    if index == 2 or index == 4 or index == 6:
        print(f"The {index + 1}th element is {item}")

num = int(input("enter number pls"))
table = [num * i for i in range(1, 22)]
print(table)

func = lambda a: a + 5
square = lambda x: x * x
sum = lambda a, b, c: a + b + c

x = 51
print(func(x))
print(square(x))
print(sum(x, 1, 2))

mylist = ["laptop", "lens", "ipad", "iophone", "camera"]
sentence = "~~\n".join(mylist)
print(sentence)

from functools import reduce

sum = lambda a, b: a + b

L = [1, 2, 3, 4]
val = reduce(sum, L)
print(val)
