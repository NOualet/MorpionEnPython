# Script Morpion.py

global tableau, ligne, colonne

tableau = ['-', '-', '-', '-', '-', '-', '-', '-', '-'] # cette liste sert à représenter la valeur affichée des boutons "-" ( non encore jouée) 'X' ( la case a été joué par l'humain) 'O' ( la case jouée par l IA)
valeur_tableau = [9, 9, 9, 9, 9, 9, 9, 9, 9] # Cette liste sert à calculer les valeurs des meilleurs coups à jouer. On met volontairement une valeur supérieur au meilleur coup

# sites internet utilises
#
# http://www.developpez.net/forums/d606424/autres-langages/python-zope/gui/tkinter/tkinter-button-passer-recuperer-valeurs/
# http://python.developpez.com/cours/TutoSwinnen/?page=Chapitre11#L11.4
# http://python.jpvweb.com/mesrecettespython/doku.php?id=morpion_console
# http://sebsauvage.net/python/gui/index_fr.html#add_events
# http://apprendre-python.com/page-tkinter-interface-graphique-python-tutoriel
# https://www.daniweb.com/software-development/python/threads/254878/tkinter-button-changing-text
# page utile pour le probleme du bouton et sa valeur.


from tkinter import *
import tkinter as tk

def change_text():
	# Change la valeur du bouton 1 en "X" (valeur du joueur humain) si le bouton n'a pas encore ete joue
	# ==================================================================================================
    if b["text"] == "-":
        b["text"] = "X"
    tableau[0] = "X"
        
def change_text2():
	# Change la valeur du bouton 2 en "X" (valeur du joueur humain) si le bouton n'a pas encore ete joue
	# ==================================================================================================
    if bu['text'] == '-':
        bu['text'] = 'X'
    tableau[1] = 'X'    

def change_text3():
	# Change la valeur du bouton 3 en "X" (valeur du joueur humain) si le bouton n'a pas encore ete joue
	# ==================================================================================================
    if but['text'] == '-':
        but['text'] = 'X'
    tableau[2] = 'X'        

def change_text4():
	# Change la valeur du bouton 4 en "X" (valeur du joueur humain) si le bouton n'a pas encore ete joue
	# ==================================================================================================
    if butt['text'] == '-':
        butt['text'] = 'X'
    tableau[3] = 'X'        

def change_text5():
	# Change la valeur du bouton 5 en "X" (valeur du joueur humain) si le bouton n'a pas encore ete joue
	# ==================================================================================================
    if butto['text'] == '-':
        butto['text'] = 'X'
    tableau[4] = 'X'        

def change_text6():
	# Change la valeur du bouton 6 en "X" (valeur du joueur humain) si le bouton n'a pas encore ete joue
	# ==================================================================================================
    if buton['text'] == '-':
        buton['text'] = 'X'
    tableau[5] = 'X'        

def change_text7():
	# Change la valeur du bouton 7 en "X" (valeur du joueur humain) si le bouton n'a pas encore ete joue
	# ==================================================================================================
    if buttn['text'] == '-':
        buttn['text'] = 'X'
    tableau[6] = 'X'        

def change_text8():
	# Change la valeur du bouton 8 en "X" (valeur du joueur humain) si le bouton n'a pas encore ete joue
	# ==================================================================================================
    if btton['text'] == '-':
        btton['text'] = 'X'
    tableau[7] = 'X'        

def change_text9():
	# Change la valeur du bouton 9 en "X" (valeur du joueur humain) si le bouton n'a pas encore ete joue
	# ==================================================================================================
    if utton['text'] == '-':
        utton['text'] = 'X'
    tableau[8] = 'X'        

def Index_Liste(x, y):
	if x == 1:
		rc = y - 1
	elif x == 2:
		rc = 2 + y
	else:
		rc = 5 + y
	return tableau[rc]
		

def Calcul_Index_Valeur(ligne, colonne):
	if ligne == 1:
		rc = colonne - 1
	elif ligne == 2:
		rc = 2 + colonne
	else:
		rc = 5 + colonne
	return rc	

