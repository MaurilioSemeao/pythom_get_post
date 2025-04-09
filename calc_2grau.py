import math

def f_calc_2grau(a, b, c):
    
    if a == 0:

         return "Não é uma equação do segundo grau.", None, None

    delta = b**2 - 4*a*c
    print(f"Delta: {delta}")

    if delta < 0:
         return "A equação não possui raízes reais.", None, None
    elif delta == 0:
        x = -b / (2*a)
        return "A equação possui uma raiz real.", x, x
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return "A equação possui duas raízes reais.", x1, x2