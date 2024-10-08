#### Imports et définition des variables globales
"""
Exercice réalisé par Arnaud POCHIC
"""
import sys
sys.setrecursionlimit(1050)

#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument
    selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    c = [s[0]]
    o = [1]
    n = len(s)
    k = 1
    for i in range (1,n):
        if s[k] == s[k-1]:
            o[-1] += 1
        else:
            c.append(s[i])
            o.append(1)
        k=k+1
    l = list(zip(c,o))
    return l



def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée
     en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # votre code ici
    # cas de base
    # recherche nombre de caractères identiques au premier
    # appel récursif
    k = 0
    if s=="":
        return []
    for chara in s:
        if chara !=s[0]:
            break
        k+=1
    return [(s[0],k)] + artcode_r(s[k:])


#### Fonction principale

def main():
    """
    fonction principale qui appelle les fonctions secondaires et qui les teste
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
