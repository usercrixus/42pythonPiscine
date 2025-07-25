class calculator:
    def __init__(self, obj):
        self.obj = obj

    def __add__(self, value):
        self.obj = [x + value for x in self.obj]
        print(self.obj)

    def __sub__(self, value):
        self.obj = [x - value for x in self.obj]
        print(self.obj)

    def __mul__(self, value):
        self.obj = [x * value for x in self.obj]
        print(self.obj)

    def __truediv__(self, value):
        if value == 0:
            raise ZeroDivisionError("division by zero")
        self.obj = [x / value for x in self.obj]
        print(self.obj)

