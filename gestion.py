# --------Application de Gestion Restaurant avec python from Scratch ---------------  
 


import time
# Mes dictionnaires  
#Nom et prenom de tous les personnes inscrits
list_nom={}
# Dictionnaire de tous les noms d'utilisateurs avec leur mot de pass 
dict_connection={
    "moussa":"passer1" ,
    "serifou" : "passer2"
}
# Dictionnaire de plat .... 
# Les plats avec leur prix correspondant
list_plat={} 
# Le numero de serie de l'article 
item_serial={} 
# Dictionnaire bill {} contient le nom du plat : et quantité pour la commande
bill={} 
no_of_dish=1 #it is used to print 1,2,3... serial no. in front of items  



# Ma fonction pour l'inscription de l'utilisateur .
# Elle prend la valeur 1 s'il est appele par l'admin et 2 s'il est appele par le client cad l'user 
def inscription(val) : 
   # print(type(val))
    print("----------------INSCRIPTION------------") 
    nom = input("Saisir votre nom svp : \n ") 
    prenom = input("Saisir votre prenom svp :\n") 
    pwd = input("Saisir votre mot de pass :\n")
    for i in dict_connection.keys() : 
        # si user existe deja 
        if i == prenom : 
            print('Ouppps cet utilisateur existe deja ') 
            if val == 1 :
                return connections(1) #On return True par defaut .
            else: 
                return connections(2)  

        # si user n'existe pas 
        else : 
            dict_connection[prenom] = pwd 
            list_nom[prenom] = nom  
            
            print("Vous vous etes inscrits avec succes ...\n Connecter vous pour Continuer") 
            if val == 1 : 
                return connections(1) # par defaut retourne True pcq forcement tout le monde est inscrit
            else : 
                return connections(2)

# Ma Fonction pour la Connection 
def connections(val) : 
    print("-------------------------------Connection--------------------------------") 
    prenom=input("Enter Votre prenom!!!!:\n")
    pwd=input("Enter votre mot de pass svp!!!!:\n")
    userexist=False # l'utilisateur par défaut n'existe pas avant de vérifier la condition
    for i in dict_connection.keys():
        if i==prenom :
            userexist=True #si l'utilisateur existe alors ce serait vrai
            if dict_connection[prenom]==pwd:
                print("\nConnection reussie ")
                print("Bienvenue",list_nom[prenom]," !\n")
                return True
            else:
                print("\nIncorrect Prenom et mot de pass.... Reesaye encore svp")
                if val==1:
                    return connections(1) 
                else:
                    return connections(2)
    if userexist==False: 
        print("\nUser non Trouve... Please inscris toi ou connect toi avec d'autre compte pour continuer")
        if val ==1:
            return administration()
        else:
            return client()
 

# fonction pour gerer l'administration ....
def administration () : 
    choix_admin = ["1","2"] 
    ch = input(""""--------------------------Connection-Inscription--------------------------------!!!!! : 
     1--: Connection.......

    2--: Inscription.......

  

   ? Votre choix svp : """ ) 
    if ch in choix_admin : 
        if ch =="1" :
            valeur = connections(1)
        elif ch =="2" :
            valeur = inscription(1)
    # si val renvoi True alors je me suis connecte ,si False alors je me suis deconnecte .. 

    while valeur == True : 
        c = ["1","2","3"] 
        print("1.Modifie le Menu\n")
        print("2.Afficher le Menu\n")
        print("3.Deconnection\n") 
        ch2 = input("Entrez votre choix :\n") 
        if ch2 in c :
            if ch2 == "1"  :  
                print("1.Ajouter un plat dans le menu")
                print("2.supprimer un plat dans le menu ")
                print("3.Go Back") 
                p = int(input("Entrer votre choix svp:\n")) 
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
# La fonction qui gere le client cad l'user ...
def client() :
    cli = ["1","2"]  
    print("1.Connection")
    print("2.Inscription") 
    c = input("Entrer votre choix svp !!!:\n") 
    if c in cli :
        if c == "1" :
            valeur = connections(2)
        else :
            valeur = inscription(2) 
    while valeur == True :
        print("---------------------------Bienvenue en Tant que Client---------------------------------")
        print("1.Afficher Menu")
        print("2.Commander")
        print("3.deconnexion")
        choice=int(input("Entrer votre choix :\n")) 
        # choix de 1 pour voir le menu ...
        if choice==1:
             afficher_menu_plat() 
        # choix 2 pour faire la commande ...
        elif choice==2:
            val=commande()
        else:
            val=False 
            print("Deconnection reussi avec succes")
            main() 


