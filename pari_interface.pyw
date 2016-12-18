# -*- coding: utf8 -*-

# Crée par Fayçal BOUSMAHA
from paris_sportif import *
from tkinter import *

#-------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Outils utiles tel que la vérification que le champs contienne un nombre entier ou un nombre à vigule

def effacer_liste():
    global liste
    liste = []

def effacer_tout():
    for w in Mafenetre.winfo_children():
        w.destroy()


def verifier_chiffres_float(entry,presence):# Si presence = 1 , On verifie seulement que ce ne soit pas vide. Si presence = 2 , verifie qu'il n'y ait que des chiffres, si presence = 3 on verifie les 2
    string = entry.get()
    if string == None:
        string = ""
    a = len(string)
    if presence !=2 :
        if a == 0:
            return -1
        elif presence ==1 :
            return 1

    if presence !=1:
        for i in range(0,a):
            if string[i] <"0" and string[i]!="." or string[i] >"9" and string[i]!=".":
                return -2
        return 1


def verifier_chiffres(entry,presence):# Si presence = 1 , On verifie seulement que ce ne soit pas vide. Si presence = 2 , verifie qu'il n'y ait que des chiffres, si presence = 3 on verifie les 2
    string = entry.get()
    if string == None:
        string = ""
    a = len(string)
    if presence !=2 :
        if a == 0:
            return -1
        elif presence ==1 :
            return 1

    if presence !=1:
        for i in range(0,a):
            if string[i] <"0"or string[i] >"9" :
                return -2
        return 1
# -------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Lire balance

def lire_balance_graphique (): #Fonction qui lit la balance avec une phrase.
    balance = calcul_balance()
    balance = balance * 100
    balance = int(balance)
    balance = balance/ 100
    if balance >= 0 :
        return("Vous avez un benefice de :\n{0} euros".format(balance))
    elif balance < 0 :
        return("Vous avez un deficite de :\n{0} euros" .format(val_absolu(balance)))





# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Historique des paris

# Une version 2 est a realiser grace à la technologie presente dans texte_disabled.py
def fenetre_historique():
    effacer_tout()
    global min,max

    Frame1 = Frame(Mafenetre,borderwidth=2, bg = '#ffffff')
    Label1 = Label(Frame1,bg = "#ffffff",fg = "#b01512",font=('Century Gothic', 16,'bold'),text="Historique")
    Label1.pack(side = TOP)

    Label2 = Label(Frame1,bg = '#ffffff',font=('Century Gothic',8),text="{0}".format(read_pari_graphique(min,max)))
    Label2.pack(padx=10,pady=10)
    Button(Frame1,text="Precedent",bg = '#2853b3',fg='#ffffff',font='Arial',command=read_pari_graphique_3).pack(side = LEFT, padx=5,pady=0)
    Button(Frame1,text="Menu",bg = '#2853b3',fg='#ffffff',font='Arial',command=menu).pack(side =LEFT, padx=5,pady=0)
    Button(Frame1,text="Suivant",bg = '#2853b3',fg='#ffffff',font='Arial',command=read_pari_graphique_2).pack(side =LEFT,padx=5,pady=0)
    Frame1.pack(padx=0,pady=0)


def read_pari_graphique_2():
    effacer_tout()
    global min,max
    min = min + 15
    max = max + 15
    Frame1 = Frame(Mafenetre,borderwidth=2, bg = '#ffffff')
    Label1 = Label(Frame1,bg = "#ffffff",fg = "#b01512",font=('Century Gothic', 16,'bold'),text="Historique")
    Label1.pack(side = TOP)

    Label2 = Label(Frame1,bg = '#ffffff',font=('Century Gothic',8),text="{0}".format(read_pari_graphique(min,max)))
    Label2.pack(padx=10,pady=10)
    Button(Frame1,text="Precedent",bg = '#2853b3',fg='#ffffff',font='Arial',command=read_pari_graphique_3).pack(side = LEFT, padx=5,pady=0)
    Button(Frame1,text="Menu",bg = '#2853b3',fg='#ffffff',font='Arial',command=menu).pack(side =LEFT, padx=5,pady=0)
    Button(Frame1,text="Suivant",bg = '#2853b3',fg='#ffffff',font='Arial',command=read_pari_graphique_2).pack(side =LEFT,padx=5,pady=0)
    Frame1.pack(padx=0,pady=0)


def read_pari_graphique_3(): # Fonction appelé qui gere l'appui sur le bouton precedent dans l'historique des paris
    effacer_tout()
    global min,max
    min = min - 15
    max = max - 15
    Frame1 = Frame(Mafenetre,borderwidth=2, bg = '#ffffff')
    Label1 = Label(Frame1,bg = "#ffffff",fg = "#b01512",font=('Century Gothic', 16,'bold'),text="Historique")
    Label1.pack(side = TOP)

    Label2 = Label(Frame1,bg = '#ffffff',font=('Century Gothic',8),text="{0}".format(read_pari_graphique(min,max)))
    Label2.pack(padx=10,pady=10)
    Button(Frame1,text="Precedent",bg = '#2853b3',fg='#ffffff',font='Arial',command=read_pari_graphique_3).pack(side = LEFT, padx=5,pady=0)
    Button(Frame1,text="Menu",bg = '#2853b3',fg='#ffffff',font='Arial',command=menu).pack(side =LEFT, padx=5,pady=0)
    Button(Frame1,text="Suivant",bg = '#2853b3',fg='#ffffff',font='Arial',command=read_pari_graphique_2).pack(side =LEFT,padx=5,pady=0)
    Frame1.pack(padx=0,pady=0)


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Ajouter un pari à la base de donnée


