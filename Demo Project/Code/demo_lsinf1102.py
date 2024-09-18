"""
  The Astronogame Menu
  Module pour le menu des jeu, visible a l'utilisateur a l'allumage
  Hadrien Allegaert, Julien Brichard, Julien Denis, Jerome Lechat
"""
from sense_hat import SenseHat, ACTION_RELEASED, ACTION_PRESSED
import random
import time

s = SenseHat()
s.low_light = True
sense = s 
s.set_imu_config(True,True,True)

Rouge = (255,0,0)
Vert = (0,255,0)
Bleu = (0,0,255)
Blanc = (255,255,255)
Noir = (0,0,0)
Rose = (210,105,30)
Jaune = (255,215,0)
Violet = (75,0,130)
Brun = (126,88,53)
Orange = (255,165,0)
"""Set des couleurs"""
R = Rouge
B = Bleu
W = Blanc
P = Rose
Y = Jaune
T = Violet
G = Orange
U = Brun

"""----menuUser----"""

G1 = [
  P, W, W, W, W, W, W, P,
  W, W, Y, U, U, Y, W, W,
  W, W, Y, W, W, Y, W, W,
  W, W, G, W, W, G, W, W,
  W, W, G, W, W, G, W, W,
  W, T, T, W, T, T, W, W,
  W, T, T, W, T, T, W, W,
  P, W, W, W, W, W, W, P,
  ]#logo jeu 1 GuitarHro
G2 = [
  P, W, W, W, W, W, W, P,
  W, B, B, W, W, W, W, W,
  W, B, W, B, W, W, W, W,
  W, B, W, B, W, W, W, W,
  W, B, B, W, R, W, R, W,
  W, W, W, W, R, R, W, W,
  W, W, W, W, R, W, R, W,
  P, W, W, W, W, W, W, P,
  ]#logo jeu 2 DonkeyKong
G3 = [
  P, W, W, W, W, W, W, P,
  W, B, W, W, W, W, R, W,
  W, B, W, W, W, R, R, W,
  W, B, W, W, W, W, R, W,
  W, B, W, W, W, W, R, W,
  W, B, W, W, W, W, W, W,
  W, B, B, B, B, W, W, W,
  P, W, W, W, W, W, W, P,
  ]#logo jeu 3 Labyrinth1
G4 = [
  P, W, W, W, W, W, W, P,
  W, B, W, W, W, R, W, W,
  W, B, W, W, R, W, R, W,
  W, B, W, W, W, R, W, W,
  W, B, W, W, R, R, R, W,
  W, B, W, W, W, W, W, W,
  W, B, B, B, B, W, W, W,
  P, W, W, W, W, W, W, P,
  ]#logo jeu 4 Labyrinth2
G = [G1,G2,G3,G4]#liste des logos du menu des jeux



def menuLogo(a):
  """
    Affiche un menu de selection de jeux
    Possibilite d'entrer son mot de passe apres avoir appuyer 
    le joystick vers le haut
  pre: 'a' numero du logo a afficher
  post: ouvre le jeu a l'appuis du joystick 'middle' ou le menu ecret si le mdp est bon 
  """
  while True:#boucle infinie
    s.set_pixels(G[a])#set l'ecran sur le logo
    for event in s.stick.get_events():#attends l'evenement
        if event.action == "pressed":#si joystick pressed
            if event.direction == "up":#si joystick direction centre
                if check(user_input(),pswd_lst("command.txt")):# si le mot de passe est correct
                    cle()
                    sense.clear()# eteinds l'ecran
                    code_menu(0)#active le menusecret dnas le module 'secretMenu'
            if event.direction == "right" :#si joystick direction est droite
                if a < (len(G)-1):
                    a += 1
                else:
                    a = 0
            elif event.direction == "left" :#si joystick direction gauche
                if a > 0:
                    a -= 1
                else:
                    a = len(G)-1
            elif event.direction == "middle":#si joystick direction centre
                if a == 0:#logo jeu 1
                    guitarHeroGame(LogoList())
                    a = 0
                elif a == 1:#logo jeu 2
                    DonkeyKong(grille())
                    a = 0
                elif a == 2:#logo jeu 3
                    labyrinthGame(labyrinth_ball(),3)
                    a = 0
                elif a == 3:#logo jeu 4
                    labyrinthBigGame(labyrinth_List(),3)    
                    a = 0

"""----Loading-----"""
def loading(): #Fonction ecran chargement (pour menu secret) [Soit loading() soit cle()]
    yellow = (255, 255, 0)
    blue = (0, 0, 128)
    white = (255,255,255)
    nothing = (0,0,0)
    purple = (128,0,128)

    O = nothing
    B = blue
    P = purple
    Y = yellow
    W = white
    
    logo1 = [
        W, W, W, W, W, W, W, W,
        W, W, B, B, B, B, W, W,
        W, B, W, W, W, W, W, W,
        B, B, B, W, W, W, B, W,
        W, B, W, W, W, B, B, B,
        W, W, W, W, W, W, B, W,
        W, W, B, B, B, B, W, W,
        W, W, W, W, W, W, W, W,
        ]
    logo2 = [
        W, W, W, W, B, W, W, W,
        W, W, W, B, B, B, W, W,
        W, B, W, W, B, W, B, W,
        W, B, W, W, W, W, B, W,
        W, B, W, W, W, W, B, W,
        W, B, W, B, W, W, B, W,
        W, W, B, B, B, W, W, W,
        W, W, W, B, W, W, W, W,
        ]
    logoloading = [logo1,logo2]
    count = 0
    while True:#boucle infinie
      s.set_pixels(logoloading[count%len(logoloading)])#set l'ecran sur le logo choisis
      time.sleep(0.5)#patiente 0.5 sec
      count += 1#incremente count de 1
      if count == 10 :# si count contient le int 10
          return

def cle(): #Fonction ecran chargement (pour menu secret) [Soit loading()soit cle()]

    O = Noir
    B = Bleu
    P = Violet
    Y = Jaune
    W = Blanc
    
    logo1 = [
        B, B, Y, Y, Y, Y, B, B,
        B, B, Y, B, B, Y, B, B,
        B, B, Y, Y, Y, Y, B, B,
        B, B, B, B, Y, B, B, B,
        B, B, B, B, Y, B, B, B,
        B, B, Y, Y, Y, B, B, B,
        B, B, Y, Y, Y, B, B, B,
        B, B, B, B, Y, B, B, B,
        ]
    logo2 = [
        B, B, B, B, B, B, B, B,
        B, B, B, B, B, B, B, B,
        Y, Y, Y, B, B, B, B, B,
        Y, B, Y, Y, Y, Y, Y, Y,
        Y, B, Y, B, B, Y, Y, B,
        Y, Y, Y, B, B, Y, Y, B,
        B, B, B, B, B, B, B, B,
        B, B, B, B, B, B, B, B,
        ]
    logo3 = [
        B, B, B, Y, B, B, B, B,
        B, B, B, Y, Y, Y, B, B,
        B, B, B, Y, Y, Y, B, B,
        B, B, B, Y, B, B, B, B,
        B, B, B, Y, B, B, B, B,
        B, B, Y, Y, Y, Y, B, B,
        B, B, Y, B, B, Y, B, B,
        B, B, Y, Y, Y, Y, B, B,
        ]
    logo4 = [
        B, B, B, B, B, B, B, B,
        B, B, B, B, B, B, B, B,
        B, Y, Y, B, B, Y, Y, Y,
        B, Y, Y, B, B, Y, B, Y,
        Y, Y, Y, Y, Y, Y, B, Y,
        B, B, B, B, B, Y, Y, Y,
        B, B, B, B, B, B, B, B,
        B, B, B, B, B, B, B, B,
        ]
    logocle = [logo1,logo2,logo3,logo4]
    count = 0
    while True:# boucle infinie
      s.set_pixels(logocle[count%len(logocle)])#set l'ecran sur le logo choisis
      time.sleep(.5)#patiente 0.5 sec
      count += 1#incremente count de 1
      if count == 10 :#quand count contient 10
          return


"""----menuSecret----"""

def Menu():
    """
    Definis une liste de logos pour le menu secret
    pre:
    post: renvoit la liste de logos
    """
    Edit_code = [
        P, W, W, W, W, W, W, P,
        W, W, R, R, R, R, W, W,
        W, W, Y, Y, Y, Y, W, W,
        W, W, Y, Y, Y, Y, W, W,
        W, W, Y, Y, Y, Y, W, W,
        W, W, N, N, N, N, W, W,
        W, W, W, N, N, W, W, W,
        P, W, W, W, W, W, W, P,
        ]#logo d'edition du message secret
    Delete_code = [
        P, W, W, W, W, W, W, P,
        W, R, W, W, W, W, R, W,
        W, W, R, W, W, R, W, W,
        W, W, W, R, R, W, W, W,
        W, W, W, R, R, W, W, W,
        W, W, R, W, W, R, W, W,
        W, R, W, W, W, W, R, W,
        P, W, W, W, W, W, W, P,
        ]#logo de suppression du message secret
    See_code = [
        P, W, W, W, W, W, W, P,
        W, W, B, B, B, B, W, W,
        W, B, B, B, B, B, B, W,
        W, B, B, N, N, B, B, W,
        W, B, B, N, N, B, B, W,
        W, B, B, B, B, B, B, W,
        W, W, B, B, B, B, W, W,
        P, W, W, W, W, W, W, P,
        ]#logo d'affichage du message secret
    Escape = [
        P, W, W, W, W, W, W, P,
        W, W, W, V, V, W, W, W,
        W, W, W, V, V, W, W, W,
        W, W, W, V, V, W, W, W,
        W, V, V, V, V, V, V, W,
        W, W, V, V, V, V, W, W,
        W, W, W, V, V, W, W, W,
        P, W, W, W, W, W, W, P,
        ]#logo exit
    Password = [
        P, W, W, W, W, W, W, P,
        W, W, W, U, U, W, W, W,
        W, W, U, W, W, U, W, W,
        W, W, Y, Y, Y, Y, W, W,
        W, W, Y, Y, Y, Y, W, W,
        W, W, Y, Y, Y, Y, W, W,
        W, W, Y, Y, Y, Y, W, W,
        P, W, W, W, W, W, W, P,
        ]#logo changement de pswd
      
    menu = [See_code,Edit_code,Delete_code,Password,Escape]
    return menu#retourne 'menu' la liste contenant les logos


