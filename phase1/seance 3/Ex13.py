#Définissez une fonction qui compte le nombre de voyelles dans une chaîne.
def VoyelleNum (t:str):
    number = 0
    voyelles = [
        'a',
        'o',
        'i',
        'e',
        'u',
        'y'
    ]
    for i in t:
        if i.lower() in voyelles:
            number +=1
    return number

#Un autre paradigme
def VoyelleNum(t:str):
    voyelles = ['a','e','i','o','u','y']
    l = [i for i in t if i.lower() in voyelles]
    return len(l)