def traitement_ligne(ligne, colonne, comparaison):
    if colonne == 1:
        #    if tableau[ligne][2] == comparaison:
        if Index_Liste(ligne, 2) == comparaison:
            if Index_Liste(ligne,3) == comparaison:
                # le joueur humain est a 1 coup de la victoire (-XX)
                return 1
            else:
                # le joueur humain est a 2 coups de la victoire (-X-)
                return 2
        else:
            if Index_Liste(ligne,3) == comparaison:
                # le joueur humain est a 2 coups de la victoire (--X)
                return 2
            else:
                # le joueur humain est a 3 coups de la victoire (---)
                return 3
    elif colonne == 2:
        if Index_Liste(ligne,1) == comparaison:
            if Index_Liste(ligne, 3) == comparaison:
                # le joueur humain est a 1 coup de la victoire (X-X)
                return 1
            else:
                # le joueur humain est a 2 coups de la victoire (X--)
                return 2
        else:
            if Index_Liste(ligne, 3) == comparaison:
                # le joueur humain est a 2 coups de la victoire (--X)
                return 2
            else:
                # le joueur humain est a 3 coups de la victoire (---)
                return 3
    else:
        if Index_Liste(ligne, 1) == comparaison:
            if Index_Liste(ligne, 2) == comparaison:
                # le joueur humain est a 1 coup de la victoire (XX-)
                return 1
            else:
                # le joueur humain est a 2 coups de la victoire (X--)
                return 2
        else:
            if Index_Liste(ligne, 2) == comparaison:
                # le joueur humain est a 2 coups de la victoire (-X-)
                return 2
            else:
                # le joueur humain est a 3 coups de la victoire (---)
                return 3

def traitement_colonne(ligne, colonne, comparaison):
    if ligne == 1:
        if Index_Liste(2, colonne) == comparaison:
            if Index_Liste(3, colonne) == comparaison:
                # le joueur humain est a 1 coup de la victoire (-XX)
                return 1
            else:
                # le joueur humain est a 2 coups de la victoire (-X-)
                return 2
        else:
            if Index_Liste(3, colonne) == comparaison:
                # le joueur humain est a 2 coups de la victoire (--X)
                return 2
            else:
                # le joueur humain est a 3 coups de la victoire (---)
                return 3
    elif ligne == 2:
        if Index_Liste(1, colonne) == comparaison:
            if Index_Liste(3, colonne) == comparaison:
                # le joueur humain est a 1 coup de la victoire (X-X)
                return 1
            else:
                # le joueur humain est a 2 coups de la victoire (X--)
                return 2
        else:
            if Index_Liste(3, colonne) == comparaison:
                # le joueur humain est a 2 coups de la victoire (--X)
                return 2
            else:
                # le joueur humain est a 3 coups de la victoire (---)
                return 3
    else:
        if Index_Liste(1, colonne) == comparaison:
            if Index_Liste(2, colonne) == comparaison:
                # le joueur humain est a 1 coup de la victoire (XX-)
                return 1
            else:
                # le joueur humain est a 2 coups de la victoire (X--)
                return 2
        else:
            if Index_Liste(2, colonne) == comparaison:
                # le joueur humain est a 2 coups de la victoire (-X-)
                return 2
            else:
                # le joueur humain est a 3 coups de la victoire (---)
                return 3

