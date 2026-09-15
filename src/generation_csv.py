import random

random.seed(0)
entete = "datetime_transaction,iban_origine,pays_source,banque_source,iban_destinataire,pays_destinataire,montant,devise\n"
iban1 = "FRXXX1"
iban2 = "FRXXX2"

destinataires = [
    "DEXXX,DE",
    "ESXXX,ES"
]
f1 = open("transactions_1.csv", "w")
f1.write(entete)
f1.write(f"2024-03-01T09:12:00,{iban1},FR,BNPPARIBAS,DEXXX,DE,6250.50,EUR\n")
f1.write(f"2024-03-01T10:15:00,{iban2},FR,BNPPARIBAS,ESXXX,ES,7400.00,EUR\n")

for i in range(5):
    dest = random.choice(destinataires)
    prix = random.randint(10, 3000)
    f1.write("2024-03-01T11:00:00," + iban1 + ",FR,BNPPARIBAS," + dest + "," + str(prix) + ".00,EUR\n")

f1.close()
f2 = open("transactions_2.csv", "w")
f2.write(entete)

for i in range(6):
    dest = random.choice(destinataires)
    prix = random.randint(50, 4000)
    if i % 2 == 0:
        source = iban1
    else:
        source = iban2
    f2.write("2024-03-02T14:20:00," + source + ",FR,BNPPARIBAS," + dest + "," + str(prix) + ".50,EUR\n")

f2.close()
f3 = open("transactions_3.csv", "w")
f3.write(entete)

for i in range(7):
    dest = random.choice(destinataires)
    prix = random.randint(20, 2000)
    f3.write("2024-03-03T16:45:00," + iban2 + ",FR,BNPPARIBAS," + dest + "," + str(prix) + ".99,EUR\n")
f3.close()

print("fichiers cree")