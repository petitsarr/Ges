# --------Application de Gestion Restaurant avec python --------------- 




list_repas = ["Thiebou dieune" , "Riz au poulet","CousCous","Fruit de Mer","Mbahalou_Saloum","C'est Bon avec Poisson"] 
print("Mes listes de Repas est \n",list_repas) 

choix_user = ["1","2","3","4","5"] 

menu = """Choisissez parmi les 5 options suivantes Svp !!!!! :
1: Ajouter un plat à la liste des plats ...
2: Supprimer un pat dans la liste des plats ... 
3: Afficher le details d'un plat de la liste ...
4: Modifier un plat de la  liste des plats ...
5: Quitter (Bye!!!)
? Votre choix : """ 

while True : 
    choix = input(menu) 
    if choix in choix_user :
        if choix == "1" :
            plat = input("Tapez votre plat svp !!!") 
            list_repas.append(plat) 
            print("Ajout d'un plat avec succes") 
        elif choix == "2" :
            plat = input("Entrez le plat a supprimer svp !!!") 
            while not plat in list_repas : 
                plat = input('Veuillez saisir un plat existant dans la liste des plats svp') 
            list_repas.remove(plat) 
        


