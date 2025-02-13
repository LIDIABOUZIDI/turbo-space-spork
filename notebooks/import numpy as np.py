import numpy as np

# EXERCICE 1: Création et manipulation de tableaux NumPy
# 1. Création d'un tableau 1D et conversion en float64
arr1 = np.array([5, 10, 15, 20, 25], dtype=np.float64)
print("Tableau 1D:", arr1)

# 2. Création d'un tableau 2D et affichage de sa forme et taille
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Shape:", arr2.shape, "Size:", arr2.size)

# 3. Création d'un tableau 3D avec des valeurs aléatoires
arr3 = np.random.rand(2, 3, 4)
print("Dimensions:", arr3.ndim, "Shape:", arr3.shape)

# EXERCICE 2: Manipulations avancées des tableaux
# 1. Inversion d'un tableau 1D
arr4 = np.arange(10)[::-1]
print("Inversé:", arr4)

# 2. Extraction d'un sous-tableau spécifique
arr5 = np.arange(12).reshape(3, 4)[:2, -2:]
print("Sous-tableau:", arr5)

# 3. Modification d'un tableau 2D
arr6 = np.random.randint(0, 11, (5, 5))
arr6[arr6 > 5] = 0
print("Tableau modifié:", arr6)

# EXERCICE 3: Initialisation et attributs
# 1. Création d'une matrice identité
identity_matrix = np.eye(3)
print("Matrice identité:", identity_matrix)

# 2. Génération d'un tableau linéairement espacé
linspace_arr = np.linspace(0, 5, 10)
print("Linspace:", linspace_arr)

# 3. Création d'un tableau 3D aléatoire et calcul de la somme
random_3D = np.random.randn(2, 3, 4)
print("Somme des éléments:", np.sum(random_3D))

# EXERCICE 4: Indexation avancée et masquage
# 1. Sélection d'éléments spécifiques
arr7 = np.random.randint(0, 50, 20)
print("Éléments sélectionnés:", arr7[[2, 5, 7, 10, 15]])

# 2. Filtrage avec un masque booléen
arr8 = np.random.randint(0, 30, (4, 5))
print("Masquage > 15:", arr8[arr8 > 15])

# 3. Remplacement des valeurs négatives par 0
arr9 = np.random.randint(-10, 10, 10)
arr9[arr9 < 0] = 0
print("Valeurs négatives remplacées:", arr9)

# EXERCICE 5: Combinaison et division
# 1. Concatenation de tableaux 1D
arr10 = np.concatenate((np.random.randint(0, 10, 5), np.random.randint(0, 10, 5)))
print("Concaténation:", arr10)

# 2. Division d'un tableau 2D en lignes
arr11 = np.random.randint(0, 10, (6, 4))
split_rows = np.split(arr11, 2, axis=0)
print("Split par lignes:", split_rows)

# 3. Division en colonnes
arr12 = np.random.randint(0, 10, (3, 6))
split_cols = np.split(arr12, 3, axis=1)
print("Split par colonnes:", split_cols)

# EXERCICE 6: Fonctions mathématiques
# 1. Calcul de statistiques sur un tableau
arr13 = np.random.randint(1, 100, 15)
print("Moyenne:", np.mean(arr13), "Médiane:", np.median(arr13), "Écart-type:", np.std(arr13), "Variance:", np.var(arr13))

# 2. Somme des lignes et colonnes
arr14 = np.random.randint(1, 50, (4, 4))
print("Somme des lignes:", np.sum(arr14, axis=1), "Somme des colonnes:", np.sum(arr14, axis=0))

# 3. Min et max sur un tableau 3D
arr15 = np.random.randint(1, 20, (2, 3, 4))
print("Max par axe:", np.max(arr15, axis=1), "Min par axe:", np.min(arr15, axis=2))

# EXERCICE 7: Reshape et transposition
# 1. Transformation d'un tableau 1D en 2D
arr16 = np.arange(1, 13).reshape(3, 4)
print("Tableau reshaped:", arr16)

# 2. Transposition d'un tableau
arr17 = np.random.randint(1, 10, (3, 4)).T
print("Tableau transposé:", arr17)

# 3. Aplatissement d'un tableau
arr18 = np.random.randint(1, 10, (2, 3)).flatten()
print("Tableau aplati:", arr18)

# EXERCICE 8: Broadcasting et opérations vectorisées
# 1. Normalisation d'un tableau par colonne
arr19 = np.random.randint(1, 10, (3, 4))
normalized = arr19 - np.mean(arr19, axis=0)
print("Normalisé:", normalized)

# 2. Produit extérieur
arr20 = np.random.randint(1, 5, 4)
print("Produit extérieur:", np.outer(arr20, arr20))

# 3. Augmentation conditionnelle d'un tableau
arr21 = np.random.randint(1, 10, (4, 5))
arr21[arr21 > 5] += 10
print("Tableau modifié:", arr21)

# EXERCICE 9: Tri et recherche
# 1. Tri d'un tableau 1D
arr22 = np.sort(np.random.randint(1, 20, 10))
print("Trié:", arr22)

# 2. Tri d'un tableau 2D par colonne
arr23 = np.random.randint(1, 50, (3, 5))
sorted_arr = arr23[arr23[:, 1].argsort()]
print("Trié par colonne:", sorted_arr)

# 3. Recherche d'indices d'éléments spécifiques
indices = np.where(np.random.randint(1, 100, 15) > 50)
print("Indices des éléments > 50:", indices)

# EXERCICE 10: Algèbre linéaire
# 1. Création d'une matrice et calcul du déterminant
mat1 = np.random.randint(1, 10, (2, 2))
determinant = np.linalg.det(mat1)
print("Matrice:", mat1)
print("Déterminant:", determinant)

