class Calculator:
    def __init__(self):
        self._result = 0
    def add(self, value):
        self._result += value
        return self._result
    def subtract(self, value):
        self._result -= value
        return self._result
    def get_result(self):
        return self._result
    def set_result(self, value):
        self._result = value
calc = Calculator()
print("Initial Result:", calc.get_result())  
calc.add(10)
print("After Adding 10:", calc.get_result()) 
calc.add(5)
print("After Adding 5:", calc.get_result())  
calc.subtract(3)
print("After Subtracting 3:", calc.get_result()) 
calc.subtract(7)
print("After Subtracting 7:", calc.get_result()) 
calc.set_result(100)
print("After Setting Result to 100:", calc.get_result())  