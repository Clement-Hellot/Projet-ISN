from tkinter import *
from unicodedata import *
from enigma.machine import EnigmaMachine
from webbrowser import open_new
import os


#apercu vide mais contenu existant "décimal de pi"
pi ="31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989380952572010654858632788659361533818279682303019520353018529689957736225994138912497217752834791315155748572424541506959508295331168617278558890750983817546374649393192550604009277016711390098488240128583616035637076601047101819429555961989467678374494482553797747268471040475346462080466842590694912933136770289891521047521620569660240580381501935112533824300355876402474964732639141992726042699227967823547816360093417216412199245863150302861829745557067498385054945885869269956909272107975093029553211653449872027559602364806654991198818347977535663698074265425278625518184175746728909777727938000816470600161452491921732172147723501414419735685481613611573525521334757418494684385233239073941433345477624168625189835694855620992192221842725502542568876717904946016534668049886272327917860857843838279679766814541009538837863609506800642251252051173929848960841284886269456042419652850222106611863067442786220391949450471237137869609563643719172874677646575739624138908658326459958133904780275900994657640789512694683983525957098258226205224894077267194782684826014769909026401363944374553050682034962524517493996514314298091906592509372216964615157098583874105978859597729754989301617539284681382686838689427741559918559252459539594310499725246808459872736446958486538367362226260991246080512438843904512441365497627807977156914359977001296160894416948685558484063534220722258284886481584560285060168427394522674676788952521385225499546667278239864565961163548862305774564980355936345681743241125150760694794510965960940252288797108931456691368672287489405601015033086179286809208747609178249385890097149096759852613655497818931297848216829989487226588048575640142704775551323796414515237462343645428584447952658678210511413547357395231134271661021359695362314429524849371871101457654035902799344037420073105785390621983874478084784896833214457138687519435064302184531910484810053706146806749192781911979399520614196634287544406437451237181921799983910159195618146751426912397489409071864942319615679452080951465502252316038819301420937621378559566389377870830390697920773467221825625996615014215030680384477345492026054146659252014974428507325186660021324340881907104863317346496514539057962685610055081066587969981635747363840525714591028970641401109712062804390397595156771577004203378699360072305587631763594218731251471205329281918261861258673215791984148488291644706095752706957220917567116722910981690915280173506712748583222871835209353965725121083579151369882091444210067510334671103141267111369908658516398315019701651511685171437657618351556508849099898599823873455283316355076479185358932261854896321329330898570642046752590709154814165498594616371802709819943099244889575712828905923233260972997120844335732654893823911932597463667305836041428138830320382490375898524374417029132765618093773444030707469211201913020330380197621101100449293215160842444859637669838952286847831235526582131449576857262433441893039686426243410773226978028073189154411010446823252716201052652272111660396665573092547110557853763466820653109896526918620564769312570586356620185581007293606598764861179104533488503461136576867532494416680396265797877185560845529654126654085306143444318586769751456614068007002378776591344017127494704205622305389945613140711270004078547332699390814546646458807972708266830634328587856983052358089330657574067954571637752542021149557615814002501262285941302164715509792592309907965473761255176567513575178296664547791745011299614890304639947132962107340437518957359614589019389713111790429782856475032031986915140287080859904801094121472213179476477726224142548545403321571853061422881375850430633217518297986622371721591607716692547487389866549494501"
    
#Chiffrage césar
def cesar_c(txt,decalage):
    A = "abcdefghijklmnopqrstuvwxyz"
    txt = txt.lower()
    txt = normalize("NFKD",txt)
    out =""
    proba=""
     

    for i in txt:
        if i.isalpha()==True:
            j = A.index(i)
            decalage = (7*j)+4
            j=decalage
            out+= A[j%26]
        else:
            out+=i
    return out