def validation(n):
    effacer_tout()
    effacer_liste()

    Mafenetre.title('Ticket validé')
    Frame1 = Frame(Mafenetre,borderwidth=2, bg = '#ffffff')
    Label1 = Label(Frame1,bg = "#ffffff",fg = "#b01512",font=('Century Gothic', 16,'bold'),text="Ticket validé")
    Label1.pack(side = TOP)
    Label(Frame1,bg = "#ffffff",fg = "#b01512",font=('Century Gothic', 16,'bold'),text="  ").pack(side = TOP)

    if n == 1:
        Label2 = Label(Frame1,bg = "#ffffff",font=('Century Gothic', 10),text="Vous reviendrez au menu automatiquement dans 3 secondes")
        Label2.pack(side = TOP)
        Frame1.pack()
        Mafenetre.after(1000,lambda:validation(2))
        Mafenetre.mainloop()

    if n == 2:
        Label2 = Label(Frame1,bg = "#ffffff",font=('Century Gothic', 10),text="Vous reviendrez au menu automatiquement dans 2 secondes")
        Label2.pack(side = TOP)
        Frame1.pack()
        Mafenetre.after(1000,lambda:validation(3))
        Mafenetre.mainloop()

    if n == 3:
        Label2 = Label(Frame1,bg = "#ffffff",font=('Century Gothic', 10),text="Vous reviendrez au menu automatiquement dans 1 seconde")
        Label2.pack(side = TOP)
        Frame1.pack()
        Mafenetre.after(1000,lambda:validation(4))
        Mafenetre.mainloop()

    if n == 4:
        menu()





def fenetre_ajouter_pari_step_3(i,entry_nb_pari,entry_mise,entry_equipe_dom,entry_equipe_ext,entry_pronostique,entry_cote):
    b = entry_pronostique.get()
    if b =="":
        a = -1
    else:
        a = int(b)

    #Verification qu'il y a bien des chiffres au bons endroits
    if verifier_chiffres(entry_equipe_dom,1)==-1:
        fenetre_ajouter_pari_step_2(i,1,-1,entry_nb_pari,entry_mise,3)
    elif verifier_chiffres(entry_equipe_ext,1)==-1:
        fenetre_ajouter_pari_step_2(i,2,-1,entry_nb_pari,entry_mise,3)

    elif verifier_chiffres_float(entry_cote,3)==-1:
        fenetre_ajouter_pari_step_2(i,3,-1,entry_nb_pari,entry_mise,3)
    elif verifier_chiffres_float(entry_cote,3)==-2:
        fenetre_ajouter_pari_step_2(i,-1,3,entry_nb_pari,entry_mise,3)
    elif a ==-1 :
        fenetre_ajouter_pari_step_2(i,4,-1,entry_nb_pari,entry_mise,3)

    global nb_pari,mise,liste
    temps_tab = time.localtime()

    liste.append([])
    liste[i-1].append("n")
    liste[i-1].append(entry_equipe_dom.get())
    liste[i-1].append(entry_equipe_ext.get())
    liste[i-1].append(mise)
    liste[i-1].append(float(entry_cote.get()))
    liste[i-1].append(0) # Gains total esperer
    liste[i-1].append(a )# Pronostique
    liste[i-1].append("{2}{1}{0}".format( temps_tab[2],temps_tab[1],temps_tab[0]))
    liste[i-1].append( "{0} {1} ".format( temps_tab[3],temps_tab[4]))
    liste[i-1].append(nb_pari)
    liste[i-1].append(return_nb() + 1)


    c = 1

    if i == nb_pari:
        for i in range (0,liste[0][9]):
            c = liste[i][4]*c
        c = c*liste[i][3]
        for i2 in range (0,liste[0][9]):
            liste[i][5] = liste[i][5]+c
        mdr = [liste[0],liste]
        add_pari(mdr)
        validation(1)

    i = i +1
    fenetre_ajouter_pari_step_2(i,-1,-1,entry_nb_pari,entry_mise,3)


