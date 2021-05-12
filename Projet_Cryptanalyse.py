#lien vers github : https://github.com/Nathan-Carre/projet_cryptanalyse/tree/main
#voici les fonctions utilisées durant le TD du projet Crypto mais j'avais eu du mal à comprendre
"""def frequence(message_chiffre):
    resultat = []
    for c in message_chiffre :
        if 97 <= ord(c) <= 122:
            exist = True
            for i in range(len(resultat)) :
                if resultat[i][0] == c :
                    exist = False
            if exist :
                resultat.append([c, round(message_chiffre.count(c)/len(message_chiffre)*100,2)])
    return resultat

def rang(lettre):
    return ord(lettre)-97


def decalage(lettre_message,lettre_cle):
    if 97 <= ord(lettre_message) <= 122 :
        return chr((rang(lettre_message) + rang(lettre_cle))%26 + 97)
    else :
        return lettre_message

def dec_texte(texte,cle):
    taille_cle = len(cle)
    res = ""
    for i in range(len(texte)):
        res += decalage(texte[i],cle[i%taille_cle])
    return res

def chiffre():
    resultat.delete(0,tk.END)
    text=entree_texte.get()
    cle=entree_cle.get()
    if((len(text)>0) and (len(cle)>0)):
        res=dec_texte(text,cle)
        resultat.insert(0,res)
    else:
        resultat.insert(0,"Il manque quelque chose")

def dechiffrer(message_chiffre,cle):
    taille_cle = len(cle)
    res = ""
    for i in range(len(message_chiffre)):
        res += decalage(message_chiffre[i],chr(256-ord(cle[i%taille_cle])))
    return res

def dechiffre():
    label_dech.config(text=dechiffrer(resultat.get(),entree_cle.get()))

def chiffre_xor(lettre_message, lettre_cle):
    return chr(ord(lettre_message)^ord(lettre_cle))"""


#j'ai donc préféré refaire mon programme et mes fonctions 
#en m'aidant des fonctions du TD pour être sûr d'avoir bien compris les notions travaillées

import tkinter as tk 

texte_1 = "kd oqnbgzhm ehbghdq ztqz tm bncd ozq rtarshstshnm zkogzadshptd: bgzptd kdssqd drs qdlokzbdd ozq tmd ztsqd. tshkhrdq kz eqdptdmbd cdr kdssqdr ontq cdbncdq kd ldrrzfd."
texte_2 = "gx qosvlnkd wkvlkxo xiu vscx qno yd fsu cx qniix cx unkggx kdvsddyx xu vsdukxdu g'kdckvx. gxi gxuuoxi cy fsu cx qniix qxofxuuxdu cx cxvngxo gxi gxuuoxi cy fxiinmx sokmkdng fscygs 26. ixygxi gxi gxuuoxi cx n n a isdu vlkwwoxxi."
texte_3 = "dceuq e n'ehfp cg p'kyhhep uqfw cgiy citudm c gzudiq ni ezhd px c jhptv ep cggsht. kg hdtymdt xdzei gdx rzyq wir mvzxpw, cifcchdb znwd ccyw wy lkcsht, dp isgd uqfw wy ?"
texte_4 = ""
textes = [texte_1, texte_2, texte_3, texte_4]
listeTextes = ["Texte 1", "Texte 2", "Texte 3", "Texte 4"]
types_de_cryptage = ["Code de César", "Chiffrement par substitution", "Décalage avec un mot de passe", "Inconnu"]
style1 = ("Times", 14)
style2 = ("Times", 10)
global str_texte_dechiffre
global indice_texte
texte_choisi = 1
indice_texte = texte_choisi 
global texte_chiffre
global frequence_triee
texte_chiffre = textes[texte_choisi]
str_texte_dechiffre = texte_chiffre
largeur_texte = 500

def calculerFrequence(texte):
    global frequence_triee
    frequence_texte = []
    frequence_triee = []
    liste_des_frequences = []
    nombre_lettres = 0
    for l in texte:
        if 97 <= ord(l) < 123:
            nombre_lettres += 1
    for c in range(97, 123):
        if chr(c) in texte:
           frequence_texte.append((chr(c), round((texte.count(chr(c)) / nombre_lettres) * 100 , 2)))
    for a in frequence_texte:
        liste_des_frequences.append(a[1])
    while(len(liste_des_frequences)):
        index_max = liste_des_frequences.index(max(liste_des_frequences))
        frequence_triee.append(frequence_texte[index_max])
        frequence_texte.remove(frequence_texte[index_max])
        liste_des_frequences.remove(liste_des_frequences[index_max])
    return frequence_triee