def traitement_diagonale(ligne, colonne, comparaison):
    if ligne == 1:
        if colonne == 1:
            if Index_Liste(2, 2) == comparaison:
                if Index_Liste(3, 3) == comparaison:
                    return 1 # -XX
                else:
                    return 2 # -X-
            else:
                if Index_Liste(3, 3) == comparaison:
                    return 2 # --X
                else:
                    return 3 # ---
        elif colonne == 3:
            if Index_Liste(2, 2) == comparaison:
                if Index_Liste(3, 1) == comparaison:
                    return 1 # -XX
                else:
                    return 2 # -X-
            else:
                if Index_Liste(3, 1) == comparaison:
                    return 2 # --X
                else:
                    return 3 # ---
    elif ligne == 2:
        if colonne == 2:
            if Index_Liste(1, 1) == comparaison:
                if Index_Liste(3, 3) == comparaison:
                    i = 1 # X-X
                else:
                    i = 2 # X--
            else:
                if Index_Liste(3, 3) == comparaison:
                    i = 2 # --X
                else:
                    i = 3 # ---

            if Index_Liste(1, 3) == comparaison:
                if Index_Liste(3, 1) == comparaison:
                    j = 1
                else:
                    j = 2
            else:
                if Index_Liste(3, 1) == comparaison:
                    j = 2
                else:
                    j = 3

            if i <= j:
                return i
            else:
                return j
    else:
        if colonne == 1:
            if Index_Liste(2, 2) == comparaison:
                if Index_Liste(1, 3) == comparaison:
                    return 1 # -XX
                else:
                    return 2 # -X-
            else:
                if Index_Liste(1, 3) == comparaison:
                    return 2 # --X
                else:
                    return 3 # ---
        elif colonne == 3:
            if Index_Liste(2, 2) == comparaison:
                if Index_Liste(1, 1) == comparaison:
                    return 1 # -XX
                else:
                    return 2 # -X-
            else:
                if Index_Liste(1, 1) == comparaison:
                    return 2 # --X
                else:
                    return 3 # ---


def humain_gagne():
	global tableau, valeur_tableau
	# ======================================
	# X correspond a un coup humain
	# O correspond a un coup ordinateur
	# ======================================
	ligne = 1
	
	rc = False
	
	if Index_Liste(1,1) == "X":
		if Index_Liste(1,2) == "X":
			if Index_Liste(1,3) == "X":
				rc = True # 1ere ligne avec XXX
		if Index_Liste(2,2) == "X":
			if Index_Liste(3,3) == "X":
				rc = True # Diagonale allant de (1,1), (2,2) , (3,3)
		if Index_Liste(2,1) == "X":
			if Index_Liste(3,1) == "X":
				rc = True # 1ere colonne
	if Index_Liste(1,2) == "X":
		if Index_Liste(2,2) == "X":
			if Index_Liste(3,2) == "X":
				rc = True # 2eme colonne avec XXX
	if Index_Liste(1,3) == "X":
		if Index_Liste(2,2) == "X":
			if Index_Liste(3,1) == "X":
				rc = True # Diagonale allant de (1,3), (2,2) , (3,1)
		if Index_Liste(2,3) == "X":
			if Index_Liste(3,3) == "X":
				rc = True # 3eme colonne
	if Index_Liste(2,1) == "X":
		if Index_Liste(2,2) == "X":
			if Index_Liste(2,3) == "X":
				rc = True # 2eme ligne avec XXX
	if Index_Liste(3,1) == "X":
		if Index_Liste(3,2) == "X":
			if Index_Liste(3,3) == "X":
				rc = True # 3eme ligne avec XXX
	if Index_Liste(3,3) == "X":
		if Index_Liste(2,2) == "X":
			if Index_Liste(1,3) == "X":
				rc = True # Diagonale allant de (1,3), (2,2) , (3,1)

	return rc				

def Ordi_gagne():
	global tableau, valeur_tableau
	# ======================================
	# X correspond a un coup humain
	# O correspond a un coup ordinateur
	# ======================================
	ligne = 1
	
	rc = False
	
	if Index_Liste(1,1) == "O":
		if Index_Liste(1,2) == "O":
			if Index_Liste(1,3) == "O":
				rc = True # 1ere ligne avec XXX
		if Index_Liste(2,2) == "O":
			if Index_Liste(3,3) == "O":
				rc = True # Diagonale allant de (1,1), (2,2) , (3,3)
		if Index_Liste(2,1) == "O":
			if Index_Liste(3,1) == "O":
				rc = True # 1ere colonne
	if Index_Liste(1,2) == "O":
		if Index_Liste(2,2) == "O":
			if Index_Liste(3,2) == "O":
				rc = True # 2eme colonne avec XXX
	if Index_Liste(1,3) == "O":
		if Index_Liste(2,2) == "O":
			if Index_Liste(3,1) == "O":
				rc = True # Diagonale allant de (1,3), (2,2) , (3,1)
		if Index_Liste(2,3) == "O":
			if Index_Liste(3,3) == "O":
				rc = True # 3eme colonne
	if Index_Liste(2,1) == "O":
		if Index_Liste(2,2) == "O":
			if Index_Liste(2,3) == "O":
				rc = True # 2eme ligne avec XXX
	if Index_Liste(3,1) == "O":
		if Index_Liste(3,2) == "O":
			if Index_Liste(3,3) == "O":
				rc = True # 3eme ligne avec XXX
	if Index_Liste(3,3) == "O":
		if Index_Liste(2,2) == "O":
			if Index_Liste(1,3) == "O":
				rc = True # Diagonale allant de (1,3), (2,2) , (3,1)

	return rc				


	