def code_menu(a):
    """
    affiche le menu secret et les logos associes gere le dernier retour au premier ou inverse
    """
    while True:#boucle infinie
        s.set_pixels(Menu()[a])#set l'ecran sur le logo
        for event in s.stick.get_events():#attends l'evenement
            if event.action == "pressed":#si joystick presse
                if event.direction == "up":
                    if check(user_input(),pswd_lst("Fast_delete.txt")):
                        """recuperation de backup"""
                        if a == 0:
                            with open('backup.txt','r') as file:#ouvre le fichier 'backup' en mode lecture
                                str = ""#initialise str en string vide
                                for line in file:#parcours les lignes du fichier
                                    str += line#ajoute la ligne a la string
                            if str != "":# si la string n'est pas vide
                                #recuperation du contenu du fichier 'backup' vers le fichiers 'secret' + vider le fichier 'backup'
                                with open('secret.txt','w') as file:
                                    file.write(str)
                                with open('three.txt', 'w') as file:
                                    file.write("")
                                with open('backup.txt' ,'w') as file:
                                   file.write("")
                                s.show_message("Backup restored")#affiche le message entre guillemet a l'ecran
                            else:
                                s.show_message("No backup")#affiche le message entre guillemet a l'ecran
                        if a == 2:
                            file = open("secret.txt", "w")#ouvre le fichier secret.txt
                            file.write(encode("cryptographie","No message!\n"))#ecrase l'ancien message et ecrit 'No message!' a la place
                            file.close()#ferme le fichier
                            s.show_message("Message deleted")#affiche le message entre guillemet a l'ecran
                        if a == 3:
                            edit_pswd("Fast_delete.txt")#appelle la fonction d'edition du mot de passe dans le fichier 'Fast_delete'
                elif event.direction == "right" :#si joystick direction est droite
                    if a < (len(Menu())-1):
                        a += 1
                    else:
                        a = 0
                elif event.direction == "left" :#si joystick direction gauche
                    if a > 0:
                        a -= 1
                    else:
                        a = len(Menu())-1
                elif event.direction == "middle":#si joystick direction centre
                    if a == 0:#logo jeu 3
                        show()
                    elif a == 1:#logo jeu 1
                        edit()
                    elif a == 2:#logo jeu 2
                        delete()
                    elif a == 3:#logo jeu 4
                        edit_pswd("command.txt")
                    elif a == 4:
                        loading()
                        exit()
                        
def secure():
    with open('three.txt','r') as file:#le fichier 'three' est ouvert en mode lecture
        m = ""#initialisation string vide
        for line in file:#parcours les lignes du fichier
            m += line#ajoute la ligne a la string
    if m == "11":#si la string contient "11"
        with open('secret.txt','r') as file:#ouverture du fichier'secret en mode lecture
            s = ""#initialisation string vide
            for line in file:#parcours les lignes du fichier
                s += line#ajoute la ligne a la string
        if decode("cryptographie",s) != "Three times wrong access":#si al string decodee n'est pas "Three times wrong access"
            with open('backup.txt','w') as file:#ouverture du fichiers backup en mode reecriture
                file.write(s)#ecrase l ancienne version du fichier pour y ecrire la string contenu dans 'secret'
            with open("secret.txt",'w') as file:#ouverture du fichier 'secret' en mode reecriture
                file.write(encode("cryptographie","Three times wrong access"))#encode et ecrit dans le fichier 'secret' le message "Three times wrong access"
    else:
        with open("three.txt" ,'a') as file:#ouverture du ficheir en mode ajout
            file.write("1")#ajoute la string"1" au fichier


