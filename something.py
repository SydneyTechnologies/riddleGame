import random
test = ['rat', 'cat', 'dog']

def removeCat():
    value = random.choice(test)
    test.remove(value)

removeCat()
print(test)
print(len(test))