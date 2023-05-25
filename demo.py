"""This is showing how to use class"""

symbols = {Meter: 'm',
           Second: 's',
           MeterperSecond: 'm/s'}

class Unit:
    def __init__(self, value, name) -> None:
        self.value = value
        self.name = name

    def __str__(self):
        return str(self.value) + " " + self.name
    
    def double(self):
        return self.value * 2


class Meter(Unit):
    def __init__(self, value) -> None:
        super().__init__(value, "meter")


class Second(Unit):
    def __init__(self, value) -> None:
        super().__init__(value, "second")

class MeterperSecond(Meter, Second):
    def __init__(self, value) -> None:
        super().__init__(value, 'meter per second')

meter = Meter(7)
second = Second(4)
print(meter.value / second.value)
print(type(meter))

