class Fuvar:
    def __init__(self,taxiazonosito,indulas,utazastartalma,tavolsag,viteldij,borravalo,fizetesmod):
        self.taxiazonosito = taxiazonosito
        self.indulas = indulas
        self.utazastartalma = utazastartalma
        self.tavolsag = tavolsag
        self.viteldij = viteldij
        self.borravalo = float(borravalo)
        self.fizetesmod = fizetesmod

fuvarlista = []
utazasfeljegyzesre = 0

with open("fuvar.csv", "rt",  encoding="utf-8") as f:
    f.readline()
    for sor in f:
        sor = sor.strip().split(";")
        sor[5] = sor[5].replace(",",".")
        sor[4] = sor[4].replace(",",".")
        tmp = Fuvar(sor[0],sor[1],sor[2],sor[3],sor[4],sor[5],sor[6])
        fuvarlista.append(tmp)
        utazasfeljegyzesre += 1
        
print("3. feladat: ",utazasfeljegyzesre,"fuvar")

fuvarszam = 0
borravalok = 0

for sor in fuvarlista:
    if sor.taxiazonosito == "6185":
        fuvarszam += 1
        borravalok += float(sor.borravalo) + float(sor.viteldij)
        print(borravalok)
        if fuvarszam == 4:
            print("4. feladat:",fuvarszam,"fuvar alatt:",borravalok,"$")


                