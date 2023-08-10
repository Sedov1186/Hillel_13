class String(str):

    def __add__(self, other):
        other_str = str(other)
        return String(super().__add__(other_str))

    def __sub__(self, other):
        other_str = str(other)
        return String(self.replace(other_str,'', 1))

print(String('New') + String(890))
print(String(1234) + 5678)
print(String('New') + 'castle')
print(String('New') + 77)
print(String('New') + True)
print(String('New') + ['s', ' ', 23])
print(String('New') + None)

print('-' * 20)

print(String('New bala7nce') - 7)
print(String('New balance') - 'bal')
print(String('New balance') - 'Bal')
print(String('pineapple apple pine') - 'apple')
print(String('New balance') - 'apple')
print(String('NoneType') - None)
print(String(55678345672) - 7)