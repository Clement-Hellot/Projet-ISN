# -*- coding: cp1252 -*-
from tkinter import *
from wckToolTips import * 
from crypto import *


#Settings Interface primaire

fen = Tk()
fen.title("Ciphering Machine")
fen.geometry("550x300")
fen.resizable(False,False)

dico={}                         #dico pour referencer les images


 #fonction de chiffrement avec selection du chiffrage/dechiffrage et de la methode

def ciphering(tech):
    txt = text1.get(1.0,END)
    text2.delete(1.0,END)


    #Cesar
    if tech ==0:
        dec = int(spin.get())
        tech= cesar_c(txt,dec)
    elif tech == 1:
        dec = int(spin.get())
        tech= cesar_d(txt,dec,checking.get(),mc_entry.get())

    #vigenere
    elif tech == 3:
        clef = cle.get()
        tech = vig_c(txt,clef)
    elif tech == 4:
        clef = cle.get()
        tech = vig_d(txt,clef)

    #Enigma
    elif tech == 5 or tech == 6:
        verifrot = []
        if controlm3_m4 == 0:
            paramrotor = v12.get()+" "+v15.get()+" "+v16.get()+" "+v17.get()
            parapos = v1.get()[0]+v2.get()[0]+v3.get()[0]+v13.get()[0]
            paramring = v4.get()[0]+" "+v5.get()[0]+" "+v6.get()[0]+" "+v14.get()[0]
            paramref = vrefm4.get()
            verifrot.append(v15.get()),verifrot.append(v16.get()),verifrot.append(v17.get())
            
        else:
            paramrotor = v7.get()+" "+v8.get()+" "+v9.get()
            parapos = v1.get()[0]+v2.get()[0]+v3.get()[0]
            paramring = v4.get()[0]+" "+v5.get()[0]+" "+v6.get()[0]
            paramref = v10.get()
            verifrot.append(v7.get()),verifrot.append(v8.get()),verifrot.append(v9.get())

        for i in range(0,len(verifrot)):        #verification que les rotors choisi ne soit pas les mêmes
            if verifrot[i] in verifrot[i+1:]:
                paramrotor = "I II III"
                v7.set(rotor[0]),v15.set(rotor[0])
                v8.set(rotor[1]),v16.set(rotor[1])
                v9.set(rotor[2]),v17.set(rotor[2])                
                messagebox.showwarning("Error rotors settings","Les valeurs des rotors ne sont pas chacune différentes, ils ont donc été défini par défault sur I II III")

        paramplug= checkplug()
        tech = enigma(txt,paramrotor,parapos,paramring,paramref,paramplug)

    #pi
    elif tech == 7:
        tech = pi_c(txt)
    elif tech == 8:
        tech = pi_d(txt)

    #bin
    elif tech == 9:
        tech = bin_c(txt)
    elif tech == 10:
        tech = bin_d(txt)

    #hex
    elif tech==11:
        tech =hex_c(txt)
    elif tech==12:
        tech = hex_d(txt)

    text2.insert(1.0,tech)
    
    #Bouton Selection enigma M3/M4
    #code placé ici car sinon aucun accès au widget ex:ref,r1,r2,ect
def enigmaSwap(typ):
    global controlm3_m4 #initialisation variable sinon error reference before assignement
    if typ == 1:
        reflector.place_forget()
        reflectorm4.place(x=70,y=10)
        r1.place_forget()
        r2.place_forget()
        r3.place_forget()
        r1m4.place(x=185,y=40)
        r2m4.place(x=245,y=40)
        r3m4.place(x=305,y=40)
        r4.place(x=105,y=40)
        posm4.place(x=270,y=70)
        ringm4.place(x=270,y=100)
        enig_type.config(text="Set to M3")
        controlm3_m4-=1
    else:
        enig_type.config(text="Set to M4(Navy Only)")
        reflectorm4.place_forget()
        posm4.place_forget()
        ringm4.place_forget()
        r1m4.place_forget()
        r2m4.place_forget()
        r3m4.place_forget()
        r4.place_forget()
        r1.place(x=105,y=40)
        r2.place(x=165,y=40)
        r3.place(x=225,y=40)
        reflector.place(x=70,y=10)
        controlm3_m4+=1

