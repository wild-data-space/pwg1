#Créez une fonction qui provoque une ValueError si un nombre négatif est passé en argument
def NonNegatif(n:float):
    if n < 0:
        raise ValueError('Le nombre est negatif')
    