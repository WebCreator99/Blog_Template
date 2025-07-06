class MathOperations: #Method overloading is the ability to define multiple methods with the same name but different parameters.
    def add(self, a, b, c=0):
        return a + b + c  #Handle both 2 and 3 parameter cases
    
# Usage
math = MathOperations()
print(math.add(5, 10))
print(math.add(5, 10, 15))
 