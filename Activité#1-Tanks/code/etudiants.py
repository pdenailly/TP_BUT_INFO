import random
import tanks

# Fonction qui retourne le résultat des 5 estimateurs
def estimations(liste):
    # Statistiques
    minimum, maximum, moyenne, mediane = tanks.stats(liste)
    n = len(liste)

    # Estimateurs
    e1 = tanks.estimateur_1(moyenne)
    e2 = tanks.estimateur_2(mediane)
    e3 = tanks.estimateur_3(minimum, maximum)
    e4 = tanks.estimateur_4(maximum, n)
    e5 = tanks.estimateur_5(minimum, maximum, n)

    return e1, e2, e3, e4, e5


# Population totale (inconnue)
N = 100000

# Décalage 1+s,2+s,...,N+s
s = 10

# Nombre d'observations (échantillon)
n = 200

###################################################################
# Génération d'une population et tirage aléatoire d'un échantillon
###################################################################

# Liste complète
population = list(range(s+1,s+N+1))

# Tirer aléatoirement n valeurs sans remise
echantillon = random.sample(population, n)

# Estimations de N : cas 1 et 2
#A completer

# Estimations de N : cas 3
#A completer


# Affichage des résultats
print(f"\nPremier et second cas : s={s} connu, N={N} inconnu (n={n})")
print(f"N1 = {e1}")
print(f"N2 = {e2}")
print(f"N3 = {e3}")
print(f"N4 = {e4}")
print(f"\nTroisième cas : s={s} inconnu, N={N} inconnu (n={n})")
print(f"N5 = {e5}\n")
