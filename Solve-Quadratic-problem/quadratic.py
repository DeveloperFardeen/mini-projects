import math

def solve_quadratic(a, b, c):
    # Calculate the discriminant
    discriminant = b ** 2 - 4 * a * c

    # Determine the nature of the roots and compute them
    if discriminant > 0:
        # Two distinct real roots
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return f"The equation has two real and distinct roots: {root1:.2f} and {root2:.2f}"
    
    elif discriminant == 0:
        # Two equal real roots
        root = -b / (2 * a)
        return f"The equation has two real and equal roots: {root:.2f}"
    
    else:
        # Complex roots
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        return f"The equation has two complex roots: {real_part:.2f} + {imaginary_part:.2f}i and {real_part:.2f} - {imaginary_part:.2f}i"

# Input values for a, b, and c from the user
try:
    a = float(input("Enter the coefficient a: "))
    b = float(input("Enter the coefficient b: "))
    c = float(input("Enter the coefficient c: "))

    if a == 0:
        print("The value of 'a' cannot be zero in a quadratic equation.")
    else:
        result = solve_quadratic(a, b, c)
        print(result)

except ValueError:
    print("Please enter valid numeric values for a, b, and c.")
