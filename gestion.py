# --------Application de Gestion Restaurant avec python --------------- 
choix_principale = ["1","2","3"] 
menu_admin = """-----------------WELCOME----------!!!!! : 
1--: Admin panel...

2--: Client Panel...

3--: Exit...

? Votre choix : """ 

choice=int(input("Enter your choice :")) 
if choice in choix_principale :
    if choice == "1" :
        admin() 
    elif choice == "2" :
        client() 
    

# fonction pour gerer l'admin 
def administration () : 
    choix_admin = ["1","2"] 
    ch = input("Faites votre choix") 
    if ch in choix_admin : 
        if ch =="1" :
            valeur = connection(1)
        elif ch =="2" :
            valeur = inscription(1)
    # si val renvoi True alors je me suis connecte ,si False alors je me suis deconnecte .. 

    while valeur == True : 
        c = ["1","2","3"] 
        print("1.Modifie le Menu\n")
        print("2.Afficher le Menu\n")
        print("3.Deconnection\n") 
        ch2 = input("Entrez votre choix ") 
        if ch2 in c :
            if ch2 == "1"  :  
                print("1.Ajouter un plat dans le menu")
                print("2.supprimer un plat dans le menu ")
                print("3.Go Back") 
                p = int(input("Entrer votre choix svp ")) 
                if p == 1 : 
                    add_plat() 
                elif p == 2 :
                    delete_plat() 
                else: 
                    continue 
            if ch2 == "2" :  
                afficher_menu_plat() 
            else:
                valeur = False  
                print("Deconnection reussi") 
                main()

def client() :
    cli = ["1","2"]  
    print("1.connection")
    print("2.Inscription") 
    c = input("Entrer votre choix") 
    if c in cli :
        if c == "1" :
            valeur = connection(2)
        else :
            valeur = inscription(2) 
    while valeur == True :
        print("------------------------------------------------------------")
        print("1.Afficher Menu")
        print("2.Commander")
        print("3.deconnexion")
        choice=int(input("Enter your choice :"))
        if choice==1:
             afficher_menu_plat() 
        elif choice==2:
            val=commande()
        else:
            val=False #session time out.... Termination of while loop
            print("Deconnection reussi avec succes")
            main() #after logout another can login so main() is called here 


# Ajouter un plat a mon dictionnnaire liste_plat
def  add_plat() : 
    nom = input("Entrer le nom du plat") 
    prix = int(input("Entrez le prix du plat svp")) 
    liste_plat[name] = prix 
    print("plat ajouter avec succes")

# Supprimer un plat dans mon dictionnaire list_plat
def delete_plat() : 
    #teste si ma liste de plat est vide 
    if len(list_plat)==0:
        print("Rien en supprime")
    else:
        nom=input("Entrer le nom du plat a supprimer :")
        for i in range(len(list_plat)):
            if nom in list_plat.keys():
                del(list_plat[nom])
                print("\nSuppression reussi")
            else:
                print("\n le nom du plat est incorect")
                break

# MA Fonction pour afficher le menu 
def  afficher_menu_plat() : 
    print("---------------------------Menu Restaurant-------------------------")
    if(len(list_plat))==0:
        print("Rien en afficher dans le menu actuellement")
    else:
        Numero=1 
        for i in list_plat.keys():
            print( Numero,".",i,"\t= ",list_plat[i])
            Numero = Numero + 1  


#La fonction pour gerer la commande : 
def commande() :
    afficher_menu_plat() 
    print("******************* Commandez de la nourriture du menu ci-dessus SVP****************") 
    if (len(list_plat)) == 0 : 
        print("Ohhhh je suis desole ya rien en commander !!!!")
    else : 
        cmd = True
    #Tant que il ya de la nourriture pour la commande alors :
    while cmd == True : 
        print("testt")

     


              
   










# test-----------------------------------test------------------
list_repas = ["Thiebou dieune" , "Riz au poulet","CousCous","Fruit de Mer","Mbahalou_Saloum","C'est Bon avec Poisson"] 
#print("Mes listes de Repas est \n",list_repas) 
choix_user = ["1","2","3","4","5"] 
print("*" * 28 + "Gestion Restaurant" + "*" * 24 + "\n")  
print("\n")
menu = """Choisissez parmi les 5 options suivantes Svp !!!!! : 

1--: Ajouter un plat à la liste des plats ...

2--: Supprimer un pat dans la liste des plats ...

3--: Afficher La liste de mes plats  ... 

4--: Modifier un plat de la  liste des plats ... 

5--: Quitter (Bye!!!) 

? Votre choix : """ 

while True : 
    choix = input(menu) 
    if choix in choix_user :
        if choix == "1" :
            plat = input("Tapez votre plat svp !!!") 
            list_repas.append(plat) 
            print("Ajout d'un plat avec succes")  
            break
        elif choix == "2" :
            plat = input("Entrez le plat a supprimer svp !!!") 
            while not plat in list_repas : 
                plat = input('Veuillez saisir un plat existant dans la liste des plats svp') 
            list_repas.remove(plat) 
            break 

        elif choix == "3" :
            print("La liste de mes plats est \n==>",list_repas) 
            break 
        elif choix =="5" :
            print("Bye Bye Mbad faye sarr !!!!!") 
            break
        


