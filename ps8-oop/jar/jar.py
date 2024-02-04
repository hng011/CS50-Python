class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError()
        self.__capacity = capacity
        self.__n = 0

    def __str__(self):
        return "🍪" * self.__n

    def deposit(self, n):
        self.__n += n
        if n > self.__capacity:
            raise ValueError("Overflow")
        self.__capacity -= n
    
    def withdraw(self, n):
        self.__n -= n
        if self.__n < 0:
            raise ValueError("Underflow")
        self.__capacity += n

    @property
    def capacity(self):
        return self.__capacity
    
    @property
    def size(self):
        return self.__n

if __name__ == "__main__":
    jar = Jar()
    print(jar.size)
    print(jar.capacity)