print(cesar_c("àéàui",0))
def cesar_d(txt,decalage,know,know_txt):
    A = "abcdefghijklmnopqrstuvwxyz"
    txt = txt.lower()
    txt = normalize("NFKD",txt)
    out =""
    proba=""
    
    if know==1:
        for k in range(0,26):
            for i in txt:
                if i.isalpha()==True:
                    j = A.index(i)
                    j = (j/7)-4
                    if j<0:
                        j+=26
                    out+=A[j]
                else:
                    out+=i
            if know_txt in out:                 #systeme de recherche des mots connus
                proba += str(k)+" "
            out=""
        if proba !="":
            messagebox.showinfo("Décalage probable","Les décalages probables sont : "+proba )
        else:
            messagebox.showinfo("Décalage probable","Aucun texte clair ne contient se mot")
                                
    else:
        for i in txt:
            if i.isalpha()==True:
                j = A.index(i)
                j-= decalage
                out+= A[j%26]
            else:
                out+=i
    

    return out

#Chiffrage Vigenère
def vig_c(txt,cle):
    A =  "abcdefghijklmnopqrstuvwxyz"
    txt,cle = txt.lower(), cle.lower()
    txt,cle = normalize("NFKD",txt),normalize("NFKD",cle)
    out =""
    k=0
    for i in txt:
        if i.isalpha()==True:
            j = A.index(i)
            l = A.index(cle[k])
            j+= l
            out+= A[j%26]
        else:
            out+=i
        k+=1
        if k==len(cle):
            k=0
    return out

def vig_d(txt,cle):
    A =  "abcdefghijklmnopqrstuvwxyz"
    txt,cle = txt.lower(), cle.lower()
    txt,cle = normalize("NFKD",txt),normalize("NFKD",cle)
    out =""
    k=0
    for i in txt:
        if i.isalpha()==True:
            j = A.index(i)
            l = A.index(cle[k])
            j-= l
            if j<0:
                j+=26
            out+= A[j]
        else:
            out+=i
        k+=1
        if k==len(cle):
            k=0
    return out


#chiffrage Enigma
def enigma(txt,rot,pos,rings,ref,plug):
    txt = normalize("NFKD",txt)
    txt = txt[:-1]
    machine = EnigmaMachine.from_key_sheet(
                           rotors=rot,
                           reflector=ref,
                           ring_settings=rings ,
                           plugboard_settings=plug)
    machine.set_display(pos)
    o = list(machine.process_text(txt))
    for i in range(0,len(txt)):
        if txt[i]== " ":
            o.insert(i," ")
    o= "".join(o)
    return o

    
#Calcul des fréquences du texte entré par l'user    
def stat(txt):
    global labFR,labTitle,langueActuel
    txt=txt.lower()
    txt = normalize("NFKD",txt)
    A =  "abcdefghijklmnopqrstuvwxyz"
    languechoisi="A : 8.4 %\nB : 1.1 %\nC : 3.0 %\nD : 4.2 %\nE : 17.3 %\nF : 1.1 %\nG : 1.3 %\nH : 0.9 %\nI : 7.3 %\nJ : 0.3 %\nK : 0.1 %\nL : 6.0 %\nM : 3.0 %\nN : 7.1 %\nO : 5.3 %\nP : 3.0 %\nQ : 1.0 %\nR : 6.6 %\nS : 8.1 %\nT : 7.1 %\nU : 5.7 %\nV : 1.3 %\nW : 0.1 %\nX : 0.4 %\nY : 0.3 %\nZ : 0.1 %\n"
    frqTxt = [0]*26
    out=""
    somme =0
    langueActuel ="Français"
    
    
    for i in txt:
        if i.isalpha()==True:
            pos = A.index(i)
            frqTxt[pos]+=1
            somme+=1

    if somme == 0:
        messagebox.showwarning("Texte vide","Texte à évaluer vide")
    else:
        for i in range(0,26):
            out += A[i].upper()+":"+str(round(float((frqTxt[i]/somme)*100),2))+"%"+"\n"

        fenS = Toplevel(takefocus=True)
        fenS.geometry("300x600")
        fenS.resizable(False,False)
        fenS.title("Ciphering Machine")
        changeLangue = Button(fenS,text="Choix du language",cursor="hand2",command=choix)
        changeLangue.place(x=100,y=25)
        labFR= Label(fenS,text=languechoisi)
        separation = Label(fenS,text ="|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n")
        labTxt = Label(fenS,text=out)
        labTitle = Label(fenS,text= "Fréquence d'apparition \ndans le français")
        labTitle2 = Label(fenS,text= "Fréquence d'apparition \ndans le texte")
        separation.place(x=140,y=110)
        labFR.place(x=50,y=110)
        labTxt.place(x=185,y=110)
        labTitle.place(x=20,y=60)
        labTitle2.place(x=145,y=60)