def fenetre_ajouter_pari_step_2(i,entry_vide,entry_non_chiffre,entry_nb_pari,entry_mise,provenance):
    global nb_pari,mise

    if provenance ==1:
        if verifier_chiffres(entry_nb_pari,3) == -1:
            fenetre_ajouter_pari(1,-1,"")
        if verifier_chiffres(entry_nb_pari,3) == -2:
            fenetre_ajouter_pari(-1,1,"")

        nb_pari = int(entry_nb_pari.get())
        if verifier_chiffres(entry_mise,3) == -1:
            fenetre_ajouter_pari(2,-1,string)
        if verifier_chiffres(entry_mise,3) == -2:
            fenetre_ajouter_pari(-1,2,string)
        mise = int(entry_mise.get())

    # Lorsqu'on arrive ici, cela signifie que l'etape précédente est bon
    effacer_tout()
    global liste
    Mafenetre.title('Ajouter un pari')
    Frame1 = Frame(Mafenetre,borderwidth=2, bg = '#ffffff')
    Label1 = Label(Frame1,bg = "#ffffff",fg = "#b01512",font=('Century Gothic', 16,'bold'),text="Ajouter un pari")
    Label1.pack(side = TOP)

    string1 = StringVar()
    Label(Frame1,bg = "#ffffff",font=('Century Gothic', 10),text="Pari n°{0}/{1} : ".format(i,nb_pari)).pack()
    Label2 = Label(Frame1,bg = "#ffffff",font=('Century Gothic', 10),text="Equipe à domicile : ")
    Label2.pack(side = TOP)
    entry_equipe_dom = Entry(Frame1, textvariable=string1 , width=30,bg = '#2853b3',fg='#ffffff',font=('Century Gothic',10))
    entry_equipe_dom.pack()

    string2 = StringVar()
    Label3 = Label(Frame1,bg = "#ffffff",font=('Century Gothic', 10),text="Equipe à l'exterieur : ")
    Label3.pack(side = TOP)
    entry_equipe_ext = Entry(Frame1, textvariable=string2, width=30,bg = '#2853b3',fg='#ffffff',font=('Century Gothic',10))
    entry_equipe_ext.pack()

    string3 = StringVar()
    Label4 = Label(Frame1,bg = "#ffffff",font=('Century Gothic', 10),text="Cote du match : ")
    Label4.pack(side = TOP)
    entry_cote = Entry(Frame1, textvariable=string3, width=30,bg = '#2853b3',fg='#ffffff',font=('Century Gothic',10))
    entry_cote.pack()


    entry_pronostique = StringVar()
    Label5 = Label(Frame1,bg = "#ffffff",font=('Century Gothic', 10),text="Pronostique : ")
    Label5.pack(side = TOP)
    Frame2 = Frame(Frame1,borderwidth=2, bg = '#ffffff')
    choix_rouge = Radiobutton(Frame2,bg = "#ffffff",fg= '#2853b3', text="1-0", variable=entry_pronostique, value="1")
    choix_vert = Radiobutton(Frame2,bg = "#ffffff",fg= '#2853b3', text="0-1", variable=entry_pronostique, value="2")
    choix_bleu = Radiobutton(Frame2,bg = "#ffffff",fg= '#2853b3', text="Nulle", variable=entry_pronostique, value="3" )
    choix_rouge.pack(side = LEFT)
    choix_vert.pack(side = LEFT)
    choix_bleu.pack(side = LEFT)
    Frame2.pack()



    Frame3 = Frame(Frame1,borderwidth=2, bg = '#ffffff')
    Button(Frame3,text="Validez",bg = '#2853b3',fg='#ffffff',font='Arial',command=lambda: fenetre_ajouter_pari_step_3(i,entry_nb_pari,entry_mise,entry_equipe_dom,entry_equipe_ext,entry_pronostique,entry_cote)).pack(side =LEFT, padx=5,pady=20)
    Button(Frame3,text="Annulez",bg = '#2853b3',fg='#ffffff',font='Arial',command=menu).pack(side = LEFT, padx=5,pady=20)
    Frame3.pack(side = TOP)



    if entry_vide!=-1 and entry_vide!=4:
        Label(Frame1,fg = "#b01512",bg = "#ffffff",font=('Century Gothic', 10),text="Attention : vous avez laissé\nle champs {0} vide".format(entry_vide)).pack(side = TOP )

    if entry_vide==4:
        Label(Frame1,fg = "#b01512",bg = "#ffffff",font=('Century Gothic', 10),text="Attention : vous n'avez pas donnez\nvotre pronostique.").pack(side = TOP )

    if entry_non_chiffre !=-1:
        Label(Frame1,fg = "#b01512",bg = "#ffffff",font=('Century Gothic', 10),text="Attention : Le champ n°{0} ne \n contenait pas que des chiffres".format(entry_non_chiffre)).pack(side = TOP)

    Frame1.pack()
    Mafenetre.mainloop()




