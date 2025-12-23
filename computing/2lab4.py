import sympy as sp

I = sp.I

u1 = sp.Matrix([3 + 4 * I, 3 + 2 * I, -5 - I])
u2 = sp.Integer(1)/64 *sp.Matrix([-139 - 36 * I, 117 - 306 * I, -131 - 167 * I])
u3 = sp.Integer(1) / 51 * sp.Matrix([49 - 68*I, -48 + 15*I, -36 - 59*I])
v2 = sp.Matrix([-1 + I, 3 - 4*I, -4 - 3*I])
v3 = sp.Matrix([-2 - I, -2 + I, 1 - 4*I])

u1_u1_inner = (u1.conjugate().T * u1)[0]
u2_u2_inner = (u2.conjugate().T * u2)[0]
u3_u3_inner = (u3.conjugate().T * u3)[0]
u1_v2_inner = (u1.conjugate().T * v2)[0]
u1_v3_inner = (u1.conjugate().T * v3)[0]
u2_v3_inner = (u2.conjugate().T * v3)[0]

# norm = sqrt(<u3,u3>)
norm_u3 = sp.sqrt((u3.conjugate().T * u3)[0])

# e3 = u3 / ||u3||
e3 = sp.simplify(u3 / norm_u3)

print("<u1,u1> =", sp.simplify(u1_u1_inner))
print("<u2,u2> =", sp.simplify(u2_u2_inner))
print("<u3,u3> =", sp.simplify(u3_u3_inner))
print("<u1,v2> =", sp.simplify(u1_v2_inner))
print("<u1,v3> =", sp.simplify(u1_v3_inner))
print("<u2,v3> =", sp.simplify(u2_v3_inner))
print("||u1||  =", sp.sqrt(u1_u1_inner))
print("||u3|| =", sp.simplify(norm_u3))
print("e3 =", e3)
