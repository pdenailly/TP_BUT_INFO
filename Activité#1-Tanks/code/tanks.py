def stats(liste):
    # Tri de la liste pour le calcul de la médiane
    liste_triee = sorted(liste)

    # Taille de la liste (nombre d’observations)
    n = len(liste_triee)
    
    # Calcul des valeurs demandées
    minimum = liste_triee[0]
    maximum = liste_triee[n-1]
    moyenne = int(sum(liste_triee) / n)
    
    # Calcul de la médiane (attention l'indice démarre à 0 et non pas à 1)
    if n % 2 == 1:
        # Si la taille est impaire, la médiane est l'élément du milieu
        mediane = liste_triee[n // 2]
    else:
        # Si la taille est paire, la médiane est la moyenne des deux éléments du milieu
        mediane = int((liste_triee[n // 2 - 1] + liste_triee[n // 2]) / 2)
    
    # Retour des 4 mesures sous forme de valeurs séparées
    return minimum, maximum, moyenne, mediane

def estimateur_1(xmoy):
    return int(2*xmoy-1)

def estimateur_2(xmed):
    return int(2*xmed-1)

def estimateur_3(xmin, xmax):
    return xmax+xmin-1

def estimateur_4(xmax, n):
    return int((n+1)*xmax/n-1)

def estimateur_5(xmin, xmax, n):
    return int((n+1)*(xmax-xmin)/(n-1)-1)