def examiner_coup_humain():
	global tableau, valeur_tableau
	# ======================================
	# X correspond a un coup humain
	# O correspond a un coup ordinateur
	# ======================================
	ligne = 1
	
	while ligne < 4:
			colonne = 1
			while colonne < 4:
				
				# On va calculer l'index de la liste par rapport a la ligne et la colonne
				# =======================================================================
				index = Calcul_Index_Valeur(ligne, colonne)
				if ligne == 1:
					if colonne == 1:
						if Index_Liste(ligne, colonne) == "-":
							# cette case n'a pas encore ete joue

							#on regarde la premiere ligne
											
							valeur_tableau[index] = traitement_ligne(ligne, colonne, "X")

							# on regarde la premiere colonne
							i = traitement_colonne(ligne, colonne, "X")
							if i < valeur_tableau[index]:
								# On prend le resultat de la fonction traitement_colonne
								# puisque c'est en jouant ainsi que le joueur humain
								# a le plus de chance de gagner
								valeur_tableau[index] = i

									# on regarde la diagonale partant de la ligne 1 et la colonne 1
							i = traitement_diagonale(ligne, colonne, "X")
							if i < valeur_tableau[index]:
								# On prend le resultat de la fonction traitement_diagonale
								# puisque c'est en jouant ainsi que le joueur humain
								# a le plus de chance de gagner
								valeur_tableau[index] = i


					elif colonne == 2:
						if Index_Liste(ligne, colonne) == "-":
							# cette case n'a pas encore ete joue

							#on regarde la premiere ligne
							valeur_tableau[index] = traitement_ligne(ligne, colonne, "X")

							# on regarde la premiere colonne
							i = traitement_colonne(ligne, colonne, "X")
							if i < valeur_tableau[index]:
								# On prend le resultat de la fonction traitement_colonne
								# puisque c'est en jouant ainsi que le joueur humain
								# a le plus de chance de gagner
								valeur_tableau[index] = i
					else:
						# ligne
						if Index_Liste(ligne, colonne) == "-":
							# cette case n'a pas encore ete joue

							#on regarde la premiere ligne
							valeur_tableau[index] = traitement_ligne(ligne, colonne, "X")

							# on regarde la premiere colonne
							i = traitement_colonne(ligne, colonne, "X")
							if i < valeur_tableau[index]:
								# On prend le resultat de la fonction traitement_colonne
								# puisque c'est en jouant ainsi que le joueur humain
								# a le plus de chance de gagner
								valeur_tableau[index] = i

							# on regarde la diagonale partant de la ligne 1 et la colonne 1
							i = traitement_diagonale(ligne, colonne, "X")
							if i < valeur_tableau[index]:
								# On prend le resultat de la fonction traitement_diagonale
								# puisque c'est en jouant ainsi que le joueur humain
								# a le plus de chance de gagner
								valeur_tableau[index] = i
				elif ligne == 2:
					if colonne == 1:
						if Index_Liste(ligne, colonne) == "-":
							# cette case n'a pas encore ete joue

							#on regarde la premiere ligne
							valeur_tableau[index] = traitement_ligne(ligne, colonne, "X")

							# on regarde la premiere colonne
							i = traitement_colonne(ligne, colonne, "X")
							if i < valeur_tableau[index]:
								# On prend le resultat de la fonction traitement_colonne
								# puisque c'est en jouant ainsi que le joueur humain
								# a le plus de chance de gagner
								valeur_tableau[index] = i

					elif colonne == 2:
						if Index_Liste(ligne, colonne) == "-":
							# cette case n'a pas encore ete joue

							#on regarde la premiere ligne
							valeur_tableau[index] = traitement_ligne(ligne, colonne, "X")

							# on regarde la premiere colonne
							i = traitement_colonne(ligne, colonne, "X")
							if i < valeur_tableau[index]:
								# On prend le resultat de la fonction traitement_colonne
								# puisque c'est en jouant ainsi que le joueur humain
								# a le plus de chance de gagner
								valeur_tableau[index] = i

							 # on regarde la diagonale partant de la ligne 1 et la colonne 1
							i = traitement_diagonale(ligne, colonne, "X")
							if i < valeur_tableau[index]:
								# On prend le resultat de la fonction traitement_diagonale
								# puisque c'est en jouant ainsi que le joueur humain
								# a le plus de chance de gagner
								valeur_tableau[index] = i
					else:
						if Index_Liste(ligne, colonne) == "-":
							# cette case n'a pas encore ete joue

							#on regarde la premiere ligne
							valeur_tableau[index] = traitement_ligne(ligne, colonne, "X")

							# on regarde la premiere colonne
							i = traitement_colonne(ligne, colonne, "X")
							if i < valeur_tableau[index]:
								# On prend le resultat de la fonction traitement_colonne
								# puisque c'est en jouant ainsi que le joueur humain
								# a le plus de chance de gagner
								valeur_tableau[index] = i
				else:
			# ligne 3
					if colonne == 1:
						if Index_Liste(ligne, colonne) == "-":
							# cette case n'a pas encore ete joue

							#on regarde la premiere ligne
							valeur_tableau[index] = traitement_ligne(ligne, colonne, "X")

							# on regarde la premiere colonne
							i = traitement_colonne(ligne, colonne, "X")
							if i < valeur_tableau[index]:
								# On prend le resultat de la fonction traitement_colonne
								# puisque c'est en jouant ainsi que le joueur humain
								# a le plus de chance de gagner
								valeur_tableau[index] = i

							# on regarde la diagonale partant de la ligne 1 et la colonne 1
							i = traitement_diagonale(ligne, colonne, "X")
							if i < valeur_tableau[index]:
								# On prend le resultat de la fonction traitement_diagonale
								# puisque c'est en jouant ainsi que le joueur humain
								# a le plus de chance de gagner
								valeur_tableau[index] = i
					elif colonne == 2:
						if Index_Liste(ligne, colonne) == "-":
							# cette case n'a pas encore ete joue
	
							#on regarde la premiere ligne
							valeur_tableau[index] = traitement_ligne(ligne, colonne, "X")

							# on regarde la premiere colonne
							i = traitement_colonne(ligne, colonne, "X")
							if i < valeur_tableau[index]:
								# On prend le resultat de la fonction traitement_colonne
								# puisque c'est en jouant ainsi que le joueur humain
								# a le plus de chance de gagner
								valeur_tableau[index] = i

					else:
						if Index_Liste(ligne, colonne) == "-":
							# cette case n'a pas encore ete joue

							#on regarde la premiere ligne
							valeur_tableau[index] = traitement_ligne(ligne, colonne, "X")

							# on regarde la premiere colonne
							i = traitement_colonne(ligne, colonne, "X")
							if i < valeur_tableau[index]:
								# On prend le resultat de la fonction traitement_colonne
								# puisque c'est en jouant ainsi que le joueur humain
								# a le plus de chance de gagner
								valeur_tableau[index] = i

							# on regarde la diagonale partant de la ligne 1 et la colonne 1
							i = traitement_diagonale(ligne, colonne, "X")
							if i < valeur_tableau[index]:
								# On prend le resultat de la fonction traitement_diagonale
								# puisque c'est en jouant ainsi que le joueur humain
								# a le plus de chance de gagner
								valeur_tableau[index] = i
				colonne += 1
			ligne += 1
	