#Tableau de connexion avec verification des entrées
#Code placé ici dans un problème de référencement des variables "valeurs des branchements"
def setplug(typ):
    global fenP
    global co1_a,co1_b,co2_a,co2_b,co3_a,co3_b,co4_a,co4_b,co5_a,co5_b,co6_a,co6_b,co7_a,co7_b,co8_a,co8_b,co9_a,co9_b,co10_a,co10_b #
    fenP = Toplevel(takefocus=True)
    fenP.resizable(False,False)
    fenP.geometry("250x250")
    fenP.title("Ciphering Machine \"Enigma Tableau de connexion\"")
    labPres = Label(fenP,text="Tableau de connexion")
    A= ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")

    #mise en place du tableau de connexion "menu déroulant"
    co1_a,co1_b,co2_a,co2_b,co3_a,co3_b,co4_a,co4_b,co5_a,co5_b,co6_a,co6_b = StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()
    co7_a,co7_b,co8_a,co8_b,co9_a,co9_b,co10_a,co10_b=StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()
    
    mo1a,mo1b,mo2a,mo2b,mo3a,mo3b = OptionMenu(fenP,co1_a,*A),OptionMenu(fenP,co1_b,*A),OptionMenu(fenP,co2_a,*A),OptionMenu(fenP,co2_b,*A),OptionMenu(fenP,co3_a,*A),OptionMenu(fenP,co3_b,*A)
    mo4a,mo4b,mo5a,mo5b,mo6a,mo6b = OptionMenu(fenP,co4_a,*A),OptionMenu(fenP,co4_b,*A),OptionMenu(fenP,co5_a,*A),OptionMenu(fenP,co5_b,*A),OptionMenu(fenP,co6_a,*A),OptionMenu(fenP,co6_b,*A)
    mo7a,mo7b,mo8a,mo8b,mo9a,mo9b =OptionMenu(fenP,co7_a,*A),OptionMenu(fenP,co7_b,*A),OptionMenu(fenP,co8_a,*A),OptionMenu(fenP,co8_b,*A),OptionMenu(fenP,co9_a,*A),OptionMenu(fenP,co9_b,*A)
    mo10a,mo10b = OptionMenu(fenP,co10_a,*A),OptionMenu(fenP,co10_b,*A)
    

    mo1a.place(x=50,y=20),mo1b.place(x=150,y=20),mo2a.place(x=50,y=50),mo2b.place(x=150,y=50),mo3a.place(x=50,y=80),mo3b.place(x=150,y=80)
    mo4a.place(x=50,y=110),mo4b.place(x=150,y=110),mo5a.place(x=50,y=140),mo5b.place(x=150,y=140),mo6a.place(x=50,y=170),mo6b.place(x=150,y=170)

    #mise en place du tableau de connexion "N° des cables"
    labco1 =Label(fenP,text="Cable 1")
    labco2 =Label(fenP,text="Cable 2")
    labco3 =Label(fenP,text="Cable 3")
    labco4 =Label(fenP,text="Cable 4")
    labco5 =Label(fenP,text="Cable 5")
    labco6 =Label(fenP,text="Cable 6")
    labco1.place(x=100,y=25)
    labco2.place(x=100,y=55)
    labco3.place(x=100,y=85)
    labco4.place(x=100,y=115)
    labco5.place(x=100,y=145)
    labco6.place(x=100,y=175)
    labPres.place(x=65,y=0)
    ok = Button(fenP,text="OK",cursor="hand2",command=checkplug)
    ok.place(x=110,y=210)

    #mise en place du tableau de connexion "bouton d'aide"
    helpb = Button(fenP,image=setImg("ico/help.gif"),command=helpi)
    helpb.place(x=200,y=5)


    #Cable enigma M4
    if typ==0:
        fenP.geometry("250x350")
        mo7a.place(x=50,y=200),mo7b.place(x=150,y=200),mo8a.place(x=50,y=230),mo8b.place(x=150,y=230),mo9a.place(x=50,y=260),mo9b.place(x=150,y=260)
        mo10a.place(x=50,y=290),mo10b.place(x=150,y=290)

        labco7 =Label(fenP,text="Cable 7")
        labco8 =Label(fenP,text="Cable 8")
        labco9 =Label(fenP,text="Cable 9")
        labco10 =Label(fenP,text="Cable 10")
        labco7.place(x=100,y=205)
        labco8.place(x=100,y=235)
        labco9.place(x=100,y=265)
        labco10.place(x=100,y=295)
        ok.place(x=110,y=320)