#Possibilité du choix des langues pour la comparaison
def choix():
    global fenC
    fenC = Toplevel(takefocus=True)
    fenC.title("Ciphering Machine")
    fenC.resizable(False,False)
    fenC.geometry("200x200")
    listelangue = ("Français","Anglais","Allemand","Espagnol")
    langue = StringVar()
    langue.set(langueActuel)
    choixlangue = OptionMenu(fenC,langue,*listelangue)
    choixlangue.place(x=50,y=50)
    ok = Button(fenC,text="OK",cursor="hand2",command=lambda :destroyed(langue.get()))
    ok.place(x=75,y=100)


#Permet d'afficher la langue et la fréquence de la langue choisi
def destroyed(langue):
    global langueActuel         #Permet d'initialiser la liste sur la langue actuel et non sur le français
    langueActuel =langue
    if langue == "Français":
        languechoisi="A : 8.4 %\nB : 1.1 %\nC : 3.0 %\nD : 4.2 %\nE : 17.3 %\nF : 1.1 %\nG : 1.3 %\nH : 0.9 %\nI : 7.3 %\nJ : 0.3 %\nK : 0.1 %\nL : 6.0 %\nM : 3.0 %\nN : 7.1 %\nO : 5.3 %\nP : 3.0 %\nQ : 1.0 %\nR : 6.6 %\nS : 8.1 %\nT : 7.1 %\nU : 5.7 %\nV : 1.3 %\nW : 0.1 %\nX : 0.4 %\nY : 0.3 %\nZ : 0.1 %\n"
        labTitle.config(text="Fréquence d'apparition \ndans le Français")
    elif langue == "Anglais":
        languechoisi="A : 8.08%\nB : 1.67%\nC : 3.18%\nD : 3.99%\nE : 12.56%\nF : 2.17%\nG : 1.80%\nH : 5.27%\nI : 7.24%\nJ : 0.14%\nK : 0.63%\nL : 4.04%\nM : 2.60%\nN : 7.38%\nO : 7.47%\nP : 1.91%\nQ : 0.09%\nR : 6.42%\nS : 6.59%\nT : 9.15%\nU : 2.79%\nV : 1.00%\nW : 1.89%\nX : 0.21%\nY : 1.65%\nZ : 0.07%"
        labTitle.config(text="Fréquence d'apparition \ndans l'Anglais")
    elif langue == "Allemand" :
        languechoisi="A : 6.28%\nB : 1.99%\nC : 2.98%\nD : 5.04%\nE : 16.92%\nF : 1.62%\nG : 3.12%\nH : 4.51%\nI : 7.42%\nJ : 0.30%\nK : 1.46%\nL : 3.56%\nM : 2.54%\nN : 10.20%\nO : 2.87%\nP : 0.77%\nQ : 0.02%\nR : 7.44%\nS : 6.62%\nT : 5.95%\nU : 4.39%\nV : 1.07%\nW : 1.52%\nX : 0.03%\nY : 0.10%\nZ : 1.2%"
        labTitle.config(text="Fréquence d'apparition \ndans l'Allemand")
    elif langue == "Espagnol" :
        languechoisi="A : 12.30%\nB : 1.03%\nC : 4.49%\nD : 5.04%\nE : 13.69%\nF : 0.77%\nG : 1.04%\nH : 0.65%\nI : 7.78%\nJ : 0.28%\nK : 0.02%\nL : 5.84%\nM : 2.84%\nN : 7.41%\nO : 8.68%\nP : 2.63%\nQ : 1.02%\nR : 6.44%\nS : 6.97%\nT : 4.82%\nU : 3.99%\nV : 1.04%\nW : 0.02%\nX : 0.16%\nY : 0.66%\nZ : 0.3%"
        labTitle.config(text="Fréquence d'apparition \ndans l'Espagnol")
    labFR.config(text=languechoisi)
    fenC.destroy()