def edit():
    O = N
    
    espaceScreen = [O, O, O, O, O, O, O, O,
                    O, O, O, O, O, O, O, O,
                    O, O, O, O, O, O, O, O,
                    O, O, O, O, O, O, O, O,
                    O, O, O, O, O, O, O, O,
                    O, W, O, O, O, O, W, O,
                    O, W, W, W, W, W, W, O,
                    O, O, O, O, O, O, O, O]
    
    backSlashnScreen = [O, O, O, O, O, O, O, O,
                        O, O, O, O, O, O, W, O,
                        O, O, O, O, O, O, W, O,
                        O, O, O, O, O, O, W, O,
                        O, O, W, O, O, O, W, O,
                        O, W, W, W, W, W, W, O,
                        O, O, W, O, O, O, O, O,
                        O, O, O, O, O, O, O, O]
    l = ["a","b","c","d","e","f","g","h","i","j","k","l",
        "m","n","o","p","q","r","s","t","u","v","w","x","y","z",
        " ","\n","_","-",",",".","!","?","0","1","2","3","4","5","6","7","8","9","t","t",
         "A","B","C","D","E","F","G","H","I","J","K","L",
         "M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]#liste caractere minuscule
    if testAccessLevel():
        aLog = 0 #initialisation de 'a' sur 0 pour la selection de la lettre dans la liste
        m = "" #initialisation de 'm' sur une string vide
        while True:#boucle infinie
            if aLog == 26: #si c'est le 26eme element de la liste
                s.set_pixels(espaceScreen)#set l'ecran sur le symbole de l'espace
            elif aLog == 27:#si c'est le 27eme element de la liste
                s.set_pixels(backSlashnScreen)#set l'ecran sur le symbole du retour a la ligne
            elif aLog == 44:
                s.set_pixels(Menu()[4])
            elif aLog == 45:
                s.set_pixels(Menu()[2])
            elif aLog != 26 and aLog != 27 and aLog != 44 and aLog != 45:# pour toutes les autres occurences de la liste
                s.show_letter(l[aLog])#set l'ecran sur la lettre ou le symbole choisis dnas la liste 
            for event in s.stick.get_events():#attends l'evenement
                if event.action == "pressed":#si le joystick est presse
                    if event.direction == "right":#si le joystick direction est centre
                    ####gere le retour au premier si au dernier et inverse####
                        if aLog < (len(l)-1):
                            aLog += 1
                        else:
                            aLog = 0
                    if event.direction == "left":#si joystick direction est gauche
                        if aLog == 0:
                            aLog = 45
                        if aLog > 0:
                          aLog -= 1
                        else:
                          aLog = len(l)-1
                    if event.direction == "down":#si joystick direction est bas
                        if aLog < 26:
                            s.clear()
                            s.show_letter(l[aLog])
                        if aLog > 45:
                            s.clear()
                            aLog -= 46
                            s.show_letter(l[aLog])
                    if event.direction == "up":#si joystick direction est haut
                        if aLog < 26:
                            s.clear()
                            aLog += 46
                            s.show_letter(l[aLog])
                        if aLog > 45:
                            s.clear()
                            s.show_letter(l[aLog])
                    if event.direction == "middle":#si joystick direction est centre
                        if aLog != 44 and aLog != 45:
                            m += l[aLog]
                        if aLog == 45:
                            return
                        if aLog == 44 :
                            if m != "":
                                file = open("secret.txt", "w")#ouvre le fichier secret.txt
                                file.write(encode("cryptographie",m))#ecrit le nouveau message dedans en ecrasant l'ancien
                                file.close()#ferme le fichier secret.txt                            
                            setAccessLevel()
                            with open("three.txt","w") as file:
                                file.write("")
                            return
    else:
        secure()
        s.show_message("Access denied")

    

def delete():
    """
    """
    if testAccessLevel() :
        file = open("secret.txt", "w")#ouvre le fichier secret.txt
        file.write(encode("cryptographie","No message!"))#ecrase l'ancien message et ecrit 'No message!' a la place
        file.close()
        file = open("accessLevel.txt", "w")#ouvre le fichier secret.txt
        file.write(encode("cryptographie","Level zero"))#ecrase l'ancien message et ecrit 'No message!' a la place
        file.close()#ferme le fichier
        s.show_message("Message deleted")#affiche a l'ecran que le message a ete supprimer
        with open("three.txt","w") as file:
            file.write("")
    else:
        secure()
        s.show_message('Access denied')


def show():
    """
    """
    if testAccessLevel():
        with open("secret.txt", "r") as file:#ouvre le fichier en mode lecture
            m = ""#initialise 'm' sur string vide
            for line in file:#pour toutes les lignes du fichier
                m += line #ajoute la ligne a la string 'm'
            s.show_message("{}".format(decode("cryptographie",m)))#affiche le message secret a l'ecran
            file.close() #ferme le fichier
        with open("three.txt","w") as file:
            file.write("")
    else:
        secure()
        s.show_message("Access denied")


def edit_pswd(filename):
    """
    """
    if testAccessLevel():
        file_lst = list()#definis 'file_lst' en liste vide
        i = 0#initialise i a 0
        s.show_message("Please choose a new password")#affiche le message user
        while i < 6:#boucle 6 passage a conditions
            for event in s.stick.get_events():#attends l'evenement
                if event.action == "pressed":#joystick presse
                    if event.direction == "middle":#joystock direction centre
                        file_lst.append([float(s.get_accelerometer_raw()['x'])*100,float(s.get_accelerometer_raw()['y'])*100,float(s.get_accelerometer_raw()['z'])*100])#ajoute a la liste'file_lst les coordonnes de position spatiale
                        s.show_message(str(i+1)+"/6")#affiche le message avec le nombre de position
                        i += 1#incrementation 'i' de 1
        newPassword = ""#definis le nouveau password sur un string vide
        for x in range(len(file_lst)):#pour x dans la longueur de la liste
            for y in range(len(file_lst[x])):#pour y dans la longueur du tuples inserer dans la liste
            ####change les coordonnes en caractere alphabetique a 45 degres pres####
                if  -50 <= float(file_lst[x][y]) < 50:
                    newPassword += 'A'
                if  50 <= float(file_lst[x][y]) <= 150:
                    newPassword += 'B'
                if -150 <= float(file_lst[x][y]) <= -50:
                    newPassword += 'C'
        file = open(filename,'w')#ouvre le fichier 'command.txt'
        file.write(hashing(newPassword))#ecrit la string 'newPassword' dans le fichier 'command.txt'
        file.close()#ferme le fichier command.txt
        s.show_message("Password changed")
    else:
        secure()
        s.show_message("Access denied")

def exit():
    s.clear()
    menuLogo(0)

"""----unlocker----"""

def user_input():
    """
        Permet a l'utilisateur d'entrer un essaie de mdp, le stocke dans une liste l et le renvoit.
    pre:
    post: renvoit l la liste contenant les direction du gryroscope selectionne rpar l'utilisateur comme mdp
    """
    l=[]
    i = 0
    while i < 6:                             #boucle jusqu'a i = 6
        for event in sense.stick.get_events(): #attends une action sur le joystick
            if event.action == ACTION_PRESSED:   #joystick presse: n'importe quel direction
                if event.direction == "middle":#joystick presse: direction centre
                    raw = sense.get_accelerometer_raw()
                    l.append([float(raw['x'])*100,float(raw['y'])*100,float(raw['z'])*100])  
                    #ajoute a la liste 'l' tous les coordonnees de la position spaciale du raspberry pi
                    i += 1   #incrementation i de 1
    for j in range(len(l)):
        for k in range(len(l[j])):
            if -50 <= l[j][k] < 50:
                l[j][k] = 'A'
            elif 50 <= l[j][k] <= 150:
                l[j][k] = 'B'
            elif -150 <= l[j][k] <= -50:
                l[j][k] = 'C'
    m = ""
    for i in range(len(l)):
        for j in range(len(l[i])):
            m += l[i][j]
    return hashing(m)
    
    
    
def pswd_lst(filename):
  """
    fonction permettant la decoupe du fichier qui detient le mot de passe 
    en liste contenant une liste pour chaque lignes
  pre:
  post: renvoit la liste contenant le mot de passe
  """
  psd_str = ""
  with open(filename,'r') as file:#ouvre le fichier 'command.txt' et on l'uitlisera sous le nom ' file'
      for line in file:#boucle iterative de chaque ligne du fichier
        for char in line:#pour tout les caracteres dans la ligne
          psd_str += char# ajoute le caractere a la string 'psd_str'
      file.close()#ferme le fichier 'command.txt'
  return psd_str
             
       
       
def check(user_l,pswd_lst_check):
  """Verifie la concordance des mot de passe
  pre : recoit 'l' la liste contenant le mdp entre pa l'utilisateurs
        et 'pswd_lst_check' la lsite contenant le mdp extrait du fichier txt
  post: renvoit True ou False
  """
  if user_l == pswd_lst_check:# condition de comparaison entre chaque occurences de chaque liste imbriquee
    return True
  else:          
    return False#retourne False
  
"""----AccessLevel----"""

def testAccessLevel():
  """
    Fonction de verification du niveau d'acces
  pre:
  post:
  """
  ###lecture du fichier accessLevel.txt###
  file = open('accessLevel.txt','r')#ouvre le fichier 'accessLevel.txt'
  l = ""#initialise une string vide
  for line in file:#pour toutes les lignes dans le fichier
    l += line.strip()#on ajoute a la string la line sans le \n final
  file.close()#fermeture du fichier
  l = decode("cryptographie",l)
  if l.rstrip("\n") == "Level zero":#si le niveau d'accreditation est egal a 0
    return True#return True et debloque la suppresion
  elif l.rstrip("\n") == "Level one":#si le niveau d'accreditation est egal a 1
    if enigmaGame(circle()):
        with open('three.txt', 'w') as files:
            files.write("")
        return True
    else:
        return False
  elif l.rstrip("\n") == "Level two":#si le niveau d'accreditation est egal a 2
    if labyrinthGame(labyrinth_ball(),3):
        with open('three.txt', 'w') as files:
            files.write("")
        return True
    else:
        return False
  elif l.rstrip("\n") == "Level three":#si le niveau d'accreditation est egal a 3
    if guitarHeroGame(LogoList()):
        with open('three.txt', 'w') as files:
            files.write("")
        return True
    else:
        return False
  elif l.rstrip("\n") == "Level four":#si le niveau d'accreditation est egal a 4
    if DonkeyKong(grille()):
        if enigmaGame(circle()):
            with open('three.txt', 'w') as files:
                files.write("")
            return True
        else:
            return False
    else:
        return False
  elif l.rstrip("\n") == "Level five":#si le niveau d'accreditation est egal a 5
    if labyrinthBigGame(labyrinth_List(),3):
        with open('three.txt', 'w') as files:
            files.write("")
        return True
    else:
        return False


def setAccessLevel():
    lst = ["0","1","2","3","4","5"]
    i = 0
    while True:
        s.show_letter(lst[i])
        for event in s.stick.get_events():#attends l'evenement
            if event.action == "pressed":#si le joystick est presse
                if event.direction == "right":#si le joystick direction est centre
                ####gere le retour au premier si au dernier et inverse####
                    if i < (len(lst)-1):
                        i += 1
                    else:
                        i = 0
                if event.direction == "left":#si joystick direction est gauche
                    if i == 0:
                        i = len(lst)-1
                    else:
                        i -= 1
                if event.direction == "middle":
                    with open("accessLevel.txt",'w') as file:
                        if i == 0:
                            t ="zero"
                        elif i ==1:
                            t ="one"
                        elif i == 2:
                            t ="two"
                        elif i == 3:
                            t ="three"
                        elif i == 4:
                            t ="four"
                        elif i == 5:
                            t ="five"
                        file.write(encode("cryptographie","Level {}".format(t)))
                        file.close()
                        return
        

"""------labyrinth-----"""
def labyrinth_ball():
  G = Vert
  Y = Jaune
  B = Bleu
  W = Blanc
  R = Rouge
  P = Rose
    
  labyrinthOne =[
    O, O, G, O, O, G, O, O,
    O, O, G, O, G, G, G, O,
    O, G, G, O, G, O, O, O,
    O, O, O, O, O, G, G, O,
    G, G, O, G, G, G, O, O,
    O, G, O, G, O, O, O, G,
    O, G, O, O, O, G, G, G,
    O, O, O, G, O, O, O, O,
     ]
  return labyrinthOne

def labyrinthGame(list,x):
  R = Rouge
  Y = Jaune
  G = Vert
  state = { "pion_x" : 0,
          "pion_y" : 0,
          "pion_color" : R,
          "arrival_x" : 5,
          "arrival_y" : 2,
          "arrival_color" :Y}
  
  pion_x =state["pion_x"]
  pion_y=state["pion_y"]
  pion_color=state["pion_color"]
  arrival_x = state["arrival_x"]
  arrival_y = state["arrival_y"]
  arrival_color = state["arrival_color"]
  life = x
  s.show_message("life : {}".format(life))
  labyrinth = list
  i=0#nombre de pas a 0
  while True:#boucle infinie
    i+=1#incremente le compteur de pas de 1
    if life == 0:#si user na plus de vie 
      s.show_message("Game Over",scroll_speed = 0.1)#affiche le message "Game Over"
      return False
    if i == 100:# is le nombre de pas est egal a 100
      s.show_message("Steps over")#affiche le message entre guillemet
      pion_y = state["pion_y"]
      pion_x = state["pion_x"]
      s.set_pixels(list)
      life -= 1
      s.show_message("life : {}".format(life))#affiche le message entre guillemet
      i = 0
      s.clear()#eteinds l ecran
      
    else:
      s.set_pixels(list)#affiche la carte a l ecran
      s.set_pixel(pion_x,pion_y,pion_color)#affiche le pion a lecran
      s.set_pixel(arrival_x,arrival_y,arrival_color)#affiche le point d arrivee
      if pion_x == arrival_x and pion_y == arrival_y:#si le pion est sur l arrivee
        s.show_message("Level passed")#affiche le message entre guillemet
        return True
      else:
        event = s.stick.wait_for_event()#attends l evenement
        if event.action == "pressed":
          if event.direction == "right":#verifie l'evenement
            if pion_x == 7:
              pass
            else:
              s.set_pixel(pion_x,pion_y,(0,0,0))#eteinds la position precedente du pion
              pion_x += 1#incremente la position du pion
              if labyrinth[8*pion_y+pion_x] ==  G:
                """gestion des murs"""
                s.show_message("Wall",scroll_speed = 0.1)#affiche le message entre guillemet
                pion_x -= 1#incremente la position du pion
                life -= 1#incremente les vie de -1
                s.show_message("life : {}".format(life))#affiche le message entre guillemet
                s.clear()#eteinds l ecran
          if event.direction == "left":#verifie l'evenement
            if pion_x == 0:
              pass
            else:
              s.set_pixel(pion_x,pion_y,(0,0,0))#eteinds la position precedente du pion
              pion_x -= 1#incremente la position du pion
              if labyrinth[8*pion_y+pion_x] ==  G:
                """gestion des murs"""
                s.show_message("Wall",scroll_speed = 0.1)#affiche le message entre guillemet
                pion_x += 1#incremente la position du pion
                life -= 1#incremente les vie de -1
                s.show_message("life : {}".format(life))#affiche le message entre guillemet
                s.clear()#eteinds l ecran
          if event.direction == "up":#verifie l'evenement
            if pion_y == 0:
              pass
            else:
              s.set_pixel(pion_x,pion_y,(0,0,0))#eteinds la position precedente du pion
              pion_y -= 1 #incremente la position du pion
              if labyrinth[8*pion_y+pion_x] ==  G:
                """gestion des murs"""
                s.show_message("Wall",scroll_speed = 0.1)#affiche le message entre guillemet
                pion_y += 1#incremente la position du pion
                life -= 1#incremente les vie de -1
                s.show_message("life : {}".format(life))#affiche le message entre guillemet
                s.clear()#eteinds l ecran
          if event.direction == "down":#verifie l'evenement
            if pion_y == 7:
              pass
            else:
              s.set_pixel(pion_x,pion_y,(0,0,0))#eteinds la position precedente du pion
              pion_y += 1 #incremente la position du pion
              if labyrinth[8*pion_y+pion_x] ==  G:
                """gestion des murs"""
                s.show_message("Wall",scroll_speed = 0.1)#affiche le message entre guillemet
                pion_y -= 1#incremente la position du pion
                life -= 1#incremente les vie de -1
                s.show_message("life : {}".format(life))#affiche le message entre guillemet
                s.clear()#eteinds l ecran
          if event.direction =='middle':#verifie l'evenement
              if -150 <= int(s.get_accelerometer_raw()['x']*100) <= -50 and -50 <= int(s.get_accelerometer_raw()['y']*100) <= 50  and -50 <= int(s.get_accelerometer_raw()['z']*100) <= 50:
                  #LEFT/position accelerometre_raw
                  if pion_x == 0:
                      pass
                  else:
                      s.set_pixel(pion_x,pion_y,(0,0,0))#eteinds la position precedente du pion
                      pion_x -= 1#incremente la position du pion
                      if labyrinth[8*pion_y+pion_x] ==  G:
                        """gestion des murs"""
                        s.show_message("Wall",scroll_speed = 0.1)#affiche le message entre guillemet
                        pion_x += 1#incremente la position du pion
                        life -= 1#incremente les vie de -1
                        s.show_message("life : {}".format(life))#affiche le message entre guillemet
                        s.clear()eteinds l ecran
              if 50 <= int(s.get_accelerometer_raw()['x']*100) <= 150 and -50 <= int(s.get_accelerometer_raw()['y']*100) <= 50  and -50 <= int(s.get_accelerometer_raw()['z']*100) <= 50:
                  #RIGHT/position accelerometre_raw
                  if pion_x == 7:
                      pass
                  else:
                      s.set_pixel(pion_x,pion_y,(0,0,0))#eteinds la position precedente du pion
                      pion_x += 1#incremente la position du pion
                      if labyrinth[8*pion_y+pion_x] ==  G:
                        """gestion des murs"""
                        s.show_message("Wall",scroll_speed = 0.1)#affiche le message entre guillemet
                        pion_x -= 1#incremente la position du pion
                        life -= 1#incremente les vie de -1
                        s.show_message("life : {}".format(life))#affiche le message entre guillemet
                        s.clear()#eteinds l ecran
              if -50 <= int(s.get_accelerometer_raw()['x']*100) <= 50 and -150 <= int(s.get_accelerometer_raw()['y']*100) <= -50  and -50 <= int(s.get_accelerometer_raw()['z'])*100 <= 50:
                  #UP/position accelerometre_raw
                  if pion_y == 0:
                      pass
                  else:
                      s.set_pixel(pion_x,pion_y,(0,0,0))#eteinds la position precedente du pion
                      pion_y -= 1 #incremente la position du pion
                      if labyrinth[8*pion_y+pion_x] ==  G:
                        """gestion des murs"""
                        s.show_message("Wall",scroll_speed = 0.1)#affiche le message entre guillemet
                        pion_y += 1#incremente la position du pion
                        life -= 1#incremente les vie de -1
                        s.show_message("life : {}".format(life))#affiche le message entre guillemet
                        s.clear()#eteinds l ecran
              elif -50 <= int(s.get_accelerometer_raw()['x']*100) <= 50 and 50 <= int(s.get_accelerometer_raw()['y']*100) <= 150  and -50 <= int(s.get_accelerometer_raw()['z']*100) <= 50:
                  #DOWN/position accelerometre_raw
                  if pion_y == 7:
                    pass
                  else:
                    s.set_pixel(pion_x,pion_y,(0,0,0))#eteinds la position precedente du pion
                    pion_y += 1 #incremente la position du pion
                    if labyrinth[8*pion_y+pion_x] ==  G:
                      """gestion des murs"""
                      s.show_message("Wall",scroll_speed = 0.1)#affiche le message entre guillemet
                      pion_y -= 1#incremente la position du pion
                      life -= 1#incremente les vie de -1
                      s.show_message("life : {}".format(life))#affiche le message entre guillemet
                      s.clear()#eteinds l ecran
""" ----enigmaOne----"""

def circle():
  """dessine un cercle bleu a centre rouge sur l ecran"""
  B = Bleu
  O = Noir
  W = Blanc
  circleOne =[
     O, O, O, B, B, B, O, O,
     O, O, B, O, O, O, B, O,
     O, B, O, O, O, O, O, B,
     O, B, O, O, W, O, O, B,
     O, B, O, O, O, O, O, B,
     O, O, B, O, O, O, B, O,
     O, O, O, B, B, B, O, O,
     O, O, O, O, O, O, O, O,
     ]
  return circleOne

def enigmaGame(list):
  s.show_message("3,1415")#affiche le message entre guillemet
  R = Rouge
  Y = Jaune
  G = Vert
  W = Blanc
  state = { "pion_x" : 4,
          "pion_y" : 3,
          "pion_color" : R,}
  
  pion_x = state["pion_x"]
  pion_y = state["pion_y"]
  pion_color = state["pion_color"]
  
  s.set_pixels(list)
  s.set_pixel(pion_x,pion_y,pion_color)
  
  temp_list = []
  i=0
  while i < 8:
    if i == 7:
      s.show_message("Steps over")#affiche le message entre guillemet
      return False
    if temp_list == [(4, 4),(4, 5),(4, 6)] or temp_list == [(5, 3), (6, 3), (7, 3)] or temp_list == [(3, 3), (2, 3), (1, 3)] :
        #verifie que l user a bien trace le rayon
        return True
    else:
      event = s.stick.wait_for_event()#attends l evenement
      if event.action == "pressed":
        if event.direction == "right":#verifie l evenement
          if pion_x == 7:#gestion bordure
            pion_x = 0
          else:
            s.set_pixel(pion_x,pion_y,W)#laisse une trace derrierre le pion
            pion_x += 1#incremente la position du pion
            s.set_pixel(pion_x,pion_y,pion_color)#allume la nouvelle poisition du pion
            temp_list.append((pion_x,pion_y))#ajoute a la liste les position actuelle du pion
        if event.direction == "left":#verifie l evenement
          if pion_x == 0:#gestion bordure
            pion_x = 7
          else:
            s.set_pixel(pion_x,pion_y,W)#laisse une trace derrierre le pion
            pion_x -= 1 #incremente la position du pion
            s.set_pixel(pion_x,pion_y,pion_color)#allume la nouvelle poisition du pion
            temp_list.append((pion_x,pion_y))#ajoute a la liste les position actuelle du pion
        if event.direction == "up":#verifie l evenement
          if pion_y == 0:#gestion bordure
            pion_y =7
          else:
            s.set_pixel(pion_x,pion_y,W)#laisse une trace derrierre le pion
            pion_y -= 1 #incremente la position du pion
            s.set_pixel(pion_x,pion_y,pion_color)#allume la nouvelle poisition du pion
            temp_list.append((pion_x,pion_y))#ajoute a la liste les position actuelle du pion
        if event.direction == "down":#verifie l evenement
          if pion_y == 7:#gestion bordure
            pion_x = 0
          else:
            s.set_pixel(pion_x,pion_y,W)#laisse une trace derrierre le pion
            pion_y += 1 #incremente la position du pion
            s.set_pixel(pion_x,pion_y,pion_color)#allume la nouvelle poisition du pion
            temp_list.append((pion_x,pion_y))#ajoute a la liste les position actuelle du pion
      i +=1
            
"""------GuitarHeroMod-----"""

def guitarHeroList():
  """creer une liste contenant un melange successif des quatre positions de base"""
  list_move = ["up","down","left","right"]
  guitarHero_list = []
  for i in range(3):#creer une liste de 12 occurence (3*4)
    random.shuffle(list_move)#melange la liste
    for j in range(len(list_move)):
      guitarHero_list.append(list_move[j])#ajoute a la liste finale chaque occurence de la liste melangee
    
  return guitarHero_list

def LogoList():
    """creer la liste des quatre logos de base"""
    UpLogo=[
        O, O, O, R, R, O, O, O,
        O, O, R, R, R, R, O, O,
        O, R, R, R, R, R, R, O,
        O, O, O, R, R, O, O, O,
        O, O, O, R, R, O, O, O,
        O, O, O, R, R, O, O, O,
        O, O, O, R, R, O, O, O,
        O, O, O, R, R, O, O, O]
    DownLogo=[
        O, O, O, R, R, O, O, O,
        O, O, O, R, R, O, O, O,
        O, O, O, R, R, O, O, O,
        O, O, O, R, R, O, O, O,
        O, O, O, R, R, O, O, O,
        O, R, R, R, R, R, R, O,
        O, O, R, R, R, R, O, O,
        O, O, O, R, R, O, O, O]
    LeftLogo =[
        O, O, O, O, O, O, O, O,
        O, O, R, O, O, O, O, O,
        O, R, R, O, O, O, O, O,
        R, R, R, R, R, R, R, R,
        R, R, R, R, R, R, R, R,
        O, R, R, O, O, O, O, O,
        O, O, R, O, O, O, O, O,
        O, O, O, O, O, O, O, O]
    RightLogo = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, R, O, O,
        O, O, O, O, O, R, R, O,
        R, R, R, R, R, R, R, R,
        R, R, R, R, R, R, R, R,
        O, O, O, O, O, R, R, O,
        O, O, O, O, O, R, O, O,
        O, O, O, O, O, O, O, O]
    ListLogo = [UpLogo,DownLogo,LeftLogo,RightLogo]
    return ListLogo