def dechiffrerCodeCesar(texte, cle): 
    str_decryptage_cesar = []
    a = 0
    b = 0
    while len(str_decryptage_cesar) != len(texte):
        rang = ord(texte[b]) - 97
        rangCle = ord(cle[b%len(cle)]) - 97
        if 0 <= rang <= 25:
            str_decryptage_cesar.append(chr((rang+rangCle)%26+97))
            a += 1
        else:
            str_decryptage_cesar.append(texte[b])
        b += 1
    return "".join(str_decryptage_cesar)

def substituerLettreMot(texte_d_entre, texte_substitue, l, s):
    str_caractere = ""
    for i in range(len(texte_d_entre)):
        if texte_d_entre[i] == l:
            str_caractere += s
        else:
            str_caractere += texte_substitue[i]
    return str_caractere

def afficherTexteParSubstitution():
    global str_texte_dechiffre
    mot_1 = Entry_1.get()
    mot_2 = Entry_2.get()
    if types_de_cryptage[indice_texte] == types_de_cryptage[0] or types_de_cryptage[indice_texte] == types_de_cryptage[2]:
        cle = trouverDecalage(mot_1, mot_2)
        texte_dechiffre.config(text=dechiffrerCodeCesar(texte_chiffre, cle))
    elif types_de_cryptage[indice_texte] == types_de_cryptage[1]:
        if len(mot_1) == len(mot_2):
            while len(Entry_1.get()):
                Entry_1.delete(0)
            while len(Entry_2.get()):
                Entry_2.delete(0)
            for i in range(len(mot_1)):
                str_texte_dechiffre = substituerLettreMot(texte_chiffre, str_texte_dechiffre, mot_1[i], mot_2[i])
            texte_dechiffre.config(text=str_texte_dechiffre)

def fractionner(texte, nombre_fractions):
    fractions = []
    taille_fractions = int(len(texte) / nombre_fractions)
    for i in range(0, nombre_fractions):
        fractions.append(texte[i * taille_fractions : (i * taille_fractions) + taille_fractions])
    if len(texte) % nombre_fractions:
        fractions[-1] = fractions[-1] + texte[-1]
    return fractions

def afficherFractions(texte):
    liste_lettres = [lettres for lettres in texte]
    #print(liste_lettres)
    for f in range(42):                       #au début 21 car 168/21 = 8 (je pensais qu'il s'agissait
        fractions = liste_lettres[f*4:(f+1)*4]#d'un mdp de taille 8 mais j'en en déduis ensuite 
        graduation = ""                       #qu'il était de taille 4, d'où "f*4")
        str_fractions = ""
        for g in range(len(fractions)):
            graduation = graduation + str(g) + " "
            if fractions[g] == " ":
                str_fractions = str_fractions + "_"+ " "
            else:
                str_fractions = str_fractions + fractions[g] + " "
        print(graduation+"\n" + str_fractions +"\n")

def trouverDecalage(mot_1, mot_2):
    global cle
    cle = []
    for i in range(len(min(mot_1, mot_2))):
        rang_mot_1 = ord(mot_1[i]) - 97
        rang_mot_2 = ord(mot_2[i]) - 97
        if 0 <= rang_mot_1 <= 25 and 0 <= rang_mot_2 <= 25:
            cle.append(chr((rang_mot_2-rang_mot_1)%26 + 97))
        else:
            cle.append(str(""))
    print(cle)
    return "".join(cle)

racine = tk.Tk()
racine.title("Projet Cryptographie")
etiquette1 = tk.Frame(racine)

msg_texte_chiffre = tk.Message(etiquette1, text=texte_chiffre, relief = "sunken", font=style1, width=largeur_texte)
texte_dechiffre = tk.Message(etiquette1, relief="ridge", font=style1, width = largeur_texte)
labelFreq = tk.Label(etiquette1, relief="ridge", font=style2)
labelFreq.config(text=calculerFrequence(textes[texte_choisi]))
boutonCorrespondance = tk.Button(etiquette1, text="Subsitué par", command=afficherTexteParSubstitution, font=style2)
Entry_1 = tk.Entry(etiquette1, font=style2)
Entry_2 = tk.Entry(etiquette1, font=style2)

msg_texte_chiffre.grid(row=0, columnspan=3)
texte_dechiffre.grid(row=2, columnspan=3)
Entry_1.grid(row=1, column=0)
Entry_2.grid(row=1, column=2)
boutonCorrespondance.grid(row=1, column=1)
labelFreq.grid(row=3, columnspan=3)

etiquette1.grid(row=0, column=3)

fractions = fractionner(texte_chiffre, 5)