# 2. Calcul des valeurs propres et vecteurs propres
mat2 = np.random.randint(1, 5, (3, 3))
eigvals, eigvecs = np.linalg.eig(mat2)
print("Matrice:", mat2)
print("Valeurs propres:", eigvals)
print("Vecteurs propres:", eigvecs)

# 3. Multiplication matricielle
mat3 = np.random.randint(1, 10, (2, 3))
mat4 = np.random.randint(1, 10, (3, 2))
mat_product = np.dot(mat3, mat4)
print("Produit matriciel:", mat_product)

# EXERCICE 11: Échantillonnage et distributions
# 1. Génération d'un échantillon uniforme
uniform_samples = np.random.rand(10)
print("Échantillon uniforme:", uniform_samples)

# 2. Génération d'un échantillon normal
normal_samples = np.random.randn(3, 3)
print("Échantillon normal:", normal_samples)

# 3. Création d'un histogramme
histogram_data = np.random.randint(1, 100, 20)
histogram = np.histogram(histogram_data, bins=5)
print("Histogramme:", histogram)

# EXERCICE 12: Indexation avancée
# 1. Sélection des éléments diagonaux
arr24 = np.random.randint(1, 20, (5, 5))
diagonal = np.diag(arr24)
print("Éléments diagonaux:", diagonal)

# 2. Sélection des nombres premiers
arr25 = np.random.randint(1, 50, 10)
is_prime = lambda x: all(x % i != 0 for i in range(2, int(x**0.5) + 1)) and x > 1
prime_numbers = arr25[[is_prime(i) for i in arr25]]
print("Nombres premiers:", prime_numbers)

# 3. Sélection des nombres pairs
even_numbers = arr25[arr25 % 2 == 0]
print("Nombres pairs:", even_numbers)

# EXERCICE 13: Gestion des valeurs manquantes
# 1. Création d'un tableau avec des NaN
arr26 = np.random.randint(1, 10, 10).astype(float)
arr26[np.random.choice(10, 3, replace=False)] = np.nan
print("Tableau avec NaN:", arr26)

# 2. Remplacement des NaN par la moyenne
arr26[np.isnan(arr26)] = np.nanmean(arr26)
print("Tableau avec NaN remplacés:", arr26)

# 3. Identification des indices contenant des NaN
nan_indices = np.where(np.isnan(arr26))
print("Indices des NaN:", nan_indices)

# EXERCICE 14: Optimisation
# 1. Création d'un grand tableau et calcul optimisé de la moyenne
arr28 = np.random.randint(1, 100, 1_000_000)
avg = np.mean(arr28)
print("Moyenne calculée efficacement:", avg)

# 2. Addition de grandes matrices
arr29 = np.random.randint(1, 10, (1000, 1000))
arr30 = np.random.randint(1, 10, (1000, 1000))
large_sum = arr29 + arr30
print("Addition rapide de grandes matrices:", large_sum)

# 3. Somme selon différents axes
arr31 = np.random.randint(1, 10, (100, 100, 100))
sum_axes = np.sum(arr31, axis=0)
print("Somme sur un axe spécifique:", sum_axes)

# EXERCICE 15: Fonctions cumulatives
# 1. Somme cumulative
arr32 = np.arange(1, 11)
cumsum_values = np.cumsum(arr32)
print("Somme cumulative:", cumsum_values)

# 2. Produit cumulatif
cumprod_values = np.cumprod(arr32)
print("Produit cumulatif:", cumprod_values)

# 3. Cumulatif par lignes et colonnes
arr33 = np.random.randint(1, 20, (4, 4))
cumsum_rows = np.cumsum(arr33, axis=1)
cumsum_cols = np.cumsum(arr33, axis=0)
print("Cumulatif par lignes:", cumsum_rows)
print("Cumulatif par colonnes:", cumsum_cols)

# EXERCICE 16: Dates et temps
# 1. Génération d'une plage de dates journalières
date_range = np.arange('2023-02-01', '2023-02-11', dtype='datetime64[D]')
print("Dates journalières:", date_range)

# 2. Génération d'une plage de dates mensuelles
month_range = np.arange('2022-01', '2022-06', dtype='datetime64[M]')
print("Dates mensuelles:", month_range)

# 3. Conversion de timestamps en datetime
timestamps = np.random.randint(1672531200, 1704067200, 10)
datetime_arr = np.datetime64(0, 's') + timestamps
print("Timestamps convertis:", datetime_arr)

# EXERCICE 17: Types personnalisés
# 1. Création d'un tableau structuré pour stocker des informations sur des livres
structured_dtype = np.dtype([('title', 'S50'), ('author', 'S50'), ('pages', np.int32)])
books = np.array([
    (b"Python Basics", b"John Doe", 300),
    (b"Advanced NumPy", b"Jane Smith", 450),
    (b"Machine Learning", b"Alice Brown", 500)
], dtype=structured_dtype)
print("Livres en tableau structuré:", books)

# 2. Création d'un tableau avec entiers et leur représentation binaire
binary_dtype = np.dtype([('number', np.int32), ('binary', 'S10')])
binary_arr = np.array([(i, bin(i)[2:].encode()) for i in range(5)], dtype=binary_dtype)
print("Représentation binaire:", binary_arr)

# 3. Création d'un tableau avec nombres complexes
complex_dtype = np.dtype([('real', np.float64), ('imag', np.float64)])
complex_arr = np.array([(1, 2), (3, 4), (5, 6)], dtype=complex_dtype)
print("Tableau de nombres complexes:", complex_arr)

