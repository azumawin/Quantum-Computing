import sympy as sp

I = sp.I

A = sp.Matrix(
    [
        [3 + 4 * I, -1 + I, -2 - I],
        [3 + 2 * I, 3 - 4 * I, -2 + I],
        [-5 - I, -4 - 3 * I, 1 - 4 * I],
    ]
)

b = sp.Matrix([-2 - I, 3 + I, -2 + 4 * I])

# solve A*x=b and simplify
x = A.LUsolve(b)
x = sp.simplify(x)

print("x =", x)
isCorrect = sp.simplify(A * x - b) == sp.Matrix([0, 0, 0])
print(f"solution is correct: {isCorrect}")