def examiner_coup_ordinateur():
    global tableau, valeur_tableau

    # ======================================
    # X correspond a un coup humain
    # O correspond a un coup ordinateur
    # ======================================
    ligne = 1
    while ligne < 4:
        colonne = 1
        while colonne < 4:
            index = Calcul_Index_Valeur(ligne, colonne)    
            if ligne == 1:
                if colonne == 1:
                    if Index_Liste(ligne, colonne) == "-":
                        # cette case n'a pas encore ete joue

                        #on regarde la premiere ligne
                        valeur_tableau[index] = traitement_ligne(ligne, colonne, "X") - 1

                        # on regarde la premiere colonne
                        i = traitement_colonne(ligne, colonne, "X") - 1
                        if i < valeur_tableau[index]:
                            # On prend le resultat de la fonction traitement_colonne
                            # puisque c'est en jouant ainsi que le joueur humain
                            # a le plus de chance de gagner
                            valeur_tableau[index] = i

                        # on regarde la diagonale partant de la ligne 1 et la colonne 1
                        i = traitement_diagonale(ligne, colonne, "X") - 1
                        if i < valeur_tableau[index]:
                            # On prend le resultat de la fonction traitement_diagonale
                            # puisque c'est en jouant ainsi que le joueur humain
                            # a le plus de chance de gagner
                            valeur_tableau[index] = i


                elif colonne == 2:
                    if Index_Liste(ligne, colonne) == "-":
                        # cette case n'a pas encore ete joue

                        #on regarde la premiere ligne
                        valeur_tableau[index] = traitement_ligne(ligne, colonne, "X") - 1

                        # on regarde la premiere colonne
                        i = traitement_colonne(ligne, colonne, "X") - 1
                        if i < valeur_tableau[index]:
                            # On prend le resultat de la fonction traitement_colonne
                            # puisque c'est en jouant ainsi que le joueur humain
                            # a le plus de chance de gagner
                            valeur_tableau[index] = i
                else:
                    # ligne
                    if Index_Liste(ligne, colonne) == "-":
                        # cette case n'a pas encore ete joue

                        #on regarde la premiere ligne
                        valeur_tableau[index] = traitement_ligne(ligne, colonne, "X") - 1

                        # on regarde la premiere colonne
                        i = traitement_colonne(ligne, colonne, "X") - 1
                        if i < valeur_tableau[index]:
                            # On prend le resultat de la fonction traitement_colonne
                            # puisque c'est en jouant ainsi que le joueur humain
                            # a le plus de chance de gagner
                            valeur_tableau[index] = i

                        # on regarde la diagonale partant de la ligne 1 et la colonne 1
                        i = traitement_diagonale(ligne, colonne, "X") - 1
                        if i < valeur_tableau[index]:
                            # On prend le resultat de la fonction traitement_diagonale
                            # puisque c'est en jouant ainsi que le joueur humain
                            # a le plus de chance de gagner
                            valeur_tableau[index] = i
            elif ligne == 2:
                if colonne == 1:
                    if Index_Liste(ligne, colonne) == "-":
                        # cette case n'a pas encore ete joue

                        #on regarde la premiere ligne
                        valeur_tableau[index] = traitement_ligne(ligne, colonne, "X") - 1

                        # on regarde la premiere colonne
                        i = traitement_colonne(ligne, colonne, "X") - 1
                        if i < valeur_tableau[index]:
                            # On prend le resultat de la fonction traitement_colonne
                            # puisque c'est en jouant ainsi que le joueur humain
                            # a le plus de chance de gagner
                            valeur_tableau[index] = i

                elif colonne == 2:
                    if Index_Liste(ligne, colonne) == "-":
                        # cette case n'a pas encore ete joue

                        #on regarde la premiere ligne
                        valeur_tableau[index] = traitement_ligne(ligne, colonne, "X") - 1

                        # on regarde la premiere colonne
                        i = traitement_colonne(ligne, colonne, "X") - 1
                        if i < valeur_tableau[index]:
                            # On prend le resultat de la fonction traitement_colonne
                            # puisque c'est en jouant ainsi que le joueur humain
                            # a le plus de chance de gagner
                            valeur_tableau[index] = i

                        # on regarde la diagonale partant de la ligne 1 et la colonne 1
                        i = traitement_diagonale(ligne, colonne, "X") - 1
                        if i < valeur_tableau[index]:
                            # On prend le resultat de la fonction traitement_diagonale
                            # puisque c'est en jouant ainsi que le joueur humain
                            # a le plus de chance de gagner
                            valeur_tableau[index] = i
                else:
                    if Index_Liste(ligne, colonne) == "-":
                        # cette case n'a pas encore ete joue

                        #on regarde la premiere ligne
                        valeur_tableau[index] = traitement_ligne(ligne, colonne, "X") - 1

                        # on regarde la premiere colonne
                        i = traitement_colonne(ligne, colonne, "X") - 1
                        if i < valeur_tableau[index]:
                            # On prend le resultat de la fonction traitement_colonne
                            # puisque c'est en jouant ainsi que le joueur humain
                            # a le plus de chance de gagner
                            valeur_tableau[index] = i
            else:
                # ligne 3
                if colonne == 1:
                    if Index_Liste(ligne, colonne) == "-":
                        # cette case n'a pas encore ete joue

                        #on regarde la premiere ligne
                        valeur_tableau[index] = traitement_ligne(ligne, colonne, "X") - 1

                        # on regarde la premiere colonne
                        i = traitement_colonne(ligne, colonne, "X") - 1
                        if i < valeur_tableau[index]:
                            # On prend le resultat de la fonction traitement_colonne
                            # puisque c'est en jouant ainsi que le joueur humain
                            # a le plus de chance de gagner
                            valeur_tableau[index] = i

                        # on regarde la diagonale partant de la ligne 1 et la colonne 1
                        i = traitement_diagonale(ligne, colonne, "X") - 1
                        if i < valeur_tableau[index]:
                            # On prend le resultat de la fonction traitement_diagonale
                            # puisque c'est en jouant ainsi que le joueur humain
                            # a le plus de chance de gagner
                            valeur_tableau[index] = i
                elif colonne == 2:
                    if Index_Liste(ligne, colonne) == "-":
                        # cette case n'a pas encore ete joue

                        #on regarde la premiere ligne
                        valeur_tableau[index] = traitement_ligne(ligne, colonne, "X") - 1

                        # on regarde la premiere colonne
                        i = traitement_colonne(ligne, colonne, "X") - 1
                        if i < valeur_tableau[index]:
                            # On prend le resultat de la fonction traitement_colonne
                            # puisque c'est en jouant ainsi que le joueur humain
                            # a le plus de chance de gagner
                            valeur_tableau[index] = i

                else:
                    if Index_Liste(ligne, colonne) == "-":
                        # cette case n'a pas encore ete joue

                        #on regarde la premiere ligne
                        valeur_tableau[index] = traitement_ligne(ligne, colonne, "X") - 1

                        # on regarde la premiere colonne
                        i = traitement_colonne(ligne, colonne, "X") - 1
                        if i < valeur_tableau[index]:
                            # On prend le resultat de la fonction traitement_colonne
                            # puisque c'est en jouant ainsi que le joueur humain
                            # a le plus de chance de gagner
                            valeur_tableau[index] = i

                        # on regarde la diagonale partant de la ligne 1 et la colonne 1
                        i = traitement_diagonale(ligne, colonne, "X") - 1
                        if i < valeur_tableau[index]:
                            # On prend le resultat de la fonction traitement_diagonale
                            # puisque c'est en jouant ainsi que le joueur humain
                            # a le plus de chance de gagner
                            valeur_tableau[index] = i


            colonne += 1
        ligne += 1

