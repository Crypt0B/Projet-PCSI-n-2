# On ouvre le fichier
# Modifier le chemin du fichier txt pour que le programme puisse bien fonctionner
fichier = open(" ", "r")


# On initialise les variables, listes et les dictionnaires
dict = {}
grande_liste = []
list_list = []


# On traite les informations du fichier et incrémente les valeurs dans des listes
for line in fichier:
  liste_ligne = line.strip()
  petite_liste = liste_ligne.split(" ")
  grande_liste.append(petite_liste)

# Nous n'avons plus besoin du fichier
fichier.close()

# Nous créons une liste prenant pour valeurs toute les fois ou un sommet interagit
for i in range(1,len(grande_liste)):
    list_list.append(grande_liste[i][0])
    list_list.append(grande_liste[i][1])

# On cherche le nombre de sommet dans notre graphe
nb_sommet = int("".join(grande_liste[0]))


# On crée un dictionnaire de la longueur du nombre de sommet et prenant pour chaque valeur le numéro du sommet
for i in range(nb_sommet+1):
    dict[i] = 0


# On compte le nombre de fois que chaque sommet est connecté à un autre sommet
def compt_sommet():
    for i in range(len(list_list)):
        var_var = int("".join(list_list[i]))
        dict[var_var] = dict[var_var] + 1
    return(dict)
dict = compt_sommet()


# On affiche le degré de chaque sommet
for i in range(1,nb_sommet+1):
    print("Le sommet numéro",i,"est de degré",dict[i])


# On compte le nombre de fois ou un sommet est de degré demander
def compt_sommet_deg2(degré):
    compt = 0
    for i in range(1,nb_sommet+1):
        if dict[i] == degré:
            compt += 1
        else:
            compt = compt
    return(compt)


# On affiche la valeur
# Pour modifier la valeur du degré il faut modifier le nombre dans compt_sommet_deg2()
print("Il y a",compt_sommet_deg2(2),"sommet ce de degré")




# Code create by Crypt0_B
