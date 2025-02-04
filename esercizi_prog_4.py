
def disuguaglianza(tripla):
    # Check if it's a valid triangle using the triangle inequality theorem
    if any(tripla[i] >= sum(tripla) - tripla[i] for i in range(3)):
        return False
    
    # Return triangle type
    if tripla[0] == tripla[1] == tripla[2]:
        return 'equilatero'
    if tripla[0] == tripla[1] or tripla[0] == tripla[2] or tripla[1] == tripla[2]:
        return 'isoscele'
    
    return 'scaleno'


# Sample test cases
test_cases = [
    (3, 3, 3),  # Equilateral
    (5, 5, 8),  # Isosceles
    (4, 5, 6),  # Scalene
    (1, 10, 12), # Invalid (triangle inequality not satisfied)
    (10, 10, 20)  # Isosceles
]

# Testing the function
for sides in test_cases:
    result = disuguaglianza(sides)
    print(f"Triangle with sides {sides} is: {result}")