def Fonction_Ia():
	# On va regarder si le joueur humain a gagne la partie
	if humain_gagne() == True:
		print("Le joueur humain a gagne la partie")
	else:
		examiner_coup_humain() # côté défensif
		examiner_coup_ordinateur() # côté offensif
		# retourne une valeur pour chacune des cases non encore joués correspondant au nombre de coups avant la victoire de l'IA
		# On va chercher dans la boucle while, la plus petite valeur, qui sera le meilleur coup ( meilleur_index) pour l'IA
		valeur = 10
		index = 0
		meilleur_index = 10
		while index < 9:
			if valeur_tableau[index] < valeur:
				valeur = valeur_tableau[index]
				meilleur_index = index
			index = index + 1
		
		print ("Meilleur index = " + str(meilleur_index))
		tableau[meilleur_index] = 'O'
		# On a trouvé le meilleur_index et on modifie la valeur initiale du meilleur_index en 'O'.

		bouton_a_choisir = meilleur_index	
		if bouton_a_choisir	 == 0:
			b['text'] = 'O'
		elif bouton_a_choisir == 1:
			bu["text"] = "O"
		elif bouton_a_choisir == 2:
			but["text"] = "O"
		elif bouton_a_choisir == 3:
			butt["text"] = "O"
		elif bouton_a_choisir == 4:
			butto["text"] = "O"
		elif bouton_a_choisir == 5:
			buton["text"] = "O"
		elif bouton_a_choisir == 6:
			buttn["text"] = "O"
		elif bouton_a_choisir == 7:
			btton["text"] = "O"
		else:
			utton["text"] = "O"
			
		# On regarde si l'IA a gagne la partie
		if Ordi_gagne() == True:
			print ("L'ordinateur a gagne")
		else:
			# On regarde si la partie est termine
			#
			# on regarde si il reste des '-' dans la liste tableau
			rc = False
			i = 0
			while i < 9:
				if tableau[i] == '-':
					rc = True
				i += 1
				
			if rc == False:
				# on n'a pas trouve de caractere '-', ce qui veut dire que toutes les cases ont ete joue
				# c'est donc une partie nulle
				print ("Match nul")
			
			

