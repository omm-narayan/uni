def power_of(x):
    def power(y):
        return y ** x
    return power

square = power_of(2)
cube = power_of(3)

print(square(5))
print(cube(5))