#bouton d'aide pour le tableau de connexion
def helpi():
    messagebox.showinfo("Information","Avant de pouvoir chiffrer à l'aide de la machine enigma, vous devez choisir si vous voulez connecter ou pas des cables au tableau de connexion.\n Plus d'info sur la machine enigma : http://vico.alwaysdata.net")


#verification des entrés du tableau pour ne pas avoir deux cables sur la même lettre ou un cable branché des deux côtés sur la meme lettre
def checkplug():
    global paramplug,fen2
    liste = [co1_a.get()+"/"+co1_b.get(),co2_a.get()+"/"+co2_b.get(),co3_a.get()+"/"+co3_b.get(),co4_a.get()+"/"+co4_b.get(),co5_a.get()+"/"+co5_b.get(),co6_a.get()+"/"+co6_b.get(),co7_a.get()+"/"+ co7_b.get(),co8_a.get()+"/"+ co8_b.get(),co9_a.get()+"/"+ co9_b.get(),co10_a.get()+"/"+ co10_b.get()]
    ok =True
    k=0
    check =[]
    for i in liste:
        if i!="/":
            a,b=i.split("/")
            if a in check or b in check or a==b:
                ok=False
                break                               #Sort de la boucle pour eviter que la condition soit valide sur le prochain cable
            else:
                liste[k]=a+b
                ok=True
            check.append(a)
            check.append(b)
        elif i=="/":
            liste[k]="a"
        k+=1
    while 'a' in liste:
        liste.remove('a')
        
    paramplug = " ".join(liste)
    if ok==True:                    #Fermeture de l'interface du tableau
        fen2.deiconify()
        fenP.destroy()
        return paramplug
    else:
        messagebox.showinfo("Settings Error","Les parametres du tableau de connexion sont incorrects. Les cables doivents se connecter à des prises differentes. Par exemple: A ne peut pas être connecter a A,A ne peut pas être connecter deux fois.")



#interface secondaire

    #Bouton retour    
def gethome():
    fen.deiconify()
    fen2.destroy()

    #Bouton d'effacement
def getclear():
    text1.delete(1.0,END)
    text2.delete(1.0,END)

    #Bouton de chargement d'un document texte dans la zone 1
def getfile():
    text1.delete(1.0,END)
    fichier =filedialog.askopenfilename()
    f =open(fichier,'r')
    f= f.read()
    text1.insert(1.0,f)
    
    #Bouton Sauvegarde du texte chiffré de la zone 2
def getsaved():
     fichier = filedialog.asksaveasfilename(defaultextension ="txt",filetypes=(("Text file","*.txt"),))
     f = open(fichier,'w')
     f.write(text2.get(1.0,END))

    #Bouton Switch chiffrement/dechiffrement
def goswitch():
    global technik
    if technik==0 or technik==3 or technik==5 or technik==7 or technik==9 or technik==11:
        cipher.config(text="Déchiffrement")
        if technik == 0:
            mot_c.config(state='normal')
            mc_entry.config(state='normal')
        technik+=1
    else:
        cipher.config(text="Chiffrement")
        if technik == 1:
            mot_c.config(state='disable')
            mc_entry.config(state='disable')
        technik-=1


    #Permet de definir une image en background des boutons
def setImg(imgfile):
    out = dico[imgfile] = PhotoImage(file = imgfile)
    return out


    
    #Gestion de la fenetre
def opening(tech):    

#initialisation des variables afin de les recup dans les autres fonctions et initialisation de la fenetre
    fen.withdraw()
    global fen2
    global text1,text2,spin,technik,cipher,cle
    global v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v12,v13,v14,v15,v16,v17,vrefm4
    global reflector,reflectorm4,rotor,r1,r2,r3,r4,r1m4,r2m4,r3m4,posm4,ringm4,enig_type,mc_entry,mot_c,checking,controlm3_m4
    technik=tech
    fen2 =Toplevel()
    fen2.geometry("650x450")
    fen2.resizable(False,False)
    

    
