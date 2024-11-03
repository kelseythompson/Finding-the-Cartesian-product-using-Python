def cartesian_product(A, B):
    cartesian_product = [(a, b) for a in A for b in B]
    return cartesian_product

# input lists
A = [1, 2, 3, 4, 5, 6]
B = [7, 8, 9, 10, 11, 12]

# Compute Cartesian product
AxB = cartesian_product(A, B)

# Print
print("AxB =", AxB)