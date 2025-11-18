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
# a, b = 0, 1
# while a < 10:
#     print(a)
#     a, b = b, a + b

a, b = 0, 1
while a < 1000:
    print(a, end=",")
    a, b = b, a + b

print(-3**2)
print((-3)**2)