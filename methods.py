import chemlib
import math
from datetime import date

def printMenu():
    dashboard = f"""

{date.today()}      Chemistry Calculator        Made by: Bilal Tabbaa

0) Show menu

1) Calculate the Equilibrium constant (Keq) of a formula
2) Calculate the Solubility equilibrium (Ksp) of a formula

99) Exit

"""
    print(dashboard)


def Keq(formula: str=None) -> int:

    if not formula:
        formula = input('Enter the formula: ')

    reaction = chemlib.Reaction.by_formula(formula)
    print('* Balancing the formula...')
    reaction.balance()
    print('+ Formula has been balanced')
    product_forms = list(set([chemlib.Compound(e).formula for e in reaction.product_formulas]))
    reactant_forms = list(set([chemlib.Compound(e).formula for e in reaction.reactant_formulas]))

    print(f'\n\nCalculating the Equilibrium constant of -=[ {reaction.formula} ]=-\n\n')

    reactant_table = {}
    product_table = {}

    for i in reactant_forms:
        reactant_table[i] = float(input(f"Enter the molar concentration of [{i.replace('₁', '')}]: "))

    for i in product_forms:
        product_table[i] = float(input(f"Enter the molar concentration of [{i.replace('₁', '')}]: "))

    top = []
    for i in product_table:
        top.append(product_table[i]**reaction.coefficients[i])

    bottom = []
    for i in reactant_table:
        bottom.append(reactant_table[i]**reaction.coefficients[i])

    print(f'\n\nKeq = {math.prod(top)/math.prod(bottom)}\n\n')



def Ksp(formula: str=None) -> int:
    if not formula:
        formula = input('Enter the formula: ')

    reaction = chemlib.Reaction.by_formula(formula)
    print('* Balancing the formula...')
    reaction.balance()
    print('+ Formula has been balanced')
    product_forms = list(set([chemlib.Compound(e).formula for e in reaction.product_formulas]))

    print(f'\n\nCalculating the Solubility equilibrium of -=[ {reaction.formula} ]=-\n\n')

    product_table = {}

    for i in product_forms:
        product_table[i] = float(input(f"Enter the molar concentration of [{i.replace('₁', '')}]: "))

    top = []
    for i in product_table:
        top.append(product_table[i]**reaction.coefficients[i])

    print(f'\n\nKsp = {math.prod(top)}\n\n')