def fenetre_ajouter_pari(entry_vide,entry_non_chiffre,string):
    effacer_tout()
    global liste
    Mafenetre.title('Ajouter un pari')
    Frame1 = Frame(Mafenetre,borderwidth=2, bg = '#ffffff')
    Label1 = Label(Frame1,bg = "#ffffff",fg = "#b01512",font=('Century Gothic', 16,'bold'),text="Ajouter un pari")
    Label1.pack(side = TOP)
    Label(Frame1,bg = "#ffffff",fg = "#b01512",font=('Century Gothic', 16,'bold'),text="  ").pack(side = TOP)



    Label2 = Label(Frame1,bg = "#ffffff",font=('Century Gothic', 10),text="Nombre de paris :\nMettez 1 si c'est un pari simple\nSinon mettez le nombre de paris que contient votre combine")
    Label2.pack(side = TOP)
    var_texte = StringVar()
    entry_nb_pari = Entry(Frame1, textvariable=var_texte,text=string, width=30,bg = '#2853b3',fg='#ffffff',font=('Century Gothic',10))
    entry_nb_pari.pack()
    Label(Frame1,bg = "#ffffff",fg = "#b01512",font=('Century Gothic', 16,'bold'),text="        ").pack()



    Label3 = Label(Frame1,bg = "#ffffff",font=('Century Gothic', 10),text="Entrez votre mise en euros")
    Label3.pack(side = TOP)
    var_texte5 = StringVar()
    entry_mise = Entry(Frame1, textvariable=var_texte5, width=30,bg = '#2853b3',fg='#ffffff',font=('Century Gothic',10))
    entry_mise.pack()

    Frame2 = Frame(Frame1,borderwidth=2, bg = '#ffffff')
    Button(Frame2,text="Validez",bg = '#2853b3',fg='#ffffff',font='Arial',command=lambda: fenetre_ajouter_pari_step_2(1,-1,-1,entry_nb_pari,entry_mise,1)).pack(side =LEFT, padx=5,pady=20)
    Button(Frame2,text="Annulez",bg = '#2853b3',fg='#ffffff',font='Arial',command=menu).pack(side = LEFT, padx=5,pady=20)
    Frame2.pack(side = TOP)

    if entry_vide!=-1:
        Label(Frame1,fg = "#b01512",bg = "#ffffff",font=('Century Gothic', 10),text="Attention : vous avez laissé\nle champs {0} vide".format(entry_vide)).pack(side = TOP )

    if entry_non_chiffre !=-1:
        Label(Frame1,fg = "#b01512",bg = "#ffffff",font=('Century Gothic', 10),text="Attention : Le champ n°{0} ne \n contenait pas que des chiffres".format(entry_non_chiffre)).pack(side = TOP)


    Frame1.pack()
    Mafenetre.mainloop()




# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# Mettre un pari gagnant, perdant ou non-déterminé. Une liste déroulante doit etre mise dans une V2

def modifier_pari_graphique():# Possibilité de mettre liste déroulante ?
    effacer_tout()
    Mafenetre.title('Modifier un pari')
    Frame1 = Frame(Mafenetre,borderwidth=2, bg = '#ffffff')
    Label1 = Label(Frame1,bg = "#ffffff",fg = "#b01512",font=('Century Gothic', 16,'bold'),text="Modifier un pari")
    Label1.pack(side = TOP)
    Label2 = Label(Frame1,bg = "#ffffff",font=('Century Gothic', 10),text="Numero du pari a modifier")
    Label2.pack(side = TOP)
    global var_texte,var_texte3
    ligne_texte = Entry(Frame1, textvariable=var_texte, width=30,bg = '#2853b3',fg='#ffffff',font=('Century Gothic',10))

    ligne_texte.pack()

    Label3 = Label(Frame1,bg = "#ffffff",font=('Century Gothic', 10),text="Entrez p si  vous ayez perdu, \ng si vous avez gagner ou\nn Si le resultat est inconnu.")
    Label3.pack(side = TOP,pady = 10)

    ligne_texte3 = Entry(Frame1, textvariable=var_texte3, width=30,bg = '#2853b3',fg='#ffffff',font=('Century Gothic',10))
    ligne_texte3.pack(side = TOP)
    Button(Frame1,text="Validez",bg = '#2853b3',fg='#ffffff',font='Arial',command=lambda: modifier_pari_envoi(ligne_texte,ligne_texte3)).pack(side =LEFT, padx=5,pady=20)
    Button(Frame1,text="Annulez",bg = '#2853b3',fg='#ffffff',font='Arial',command=menu).pack(side =LEFT, padx=5,pady=20)
    Frame1.pack()

def juste_chiffres(event):
    #ligne_texte.bind("<KeyPress>", juste_chiffres) Voila ce qu'il faut faire pour récuperer l'evenement
    touche=event
    print(touche.keysym)