def guitarHeroGame(list):
  """creer le jeu guitarHero a l'ecran
     et gere la jouabilitee
  """
  lst =[]#initialisation liste vide
  guitarHero_list = guitarHeroList()#initialisation liste mouvement
  for i in range(len(guitarHero_list)):#boucle nombre d'iteration = nombre d'occurence dan sla liste
    if guitarHero_list[i] == "up":#si la liste contient la string entre guillemet
      s.clear()#eteinds l'ecran
      time.sleep(0.5)#patiente 0.5sec
      s.set_pixels(list[0])#set l ecran su rle logo correspondant
      time.sleep(1.5)#patiente 1.5sec
      for event in s.stick.get_events():
          if event.action == "pressed":
              if event.direction == "up":#verifie l'evenement
                  if i == len(guitarHero_list)-1:
                      s.show_message("Level passed")#affiche le message entre guillemet
                      return True
                  else:
                      lst.append(event.direction)
                      continue
              else:
                  """gestion d erreur"""
                  s.show_message("Fail")#affiche le message entre guillemet
                  return False
    if guitarHero_list[i] == "down":#si la liste contient la string entre guillemet
      s.clear()#eteinds l'ecran
      time.sleep(0.5)#patiente 0.5sec
      s.set_pixels(list[1])#set l ecran su rle logo correspondant
      time.sleep(1.5)#patiente 1.5sec
      for event in s.stick.get_events():
          if event.action == "pressed":
              if event.direction == "down":#verifie l'evenement
                  if i == len(guitarHero_list)-1:
                      s.show_message("Level passed")#affiche le message entre guillemet
                      return True
                  else:
                      lst.append(event.direction)
                      continue
              else:
                  """gestion d erreur"""
                  s.show_message("Fail")#affiche le message entre guillemet
                  return False
    if guitarHero_list[i] == "right":#si la liste contient la string entre guillemet
      s.clear()#eteinds l'ecran
      time.sleep(0.5)#patiente 0.5sec
      s.set_pixels(list[3])#set l ecran su rle logo correspondant
      time.sleep(1.5)#patiente 1.5sec
      for event in s.stick.get_events():
          if event.action == "pressed":
              if event.direction == "right":#verifie l'evenement
                  if i == len(guitarHero_list)-1:
                      s.show_message("Level passed")#affiche le message entre guillemet
                      return True
                  else:
                      lst.append(event.direction)
                      continue
              else:
                  """gestion d erreur"""
                  s.show_message("Fail")#affiche le message entre guillemet
                  return False
    if guitarHero_list[i] == "left":#si la liste contient la string entre guillemet
      s.clear()#eteinds l'ecran
      time.sleep(0.5)#patiente 0.5sec
      s.set_pixels(list[2])#set l ecran su rle logo correspondant
      time.sleep(1.5)#patiente 1.5sec
      for event in s.stick.get_events():
          if event.action == "pressed":
              if event.direction == "left":#verifie l'evenement
                  if i == len(guitarHero_list)-1:
                      s.show_message("Level passed")#affiche le message entre guillemet
                      return True
                  else:
                      lst.append(event.direction)
                      continue
              else:
                  """gestion d erreur"""
                  s.show_message("Fail")#affiche le message entre guillemet
                  return False
    """gestion manque une action dans le delais"""
    if len(lst) == 0 and i != 0:
        s.show_message("Miss an action")#affiche le message entre guillemet
        return False
    if len(lst)-1 != i:
        s.show_message("Miss an action")#affiche le message entre guillemet
        return False
            
"""-----DonkeyKong-----"""
def grille():
  G = Vert
  O = Noir
    
  grille1 =[
    O, O, O, O, O, O, O, G,
    O, O, O, O, O, O, O, G,
    O, O, O, O, O, O, O, G,
    O, O, O, O, O, O, O, G,
    O, O, O, O, O, O, O, G,
    O, O, O, O, O, O, O, G,
    O, O, O, O, O, O, O, G,
    O, O, O, O, O, O, O, G,
     ]
  return grille1

