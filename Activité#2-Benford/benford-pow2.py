'''
Vérifier si la loi de Benford semble satisfaite pour la suite
des nombres (2^n) (n∈N) en comparant l'histogramme empirique
avec la loi de Benford.
'''

import math
import matplotlib.pyplot as plt

def benford():
    # Calculer les probabilités de la loi de Benford pour d = 1, ..., 9
    p = {d: math.log10(1 + 1/d) for d in range(1, 10)}
    return p

def firstdigit(n):
    # Prendre la valeur absolue de n et convertir en chaîne
    n_str = str(abs(n))
    
    # Enlever la partie avant et après le point décimal si présent
    if '.' in n_str:
        n_str = n_str.replace('.', '')
    
    # Chercher le premier chiffre non nul
    for char in n_str:
        if char != '0':
            return int(char)
    
    # Si n vaut 0, retourner 0
    return 0

def occurrences(liste):
    # Créer un dictionnaire pour compter les occurrences des premiers chiffres
    count = {i: 0 for i in range(1, 10)}  # Dictionnaire pour les chiffres de 1 à 9
    
    # Parcourir chaque élément de la liste
    for n in liste:
        # Trouver le premier chiffre non nul du nombre
        premier_chiffre = firstdigit(n)
        
        # On ignore les occurrences de 0
        if premier_chiffre != 0:
            count[premier_chiffre] += 1
    
    return count

def frequencies(count):
    # Calculer le total des occurrences
    total = sum(count.values())
    
    # Calculer la fréquence de chaque élément
    f = {k: v / total for k, v in count.items()}
    
    return f

# Fonction pour générer les puissances de 2 et extraire les premiers chiffres non nuls
def generate_powers_of_2(n_max):
    return [2 ** n for n in range(n_max)]

# Nombre de puissances de 2 à analyser
n_max = 1000  # Par exemple, les 1000 premières puissances de 2

# Générer les puissances de 2
powers_of_2 = generate_powers_of_2(n_max)

# Calcul des occurrences et des fréquences empiriques
occurrences_empiriques = occurrences(powers_of_2)
frequences_empiriques = frequencies(occurrences_empiriques)

# Calcul des fréquences théoriques selon la loi de Benford
frequences_benford = benford()

# Affichage des résultats
# Histogramme des fréquences empiriques
plt.bar(frequences_empiriques.keys(), frequences_empiriques.values(), alpha=0.6, label='Fréquences empiriques')

# Histogramme des fréquences théoriques (Loi de Benford)
plt.plot(frequences_benford.keys(), frequences_benford.values(), 'ro-', label='Loi de Benford')

# Titrage et légendes
plt.title('Comparaison de la loi de Benford avec les puissances de 2')
plt.xlabel('Premier chiffre non nul')
plt.ylabel('Fréquence')
plt.legend()

# Affichage
plt.show()