def modifier_pari_envoi(ligne_texte,ligne_texte2): # Il ya beaucoup d'oprimisations à faire
    global var_texte,var_texte3
    a = ligne_texte.get()
    b = len(a)
    c = var_texte3.get()
    d = len(c)
    if b == 0:
        effacer_tout()
        Mafenetre.title('Modifier un pari')
        Frame1 = Frame(Mafenetre,borderwidth=2, bg = '#ffffff')
        Label1 = Label(Frame1,bg = "#ffffff",fg = "#b01512",font=('Century Gothic', 16,'bold'),text="Modifier un pari")
        Label1.pack(side = TOP)
        Label2 = Label(Frame1,bg = "#ffffff",font=('Century Gothic', 10),text="Numero du pari a modifier")
        Label2.pack(side = TOP)
        Label(Frame1,bg = "#ffffff",fg = "#b01512",font=('Century Gothic', 10),text="Attention : Ce champs est vide").pack(side = TOP)
        global var_texte,var_texte3
        ligne_texte = Entry(Frame1, textvariable=var_texte, width=30,bg = '#2853b3',fg='#ffffff',font=('Century Gothic',10))
        ligne_texte.bind("<KeyPress>", juste_chiffres)
        ligne_texte.pack()

        Label3 = Label(Frame1,bg = "#ffffff",font=('Century Gothic', 10),text="Entrez p si  vous ayez perdu, \ng si vous avez gagner ou\nn Si le resultat est inconnu.")
        Label3.pack(side = TOP,pady = 10)

        ligne_texte3 = Entry(Frame1, textvariable=var_texte3, width=30,bg = '#2853b3',fg='#ffffff',font=('Century Gothic',10))
        ligne_texte3.pack(side = TOP)
        Button(Frame1,text="Validez",bg = '#2853b3',fg='#ffffff',font='Arial',command=lambda: modifier_pari_envoi(ligne_texte,ligne_texte3)).pack(side =LEFT, padx=5,pady=20)
        Button(Frame1,text="Annulez",bg = '#2853b3',fg='#ffffff',font='Arial',command=menu).pack(side =LEFT, padx=5,pady=20)
        Frame1.pack()
        Mafenetre.mainloop()

    for i in range (0,b):
        if a[i] <"0" or a[i] >"9":
            effacer_tout()
            Mafenetre.title('Modifier un pari')
            Frame1 = Frame(Mafenetre,borderwidth=2, bg = '#ffffff')
            Label1 = Label(Frame1,bg = "#ffffff",fg = "#b01512",font=('Century Gothic', 16,'bold'),text="Modifier un pari")
            Label1.pack(side = TOP)
            Label2 = Label(Frame1,bg = "#ffffff",font=('Century Gothic', 10),text="Numero du pari a modifier")
            Label2.pack(side = TOP)
            Label(Frame1,bg = "#ffffff",fg = "#b01512",font=('Century Gothic', 10),text="Attention : Dans ce champs, \nseul les chiffres sont acceptes").pack(side = TOP)
            global var_texte,var_texte3
            ligne_texte = Entry(Frame1, textvariable=var_texte, width=30,bg = '#2853b3',fg='#ffffff',font=('Century Gothic',10))
            ligne_texte.bind("<KeyPress>", juste_chiffres)
            ligne_texte.pack()

            Label3 = Label(Frame1,bg = "#ffffff",font=('Century Gothic', 10),text="Entrez p si  vous ayez perdu, \ng si vous avez gagner ou\nn Si le resultat est inconnu.")
            Label3.pack(side = TOP,pady = 10)

            ligne_texte3 = Entry(Frame1, textvariable=var_texte3, width=30,bg = '#2853b3',fg='#ffffff',font=('Century Gothic',10))
            ligne_texte3.pack(side = TOP)
            Button(Frame1,text="Validez",bg = '#2853b3',fg='#ffffff',font='Arial',command=lambda: modifier_pari_envoi(ligne_texte,ligne_texte3)).pack(side =LEFT, padx=5,pady=20)
            Button(Frame1,text="Annulez",bg = '#2853b3',fg='#ffffff',font='Arial',command=menu).pack(side =LEFT, padx=5,pady=20)
            Frame1.pack()
            Mafenetre.mainloop()
    if d == 1:
        if c == "g" or c == "p" or c == "n":
            modifie_pari(int(a),c)
            menu()
        else :
            effacer_tout()
            Mafenetre.title('Modifier un pari')
            Frame1 = Frame(Mafenetre,borderwidth=2, bg = '#ffffff')
            Label1 = Label(Frame1,bg = "#ffffff",fg = "#b01512",font=('Century Gothic', 16,'bold'),text="Modifier un pari")
            Label1.pack(side = TOP)
            Label2 = Label(Frame1,bg = "#ffffff",font=('Century Gothic', 10),text="Numero du pari a modifier")
            Label2.pack(side = TOP)
            global var_texte,var_texte3
            ligne_texte = Entry(Frame1, textvariable=var_texte, width=30,bg = '#2853b3',fg='#ffffff',font=('Century Gothic',10))
            ligne_texte.bind("<KeyPress>", juste_chiffres)
            ligne_texte.pack()

            Label3 = Label(Frame1,bg = "#ffffff",font=('Century Gothic', 10),text="Entrez p si vous ayez perdu, \ng si vous avez gagner ou\nn Si le resultat est inconnu.")
            Label3.pack(side = TOP,pady = 10)
            Label(Frame1,bg = "#ffffff",fg = "#b01512",font=('Century Gothic', 10),text="Attention : Le caractère que vous\navez entré n'est ni p,\nni g ni n. Veuillez n'entrer qu'un\nde ces caractères").pack(side = TOP)

            ligne_texte3 = Entry(Frame1, textvariable=var_texte3, width=30,bg = '#2853b3',fg='#ffffff',font=('Century Gothic',10))
            ligne_texte3.pack(side = TOP)
            Button(Frame1,text="Validez",bg = '#2853b3',fg='#ffffff',font='Arial',command=lambda: modifier_pari_envoi(ligne_texte,ligne_texte3)).pack( padx=5,pady=20)
            Button(Frame1,text="Annulez",bg = '#2853b3',fg='#ffffff',font='Arial',command=menu).pack( padx=5,pady=20)
            Frame1.pack()
    else :
        effacer_tout()
        Mafenetre.title('Modifier un pari')
        Frame1 = Frame(Mafenetre,borderwidth=2, bg = '#ffffff')
        Label1 = Label(Frame1,bg = "#ffffff",fg = "#b01512",font=('Century Gothic', 16,'bold'),text="Modifier un pari")
        Label1.pack(side = TOP)
        Label2 = Label(Frame1,bg = "#ffffff",font=('Century Gothic', 10),text="Numero du pari a modifier")
        Label2.pack(side = TOP)
        global var_texte,var_texte3
        ligne_texte = Entry(Frame1, textvariable=var_texte, width=30,bg = '#2853b3',fg='#ffffff',font=('Century Gothic',10))
        ligne_texte.bind("<KeyPress>", juste_chiffres)
        ligne_texte.pack()

        Label3 = Label(Frame1,bg = "#ffffff",font=('Century Gothic', 10),text="Entrez p si  vous ayez perdu, \ng si vous avez gagner ou\nn Si le resultat est inconnu.")
        Label3.pack(side = TOP,pady = 10)
        Label(Frame1,bg = "#ffffff",fg = "#b01512",font=('Century Gothic', 10),text="Attention : Veuillez verifier que vous \nn'avez entré qu'un caractère").pack(side = TOP)

        ligne_texte3 = Entry(Frame1, textvariable=var_texte3, width=30,bg = '#2853b3',fg='#ffffff',font=('Century Gothic',10))
        ligne_texte3.pack(side = TOP)
        Button(Frame1,text="Validez",bg = '#2853b3',fg='#ffffff',font='Arial',command=lambda: modifier_pari_envoi(ligne_texte,ligne_texte3)).pack(side =LEFT, padx=5,pady=20)
        Button(Frame1,text="Annulez",bg = '#2853b3',fg='#ffffff',font='Arial',command=menu).pack(side =LEFT, padx=5,pady=20)
        Frame1.pack()

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Supprimer les paris
def del_all_pari_graphique():
    effacer_tout()
    Mafenetre.title('Supprimer tous les paris')
    Frame1 = Frame(Mafenetre,borderwidth=2, bg = '#ffffff')
    Label1 = Label(Frame1,bg = "#ffffff",fg = "#b01512",font=('Century Gothic', 16,'bold'),text="Supprimer tous les paris")
    Label1.pack(side = TOP)

    Label2 = Label(Frame1,bg = "#ffffff",font=('Century Gothic', 10),text="Voulez-vous réinitialiser la base de donnée ?")
    Label2.pack(side = TOP)

    Frame2 = Frame(Frame1,borderwidth=2, bg = '#ffffff')
    Button(Frame2,text="Validez",bg = '#2853b3',fg='#ffffff',font='Arial',command=lambda: validation_del_all_1()).pack(side =LEFT, padx=5,pady=20)
    Button(Frame2,text="Annulez",bg = '#2853b3',fg='#ffffff',font='Arial',command=menu).pack(side = LEFT, padx=5,pady=20)
    Frame2.pack(side = TOP)
    Frame1.pack()
    Mafenetre.mainloop