#Mise en place de zone de texte/retour/effacement/info/chargement de fichier/sauvegarde/switch/frequence/IOC 
    text1 = Text(fen2,xscrollcommand=True,width=25,height=15)
    text2 = Text(fen2,xscrollcommand=True,width=25,height=15)
    home = Button(fen2,text="home",relief="groove",cursor="hand2",image=setImg("ico/home.gif"),command=gethome)
    clear = Button(fen2,text="clear",relief="groove",cursor="hand2",image=setImg("ico/clear.gif"),command=getclear)
    info = Button(fen2,text="info",relief="groove",cursor="hand2",image=setImg("ico/info.gif"),command= lambda:getinfo(tech))
    file = Button(fen2,text="Open",relief="groove",cursor="hand2",image=setImg("ico/open.gif"),command=getfile)
    save = Button(fen2,text="Save",relief="groove",cursor="hand2",image=setImg("ico/save.gif"),command=getsaved)
    switch = Button(fen2,text="Switch",relief='groove',cursor="hand2",image=setImg("ico/swap.gif"),command=goswitch)
    frequence = Button(fen2,text="F",relief="groove",cursor="hand2",width=5,height=2,command= lambda: stat(text1.get(1.0,END)))
    IOC = Button(fen2,text="IOC",relief="groove",cursor="hand2",width=5,height=2,command= lambda: ioc(text1.get(1.0,END)))
    cipher = Button(fen2,text="Chiffrement",relief="groove",cursor="hand2",width  = 30, height = 3,command= lambda :ciphering(technik))

    
    text1.place(x = 50,y=135)
    text2.place(x = 350,y = 135)
    home.place(x= 585, y=80)
    clear.place(x=535,y=80)
    info.place(x=485,y=80)
    file.place(x=435,y=80)
    save.place(x=385,y=80)
    switch.place(x=335,y=80)
    frequence.place(x=575,y=150)
    IOC.place(x=575,y=200)
    cipher.place(x=190,y=390)

#ToolTips    
    register(home,"Retour au choix du chiffrage")
    register(clear,"Efface le contenu des zones de textes")
    register(info,"Information sur la technique de chiffrement")
    register(file,"Charge le contenu d'un fichier *txt dans la zone de texte à chiffrer")
    register(save,"Sauvegarde le contenu chiffré/déchiffré dans un fichier *txt")
    register(switch,"Chiffrement/Déchiffrement")
    register(frequence,"Compare les fréquences d'apparition des lettres du texte avec ceux de la langue française")
    register(IOC,"Calcule l'indice de coincidence du texte")
    
#Cesar
    if tech ==0:
        fen2.title("Ciphering Machine \"César\"")
        spin = Spinbox(fen2,from_ = 1,to=25)
        checking = IntVar()
        mot_c = Checkbutton(fen2,text="Mot Clair Connu :",variable=checking,state='disable')
        mc_entry = Entry(fen2,state='disable')
        lab_dec= Label(fen2,text="Décalage :")
        lab_dec.place(x=50,y=25)
        spin.place(x=50,y=50)
        mot_c.place(x=40,y=80)
        mc_entry.place(x=170,y=80)

#Vigenère
    elif tech==3:
        fen2.title("Ciphering Machine \"Vigenere\"")
        cle = Entry(fen2)
        lab_cle = Label(fen2,text="Clé de chiffrement :")
        lab_cle.place(x=50,y=25)
        cle.place(x=75,y=50)

