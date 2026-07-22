from sympy import symbol, Function, Number
from modulus.sym.eq.pde import PDE

class WaveEquation1D(PDE):
    name = "WaveEquation1D"

    def __init__(self, c=1.0):
        x = symbol("x")
        t = symbol("t")

        input_variables = {"x": x, "t": t}
        u = Function("u")(*input_variables)

        if type(c) is str:
            c = 1.0
            c = Function("c")(*input_variables)
        elif type(c) is [float, int]:
            c = Number(c)
        
        self.equations = {}
        self.equations["wave_equation"] = u.diff(t, 2) - (c**2 * u.diff(x)).diff(x)
        # self.equations["wave_equation"] = u.diff(t, 2) - c**2 * u.diff(x)