#Calcul de l'indice de coincidence du texte permettant de distinguer un texte à substitution monoalphabetique/polyalphabetique  
def ioc(txt):
    A = "abcdefghijklmnopqrstuvwxyz"
    txt = txt.lower()
    txt = normalize("NFKD",txt)
    n=0
    ioc = 0.0
    for u in txt:
        if u.isalpha()==True:
            n+=1
    if n == 0:
        messagebox.showwarning("Texte vide","Texte à évaluer vide")
    else:
        for i in A:
            ni=0
            for o in txt:
                if o==i:
                    ni+=1
            ioc+= (ni*(ni-1))/(n*(n-1))
        messagebox.showinfo("IOC",("IOC ="+str(ioc)))

#Chiffrage par PI   
def pi_c(txt):
    A = "abcdefghijklmnopqrstuvwxyz"
    txt = txt.lower()
    txt = normalize("NFKD",txt)
    key=pi
    key = key[0:len(txt)]
    out = ""


    for i in range(0,len(txt)):
        if txt[i].isalpha() == True:
            a=A.index(txt[i])
            b= int(key[i])
            c = (a+b)%26
            out+=A[c]
        else:
            out+=" "
    return out

def pi_d(txt):
    A = "abcdefghijklmnopqrstuvwxyz"
    txt = txt.lower()
    txt = normalize("NFKD",txt)
    key = pi
    key = key[0:len(txt)]
    out = ""


    for i in range(0,len(txt)):
        if txt[i].isalpha() == True:
            a=A.index(txt[i])
            b= int(key[i])
            if a-b<0:
                a+=26
            c = (a-b)
            out+=A[c]
        else:
            out+=" "
    return out


#chiffrage par binaire
def bin_c(ph):
    alphabet=" abcdefghijklmnopqrstuvwxyz"
    somme=""
    ph= normalize("NFKD",ph)

    for i in ph.lower():
        if i in alphabet:
            position=alphabet.index(i)
            x=bin(position)+" "
            x=x[2:]
            somme=somme+x
    return somme

def bin_d(ph):
    alphabet=" abcdefghijklmnopqrstuvwxyz"
    ph = ph.lower()
    ph = normalize("NFKD",ph)
    somme=""
    liste=ph.split(' ')
    for i in liste:
        if i.isdigit()==True and (i==0 or i==1):
            x=int(i,2)
            somme+=alphabet[x]
        else:
            messagebox.showwarning("Error","Veuillez rentrer des données valides")
            break
    return somme


#Chiffrage par hexadécimale
def hex_c(ph):
    alphabet=" abcdefghijklmnopqrstuvwxyz"
    ph = normalize("NFKD",ph)
    somme=""
    for i in ph.lower():
        if i in alphabet:
            position=alphabet.index(i)
            x=hex(position)+" "
            x=x[2:]
            somme=somme+x
    return somme

def hex_d(txt):
    A = " abcdefghijklmnopqrstuvwxyz"
    txt = txt.lower()
    txt = normalize("NFKD",txt)
    liste = txt.split(" ")
    out=""
    for i in liste:
        if str(int(i,16)).isdigit()==True:
            out += A[int(i,16)]
        else:
            messagebox.showwarning("Error","Veuillez rentrer des données valides")
            break
    return out


#Permet d'acceder au site web grâce au bouton info
def getinfo(number):
    if number == 0 :
        open_new("https://vico.alwaysdata.net/index.html")
    elif number == 3:
        open_new("https://vico.alwaysdata.net/vigenere.html")
    elif number == 5:
        open_new("https://vico.alwaysdata.net/enigma.html")
    elif number == 9:
        open_new("https://vico.alwaysdata.net/binaire.html")
    elif number == 11:
        open_new("https://vico.alwaysdata.net/hex.html")
    elif number == 7:
        open_new("https://vico.alwaysdata.net/pi.html")
        








        



