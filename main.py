from ast import Or

class Település:
    lista=[]
    def __init__(self,id,nev,rang,besorolas,terulet,nepesseg,lakosszam):
        self.id = id
        self.nev =  nev
        self.rang = rang
        self.besorolas = besorolas
        self.terulet = terulet
        self.nepesseg = nepesseg
        self.lakosszam = lakosszam
        Település.lista.append(self)

with open("telepules.txt", "r", encoding="utf8") as f:
    for sor in f:
        s = sor.strip().split("\t")
        t = Település(s[0],s[1],(s[2]),s[3],int(s[4]),int(s[5]),int(s[6]))

print(len(Település.lista))