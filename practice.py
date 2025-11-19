cubes = [1, 8, 27, 65, 125]

cubes[3] = 4**3

# print(cubes)

cubes.append(7**3)

# print(cubes)


rgb = ["Red", "Green", "Blue"]
rgba = rgb

rgba.append("Alpha")

print(id(rgb) == id(rgba))

# print(rgb,"\n",rgba)


letters = ["a", "b", "c", "d", "e", "f", "g"]

# print(letters)


letters[4:] = ["E", "F", "G"]

# print(letters)
# print(letters[-1:-3] )

letters[4:] = []

print(letters)


# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
    # print(a)
    a, b = b, a + b

a, b = 0, 1
while a < 1000:
    # print(a, end=",")
    a, b = b, a + b

print(-3**2)
print((-3)**2)

x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

print(x)

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))


# Create a sample collection
users = {"Hans": "active", "Éléonore": "inactive", "景太郎": "active"}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == "inactive":
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == "active":
        active_users[user] = status

print(users)


for i in range(5):
    print(i)


# -----------------------------------------------------------------------



# data types in python
# int (-22,22)
# float (22.3339)
# string ('')
# bool (True,False)


print('a' < 'Z')
print(ord('a'),ord('a'))


x = [30,432,43234,443,223,4]

for i in range(len(x)):
    print(x[i])

for i, element in enumerate(x):
    print(i, element)


sliced = x[0:4:2]
# [start:stop:step]

print(sliced)



a = set()
b = {3,2,24,2}
c = {'string','string'}

print(b)
print(24 in b)

print(b.union(c))
print(b.difference(c))
print(b.intersection(c))






d = {'key': 'value'}
print(d['key'])

d['key2'] = 'string'

print(d)

print('key' in d)
print(d.values())
print(list(d['key']))


del d['key2']
print(d)



e = [e for e in range(5)]
print(e)

f = [[1 for e in range(10)] for e in range(10)]
print(f)

g = [g for g in range(100) if g % 5 == 0]
print(g)


def func1():
    x = input('Your Name: ')
    y = input('Your Age: ')
    z = input('Your Gender: ')
    if(y.isdigit()):
        y = int(y)
    if(y < 18 and z.lower() == 'female'):
        return print("You're beautiful")
    else:
        raise Exception('Go away boy!')
    
    
func1()


h = [1,2,3,4,54,5]

print(*h)


i = lambda x, y : x + y
print(i(2,3))


j = [1,2,3,4,5,6,7,8,8,6,56,4,34,23,2,3,4,5,6,7,8,9]

mp = map(lambda x: x*2,j)

print(mp)
print(list(mp))