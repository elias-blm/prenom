from tkinter import * #importe toute la biblothèque
fichier_prenom= open("prenom.csv", "r", encoding='utf8') #ouvre le fichier
donnees= fichier_prenom.readlines() #lis l'ensemble du fichier et transforme une ligne en sous-liste
fichier_prenom.close() #ferme le fichier

del donnees[0] #supprime la première liste car elle ne contient pas de données importantes
for i in range (len(donnees)): #pour chaque item de la liste
    donnees[i]=donnees[i].rstrip('\n') #retire le \n de saut de ligne
    donnees[i]=donnees[i].split(';') #transforme les ; en , . Ce qui permet d'avoir des sous-items dans chaque sous-liste
    donnees[i][3]=int(donnees[i][3]) #transforme la colonne année en integer
    donnees[i]=tuple(donnees[i]) #transforme la liste i en tuple

def requete1(donnees):
	'''
	donne le nombre d'individus pour un prénom et une année donnés
	'''
	prenom=vérification("prénom",donnees,1) #obtient le prénom

	annee= vérification('année',donnees,2) #obtient l'année
	nombre=0

	for i in range (0,len(donnees)):
		if donnees[i][1]== prenom and donnees[i][2] ==annee: #si le prénom et l'année correspondent 
				nombre=donnees[i][3] #y prend la valeur du nombre de naissance

	if nombre=='XXXX': #si XXXX est la valeur
		print("Le nombre n'est pas disponible")

	elif nombre==0: #si il n’y a pas de chiffre pour le couple année/prénom
		print("Aucune données disponibles ou aucune naissance cette année là")

	else: #dans tout les autres cas
		print("En ",annee,',',nombre, prenom,'sont nés.')
	
	return i #permet de couper la fonction

def vérification(variable,donnees,nombre):
	'''
	vérifie si un élément est dans une liste
	'''
	i= str(input("Quel(le) "+variable+" voulez vous rechercher? ")).upper() #demande qune valeur que le programme met en majuscule
	while 1>0: #tant que i n'est pas dans la liste, il le demande
		for g in range (0,len(donnees)):
			if i==donnees[g][nombre]: #si i correspond à l'item du tuple
				return i #retourne i 
		i=str(input("Ce(tte) "+variable+ " n'est pas dans la liste. Peut-etre l'avez vous mal orthographié(e). ")).upper() 

def requete2(donnees):
	'''
	donne le prénom le plus courant (fille et garçon) pour une année donnée
	'''
	année= vérification("annee",donnees,2) #obtient l'année
	fille=[]
	garcon=[]
	for quadruplet in range (0,len(donnees)): #parcourt toute la liste
		if année==donnees[quadruplet][2] and donnees[quadruplet][0]== '1': #si l'année correspond et que c'est un garçon
				garcon.append(donnees[quadruplet])
		elif année==donnees[quadruplet][2] and donnees[quadruplet][0]== '2':#si l'année correspond et que c'est une fille
				fille.append(donnees[quadruplet])
	
	fille=listesortie(fille,3) #trie la liste par ordre croissant de naissance
	garcon= listesortie(garcon,3) #trie la liste par ordre croissant de naissance
	if fille[-1][1]=='_PRENOMS_RARES': #si le prénom lié au dernier tuple de la liste fille est 'PRENOMS_RARES'
		print("La donnée n'est pas disponible pour les filles, mais le 2 ème prénom le plus populaire est: ", fille[-2][1] ) #donne l'avant dernière valeur
	else:	
		print("En ",année,", le prénom le plus populaire chez les filles est",fille[-1][1])
	
	if garcon[-1][1]=='_PRENOMS_RARES':#si le prénom lié au dernier tuple de la liste garcon est 'PRENOMS_RARES'
		
		print("La donnée n'est pas disponible pour les garcons mais le 2 ème prénom le plus populaire est: ", garcon[-2][1])#donne l'avant dernière valeur

	else:
		print("En ",année,",le prénom le plus populaire chez les garcons est",garcon[-1][1])
	
	return i
	
def listesortie(liste,nb):
	'''
	trie une liste par ordre croissant
	'''
	donnees=sorted(liste, key=lambda colonnes: int(colonnes[nb])) #trie une liste en fonction de la colonne demandée
	return donnees #retourne la liste triée

def requete3(donnees):
	'''
	donne l'année de l'effectif maximal pour un prénom donné 
	'''
	prenom=vérification("prenom",donnees,1)
	l=[]
	for quadruplet in range (0,len(donnees)):
		if prenom==donnees[quadruplet][1]:
				l.append(donnees[quadruplet])
	l= listesortie(l,3)
	if l[-1][2]=='XXXX':
		print("C'est en ", l[-2][2], "qu'il y a eu le plus de",prenom)
	else:
		print("C'est en", l[-1][2], "qu'il y a eu le plus de",prenom)

def top10(donnees):
	'''
	donne le top 10 des prénoms les plus donnés (chez les filles et les garçons) en fonction d’une année
	'''
	année= vérification("annee",donnees,2) #récupère l'annéee
	fille=[]
	garcon=[]
	for quadruplet in range (0,len(donnees)):
		if année==donnees[quadruplet][2] and donnees[quadruplet][0]== '1': #si l'annéé correspond et que c'est un garçon
			garcon.append(donnees[quadruplet])
		elif année==donnees[quadruplet][2] and donnees[quadruplet][0]== '2':#si l'annéé correspond et que c'est une fille
			fille.append(donnees[quadruplet])
	
	fille=listesortie(fille,3) #trie la liste
	garcon= listesortie(garcon,3) #trie la liste
	
	print("En ",année,", les prénoms les plus populaires chez les filles sont:")
	for i in range(1,11): #répète 10 fois
		if fille[-i][1]=='_PRENOMS_RARES': #si le prénom dans le tuple est 'PRENOMS_RARES'
			fille[-i]=list(fille[-i]) #transforme le tuple en liste
			del fille[-i] #le supprime
		print(i,"-",fille[-i][1]) #affiche le rang avec le prénom associé
	
	print("En ",année,",les prénoms les plus populaires chez les garçons sont:")
	for i in range(1,11):#répète 10 fois
		if garcon[-i][1]=='_PRENOMS_RARES': #si le prénom dans le tuple est 'PRENOMS_RARES'
			garcon[-i]=list(garcon[-i])#transforme le tuple en liste
			del garcon[-i]#la supprime
		print(i,"-",garcon[-i][1])#affiche le rang avec le prénom associé
	return i

def appelre1():
	'''
	lance la requete1()
	'''
	requete1(donnees)

def appelre2():
	'''
	lance la requete2()
	'''
	requete2(donnees)

def appelre3():
	'''
	lance la requete3()
	'''
	requete3(donnees)

def appelreb():
	'''
	lance la top10()
	'''
	top10(donnees)

fenetre = Tk() # fenetre est une interface tinker
bouton2=Button(fenetre, text="Requete 1", command=appelre1) #créee un bouton nommé requete 1 qui lance la fonction appelre1()
bouton2.pack() #organise le bouton pour l'afficher plus tard
bouton1=Button(fenetre, text="Requete 2", command=appelre2)
bouton1.pack()
bouton3=Button(fenetre, text="Requete 3", command=appelre3)
bouton3.pack()
bouton4=Button(fenetre, text=" Requete Top 10", command=appelreb)
bouton4.pack()
bouton=Button(fenetre, text="Fermer", command=fenetre.quit)
bouton.pack()
fenetre.mainloop() #affiche les différents boutons