#Enigma
    elif tech==5:
        fen2.title("Ciphering Machine \"Enigma\"")
        fen2.withdraw()     #affichage d'abord du tbl de co pour palier à la non def des var cable
        
        #Initialisation Rotor/alphabet/reflector
        a1 = ("A-1","B-2","C-3","D-4","E-5","F-6","G-7","H-8","I-9","J-10","K-11","L-12","M-13","N-14","O-15","P-16","Q-17","R-18","S-19","T-20","U-21","V-22","W-23","X-24","Y-25","Z-26")
        rotor = ("I","II","III","IV","V")
        rotorsup = ("I","II","III","IV","V","VI","VII","VIII")
        rotorM4 = ("Beta","Gamma")
        ref = ('B','C')
        refM4 = ("B-Thin","C-Thin")
        controlm3_m4=1
        
            #Variable de controle pour les listes deroulantes
        v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,vrefm4=StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()        
        v1.set(a1[0]),v2.set(a1[0]),v3.set(a1[0]),v4.set(a1[0]),v5.set(a1[0]),v6.set(a1[0]),v7.set(rotor[0]),v8.set(rotor[1]),v9.set(rotor[2]),v10.set(ref[0]),vrefm4.set(refM4[0])
        v12,v13,v14,v15,v16,v17=StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()
        v12.set(rotorM4[0]),v13.set(a1[0]),v14.set(a1[0]),v17.set(rotorsup[2]),v15.set(rotorsup[0]),v16.set(rotorsup[1])
        
            #Mise en place liste deroulante
        posrl,posrm,posrd,posm4 = OptionMenu(fen2, v1, *a1),OptionMenu(fen2,v2,*a1),OptionMenu(fen2,v3,*a1),OptionMenu(fen2,v13,*a1)           #Voir chapitre tuples pour *
        ringl,ringm,ringd,ringm4 = OptionMenu(fen2, v4, *a1),OptionMenu(fen2,v5,*a1),OptionMenu(fen2,v6,*a1),OptionMenu(fen2,v14,*a1)
        r1,r2,r3,r4 = OptionMenu(fen2, v7, *rotor),OptionMenu(fen2,v8,*rotor),OptionMenu(fen2,v9,*rotor),OptionMenu(fen2,v12,*rotorM4)
        r1m4,r2m4,r3m4= OptionMenu(fen2, v15, *rotorsup),OptionMenu(fen2,v16,*rotorsup),OptionMenu(fen2,v17,*rotorsup)
        reflector = OptionMenu(fen2,v10,*ref)
        reflectorm4 = OptionMenu(fen2,vrefm4,*refM4)



            #Label et placement widget
        plugboard = Button(fen2,text="Tableau de Connexion",cursor="hand2",relief="ridge",command=lambda: setplug(controlm3_m4))
        lab_ref = Label(fen2,text="Reflector :")
        lab_odr = Label(fen2,text="Ordre des rotors :")
        lab_grs = Label(fen2,text="Grundstellung :")
        lab_ris = Label(fen2,text="Ringstellung :")
        lab_m4 = Label(fen2,text="Enigma Type :")
        enig_type = Button(fen2,text="Set To M4(Navy only)",cursor="hand2",command=lambda: enigmaSwap(controlm3_m4))
        
        lab_ref.place(x=5,y=15)
        lab_odr.place(x=5,y=45)
        lab_grs.place(x=5,y=75)
        lab_ris.place(x=5,y=105)
        lab_m4.place(x=440,y=10)
        enig_type.place(x=520,y=10)
        posrl.place(x=90,y=70)
        posrm.place(x=150,y=70)
        posrd.place(x=210,y=70)
        ringl.place(x=90,y=100)
        ringm.place(x=150,y=100)
        ringd.place(x=210,y=100)
        r1.place(x=105,y=40)
        r2.place(x=165,y=40)
        r3.place(x=225,y=40)
        reflector.place(x=70,y=10)
        plugboard.place(x=250,y=10)
        setplug(controlm3_m4)
    

#Bouton Interface principale

l1 = Label(fen,text="Choississez la méthode de chiffrement",font=("Arial",12))
b1 = Button(fen,text="1",relief="groove",cursor="hand2",image=setImg("ico/cesar1.gif"),command= lambda :opening(0))
b2 = Button(fen,text="2",relief="groove",cursor="hand2",image=setImg("ico/Vig.gif"),command= lambda :opening(3))
b3 = Button(fen,text="3",relief="groove",cursor="hand2",image=setImg("ico/img_enigma.gif"),command= lambda :opening(5))
b4 = Button(fen,text="42",relief="groove",cursor="hand2",image=setImg("ico/img_binaire.gif"),command= lambda :opening(9))
b5 = Button(fen,text="1",relief="groove",cursor="hand2",image=setImg("ico/img_hexadecimal.gif"),command= lambda :opening(11))
b6 = Button(fen,text="2",relief="groove",cursor="hand2",image=setImg("ico/img_pi.gif"),command= lambda :opening(7))

    #Tooltips
register(b1,"Chiffrage de César")
register(b2,"Chiffrage de vigenère")
register(b3,"Enigma Machine")
register(b4,"Chiffrage Binaire")
register(b5,"Chiffrage Hexadécimale")
register(b6,"Chiffrage par PI")


l1.grid(row=1, column=2,pady = 20)
b1.grid(row = 2, column=1,padx=45,pady=20)
b2.grid(row = 2, column=2,padx=45,pady=20)
b3.grid(row = 2, column=3,padx=45,pady=20)
b4.grid(row = 3, column=1,padx=45,pady=40)
b5.grid(row = 3, column=2,padx=45,pady=40)
b6.grid(row = 3, column=3,padx=45,pady=40)


