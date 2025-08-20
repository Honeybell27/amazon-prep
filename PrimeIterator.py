def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


class PrimeNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return PrimeIterator(self.start, self.end)


class PrimeIterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        while self.start <= self.end:
            value = self.start
            self.start += 1
            if is_prime(value):
                return value
        raise StopIteration


p = PrimeNumbers(1, 20)
print(list(p))