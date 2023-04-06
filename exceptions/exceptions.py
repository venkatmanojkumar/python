digit_map = {
    'one' : '1',
    'two' : '2',
    'three' : '3',
    'four' : '4',
    'five' : '5',
    'six' : '6',
    'seven' : '7'
}

def convert(s):
    number = ''
    for token in s:
        number += digit_map[token]
        print(number)
    x = int(number)
    print(x)

# exception handling

def convert(s):
    """convert a string to an integer"""
    try:
        number = ''
        for token in s:
            number += digit_map(token)
        x = int(number)
        print(f'conversion succededed! x = {x}')
    except KeyError:
        print("conversion failed")
        x =-1
    except TypeError:
        print('conversion type failed')
        x =-1
    return x

convert([1,2,3,4])


try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print("Error: can\'t find file or read data")
else:
   print("Written content in the file successfully")
   fh.close()

# using finally

try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
finally:
   print("Error: can\'t find file or read data")