# Interface graphique
# ===================
fen=tk.Tk()
fen.title("Morpion 2.0")
fen.geometry("250x175+10+10")# dimension et position par defaut
fen.minsize(400, 300) # taille minimum de la fenetre
fen.maxsize(1024,768) # taille maximum de la fenetre

   

b = tk.Button( text = "-", relief='groove', command=change_text)
b.grid(row = 1 , column = 1,ipadx = 5, ipady = 5,  padx=1, pady=1 )

bu = tk.Button( text = '-', relief='groove', command = change_text2)
bu.grid(row = 1 ,column = 2 ,ipadx = 5, ipady = 5, padx=1, pady=1  )

but = tk.Button( text = '-', relief='groove', command = change_text3)
but.grid(row = 1, column = 3 ,ipadx = 5, ipady = 5, padx=1, pady=1 )

butt = Button(fen, text = '-', relief='groove', command = change_text4)
butt.grid(row = 2 , column = 1 ,ipadx = 5, ipady = 5,  padx=1, pady=1  )

butto = Button(fen, text = '-', relief='groove', command = change_text5)
butto.grid(row = 2 , column = 2 ,ipadx = 5, ipady = 5,  padx=1, pady=1 )

buton = Button(fen, text = '-', relief='groove', command = change_text6)
buton.grid(row = 2 , column = 3 ,ipadx = 5, ipady = 5,  padx=1, pady=1 )

buttn = Button(fen, text = '-', relief='groove', command = change_text7)
buttn.grid(row = 3 , column = 1 ,ipadx = 5, ipady = 5,  padx=1, pady=1 )

btton = Button(fen, text = '-', relief='groove', command = change_text8)
btton.grid(row = 3 , column = 2 ,ipadx = 5, ipady = 5, padx=1, pady=1 )

utton = Button(fen, text = '-', relief='groove', command = change_text9)
utton.grid(row = 3  ,column = 3 ,ipadx = 5, ipady = 5,  padx=1, pady=1 )

o = tk.Button(fen, text = 'A toi de jouer IA', relief='groove', command = Fonction_Ia)
o.grid(row = 3  ,column = 4 ,ipadx = 5, ipady = 5,  padx=1, pady=1 )


fen.mainloop()