def validation_del_all_1():
    if del_all_pari() == 1:
        validation_del_all(1)
    else :
        non_validation_del_all(1)


def non_validation_del_all(n):
    effacer_tout()
    effacer_liste()
    Mafenetre.title('Ticket non validé')
    Frame1 = Frame(Mafenetre,borderwidth=2, bg = '#ffffff')
    Label1 = Label(Frame1,bg = "#ffffff",fg = "#b01512",font=('Century Gothic', 16,'bold'),text="Base de donnée non réinitialisée, il y a eu une ERREUR.")
    Label1.pack(side = TOP)
    Label(Frame1,bg = "#ffffff",fg = "#b01512",font=('Century Gothic', 16,'bold'),text="  ").pack(side = TOP)
    Label(Frame1,bg = "#ffffff",font=('Century Gothic', 10),text="Cela peut etre du au fait que la base de données est déja vide. ").pack()

    if n == 1:
        Label2 = Label(Frame1,bg = "#ffffff",font=('Century Gothic', 10),text="Vous reviendrez au menu automatiquement dans 3 secondes")
        Label2.pack(side = TOP)
        Frame1.pack()
        Mafenetre.after(1000,lambda:non_validation_del_all(2))
        Mafenetre.mainloop()

    if n == 2:
        Label2 = Label(Frame1,bg = "#ffffff",font=('Century Gothic', 10),text="Vous reviendrez au menu automatiquement dans 2 secondes")
        Label2.pack(side = TOP)
        Frame1.pack()
        Mafenetre.after(1000,lambda:non_validation_del_all(3))
        Mafenetre.mainloop()

    if n == 3:
        Label2 = Label(Frame1,bg = "#ffffff",font=('Century Gothic', 10),text="Vous reviendrez au menu automatiquement dans 1 seconde")
        Label2.pack(side = TOP)
        Frame1.pack()
        Mafenetre.after(1000,lambda:non_validation_del_all(4))
        Mafenetre.mainloop()

    if n == 4:
        menu()


