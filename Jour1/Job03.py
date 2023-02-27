class Operation:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Operation(self.value + other.value)

nb1 = Operation(10)
nb2 = Operation(11)
total = nb1 + nb2

print(total.value)