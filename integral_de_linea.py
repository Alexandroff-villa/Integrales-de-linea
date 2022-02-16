#%matplotlib inline

import sympy as sp
from math import pi


x,y,t = sp.symbols("x y t")

def Int_Lin_vect(tinf,tsup,xt,yt,U,V):
    U = sp.parse_expr(U)
    V= sp.parse_expr(V)

    xt = sp.parse_expr(xt)
    yt = sp.parse_expr(yt)

    Ut = U.subs([(x,xt),(y,yt)])
    Vt = V.subs([(x,xt),(y,yt)])

    xt_diff = sp.diff(xt,t)
    yt_diff = sp.diff(yt,t)

    fr= Ut * xt_diff + Vt * yt_diff
    int_lin_vect = sp.integrate(fr,(t,tinf,tsup))
    return int_lin_vect


def Int_lin_escalar(tinf,tsup,xt,yt,f):

    xt = sp.parse_expr(xt)
    yt = sp.parse_expr(yt)
    f = sp.parse_expr(f)

    ft = f.subs([(x,xt),(y,yt)])

    xt_diff = sp.diff(xt,t)
    yt_diff = sp.diff(yt,t)

    fr = ft * (xt_diff**2+yt_diff**2)**(0.5)
    int_lin_escalar = sp.integrate(fr,(t,tinf,tsup))
    return int_lin_escalar


#int = Int_Lin_vect(-1.4,1.4,'t','t',"(sin(x)*cos(y)","-cos(x)*sin(y))")
int2 = Int_lin_escalar(0,pi/2,'-sin(t)','cos(t)','x*y**2')

print(int2)






