a = 12
b = 23
 # with third variable
t = a
a = b
b = t
print(a)
print(b)

# without third variable
a = a + b
b = a - b
a = a - b
print(a)
print(b)

# without losing bits
a = a ^ b
b = a ^ b
a = a ^ b
print(a)
print(b)
# swap in one line with rot2
a,b = b,a
print(a)
print(b)

