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

# print(letters)


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

# print(-3**2)
# print((-3)**2)

# x = int(input("Please enter an integer: "))
# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')

# print(x)

# words = ['cat', 'window', 'defenestrate']
# for w in words:
#     print(w, len(w))


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