def DonkeyKong(list):
    """Creer un jeu d evitement de boules rouge affiche sur l ecran"""
  R = Rouge
  G = Vert
  B = Bleu
  
  state = { "pion_x" : 0,#position pion depart x
          "pion_y" : 0,#position pion depart y
          "pion_color" : B,#couleurs pion 
          "arrival_x" : 7,#ligne d'arrivee
          "arrival_y" : 7,#non utilise /sans imortance
          "arrival_color" :G,#couleur arrivee
          "ennemy_x" : 5,
          "ennemy_y" : 0,
          "ennemy_color" : R}
  
  pion_x = state["pion_x"]
  pion_y = state["pion_y"]
  pion_color = state["pion_color"]
  arrival_x = state["arrival_x"]
  arrival_y = state["arrival_y"]
  arrival_color = state["arrival_color"]
  ennemy_x = state["ennemy_x"]
  ennemy_y = state["ennemy_y"]
  ennemy_color = state["ennemy_color"]
  ogre_x = 1
  ogre_y = 3
  ogre_color = R
  polo_x = 3
  polo_y = 6
  polo_color = R
  
  s.set_pixels(list)
  s.set_pixel(pion_x,pion_y,pion_color)
  s.set_pixel(arrival_x,arrival_y,arrival_color)
  s.set_pixel(ennemy_x,ennemy_y,ennemy_color)
  s.set_pixel(ogre_x,ogre_y,ogre_color)
  s.set_pixel(polo_x,polo_y,polo_color)
      
  while True:#boucle 200 iteration
      """corps de jeu"""
    if ennemy_y < 8:
      s.set_pixel(ennemy_x,ennemy_y,(0,0,0))#eteinds position precedente
      ennemy_y = random.randint(0,7)#set up position aleatoire 
      if ennemy_y == 3:#porte derobe
          ennemy_y += 1
      s.set_pixel(ennemy_x,ennemy_y,ennemy_color)
    if ogre_y < 8:
      s.set_pixel(ogre_x,ogre_y,(0,0,0))#eteinds position precedente
      ogre_y = random.randint(0,7)#set up position aleatoire 
      if ogre_y == 5:#porte derobe
          ogre_y += 1
      s.set_pixel(ogre_x,ogre_y,ogre_color)
    if polo_y < 8:
      s.set_pixel(polo_x,polo_y,(0,0,0))#eteinds position precedente
      polo_y = random.randint(0,7)#set up position aleatoire 
      if polo_y == 2:#porte derobee
          polo_y += 1
      s.set_pixel(polo_x,polo_y,polo_color)
      """gestion rencontre enemis"""
    if pion_x == ennemy_x and pion_y == ennemy_y:
      s.show_message("RIP")
      return False
    elif pion_x == ogre_x and pion_y == ogre_y:
      s.show_message("RIP")
      return False
    elif pion_x == polo_x and pion_y == polo_y:
      s.show_message("RIP")
      return False
    elif i == 199:
      s.show_message("Steps over")
      return False
    """gestion arrivee"""
    elif pion_x == arrival_x:
      s.show_message('Nice job')
      return True
    else:
      event = s.stick.wait_for_event()#attends l evenement
      if event.action == "pressed":#verifie l'evenement
        if event.direction == "right":#verifie l'evenement
          if pion_x == 7:
            pass
          else:
            s.set_pixel(pion_x,pion_y,(0,0,0))#eteinds position precedente
            pion_x += 1#incremente position pion
            s.set_pixel(pion_x,pion_y,pion_color)#set position pion new
        if event.direction == "left":#verifie l'evenement
          if pion_x == 0:
            pass
          else:
            s.set_pixel(pion_x,pion_y,(0,0,0))#eteinds position precedente
            pion_x -= 1#incremente position pion 
            s.set_pixel(pion_x,pion_y,pion_color)#set position pion new
        if event.direction == "up":#verifie l'evenement
          if pion_y == 0:
            pass
          else:
            s.set_pixel(pion_x,pion_y,(0,0,0))#eteinds position precedente
            pion_y -= 1 #incremente position pion
            s.set_pixel(pion_x,pion_y,pion_color)#set position pion new
        if event.direction == "down":#verifie l'evenement
          if pion_y == 7:
            pass
          else:
            s.set_pixel(pion_x,pion_y,(0,0,0))#eteinds position precedente
            pion_y += 1 #incremente position pion
            s.set_pixel(pion_x,pion_y,pion_color)#set position pion new
    i+=1#incremente nombre de pas
    