def validation_del_all(n):
    effacer_tout()
    effacer_liste()
    Mafenetre.title('Base de donnée réinitialisée')
    Frame1 = Frame(Mafenetre,borderwidth=2, bg = '#ffffff')
    Label1 = Label(Frame1,bg = "#ffffff",fg = "#b01512",font=('Century Gothic', 16,'bold'),text="Base de donnée réinitialisée")
    Label1.pack(side = TOP)
    Label(Frame1,bg = "#ffffff",fg = "#b01512",font=('Century Gothic', 16,'bold'),text="  ").pack(side = TOP)

    if n == 1:
        Label2 = Label(Frame1,bg = "#ffffff",font=('Century Gothic', 10),text="Vous reviendrez au menu automatiquement dans 3 secondes")
        Label2.pack(side = TOP)
        Frame1.pack()
        Mafenetre.after(1000,lambda:validation_del_all(2))
        Mafenetre.mainloop()

    if n == 2:
        Label2 = Label(Frame1,bg = "#ffffff",font=('Century Gothic', 10),text="Vous reviendrez au menu automatiquement dans 2 secondes")
        Label2.pack(side = TOP)
        Frame1.pack()
        Mafenetre.after(1000,lambda:validation_del_all(3))
        Mafenetre.mainloop()

    if n == 3:
        Label2 = Label(Frame1,bg = "#ffffff",font=('Century Gothic', 10),text="Vous reviendrez au menu automatiquement dans 1 seconde")
        Label2.pack(side = TOP)
        Frame1.pack()
        Mafenetre.after(1000,lambda:validation_del_all(4))
        Mafenetre.mainloop()

    if n == 4:
        menu()





# Supprimer un seul pari
def del_pari_graphique(entry_vide,entry_non_chiffre):

    effacer_tout()
    Mafenetre.title('Supprimer un pari')
    Frame1 = Frame(Mafenetre,borderwidth=2, bg = '#ffffff')
    Label1 = Label(Frame1,bg = "#ffffff",fg = "#b01512",font=('Century Gothic', 16,'bold'),text="Supprimer un pari.")
    Label1.pack(side = TOP)

    Label2 = Label(Frame1,bg = "#ffffff",font=('Century Gothic', 10),text="Numero du pari a supprimer")
    Label2.pack(side = TOP)

    if entry_vide == 1:
        Label(Frame1,bg = "#ffffff",fg = "#2853b3",font=('Century Gothic', 10),text="Vous n'avez pas entrer le numero du pari à supprimer.").pack(side=TOP)
    if entry_non_chiffre == 1:
        Label(Frame1,bg = "#ffffff",fg = "#2853b3",font=('Century Gothic', 10),text="Vous ne devez entrer que des chiffre dans ce champs de saisie.").pack(side=TOP)

    var_texte_8 = StringVar()
    ligne_texte = Entry(Frame1, textvariable=var_texte_8, width=30,bg = '#2853b3',fg='#ffffff',font=('Century Gothic',10))
    ligne_texte.pack()

    Label3 = Label(Frame1,bg = "#ffffff",font=('Century Gothic', 10),text="Voulez-vous supprimer le pari ? \nSi ce pari est dans un combiné, c'est le combiné entier qui sera supprimé")
    Label3.pack(side = TOP)

    Frame2 = Frame(Frame1,borderwidth=2, bg = '#ffffff')
    Button(Frame2,text="Validez",bg = '#2853b3',fg='#ffffff',font='Arial',command=lambda: validation_del_1(ligne_texte)).pack(side =LEFT, padx=5,pady=20)
    Button(Frame2,text="Annulez",bg = '#2853b3',fg='#ffffff',font='Arial',command=menu).pack(side = LEFT, padx=5,pady=20)
    Frame2.pack(side = TOP)
    Frame1.pack()
    Mafenetre.mainloop


def validation_del_1(ligne_texte):
    if verifier_chiffres_float(ligne_texte,3)==-1:
        del_pari_graphique(1,0)
    elif verifier_chiffres_float(ligne_texte,3)==-1:
        del_pari_graphique(0,1)


    if del_pari(int(ligne_texte.get())) == 1:
        validation_del(1)
    else :
        non_validation_del(1)


def validation_del(n):
    effacer_tout()
    effacer_liste()
    Mafenetre.title('Le pari a bien été supprimé')
    Frame1 = Frame(Mafenetre,borderwidth=2, bg = '#ffffff')
    Label1 = Label(Frame1,bg = "#ffffff",fg = "#b01512",font=('Century Gothic', 16,'bold'),text="Pari supprimé")
    Label1.pack(side = TOP)
    Label(Frame1,bg = "#ffffff",fg = "#b01512",font=('Century Gothic', 16,'bold'),text="  ").pack(side = TOP)

    if n == 1:
        Label2 = Label(Frame1,bg = "#ffffff",font=('Century Gothic', 10),text="Vous reviendrez au menu automatiquement dans 3 secondes")
        Label2.pack(side = TOP)
        Frame1.pack()
        Mafenetre.after(1000,lambda:validation_del(2))
        Mafenetre.mainloop()

    if n == 2:
        Label2 = Label(Frame1,bg = "#ffffff",font=('Century Gothic', 10),text="Vous reviendrez au menu automatiquement dans 2 secondes")
        Label2.pack(side = TOP)
        Frame1.pack()
        Mafenetre.after(1000,lambda:validation_del(3))
        Mafenetre.mainloop()

    if n == 3:
        Label2 = Label(Frame1,bg = "#ffffff",font=('Century Gothic', 10),text="Vous reviendrez au menu automatiquement dans 1 seconde")
        Label2.pack(side = TOP)
        Frame1.pack()
        Mafenetre.after(1000,lambda:validation_del(4))
        Mafenetre.mainloop()

    if n == 4:
        menu()



