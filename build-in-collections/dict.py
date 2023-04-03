a = [('a',1),('b',2)]
c = dict(a)
print(c)


# update

b = [('c',1),('d',2)]
d = dict(b)
c.update(d)
print(c)


# add

m = {
    'H' : [1,2,3],
    'he': [4,5],
    'li': [10,11]
}
m['H'] += [4,5,6]
print(m)