#les boucles utilisées pour trouver "manuellement" le mdp du texte 3:
"""fractions = fractionner(texte_chiffre, 5)
for i in range(1, 22):
    somme = 0
    for seg in fractionner(texte_chiffre, i):
        somme += calculer_frequence(seg)[0][1]
print(len(texte_chiffre))
fractions = fractionner(texte_chiffre, 42)
for i in range(len(cle)):
    if cle[i] == "w" or cle[i] == "y":
        print(i)
print(fractions)"""

#les fonctions utilisées pour trouver mdp du texte 3:

#trouverDecalage("dceuq e n'ehfp cg p'kyhhep uqfw cgiy citudm c gzudiq ni ezhd px c jhptv ep cggsht. kg hdtymdt xdzei gdx rzyq wir mvzxpw, cifcchdb znwd ccyw wy lkcsht, dp isgd uqfw wy ?", "dceuq a l'ehfp cg l'kyhhep uqfw cgiy citudm a gzudiq ni ezhd px a jhptv ep cggsht. le hdtymdt xdzei gdx rzyq wir mvzxpw, cifcchdb znwd ccyw le lkcsht, dp isgd uqfw wy ?")
#afficherFractions(textes[2])
#print(len(texte_chiffre))


texte_1_decrypte = dechiffrerCodeCesar(textes[0],"b")
print(texte_1_decrypte)
texte_2_decrypte = "le prochain fichier est code par un mot de passe de taille inconnue et contient l'indice. les lettres du mot de passe permettent de decaler les lettres du message original modulo 26. seules les lettres de a a z sont chiffrees."
print("\n" + texte_2_decrypte)
texte_3_decrypte = dechiffrerCodeCesar(textes[2],"ypwb")
print("\n" + texte_3_decrypte)
#texte_1_decrypte = le prochain fichier aura un code par substitution alphabetique: chaque lettre est remplacee par une autre. utiliser la frequence des lettres pour decoder le message.
#texte_2_decrypte = le prochain fichier est code par un mot de passe de taille inconnue et contient l'indice. les lettres du mot de passe permettent de decaler les lettres du message original modulo 26. seules les lettres de a a z sont chiffrees.
#texte_3_decrypte = bravo a l'aide de l'indice vous avez reussi a casser ce code et a finir ce devoir. le dernier texte est pour les braves, regardez vous dans un miroir, en etes vous un ?

racine.mainloop()

#Pour les décryptage du texte 1, j'ai appliqué le décalage (b) vu en TD
#Pour le texte 4, je me suis aidé de la fréquence de la lettre "x" qui correspdondait surement au "e" puis je me suis inspiré
#du film sur Alan Turing: "The Imitation Game" où Alan Turing arrive à décrypter Enigma en utlisisant la redondance des mots
#utilisé à chaque fois que l'Allemagne annoçait la météo. J'ai donc fais pareil car j'ai remarqué que les 3 premiers mots
#du texte 2 avaient exactement la même longueur et le même emplacement que les 3 premiers mots du texte 1. De plus, les "e" 
#correspondaient parfaitement pour "le" et "fichier". J'ai donc subtitué les 3 premiers mots, ce qui m'a donné une grosse esquisse 
#du texte déchiffré. J'ai ensuite substituer des mots qui ressemblaient énormément à des mots français avec seulement 1 à 2 lettres
#mal substituées.
#Pour le texte 3, je suis parti du principe que les lettres seules correspondaient à un "a" puis que les lettres avec une apostrophe 
#à un "l" car aucun mot précédé d'une apostrophe était de longueur 3 : "c'est" n'était donc pas possible.
#Ensuite j'ai trouvé les lettres "w" pour le premier "a" et ensuite "y" pour le premier "l ' ". J'ai vu ensuite que les lettres étaient répétées 
#pour décaler d'autres lettres. J'en ai donc conclu qu'il s'agissait d'un mot de passe de longueur 8 au début car le "y" et le "w" était répétés
#dans les 8 premier indices. Mais en essayant de remplacer les mots de longuer 2 dans la seconde phrase par "le", j'ai trouvé une itération de 
#de longueur 4 avec "ypwh" comme mot de passe. Je l'ai donc essayé et de même que pour le texte 2, cela m'a donné une grosse esquisse.
#J'ai donc ensuite déduit le "b" dans "ypwb" grâce au premier mot qui ressemblait très fortement à "bravo" ("brauo") avec comme mdp "ypwa"
#Le "a" du mot de passe sort du fait que je ne voulais pas décaler les dernières lettres car je n'avais trouver aucun indice pour la 
#dernière lettre du mot de passe. 