"""-----Grand labyrinthe-----"""
def labyrinth_List():
  """Liste des cartes des labyrinth"""
  G = Vert
  O = Noir
  Y = Jaune
  R = Rouge
    
  labyrinthOne =[
    G, G, G, G, G, G, G, G,
    G, O, O, O, O, O, G, G,
    G, G, G, G, O, O, G, G,
    G, O, O, O, O, O, O, O,
    G, O, O, G, G, G, G, O,
    G, G, O, O, O, O, G, G,
    G, G, G, O, G, O, B, G,
    G, G, G, O, O, G, G, G,
     ]
  labyrinthTwo =[
    G, G, G, G, G, G, G, G,
    G, G, O, O, O, O, G, G,
    G, G, O, O, O, G, G, G,
    O, G, G, G, O, G, O, O,
    O, O, O, O, O, O, O, O,
    G, O, G, G, G, O, G, G,
    G, O, G, G, O, O, G, G,
    G, G, G, O, O, G, G, G,
     ]
  labyrinthThree =[
    G, G, G, G, G, G, G, G,
    G, O, G, G, G, G, O, G,
    G, O, G, O, G, O, G, G,
    O, O, O, O, G, O, O, O,
    O, O, O, G, G, O, G, O,
    G, O, O, G, O, O, O, G,
    G, G, O, O, O, G, G, G,
    G, G, G, O, O, G, G, G,
     ]
  labyrinthFour =[
    G, G, G, G, G, G, G, G,
    G, G, O, O, O, O, O, G,
    G, O, G, O, G, G, O, G,
    O, O, G, O, O, O, G, O,
    O, O, O, G, G, O, O, O,
    G, O, O, O, O, O, G, G,
    G, O, G, G, O, O, G, G,
    G, G, G, O, O, G, G, G,
     ]
  labyrinthFive =[
    G, G, G, G, G, G, G, G,
    G, O, G, G, O, O, G, G,
    G, O, O, O, G, O, G, G,
    O, O, G, O, G, O, O, O,
    O, O, G, O, O, O, G, O,
    G, O, O, O, G, G, G, G,
    G, G, G, O, O, O, G, G,
    G, G, G, O, O, G, G, G,
     ]
  labyrinthSix =[
    G, G, G, G, G, G, G, G,
    G, O, O, G, O, G, O, G,
    G, G, O, O, O, O, O, G,
    O, G, O, G, O, G, O, O,
    O, O, O, G, G, O, O, O,
    G, O, O, O, G, O, G, G,
    G, O, G, G, O, O, O, G,
    G, G, G, O, O, G, G, G,
     ]
  labyrinthSeven =[
    G, G, G, G, G, G, G, G,
    G, G, O, G, G, G, G, G,
    G, O, O, O, O, O, G, G,
    O, O, O, G, G, O, G, O,
    O, G, O, G, G, O, O, O,
    G, O, O, O, O, G, G, G,
    G, G, G, G, G, G, G, G,
    G, G, G, O, O, G, G, G,
     ]
  labyrinthEight =[
    G, G, G, G, G, G, G, G,
    G, G, O, G, G, G, O, G,
    G, G, O, O, O, O, G, G,
    O, G, O, G, G, G, O, G,
    O, O, O, O, G, G, O, G,
    G, O, O, O, G, O, O, G,
    G, G, O, O, G, O, G, G,
    G, G, G, O, O, G, G, G,
     ]
  labyrinthNine =[
    G, G, G, O, O, G, G, G,
    G, O, O, O, O, G, B, G,
    G, O, G, G, O, G, O, G,
    G, O, O, G, G, G, O, O,
    G, O, O, G, O, O, O, O,
    G, O, O, O, O, O, G, G,
    G, G, O, O, O, G, O, G,
    G, G, G, O, O, G, G, G,
     ]
  labyrinthTen =[
    G, G, G, O, O, G, G, G,
    G, O, G, O, G, G, G, G,
    G, G, G, O, O, O, G, G,
    O, O, O, O, G, O, O, O,
    O, O, G, O, G, G, O, O,
    G, O, O, O, O, G, O, G,
    G, G, O, G, G, G, O, G,
    G, G, G, O, O, G, G, G,
     ]
  labyrinthEleven =[
    G, G, G, O, O, G, G, G,
    G, G, O, O, G, G, O, G,
    G, G, G, O, G, O, O, G,
    O, O, O, O, O, G, O, O,
    O, G, O, O, O, O, O, O,
    G, G, O, O, G, O, G, G,
    G, O, O, O, G, O, G, G,
    G, G, G, O, O, G, G, G,
     ]
  labyrinthTwelve =[
    G, G, G, O, O, G, G, G,
    G, G, O, O, G, O, O, G,
    G, O, O, O, O, G, O, G,
    O, O, G, G, O, G, O, O,
    O, O, O, G, O, O, O, O,
    G, O, G, O, G, G, O, G,
    G, O, G, O, O, G, O, G,
    G, G, G, O, O, G, G, G,
     ]
  labyrinthThirTeen =[
    G, G, G, O, O, G, G, G,
    G, O, O, G, O, O, G, G,
    G, G, O, G, G, O, G, G,
    O, O, O, G, O, O, O, O,
    O, G, O, G, G, G, O, O,
    G, G, O, O, O, O, O, G,
    G, O, O, G, G, G, O, G,
    G, G, G, O, O, G, G, G,
     ]
  labyrinthFourTeen =[
    G, G, G, O, O, G, G, G,
    G, G, G, O, O, G, G, G,
    G, O, O, O, O, O, O, G,
    O, O, G, G, G, G, O, O,
    O, O, O, G, O, O, O, O,
    G, G, O, O, G, O, O, G,
    G, G, O, G, G, O, O, G,
    G, G, G, O, O, G, G, G,
     ]
  labyrinthFifTeen =[
    G, G, G, O, O, G, G, G,
    G, G, G, O, G, G, G, G,
    G, O, O, O, O, G, G, G,
    O, G, G, G, O, O, O, O,
    O, O, O, O, O, O, G, O,
    G, O, O, O, G, O, O, G,
    G, O, G, G, G, O, O, G,
    G, G, G, O, O, G, G, G,
     ]
  labyrinthSixTeen =[
    G, G, G, O, O, G, G, G,
    G, G, O, O, O, G, B, G,
    G, G, O, G, O, G, O, G,
    O, O, O, G, O, O, O, G,
    O, G, G, G, O, G, G, G,
    G, O, O, O, O, O, O, G,
    G, G, O, G, G, G, G, G,
    G, G, G, O, O, G, G, G,
     ]
  labyrinthSevenTeen =[
    G, G, G, O, O, G, G, G,
    G, O, G, O, O, G, O, G,
    G, O, G, O, O, O, O, G,
    G, G, G, O, O, G, G, O,
    G, O, O, O, G, O, O, O,
    G, O, G, O, O, O, G, G,
    G, G, G, G, O, O, G, G,
    G, G, G, O, O, G, G, G,
     ]
  labyrinthEighTeen =[
    G, G, G, O, O, G, G, G,
    G, O, G, O, G, G, O, G,
    G, O, O, O, G, O, O, G,
    O, O, O, G, G, O, G, O,
    O, G, O, G, O, O, G, O,
    G, G, O, O, O, O, O, G,
    G, O, O, G, G, G, O, G,
    G, G, G, O, O, G, G, G,
     ]
  labyrinthNineTeen =[
    G, G, G, O, O, G, G, G,
    G, O, G, O, G, O, O, G,
    G, O, G, O, O, O, G, G,
    O, G, O, G, O, O, O, O,
    O, O, O, O, O, G, O, O,
    G, O, G, G, O, G, G, G,
    G, O, O, G, O, O, O, G,
    G, G, G, O, O, G, G, G,
     ]
  labyrinthTwenty =[
    G, G, G, O, O, G, G, G,
    G, G, O, G, G, G, O, G,
    G, G, O, O, G, O, O, G,
    O, G, O, O, G, G, G, O,
    O, O, G, O, O, O, O, O,
    G, O, G, O, O, G, G, G,
    G, O, G, G, O, G, G, G,
    G, G, G, O, O, G, G, G,
      ]
  labyrinthTwentyOne =[
    G, G, G, O, O, G, G, G,
    G, G, G, G, O, G, G, G,
    G, O, O, O, O, O, O, G,
    O, O, G, O, G, O, O, O,
    O, O, G, G, G, O, G, O,
    G, O, O, O, O, O, O, G,
    G, O, G, G, G, O, G, G,
    G, G, G, O, O, G, G, G,
     ]
  labyrinthTwentyTwo =[
    G, G, G, O, O, G, G, G,
    G, G, O, O, G, G, O, G,
    G, O, O, G, O, O, O, G,
    O, G, G, O, O, G, G, O,
    O, O, O, O, G, G, O, O,
    G, O, G, O, G, G, O, G,
    G, O, G, O, O, O, O, G,
    G, G, G, O, O, G, G, G,
      ]
  labyrinthTwentyThree =[
    G, G, G, O, O, G, G, G,
    G, G, O, O, O, O, O, G,
    G, O, O, O, G, G, O, G,
    O, O, G, O, G, O, O, O,
    O, O, G, O, O, O, O, O,
    G, G, G, O, G, G, O, G,
    G, O, G, O, O, O, O, G,
    G, G, G, O, O, G, G, G,
      ]
  labyrinthTwentyFour =[
    G, G, G, O, O, G, G, G,
    G, O, G, O, G, G, O, G,
    G, O, O, O, O, O, O, G,
    O, G, G, O, G, O, O, G,
    O, O, O, G, G, G, O, G,
    G, G, O, O, O, O, G, G,
    G, O, G, G, G, O, G, G,
    G, G, G, O, O, G, G, G,
      ]
  labyrinthTwentyFive =[
    G, G, G, O, O, G, G, G,
    G, O, O, O, O, O, G, G,
    G, O, G, G, G, O, G, G,
    G, O, O, O, G, O, O, O,
    G, O, O, G, G, G, O, O,
    G, G, O, G, O, O, O, G,
    G, G, O, O, O, O, G, G,
    G, G, G, O, O, G, G, G,
      ]
  labyrinthTwentySix =[
    G, G, G, O, O, G, G, G,
    G, O, O, O, O, O, O, G,
    G, O, O, G, G, O, O, G,
    O, O, G, O, G, O, G, O,
    O, O, G, O, O, O, O, O,
    G, O, O, G, G, O, O, G,
    G, O, O, O, O, O, O, G,
    G, G, G, O, O, G, G, G,
      ]
  labyrinthTwentySeven =[
    G, G, G, O, O, G, G, G,
    G, O, O, G, O, O, G, G,
    G, G, G, G, O, G, O, G,
    O, O, O, O, O, O, O, O,
    O, G, O, G, G, G, O, O,
    G, G, O, O, O, O, G, G,
    G, G, O, G, G, O, G, G,
    G, G, G, O, O, G, G, G,
      ]
  labyrinthTwentyEight =[
    G, G, G, O, O, G, G, G,
    G, G, O, O, O, O, G, G,
    G, O, O, O, O, G, O, G,
    O, O, G, O, O, G, O, O,
    O, O, O, O, G, O, O, O,
    G, G, G, O, O, O, G, G,
    G, G, O, G, G, O, G, G,
    G, G, G, O, O, G, G, G,
     ]
  labyrinthTwentyNine =[
    G, G, G, O, O, G, G, G,
    G, O, G, O, G, O, O, G,
    G, O, O, O, G, G, O, G,
    O, G, O, O, O, O, O, O,
    O, O, O, G, O, G, G, O,
    G, O, G, G, O, O, G, G,
    G, B, G, O, O, O, O, G,
    G, G, O, O, O, G, G, G,
      ]
  labyrinthThirty =[
    G, G, G, O, O, G, G, G,
    G, O, G, O, G, G, O, G,
    G, O, G, O, G, O, O, G,
    O, G, G, G, G, G, O, O,
    O, G, O, O, O, G, O, O,
    G, O, O, G, O, O, O, G,
    G, O, O, G, O, G, O, G,
    G, G, G, O, O, G, G, G,
      ]
  labyrinthThirtyOne =[
    G, G, G, O, O, G, G, G,
    G, O, O, G, O, O, O, G,
    G, G, O, G, G, O, G, G,
    O, G, O, G, G, O, O, O,
    O, O, O, O, G, G, G, O,
    G, G, G, O, O, O, O, G,
    G, G, O, O, G, G, O, G,
    G, G, G, O, O, G, G, G,
      ]
  labyrinthThirtyTwo =[
    G, G, G, O, O, G, G, G,
    G, O, G, O, G, O, G, G,
    G, G, O, O, O, O, O, G,
    O, G, O, G, G, O, G, G,
    O, G, O, G, O, O, O, G,
    G, O, O, O, O, G, G, G,
    G, G, O, O, G, G, O, G,
    G, G, G, O, O, G, G, G,
      ]
  labyrinthThirtyThree =[
    G, G, G, O, O, G, G, G,
    G, G, G, G, O, O, G, G,
    G, G, G, O, O, O, G, G,
    G, O, O, O, G, O, O, O,
    G, O, G, G, G, G, O, O,
    G, O, O, O, O, G, O, G,
    G, G, G, G, O, G, G, G,
    G, G, G, O, O, G, G, G,
     ]
  labyrinthThirtyFour =[
    G, G, G, O, O, G, G, G,
    G, O, G, G, O, G, O, G,
    G, O, G, O, O, G, O, G,
    O, O, G, G, O, O, O, O,
    O, O, O, O, O, O, G, O,
    G, G, G, O, G, O, G, G,
    G, O, O, O, G, O, O, G,
    G, G, G, O, O, G, G, G,
      ]
  labyrinthThirtyFive =[
    G, G, G, O, O, G, G, G,
    G, G, O, G, G, O, G, G,
    G, O, O, O, G, O, G, G,
    O, O, G, O, G, O, G, O,
    O, G, G, O, O, O, G, O,
    G, O, G, G, O, O, O, G,
    G, G, O, O, O, G, O, G,
    G, G, G, O, O, G, G, G,
      ]
  labyrinthThirtySix =[
    G, G, G, O, O, G, G, G,
    G, O, G, O, G, B, G, G,
    G, O, O, O, O, O, O, G,
    O, G, G, O, G, G, O, O,
    O, O, O, O, O, G, O, O,
    G, G, G, G, O, O, O, G,
    G, G, O, O, O, G, G, G,
    G, G, G, O, O, G, G, G,
      ]
  labyrinthThirtySeven =[
    G, G, G, O, O, G, G, G,
    G, O, O, O, O, O, G, G,
    G, O, G, G, G, O, O, G,
    O, G, O, O, G, O, G, O,
    O, O, G, O, O, O, O, O,
    G, O, G, O, G, G, O, G,
    G, O, O, O, G, G, O, G,
    G, G, G, O, O, G, G, G,
      ]
  labyrinthThirtyEight =[
    G, G, G, O, O, G, G, G,
    G, G, O, G, G, O, O, G,
    G, G, O, G, O, O, G, G,
    O, O, O, O, G, O, O, O,
    O, G, G, O, G, O, G, O,
    G, O, G, G, O, O, G, G,
    G, O, O, O, O, G, G, G,
    G, G, G, O, O, G, G, G,
      ]
  labyrinthThirtyNine =[
    G, G, G, O, O, G, G, G,
    G, G, O, O, O, O, O, G,
    G, O, O, G, G, O, G, G,
    O, G, O, G, O, O, O, O,
    O, O, O, G, G, O, O, O,
    G, G, O, O, O, G, O, G,
    G, G, G, G, O, G, G, G,
    G, G, G, O, O, G, G, G,
      ]
  labyrinthFourty =[
    G, G, G, O, O, G, G, G,
    G, O, G, O, G, O, G, G,
    G, G, O, O, O, G, O, G,
    O, G, O, G, O, G, O, G,
    O, O, O, G, G, G, G, G,
    G, G, O, O, O, G, O, G,
    G, G, G, G, O, O, O, G,
    G, G, G, O, O, G, G, G,
      ]
  labyrinthFourtyOne =[
    G, G, G, O, O, G, G, G,
    G, G, G, O, G, G, G, G,
    G, O, O, O, O, O, O, G,
    G, O, G, G, G, Y, O, O,
    G, O, O, G, O, O, G, O,
    G, G, O, O, O, O, G, G,
    G, G, O, O, G, O, O, G,
    G, G, G, O, O, G, G, G,
      ]
  labyrinthFourtyTwo =[
    G, G, G, O, O, G, G, G,
    G, O, O, G, O, G, G, G,
    G, O, O, O, O, O, O, G,
    O, O, G, G, G, G, O, O,
    O, G, G, O, O, G, G, O,
    G, G, O, O, O, O, O, G,
    G, G, O, O, G, O, O, G,
    G, G, G, O, O, G, G, G,
      ]
  labyrinthFourtyThree =[
    G, G, G, O, O, G, G, G,
    G, O, O, G, O, O, O, G,
    G, O, O, O, G, G, O, G,
    O, G, G, O, G, O, G, O,
    O, O, O, O, G, O, O, O,
    G, O, G, G, G, G, O, G,
    G, O, O, G, O, O, O, G,
    G, G, G, O, O, G, G, G,
      ]
  labyrinthFourtyFour =[
    G, G, G, O, O, G, G, G,
    G, O, G, G, O, O, O, G,
    G, G, G, G, O, O, G, G,
    O, G, O, O, O, G, G, O,
    O, G, O, G, O, O, O, O,
    G, G, O, O, G, O, G, G,
    G, G, G, O, G, O, G, G,
    G, G, G, O, O, G, G, G,
      ]
  labyrinthFourtyFive =[
    G, G, G, O, O, G, G, G,
    G, G, O, G, O, O, G, G,
    G, O, O, G, G, O, O, G,
    O, G, O, O, O, O, O, O,
    O, G, G, O, G, G, O, O,
    G, G, O, O, G, O, O, G,
    G, O, O, O, G, O, O, G,
    G, G, G, O, O, G, G, G,
      ]
  labyrinthFourtySix =[
    G, G, G, O, O, G, G, G,
    G, O, O, O, O, G, O, G,
    G, G, O, G, G, G, O, G,
    O, O, O, O, O, O, O, O,
    O, G, O, G, O, G, O, O,
    G, O, O, G, O, O, O, G,
    G, O, O, G, G, O, G, G,
    G, G, G, O, O, G, G, G,
      ]
  labyrinthFourtySeven =[
    G, G, G, O, O, G, G, G,
    G, G, O, G, G, O, B, G,
    G, O, O, G, O, O, G, G,
    O, G, O, O, O, G, G, O,
    O, O, G, G, O, O, O, O,
    G, O, O, O, O, G, G, G,
    G, G, O, O, G, G, O, G,
    G, G, G, O, O, G, G, G,
      ]
  labyrinthFourtyEight =[
    G, G, G, O, O, G, G, G,
    G, G, O, G, G, G, O, G,
    G, O, G, O, G, O, O, G,
    O, O, O, O, O, O, O, G,
    O, O, O, G, O, G, G, G,
    G, O, G, O, O, O, O, G,
    G, G, G, O, G, G, O, G,
    G, G, G, O, O, G, G, G,
      ]
  labyrinthFourtyNine =[
    G, G, G, O, O, G, G, G,
    G, G, G, O, G, G, G, G,
    G, O, O, O, O, O, O, G,
    G, G, O, O, G, G, O, O,
    G, O, O, O, G, O, G, O,
    G, G, G, O, G, G, G, G,
    G, G, O, O, O, O, G, G,
    G, G, G, O, O, G, G, G,
      ]
  labyrinthFifty =[
    G, G, G, O, O, G, G, G,
    G, O, O, O, O, O, G, G,
    G, G, G, G, G, O, G, G,
    O, G, O, O, O, O, O, O,
    O, G, G, O, G, G, O, O,
    G, G, O, O, O, G, O, G,
    G, G, G, G, O, O, G, G,
    G, G, G, O, O, G, G, G,
      ]
  labyrinthFiftyOne =[
    G, G, G, O, O, G, G, G,
    G, G, G, G, O, O, G, G,
    G, O, O, G, O, O, O, G,
    O, G, O, G, O, G, G, O,
    O, G, O, O, O, O, O, O,
    G, G, G, O, G, G, O, G,
    G, G, O, O, G, O, O, G,
    G, G, G, O, O, G, G, G,
      ]
  labyrinthFiftyTwo =[
    G, G, G, O, O, G, G, G,
    G, O, O, O, O, O, G, G,
    G, O, G, G, G, O, G, G,
    O, G, O, O, G, O, O, O,
    O, G, O, O, O, O, O, O,
    G, G, G, O, G, O, G, G,
    G, O, O, O, O, O, G, G,
    G, G, G, O, O, G, G, G,
      ]
  labyrinthFiftyThree =[
    G, G, G, O, O, G, G, G,
    G, O, G, O, O, O, O, G,
    G, O, O, G, G, O, G, G,
    O, O, O, O, O, O, O, O,
    O, G, O, O, G, G, O, O,
    G, O, O, O, G, O, O, G,
    G, O, G, G, G, O, G, G,
    G, G, G, O, O, G, G, G,
     ]
  labyrinthFiftyFour =[
    G, G, G, O, O, G, G, G,
    G, O, G, O, G, G, O, G,
    G, G, G, O, O, G, O, G,
    O, O, O, O, O, G, G, O,
    O, G, G, G, O, O, O, O,
    G, O, G, G, G, O, G, G,
    G, G, O, O, O, O, G, G,
    G, G, G, O, O, G, G, G,
      ]
  labyrinthFiftyFive =[
    G, G, G, O, O, G, G, G,
    G, O, O, O, O, O, G, G,
    G, O, G, O, G, O, G, G,
    O, G, O, O, G, O, O, O,
    O, G, O, G, G, O, O, O,
    G, O, O, O, O, O, G, G,
    G, G, O, G, G, O, G, G,
    G, G, G, O, O, G, G, G,
      ]
  labyrinthFiftySix =[
    G, G, G, O, O, G, G, G,
    G, O, O, G, O, O, O, G,
    G, G, O, O, O, G, G, G,
    O, G, G, O, G, O, O, G,
    O, G, O, O, G, O, G, G,
    G, G, O, G, G, O, G, G,
    G, O, O, O, O, O, O, G,
    G, G, G, O, O, G, G, G,
      ]
  labyrinthFiftySeven =[
    G, G, G, O, O, G, G, G,
    G, G, O, O, O, G, G, G,
    G, O, O, G, O, O, O, G,
    G, G, G, O, O, G, O, O,
    G, G, G, O, O, G, O, O,
    G, G, O, G, O, O, O, G,
    G, O, O, G, O, G, G, G,
    G, G, G, G, G, G, G, G,
      ]
  labyrinthFiftyEight =[
    G, G, G, O, O, G, G, G,
    G, G, O, O, G, O, O, G,
    G, G, O, G, G, O, G, G,
    O, O, O, G, O, O, O, O,
    O, G, O, G, G, G, O, O,
    G, O, O, O, O, G, O, G,
    G, G, G, G, O, O, O, G,
    G, G, G, G, G, G, G, G,
      ]
  labyrinthFiftyNine =[
    G, G, G, O, O, G, G, G,
    G, G, O, O, O, O, G, G,
    G, O, G, G, G, O, O, G,
    O, O, G, O, O, G, O, O,
    O, O, G, G, O, G, G, O,
    G, O, O, O, O, O, O, G,
    G, G, G, G, G, G, O, G,
    G, G, G, G, G, G, G, G,
      ]
  labyrinthSixty =[
    G, G, G, O, O, G, G, G,
    G, G, O, G, O, O, G, G,
    G, O, O, G, G, O, O, G,
    O, G, O, O, O, O, O, O,
    O, O, O, G, G, O, O, O,
    G, G, O, O, O, O, G, G,
    G, G, O, G, G, O, G, G,
    G, G, G, G, G, G, G, G,
      ]
  labyrinthSixtyOne =[
    G, G, G, O, O, G, G, G,
    G, G, O, G, O, G, O, G,
    G, O, O, G, O, G, O, G,
    O, G, O, O, O, G, O, O,
    O, O, O, O, O, O, O, O,
    G, O, G, O, G, O, O, G,
    G, G, O, O, O, G, O, G,
    G, G, G, G, G, G, G, G,
      ]
  labyrinthSixtyTwo =[
    G, G, G, O, O, G, G, G,
    G, G, O, O, O, O, G, G,
    G, G, O, G, G, O, O, G,
    O, O, O, G, G, G, G, O,
    O, G, O, G, G, O, O, O,
    G, O, O, O, O, G, O, G,
    G, O, G, G, O, O, O, G,
    G, G, G, G, G, G, G, G,
      ]
  labyrinthSixtyThree =[
    G, G, G, O, O, G, G, G,
    G, G, O, G, O, O, O, G,
    G, O, O, O, G, O, G, G,
    O, G, G, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    G, G, O, O, G, G, O, G,
    G, O, G, O, O, G, G, G,
    G, G, G, G, G, G, G, G,
      ]
  labyrinthSixtyFour =[
    G, G, G, O, O, G, G, G,
    G, G, G, G, O, O, O, G,
    G, G, O, O, G, G, O, G,
    O, O, G, O, O, O, G, G,
    O, O, O, O, G, O, G, G,
    G, G, O, G, O, O, O, G,
    G, G, G, G, G, G, O, G,
    G, G, G, G, G, G, G, G,
         ]
  laby = [labyrinthOne, labyrinthTwo, labyrinthThree, labyrinthFour, labyrinthFive, labyrinthSix, labyrinthSeven, labyrinthEight, labyrinthNine, labyrinthTen, labyrinthEleven, labyrinthTwelve, labyrinthThirTeen, labyrinthFourTeen, labyrinthFifTeen, labyrinthSixTeen, labyrinthSevenTeen, labyrinthEighTeen, labyrinthNineTeen, labyrinthTwenty, labyrinthTwentyOne, labyrinthTwentyTwo, labyrinthTwentyThree, labyrinthTwentyFour, labyrinthTwentyFive, labyrinthTwentySix, labyrinthTwentySeven, labyrinthTwentyEight, labyrinthTwentyNine, labyrinthThirty, labyrinthThirtyOne, labyrinthThirtyTwo, labyrinthThirtyThree, labyrinthThirtyFour, labyrinthThirtyFive, labyrinthThirtySix, labyrinthThirtySeven, labyrinthThirtyEight, labyrinthThirtyNine, labyrinthFourty, labyrinthFourtyOne, labyrinthFourtyTwo, labyrinthFourtyTwo, labyrinthFourtyThree, labyrinthFourtyFour, labyrinthFourtyFive, labyrinthFourtySix, labyrinthFourtySeven, labyrinthFourtyEight, labyrinthFourtyNine, labyrinthFifty, labyrinthFiftyOne, labyrinthFiftyTwo, labyrinthFiftyThree, labyrinthFiftyFour, labyrinthFiftyFive, labyrinthFiftySix, labyrinthFiftySeven, labyrinthFiftyEight, labyrinthFiftyNine, labyrinthSixty, labyrinthSixtyOne, labyrinthSixtyTwo, labyrinthSixtyThree, labyrinthSixtyFour]
  return laby

