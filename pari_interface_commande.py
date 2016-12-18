# -*- coding: utf-8 -*-

from paris_sportif import *
import os
from time import *
import time

def ajouter_pari():
    os.system("cls")
    match = [None]*11
    match[0] = "n" # Ce n signifie que le resultat du pari n'est pas encore connu. Les autres valeurs sont g (pour gagne) et p (pour perdu)
    match[9] = int(input("Entrez le nombre de matchs que vous pariez en combine. \nSi c'est un pari simple  notez 1 : "))
    lol = [[]]*match[9]
    match[10] = return_nb() + 1
    match[3] = float(input("Quelle est votre mise ? "))
    print("\n\n")
    gain_net =  match[3]

    for i in range (0,match[9]):
        match[1] = input("Quelle est l'equipe a domicile ? ")
        match[2] = input("Quelle est l'equipe a l'exterieur ? ")
        match[4] = float(input("Quelle est votre cote ? "))
        if match[9] == 1:
            gain_net = gain_net* match[4]
        elif match[9]>1 :
            gain_net = gain_net * match[4]
        match[5] = gain_net
        prono_txt = input("Quelle est votre prono ? \n Mettez 1-0, n ou 0-1  :")
        print("\n\n")
        if prono_txt == "1-0":
            match[6] = 1

        elif prono_txt == "0-1":
            match[6] = 2

        elif prono_txt == "n":
            match[6] = 3


        temps_tab = time.localtime()
        match[7] = "{2}{1}{0}".format( temps_tab[2],temps_tab[1],temps_tab[0])
        match[8] = "{0} {1} ".format( temps_tab[3],temps_tab[4])
        lol[i]= list(match)
    match[5] = gain_net / match[9] -  match[3]

    for i0 in range (0,match[9]):
        lol[i0][5] = gain_net
    a = [match,lol]
    add_pari(a)
    os.system("cls")
    print("Voici le pari qui vient d'etre entre : ")
    print("Mise : ",match[3],"euros \n\n")
    fb = ""
    moy = match[3]
    for i5 in range (0,match[9]):
        if lol[i5][6] == 1:
            fb = lol[i5][1]
        if lol[i5][6] == 2:
            fb = lol[i5][2]
        if lol[i5][6]==3:
            fb = "le nul"
        print (lol[i5][1] , " - ",lol[i5][2], "cote : ",lol[i5][4], "\nVous avez parie sur ",fb,"\n\n")
        moy = lol[i5][4] * moy
    moy = moy - match[3]
    print("Voici le gain net total du pari : ",moy)
    g = input("Si vous souhaitez revenir au menu appuyez sur Ok")


def lire_pari (): #Interface console pour lire la base de donnee des paris.
    os.system("cls")
    print(read_pari())
    input("Si vous souhaitez revenir au menu appuyez sur Ok")
def modifier_pari (): #Interface console pour modifier un pari
    os.system("cls")
    nb = int(input("Quel est le numero du pari que vous souhaitez modifie ?"))
    resultat = input("Si vous avez gagne ce pari, mettez g. \nSi celui ci a ete annuler mettez n. \nSi vous avez perdu celui-ci mettez p :\n")
    a = modifie_pari(nb,resultat)
    if a == 1 :
        print("Le changement a bien ete effectue")
    else :
        print("Le changement a echoue . N'essayez d'entrer que g, n ou p")
    input("Si vous souhaitez revenir au menu appuyez sur Ok")

def lire_balance (): #Fonction qui lit la balance avec une phrase.
    balance = calcul_balance()
    if balance >= 0 :
        return("vous avez un benefice de {0} euros".format(balance))
    elif balance < 0 :
        return("vous avez un deficite de {0} euros" .format(val_absolu(balance)))


def sup_pari ():
    os.system("cls")
    n = int(input("Quel est le numero du pari que vous souhaitez supprimer ? "))
    a = del_pari(n)
    if a == 1 :
        print("La suppression a bien ete effectue")
    else :
        print("La suppression a echoue . N'essayez d'entrer que g, n ou p")
    input("Si vous souhaitez revenir au menu appuyez sur Ok")

def sup_tous_paris ():
    os.system("cls")
    a = del_all_pari() #Lancer la fonction qui supprime tous les paris
    if a == 1 :
        print("La suppression a bien ete effectue")
    else :
        print("La suppression a echoue .")
    input("Si vous souhaitez revenir au menu appuyez sur Ok")


def menu():
    a = 0
    while 1:
        os.system("cls")
        if a ==0 :
            print("________________________________________________________________________________")
            print("--------------------------------------------------------------------------------")
            print("_____     _     _____     _______   ________ ")
            print("|   |    / \    |   |        |     |         ")
            print("|___|   /___\   |___|        |     |_______  ")
            print("|      /     \  |   \        |             | ")
            print("|     /       \ |    \    ___|___  ________| ")
            print("________________________________________________________________________________")
            print("--------------------------------------------------------------------------------")
            print("\n\nBy Faycal BOUSMAHA")
            sleep(3)
            a = 1
            os.system("cls")
        print ("Bienvenu sur le programme paris de Faycal BOUSMAHA.\n")
        print("Celui ci permet de gerer ses paris sportifs en constituant une base de donnee.\n Cette base de donnee permet de suivre ses gains et ses pertes.")
        print("\nD'ailleurs, " + lire_balance()+"\n")
        print("D'autres fonctionnalitees sont a venir, \ncomme la possibilite de chercher un pari precis\nou encore recuperer les matchs de la prochaine journee du championnat")
        print(return_nb())
        b = int(input("Veuillez entrer :\n1 si vous souhaitez ajouter un pari\n2 si vous souhaitez consulte la base de donnee\n3 si vous souhaitez rentrer le resultat d'un pari (avez-vous gagner ? perdu ?)\n4 si vous souhaitez remettre a 0 votre base de donnees\n5 si vous souhaitez supprimer un unique pari de la base de donnees\n\n"))

        if b == 1:
            ajouter_pari()
        elif b == 2:
            lire_pari()
        elif b == 3:
            modifier_pari()
        elif b == 4:
            sup_tous_paris()
        elif b==5 :
            sup_pari()
        else:
            print("Veuillez n'entrer qu'un nombre entre 1 et 5. Veuillez reessayer.")
            os.system("cls")

def main():
    ajouter_pari()


menu()
input("")
