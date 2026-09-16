from traitement import load_fichier_csv, ajout_drapeau
from bdd import init_db, inserer_transactions

init_db()

donnees = load_fichier_csv("transactions_1.csv")
donnees_traitees = ajout_drapeau(donnees)
inserer_transactions(donnees_traitees)
print("test bon")