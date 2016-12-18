# -*- coding: utf8 -*-
import os
import time
import pickle

def ecrire_fichier(lieu,objet): # Fonction qui permet d'ecrire dans un fichier plus facilement. Prends pour parametre l'emplacement du fichier et l'objet qu'on veut ecrire sur le fichier.
    fichier_nb = open(lieu, "wb")
    mon_pickler = pickle.Pickler(fichier_nb)
    mon_pickler.dump(objet)
    fichier_nb.close()

def lire_fichier(lieu): # Fonction qui permet de lire dans un fichier plus facilement. Prends pour parametre l'emplacement du fichier.
    mon_fichier = open(lieu, "rb")
    depickler = pickle.Unpickler(mon_fichier)
    objet = depickler.load()
    mon_fichier.close()
    return objet


def return_nb (): #Retourne le nombre de pari qui sont dans la base de donnee.
    nb_recuperer = lire_fichier("Donnees/nbfichier.txt")
    return nb_recuperer

def modifie_nb(nb): #Fonction qui permet de modifier le fichier nbfichier.txt en lui mettant la valeur donnee en argument.
    fichier_nb = open("Donnees/nbfichier.txt", "wb")
    mon_pickler = pickle.Pickler(fichier_nb)
    mon_pickler.dump(nb)
    fichier_nb.close()

# ------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------

def del_all_pari (): # Fonction qui permet de remmettre tout son historique a 0.
    nb_recuperer = return_nb() # On recupere le nombre de pari present dans la base de donnee
    if nb_recuperer !=0 :

        for i in range (1,nb_recuperer+1): #On supprime du premier fichier au dernier fichier.
            b = "Donnees/fichier{0}.txt".format(i)
            os.remove(b)
        modifie_nb(0) # Il n'y a plus de pari desormais. On modifie donc l'indicateur de paris dans la base de donnee.
        return 1
    else :
        return 0 # Il n'y  a rien a supprimer car la base de donnee est vide.



def del_pari(n) :                            # Fonction qui supprime un pari bien precis et qui renomme ensuite les fichiers pour ne pas laisser de vide.
    nb = return_nb()                         # On recupere le nombre de pari dans la base de donnee
    b = "Donnees/fichier{0}.txt".format(n)   # On met dans b l'emplacement du fichier a supprimer.
    liste = lire_fichier(b)
    if n > 0 and n<=nb :                     # Si cet emplacement est viable ( qu'il est plus grand que 0 et qu'il est plus petit ou egal au nombre de pari dans la base de donnee.
        a = liste[10]                        # On recupere l'emplacement du premier pari du combine
        c =liste[9]                          # On recupere le nombre de paris présents dans le combiné
        d = c+a                              # On recupere le numero du dernier pari a supprimer
        for i2 in range(a,d):
            os.remove("Donnees/fichier{0}.txt".format(i2)  )   # Alors on supprime les fichier du pari ou du combiné.
        for i in range (d+1,nb+1):           # On renomme ensuite tous les fichiers ulterieurs.
            os.rename("Donnees/fichier{0}.txt".format(i),"Donnees/fichier{0}.txt".format(i-1))
        modifie_nb(nb-c)                     # Comme on a supprimer un oy plusieurs paris, on modifie le nombre de paris dans la base
        return 1                             # On retourne 1 puisque la supression a ete effective.
    else :                                   # Sinon, cela signiifie que l'emplacement n'est pas viable
        return 0                             # On retourne alors 0



# ----------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------

def val_absolu(a):
    if a <0 :
        a = a * -1
    return a

# ----------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------

def add_pari (a):#Fonction qui ajoute des matchs dans la base de donnÃƒÆ’Ã‚Â©e ÃƒÆ’Ã‚Â  partir d'une liste a double dimension. La liste est a double dimension au cas ou  il faudrait entrer un combinÃƒÆ’Ã‚Â©.
    match = a[0]
    lol = a[1]

    chaine_finale = "[{0}] [{1}] [{2}] [{3}] [{4}] [{5}] [{6}] [{7}] [{8}]".format(match[0],match[1], match[2],match[3],match[4],match[5],match[6],match[7],match[8],)


    for i2 in range (0,match[9]):
        nb_recuperer = return_nb()
        nb_recuperer = nb_recuperer +1
        nom = "Donnees/fichier{0}.txt".format(nb_recuperer)
        ecrire_fichier(nom, lol[i2])
        modifie_nb(nb_recuperer)


