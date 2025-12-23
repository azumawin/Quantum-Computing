import sympy as sp

I = sp.I

v1 = sp.Matrix([3 + 4*I, 3 + 2*I, -5 - I])
v2 = sp.Matrix([-1 + I, 3 - 4*I, -4 - 3*I])
v3 = sp.Matrix([-2 - I, -2 + I, 1 - 4*I])

e1 = sp.Integer(1)/8 * sp.Matrix([3 + 4*I, 3 + 2*I, -5 - I])

e2 = sp.Integer(1)/(8*sp.sqrt(2703)) * sp.Matrix([
    -139 - 36*I,
     117 - 306*I,
    -131 - 167*I
])

e3 = sp.Integer(1)/sp.sqrt(14331) * sp.Matrix([
    49 - 68*I,
    -48 + 15*I,
    -36 - 59*I
])

E = [e1, e2, e3]

E_notes = [
    sp.Integer(1)/8 * sp.Matrix([3+4*I, 3+2*I, -5-I]),
    sp.Integer(1)/(8*sp.sqrt(2703)) * sp.Matrix([-139-36*I, 117-306*I, -131-167*I]),
    sp.Integer(1)/sp.sqrt(14331) * sp.Matrix([49-68*I, -48+15*I, -36-59*I])
]

# prints zero vectors if answers were correct (theres no diff between E and E_notes)
for k in range(3):
    diff = sp.simplify(E[k] - E_notes[k])
    print(f"diff e{k+1} =", diff)
