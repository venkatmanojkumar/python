words = "why are the strings are is in this format"
word = words.split()
a = [len(wor) for wor in word]
print(a)


length = []
for wor in word:
    length.append(len(wor))
    
print(length)

from math import factorial
f = [len(str(factorial(x))) for x in range(20)]
print(f)

# dict comprehension

country_to_capital = {
    'United Kingdom' : 'London',
    'Brazil' : 'brazilia',
    'morocco' : 'Rabat',
    'Sweden' : 'Stockholm'
}

capital_to_country = {capital:country for country,capital in country_to_capital.items()}

from pprint import pprint as pp
print(pp(capital_to_country))

# iterable protocal

iterable = ['1','2','3','4']
iterabol = print(iter(iterable))
print(next(iterabol))
print(next(iterabol))
print(next(iterabol))