def modifie_pari (n,resultat) : #Fonction qui permet de changer le pari en mettant si il a ete gagnant ou perdu

    a = lire_fichier("Donnees/fichier{0}.txt".format(n))

    for i in range (a[10],a[9] + a[10] ):
        t = lire_fichier("Donnees/fichier{0}.txt".format(i))
        if resultat == "n" or resultat == "g" or resultat =="p":
            t[0] = resultat
            ecrire_fichier("Donnees/fichier{0}.txt".format(i), t)

        else :
            return(0)
    return 1



def read_pari(): # Lis tous les paris du plus ancien au plus rÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â‚¬Å¾Ã‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©cent.
    try :
        h = lire_fichier("Donnees/nbfichier.txt")
    except :
        print("impossible de lire le fichier ")
        exit()

    nb_recuperer = return_nb()
    lol2 = ""
    for i in range (1,nb_recuperer+1):
        nom_fichier = "Donnees/fichier{0}.txt".format(i)
        match = lire_fichier(nom_fichier)
        lol = ""
        for i2 in range (0,11):
            lol = lol + " [" + str(match[i2]) + "] "

        lol = "\n{0} - {1}".format(i,lol)
        lol2 = lol2 + lol


    return(lol2)


def read_pari_graphique(deb,fin): # Lis tous les paris du plus ancien au plus rÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â‚¬Å¾Ã‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©cent.
    try :
        h = lire_fichier("Donnees/nbfichier.txt")
    except :
        print("impossible de lire le fichier ")
        exit()

    nb_recuperer = return_nb()
    if fin > nb_recuperer :
        fin = nb_recuperer
        deb = nb_recuperer-14
        if deb < 1 :
            deb = 1

    elif deb < 1 :
        deb = 1
        fin = 15
        if fin > nb_recuperer :
            fin  = nb_recuperer

    lol2 = ""
    for i in range (deb,fin+1):
        nom_fichier = "Donnees/fichier{0}.txt".format(i)
        match = lire_fichier(nom_fichier)
        lol = ""
        for i2 in range (0,11):
            lol = lol + " [" + str(match[i2]) + "] "

        lol = "\n{0} - {1}".format(i,lol)
        lol2 = lol2 + lol


    return(lol2)



def calcul_balance(): # Calcul le benefice ou le deficite
    try :
        h = lire_fichier("Donnees/nbfichier.txt")
    except :
        print("impossible de lire le fichier ")
        exit()

    nb_recuperer = return_nb()
    resultat =[None]*nb_recuperer
    gains =[None]*nb_recuperer
    mise =[None]*nb_recuperer
    nb_match=[None]*nb_recuperer
    balance = 0

    for i in range (1,nb_recuperer+1):
        nom_fichier = "Donnees/fichier{0}.txt".format(i)
        match = lire_fichier(nom_fichier)
        lol = ""

        if match[0] == "g": # Si le pari a ete gagne
            balance = balance + match[5] / match[9]  - match[3] / match[9]

        if match[0] == "p": # Si le pari a ete perdu
            balance= balance - match[3]/match[9]

    return balance

def initialisation():
    if not os.path.exists("Donnees/"):    # On cree le dossier si il n'existe pas
            os.mkdir("Donnees/")
    try :#On tente d'ouvrire le fichiers contenant le nombre de paris dans la base de donnÃƒÆ’Ã‚Â©e
        fichier = open("Donnees/nbfichier.txt", "rb")
        fichier.close()

    except : #Si il n'existe pas, on cree un fichier avec 0 a l'interieur
        fichier_nb = open("Donnees/nbfichier.txt", "wb")
        nb = 0
        mon_pickler = pickle.Pickler(fichier_nb)
        mon_pickler.dump(nb)
        fichier_nb.close()