def labyrinthBigGame(list,x):
  R = Rouge
  Y = Jaune
  G = Vert
  state = { "pion_x" : 1,
          "pion_y" : 1,
          "pion_color" : R}
  
  pion_x =state["pion_x"]
  pion_y=state["pion_y"]
  pion_color=state["pion_color"]
  life = x
  s.show_message("life : {}".format(life))#affiche le message entre guillemet
  z=0
  i=0
  while True:
    z+=1
    if life == 0:
      s.show_message("Game Over",scroll_speed = 0.1)#affiche le message entre guillemet
      return False
    if z == 1000:
      s.show_message("Steps over")#affiche le message entre guillemet
      pion_y = state["pion_y"]
      pion_x = state["pion_x"]
      s.set_pixels(list[0])
      life -= 1
      s.show_message("life : {}".format(life))
      z = 0
      s.clear()#eteinds l'ecran
      
    else:
      s.set_pixels(list[i])#set l'ecran sur la carte chosisie
      s.set_pixel(pion_x,pion_y,pion_color)#set le pion sur sa position
      labyrinth = list[i]
      if labyrinth[8*pion_y+pion_x] == Y  :
        s.show_message("Level passed")#affiche le message entre guillemet
        return True
      else:
        event = s.stick.wait_for_event()
        if event.action == "pressed":
          if event.direction == "right":
            if pion_x == 7:
              if i in {0,1,2,3,4,5,6,8,9,10,11,12,13,14,16,17,18,19,20,21,22,24,25,26,27,28,29,30,32,33,34,35,36,37,38,40,41,42,43,44,45,46,48,49,50,51,52,53,54,56,57,58,59,60,61,62}:
                i+=1
                pion_x = 0
              else :
                pass
            else:
              s.set_pixel(pion_x,pion_y,(0,0,0))#eteinds la position precedente du pions
              pion_x += 1#incremente la position du pion de 1
              if labyrinth[8*pion_y+pion_x] ==  G:
                """gestion des murs"""
                s.show_message("Wall",scroll_speed = 0.1)
                pion_x -= 1
                life -= 1
                s.show_message("life : {}".format(life))
                s.clear()
              elif labyrinth[8*pion_y+pion_x] ==  B :
                  """teleporteur"""
                if i == 0 :
                  i+= 35#set carte
                  pion_x = 5#set position pion
                  pion_y = 1#set position pion
                elif i == 35 :
                  i-= 35#set carte
                  pion_x = 6#set position pion
                  pion_y = 6#set position pion
                elif i == 8 :
                  i+= 7#set carte
                  pion_x = 6#set position pion
                  pion_y = 1#set position pion
                elif i == 15 :
                  i-= 7#set carte
                  pion_x = 6#set position pion
                  pion_y = 1#set position pion
                elif i == 28 :
                  i+= 18#set carte
                  pion_x = 6#set position pion
                  pion_y = 1#set position pion
                elif i == 46 :
                  i-= 18#set carte
                  pion_x = 1#set position pion
                  pion_y = 6#set position pion
          if event.direction == "left":
            if pion_x == 0:
              if i in {1,2,3,4,5,6,7,9,10,11,12,13,14,15,17,18,19,20,21,22,23,25,26,27,28,29,30,31,33,34,35,36,37,38,39,41,42,43,44,45,46,47,49,50,51,52,53,54,55,57,58,59,60,61,62,63}:
                  i-=1
                  pion_x = 7
              else :
                pass
            else:
              s.set_pixel(pion_x,pion_y,(0,0,0))
              pion_x -= 1
              if labyrinth[8*pion_y+pion_x] ==  G:
                """gestion des murs"""
                s.show_message("Wall",scroll_speed = 0.1)
                pion_x += 1#incremente la position du pion de 1
                life -= 1
                s.show_message("life : {}".format(life))
                s.clear()
              elif labyrinth[8*pion_y+pion_x] ==  B :
                  """teleporteur"""
                if i == 0 :
                  i+= 35#set carte
                  pion_x = 5#set position pion
                  pion_y = 1#set position pion
                elif i == 35 :
                  i-= 35#set carte
                  pion_x = 6#set position pion
                  pion_y = 6#set position pion
                elif i == 8 :
                  i+= 7#set carte
                  pion_x = 6#set position pion
                  pion_y = 1#set position pion
                elif i == 15 :
                  i-= 7#set carte
                  pion_x = 6#set position pion
                  pion_y = 1#set position pion
                elif i == 28 :
                  i+= 18#set carte
                  pion_x = 6#set position pion
                  pion_y = 1#set position pion
                elif i == 46 :
                  i-= 18#set carte
                  pion_x = 1#set position pion
                  pion_y = 6#set position pion  
          if event.direction == "up":
            if pion_y == 0:
              if i in {8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63}:
                i-=8
                pion_y = 7
            else:
              s.set_pixel(pion_x,pion_y,(0,0,0))
              pion_y -= 1 #incremente la position du pion de 1
              if labyrinth[8*pion_y+pion_x] ==  G:
                """gestion des murs"""
                s.show_message("Wall",scroll_speed = 0.1)
                pion_y += 1#incremente la position du pion de 1
                life -= 1
                s.show_message("life : {}".format(life))
                s.clear()
              elif labyrinth[8*pion_y+pion_x] ==  B :
                  """teleporteur"""
                if i == 0 :
                  i+= 35#set carte
                  pion_x = 5#set position pion
                  pion_y = 1#set position pion
                elif i == 35 :
                  i-= 35#set carte
                  pion_x = 6#set position pion
                  pion_y = 6#set position pion
                elif i == 8 :
                  i+= 7#set carte
                  pion_x = 6#set position pion
                  pion_y = 1#set position pion
                elif i == 15 :
                  i-= 7#set carte
                  pion_x = 6#set position pion
                  pion_y = 1#set position pion
                elif i == 28 :
                  i+= 18
                  pion_x = 6#set position pion
                  pion_y = 1#set position pion
                elif i == 46 :
                  i-= 18#set carte
                  pion_x = 1#set position pion
                  pion_y = 6#set position pion  
          if event.direction == "down":
            if pion_y == 7:
              if i in {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55}:
                i+=8
                pion_y = 0
              else : 
                pass
            else:
              s.set_pixel(pion_x,pion_y,(0,0,0))
              pion_y += 1 
              if labyrinth[8*pion_y+pion_x] ==  G:
                """gestion des mur"""
                s.show_message("Wall",scroll_speed = 0.1)
                pion_y -= 1#incremente la position du pion de 1
                life -= 1
                s.show_message("life : {}".format(life))
                s.clear()
              elif labyrinth[8*pion_y+pion_x] ==  B :
                """teleporteur"""
                if i == 0 :
                  i+= 35#set carte
                  pion_x = 5#set position pion
                  pion_y = 1#set position pion
                elif i == 35 :
                  i-= 35#set carte
                  pion_x = 6#set position pion
                  pion_y = 6#set position pion
                elif i == 8 :
                  i+= 7#set carte
                  pion_x = 6#set position pion
                  pion_y = 1#set position pion
                elif i == 15 :
                  i-= 7#set carte
                  pion_x = 6#set position pion
                  pion_y = 1#set position pion
                elif i == 28 :
                  i+= 18#set carte
                  pion_x = 6#set position pion
                  pion_y = 1#set position pion
                elif i == 46 :
                  i-= 18#set carte
                  pion_x = 1#set position pion
                  pion_y = 6#set position pion  
          if event.direction =='middle':
              if -150 <= int(s.get_accelerometer_raw()['x']*100) <= -50 and -50 <= int(s.get_accelerometer_raw()['y']*100) <= 50  and -50 <= int(s.get_accelerometer_raw()['z']*100) <= 50:
                  #LEFT/position accelerometre_raw
                  if pion_x == 0:
                      if i in {1,2,3,4,5,6,7,9,10,11,12,13,14,15,17,18,19,20,21,22,23,25,26,27,28,29,30,31,33,34,35,36,37,38,39,41,42,43,44,45,46,47,49,50,51,52,53,54,55,57,58,59,60,61,62,63}:
                          i-=1
                          pion_x = 7
                  else:
                      s.set_pixel(pion_x,pion_y,(0,0,0))
                      pion_x -= 1#incremente la position du pion de 1
                      if labyrinth[8*pion_y+pion_x] ==  G:
                        """gestion des murs"""
                        s.show_message("Wall",scroll_speed = 0.1)
                        pion_x += 1#incremente la position du pion de 1
                        life -= 1
                        s.show_message("life : {}".format(life))
                        s.clear()
                      elif labyrinth[8*pion_y+pion_x] ==  B :
                        """teleporteur"""
                        if i == 0 :
                          i+= 35#set carte
                          pion_x = 5#set position pion
                          pion_y = 1#set position pion
                        elif i == 35 :
                          i-= 35#set carte
                          pion_x = 6#set position pion
                          pion_y = 6#set position pion
                        elif i == 8 :
                          i+= 7#set carte
                          pion_x = 6#set position pion
                          pion_y = 1#set position pion
                        elif i == 15 :
                          i-= 7#set carte
                          pion_x = 6#set position pion
                          pion_y = 1#set position pion
                        elif i == 28 :
                          i+= 18#set carte
                          pion_x = 6#set position pion
                          pion_y = 1#set position pion
                        elif i == 46 :
                          i-= 18#set carte
                          pion_x = 1#set pos pions
                          pion_y = 6#set position pion
              if 50 <= int(s.get_accelerometer_raw()['x']*100) <= 150 and -50 <= int(s.get_accelerometer_raw()['y']*100) <= 50  and -50 <= int(s.get_accelerometer_raw()['z']*100) <= 50:
                  #RIGHT/position accelerometre_raw
                  if pion_x == 7:
                      if i in {0,1,2,3,4,5,6,8,9,10,11,12,13,14,16,17,18,19,20,21,22,24,25,26,27,28,29,30,32,33,34,35,36,37,38,40,41,42,43,44,45,46,48,49,50,51,52,53,54,56,57,58,59,60,61,62}:
                        i+=1
                        pion_x = 0
                  else:
                      s.set_pixel(pion_x,pion_y,(0,0,0))
                      pion_x += 1#incremente la position du pion de 1
                      if labyrinth[8*pion_y+pion_x] ==  G:
                        """gestion des murs"""
                        s.show_message("Wall",scroll_speed = 0.1)
                        pion_x -= 1#incremente la position du pion de 1
                        life -= 1
                        s.show_message("life : {}".format(life))
                        s.clear()
                      elif labyrinth[8*pion_y+pion_x] ==  B :
                        """teleporteur"""
                        if i == 0 :
                          i+= 35#set carte
                          pion_x = 5#set position pion
                          pion_y = 1#set position pion
                        elif i == 35 :
                          i-= 35#set carte
                          pion_x = 6#set position pion
                          pion_y = 6#set position pion
                        elif i == 8 :
                          i+= 7#set carte
                          pion_x = 6#set position pion
                          pion_y = 1#set position pion
                        elif i == 15 :
                          i-= 7#set carte
                          pion_x = 6#set position pion
                          pion_y = 1#set position pion
                        elif i == 28 :
                          i+= 18#set carte
                          pion_x = 6#set position pion
                          pion_y = 1#set position pion
                        elif i == 46 :
                          i-= 18#set carte
                          pion_x = 1#set position pion
                          pion_y = 6#set position pion  
              if -50 <= int(s.get_accelerometer_raw()['x']*100) <= 50 and -150 <= int(s.get_accelerometer_raw()['y']*100) <= -50  and -50 <= int(s.get_accelerometer_raw()['z'])*100 <= 50:
                  #UP/position accelerometre_raw
                  if pion_y == 0:
                      if i in {8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63}:
                          i-=8
                          pion_y = 7
                  else:
                      s.set_pixel(pion_x,pion_y,(0,0,0))
                      pion_y -= 1 #incremente la position du pion de 1
                      if labyrinth[8*pion_y+pion_x] ==  G:
                        """gestion des murs"""
                        s.show_message("Wall",scroll_speed = 0.1)
                        pion_y += 1#incremente la position du pion de 1
                        life -= 1
                        s.show_message("life : {}".format(life))
                        s.clear()
                      elif labyrinth[8*pion_y+pion_x] ==  B :
                        """teleporteur"""
                        if i == 0 :
                          i+= 35#set carte
                          pion_x = 5#set position pion
                          pion_y = 1#set position pion
                        elif i == 35 :
                          i-= 35#set carte
                          pion_x = 6#set position pion
                          pion_y = 6#set position pion
                        elif i == 8 :
                          i+= 7#set carte
                          pion_x = 6#set position pion
                          pion_y = 1#set position pion
                        elif i == 15 :
                          i-= 7#set carte
                          pion_x = 6#set position pion
                          pion_y = 1#set position pion
                        elif i == 28 :
                          i+= 18#set carte
                          pion_x = 6#set position pion
                          pion_y = 1#set position pion
                        elif i == 46 :
                          i-= 18#set carte
                          pion_x = 1#set position pion
                          pion_y = 6 #set position pion 
              elif -50 <= int(s.get_accelerometer_raw()['x']*100) <= 50 and 50 <= int(s.get_accelerometer_raw()['y']*100) <= 150  and -50 <= int(s.get_accelerometer_raw()['z']*100) <= 50:
                  #DOWN/position accelerometre_raw
                  if pion_y == 7:
                    if i in {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55}:
                        i+=8
                        pion_y = 0
                  else:
                    s.set_pixel(pion_x,pion_y,(0,0,0))
                    pion_y += 1 #incremente la position du pion de 1
                    if labyrinth[8*pion_y+pion_x] ==  G:
                      """gestion des murs"""
                      s.show_message("Wall",scroll_speed = 0.1)
                      pion_y -= 1#incremente la position du pion de 1
                      life -= 1
                      s.show_message("life : {}".format(life))
                      s.clear()
                    elif labyrinth[8*pion_y+pion_x] ==  B :
                        """teleporteur"""
                        if i == 0 :
                          i+= 35#set carte
                          pion_x = 5#set position pion
                          pion_y = 1#set position pion
                        elif i == 35 :
                          i-= 35#set carte
                          pion_x = 6#set position pion
                          pion_y = 6#set position pion
                        elif i == 8 :
                          i+= 7#set carte
                          pion_x = 6#set position pion
                          pion_y = 1#set position pion
                        elif i == 15 :
                          i-= 7#set carte
                          pion_x = 6#set position pion
                          pion_y = 1#set position pion
                        elif i == 28 :
                          i+= 18#set carte
                          pion_x = 6#set position pion
                          pion_y = 1#set position pion
                        elif i == 46 :
                          i-= 18#set carte
                          pion_x = 1#set position pion
                          pion_y = 6#set position pion
                
"""-----Crypto-----"""

def encode(pwd, plain_text):
    key = pwd
    enc = []
    for i, e in enumerate(plain_text):
        key_c = key[i % len(key)]
        enc_c = chr((ord(e) + ord(key_c)) % 256)
        enc.append(enc_c)
    return ("".join(enc).encode()).decode()

def decode(pwd, cipher_text):
    key = pwd
    dec = []
    for i, e in enumerate(cipher_text):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(e) - ord(key_c)) % 256)
        dec.append(dec_c)
    return str("".join(dec))

def hashing(pwd):
    def to_32(value):
        value = value % (2 ** 32)
        if value >= 2**31:
            value = value - 2 ** 32
        value = int(value)
        return value

    if pwd:
        x = ord(pwd[0]) << 7
        m = 1000003
        for c in pwd:
            x = to_32((x*m) ^ ord(c))
        x ^= len(pwd)
        if x == -1:
            x = -2
        return str(x)
    return ""


"""------Execution-------"""
while True :
    menuLogo(0)