import pandas as pd
import matplotlib.pyplot as plt
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

annee = 2018

# Charger les données dans un DataFrame Pandas
df = pd.read_csv(f"tesla{annee}.csv", sep=';')
#df = df.drop_duplicates(subset='VIN')

# Convertir la colonne DATE en format datetime (aaaa-mm-jj)
df['DATE'] = pd.to_datetime(df['DATE'], dayfirst=True)

# Créer le nuage de points avec l'année en abscisse et la valeur du VIN en ordonnée
plt.figure(figsize=(7,6))
plt.scatter(df['DATE'], df['VIN'], alpha=0.25)

# Ajouter des labels et un titre
plt.title(f"VINs pour l\'année {annee}")
plt.xlabel('Date')
plt.ylabel('VIN')

# Afficher le graphique
plt.show()

#######################################################
# Estimation de la production par mois
#######################################################

# Colonne contenant le mois
df['MOIS'] = df['DATE'].dt.month

print(df)

for mois in range(1,13):
    # Filtrer le mois spécifique
    vins = df[df['MOIS'] == mois]['VIN'].to_list()
    n = len(vins)
    print(n)
    e1, e2, e3, e4, e5 = estimations(vins)
    print(f"Année {annee} - mois {mois} (n={n})")
    print(f"N1 = {e1}")
    print(f"N2 = {e2}")
    print(f"N3 = {e3}")
    print(f"N4 = {e4}")
    print(f"N5 = {e5}")

#######################################################
# Estimation de la production pour l'année
#######################################################
vins = df['VIN'].to_list()
n = len(vins)
e1, e2, e3, e4, e5 = estimations(vins)

print(f"Année {annee} (n={n})")
print(f"N1 = {e1}")
print(f"N2 = {e2}")
print(f"N3 = {e3}")
print(f"N4 = {e4}")
print(f"N5 = {e5}")


#######################################################
# Estimation de la production par trimestre
#######################################################
trimestres = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

# Filtrer par trimestre en utilisant l'indice de boucle
for trimestre in trimestres:  # Trimestres de 1 à 4 
    # Filtrer les données pour les mois du trimestre actuel
    vins_trimestre = df[df['MOIS'].isin(trimestre)]['VIN'].to_list()
    n = len(vins_trimestre)
    e1, e2, e3, e4, e5 = estimations(vins_trimestre)
    print(f"Année {annee} - mois {trimestre} (n={n})")
    print(f"N1 = {e1}")
    print(f"N2 = {e2}")
    print(f"N3 = {e3}")
    print(f"N4 = {e4}")
    print(f"N5 = {e5}")