# Ajouter un plat a mon dictionnnaire liste_plat
def  add_plat() : 
    nom = input("Entrer le nom du plat:\n") 
    prix = int(input("Entrez le prix du plat svp :\n")) 
    list_plat[nom] = prix 
    global no_of_dish 
    item_serial[no_of_dish]=nom # serial number(key):dish_name(value)
    no_of_dish+=1
    print("plat ajouter avec succes")

# Supprimer un plat dans mon dictionnaire list_plat
def delete_plat() : 
    #teste si ma liste de plat est vide 
    if len(list_plat)==0:
        print("Rien en supprime")
    else:
        nom=input("Entrer le nom du plat a supprimer :\n")
        for i in range(len(list_plat)):
            if nom in list_plat.keys():
                del(list_plat[nom])
                print("\nSuppression reussi")
            else:
                print("\n le nom du plat est incorect")
                break

# Ma Fonction pour afficher le menu du Restaurant ....
def afficher_menu_plat() : 
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
        cmd = False 
    else : 
        cmd = True
    #Tant que il ya de la nourriture pour la commande alors :
    while cmd == True : 
         numero_plat=int(input("Entrer le numero de plat svp:\t"))
         quantity=int(input("Entrer la quantite svp:\t")) 
        
         bill[item_serial[numero_plat]]=quantity  
         print("Mon bill est \n :",bill) 
        #bill[numero_plat]=quantity 

         #On demande a l'user sil commander encore ou non  .
         cont=input("Voulez vous ajoute plus ou non svp!!!?(y/n): ") 
         # si oui j'affecte True a cmd pour parcourir encore la boucle 
         if cont=='Y' or cont=='y':
            cmd=True
         else:
            cmd=False 
    print("\nNourriture commandée avec succès !!!!\n\n")  

    # cette fonction permet de generer de la facture apres la commande .
    return genere_facture()

# Animation de ma facture en utilisant le module time et la fonction sleep .
def animation_facture():
    for i in range(4):
        print("\rGénération de votre FACTURE...   ",end="");
        time.sleep(0.5)
        print("\rGénération de votre FACTURE...   ",end="");
        time.sleep(0.5)
        print("\rGénération de votre FACTURE..  ",end="");
        time.sleep(0.5)
        print("\rGénération de votre FACTURE... ",end="");
        time.sleep(0.5)
        print("\rGénération de votre FACTURE....",end="");
        time.sleep(0.5)
    print("\n\tGénération de votre FACTURE")



def genere_facture() : 
    animation_facture() 
    print("*****************Hello Votre Facture est la *****************") 

    numero=1 

    # montant_total_commande : est Le montant total des commandes 
    montant_total_commande=0
    for i in bill.keys():
        #Calcul du Montant total d'un commande ==> quantity * prix 
        montant_une_seule_commande=bill[i]*list_plat[i] 
    
        print(numero,".",i,"\t",bill[i],"x",list_plat[i]," = ",montant_une_seule_commande)
        montant_total_commande+=montant_une_seule_commande
        numero = numero + 1 
    print("--------------------------------------------------")
    print(" TOTAL FACTURE    =      ",montant_total_commande)
    
    message_merci ()
  
    return True 


def message_merci () :
     print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
                    Merci Beaucoup Bye Bye Bye ......                                         \n\
                    A la Prochaine !                                        \
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
   
def main() : 
    
  choix_principale = ["1","2","3"] 
  menu_admin = """-----------------------------------WELCOME--------------------------------!!!!! : 
     1--: Panel Administration.......

    2--: Panel Client.......

    3--: Quitter.......

   ? Votre choix svp : """ 

  choice= input(menu_admin)
  if choice in choix_principale :
    if choice == "1" :
        administration()
    elif choice == "2" :
        client() 
    else :
        return 0 
main()











        


