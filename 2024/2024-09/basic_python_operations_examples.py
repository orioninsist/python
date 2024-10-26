A = 8
print(A)  # Output: 8
B = 2
print(B)  # Output: 2
print(A + B)  # Adds A and B, Output: 10
TOTAL = A + B
print(TOTAL)  # Stores the sum of A and B in TOPLAM, Output: 10
A = B  # Assigns the value of B (2) to A
print(A)  # Now A is 2, Output: 2
A = B = 0  # Assigns 0 to both A and B
print(A)  # Output: 0
print(B)  # Output: 0


# Variable naming in Python
_ali = 3
a_li = 4
# ali# = "BTK" would cause a syntax error due to the `#` symbol in the variable name


# To see the list of reserved keywords in Python:
import keyword
print(keyword.kwlist)
# Output: List of Python reserved keywords, like 'False', 'None', 'True', etc.

# To see the list of reserved keywords in Python:
import keyword
print(keyword.kwlist)
# Output: List of Python reserved keywords, like 'False', 'None', 'True', etc.

# Built-in functions in Python:
print(dir(__builtins__))  # Displays all available built-in functions and exceptions

# Example of variable assignments and printing:
A = 3
print(A)  # Output: 3
a = 4
print(a)  # Output: 4
print(A, a)  # Output: 3 4


# Variable swapping in Python:
A = 3
B = 4
C = A  # Temporarily stores A's value in C
A = B  # A gets B's value
B = C  # B gets C's (original A's) value
print(A, B, C)  # Output: 4 3 3

# Quick swapping:
A, B = B, A
print(A)  # Output: 3
print(B)  # Output: 4

# Swapping strings:
K = "BTK"
Y = "ACADEMY"
K, Y = Y, K
print(K, Y)  # Output: ACADEMY BTK


# Accumulating values in a variable:
Phone = 0
Phone = Cep + 10
Phone = Cep + 20
Phone = Cep + 25
Phone = Cep + 40
print(Phone)  # Output: 95


# Basic math operations:
Total = 0
A = 45
B = 35
Total = A + B
print(Total)  # Output: 80


# More math examples:
3 + 5         # Output: 8
17 - 5        # Output: 12
5 * 3         # Output: 15
25 / 5        # Output: 5.0
26 / 5        # Output: 5.2
26 // 5       # Output: 5 (floor division)
2 ** 2        # Output: 4 (exponentiation)
3 ** 2        # Output: 9
10 % 4        # Output: 2 (modulus)
12 % 5        # Output: 2


# Performing and printing various arithmetic operations:
A = 9
B = 15
print(A, '+', B, '=', A + B)  # Addition, Output: 9 + 15 = 24
print(A, '-', B, '=', A - B)  # Subtraction, Output: 9 - 15 = -6
print(A, '*', B, '=', A * B)  # Multiplication, Output: 9 * 15 = 135
print(A, '/', B, '=', A / B)  # Division, Output: 9 / 15 = 0.6
print(A, '//', B, '=', A // B)  # Floor division, Output: 9 // 15 = 0
print(A, 'mod', B, '=', A % B)  # Modulus, Output: 9 mod 15 = 9
print(A, '**', B, '=', A ** B)  # Exponentiation, Output: 9**15


# Order of operations in Python:
3 + 5 * 2  # Output: 13
2 + 3 * 2 ** 2  # Output: 14
3 + 5 * 2 / 4  # Multiplication/division/modulus has the same precedence, Output: 5.5
(5 - 3) * 5 + 2  # Parentheses have the highest precedence, Output: 12
(-3) * (-2)  # Output: 6
6 - -5  # Output: 11


# A more complex mathematical expression:
X = (2 ** 2 + 3 / 5) / (3 ** 2 - 2 * 5)
print(X)  # Calculates the value based on the specified order of operations