def non_validation_del(n):
    effacer_tout()
    effacer_liste()
    Mafenetre.title('Pari non supprimé')
    Frame1 = Frame(Mafenetre,borderwidth=2, bg = '#ffffff')
    Label1 = Label(Frame1,bg = "#ffffff",fg = "#b01512",font=('Century Gothic', 16,'bold'),text="Pari non supprimé, il y a eu une ERREUR.")
    Label1.pack(side = TOP)
    Label(Frame1,bg = "#ffffff",fg = "#b01512",font=('Century Gothic', 16,'bold'),text="  ").pack(side = TOP)
    Label(Frame1,bg = "#ffffff",font=('Century Gothic', 10),text="Cela peut etre du au fait que le numéro du pari qui a été donné n'existe pas. ").pack()

    if n == 1:
        Label2 = Label(Frame1,bg = "#ffffff",font=('Century Gothic', 10),text="Vous reviendrez au menu automatiquement dans 3 secondes")
        Label2.pack(side = TOP)
        Frame1.pack()
        Mafenetre.after(1000,lambda:non_validation_del(2))
        Mafenetre.mainloop()

    if n == 2:
        Label2 = Label(Frame1,bg = "#ffffff",font=('Century Gothic', 10),text="Vous reviendrez au menu automatiquement dans 2 secondes")
        Label2.pack(side = TOP)
        Frame1.pack()
        Mafenetre.after(1000,lambda:non_validation_del(3))
        Mafenetre.mainloop()

    if n == 3:
        Label2 = Label(Frame1,bg = "#ffffff",font=('Century Gothic', 10),text="Vous reviendrez au menu automatiquement dans 1 seconde")
        Label2.pack(side = TOP)
        Frame1.pack()
        Mafenetre.after(1000,lambda:non_validation_del(4))
        Mafenetre.mainloop()

    if n == 4:
        menu()

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------


#On vas créer le menu :
def menu():
    effacer_tout()
    global min,max
    min = 1
    max= 15
    # On modifie les caractéristiques liées Ã  la fenetre
    Mafenetre.update()
    Mafenetre.geometry("700x350+300+0")
    Mafenetre.title('Menu Paris Sportif')
    Mafenetre["bg"] = "#ffffff"

    #On modifie les caractéristiques liées Ã  la frame 1
    Frame1 = Frame(Mafenetre,borderwidth=2, bg = '#ffffff')
    Label(Frame1,bg = "#ffffff",fg = '#2853b3',font=('Century Gothic', 16),text="Voici votre balance en cours :").pack(padx=10,pady=10)
    Label(Frame1,bg = "#ffffff",font=('Century Gothic', 12),text="{0}".format(lire_balance_graphique())).pack(padx=10,pady=10)
    #Creation des boutons
    a = Button(Frame1,text="Lire l'historique des paris",bg = '#2853b3',fg='#ffffff',width=19,font=('Arial',11),command=fenetre_historique)
    b = Button(Frame1,text="Ajouter un pari",bg = '#2853b3',fg='#ffffff',width=19,font=('Arial',11),command=lambda: fenetre_ajouter_pari(-1,-1,""))
    c = Button(Frame1,text="Modifier un pari",bg = '#2853b3',fg='#ffffff',width=19,font=('Arial',11),command=modifier_pari_graphique)
    d =  Button(Frame1,text="Supprimer un pari",bg = '#2853b3',fg='#ffffff',width=19,font=('Arial',11),command=lambda: del_pari_graphique(0,0))
    e =  Button(Frame1,text="Supprimer tous les paris",bg = '#2853b3',fg='#ffffff',width=19,font=('Arial',11),command = del_all_pari_graphique)
    print("width :",b['width'])
    a.pack(padx=10,pady=5)
    b.pack(padx=10,pady=5)
    c.pack(padx=10,pady=5)
    d.pack(padx=10,pady=5)
    e.pack(padx=10,pady=5)
    Frame1.update()
    Frame1.pack(side=RIGHT,padx=10,pady=10)

    # On modifie les caracteristiques liees a la Frame 2
    Frame2 = Frame(Mafenetre,borderwidth=2, bg = '#ffffff')
    Label(Frame2,bg = "#ffffff",fg = "#b01512",font=('Century Gothic', 16,'bold'),text="Bienvenue").pack(pady=50)
    Label(Frame2,bg = "#ffffff",font=('Century Gothic', 10),text="Vous etes dans le \nprogramme de gestion de paris de ").pack(pady=10)
    Label(Frame2,bg = "#ffffff",fg = '#2853b3',font=('Century Gothic', 14,'bold'),text="Faycal BOUSMAHA").pack(pady=10)

    Frame2.update()
    Frame2.pack(padx=10,pady=10)





    Mafenetre.mainloop()
# ------------------------------------------------------------------------------
#------------------------------------------------------------------------------

#Declaration des variables globales et appel de menu()
initialisation()
Mafenetre = Tk()
liste = []
mise = -1
var_texte = StringVar()
var_texte3 = StringVar()
min = 1
max = 15
nb_pari = -1.0
menu()


