class SquareIterator:
    
    def __init__(self,n):
        self.a = 1
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.a <= self.n:
            x = self.a**2
            self.a += 1
            return x
        else:
            raise StopIteration     




mynums = SquareIterator(5)
myiter = iter(mynums)

for x in myiter:
    print(x)