x = 1000
x = 500
print(x)



# below code is for id()
a = 3
print(id(a))
b = 3
print(id(b))

c = id(a) == id(b)
print(c)

#list mutable objects
a = [1,2,3,4]
a[1] = 3
print(a)