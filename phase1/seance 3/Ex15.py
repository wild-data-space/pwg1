#Utilisez une instruction try et except pour traiter un dépassement de liste lors de l'accès à une taille fixe.
def IndexList(l:list):
    try:
        return l[10]
    except IndexError:
        return None

