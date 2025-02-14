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

# Filtrer les VINS en spécifiant le mois retenu, par exemple 6 (juin)
mois_cible = 6
vins = df[df['MOIS'] == mois_cible]['VIN'].to_list()
print(vins)

#A completer : estimation de N avec chaque estimateur, et pour chaque mois.


#######################################################
# Estimation de la production pour l'année
#######################################################

#A completer

#######################################################
# Estimation de la production par trimestre
#######################################################

#A completer 