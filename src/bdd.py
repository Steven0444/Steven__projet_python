import sqlite3
from traitement import Transaction

def init_db(nom_bdd: str = "banque.db") -> None:
    connexion = sqlite3.connect(nom_bdd)
    curseur = connexion.cursor()
    curseur.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            datetime_transaction TEXT,
            iban_origine TEXT,
            pays_source TEXT,
            banque_source TEXT,
            iban_destinataire TEXT,
            pays_destinataire TEXT,
            montant REAL,
            devise TEXT,
            depasse_5k INTEGER
        )
    """)
    connexion.commit()
    connexion.close()

def inserer_transactions(transactions: list[Transaction], nom_bdd: str = "banque.db") -> None:
    connexion = sqlite3.connect(nom_bdd)
    with connexion:
        for t in transactions:
            connexion.execute("""
                INSERT INTO transactions VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                t["datetime_transaction"],
                t["iban_origine"],
                t["pays_source"],
                t["banque_source"],
                t["iban_destinataire"],
                t["pays_destinataire"],
                float(t["montant"]),
                t["devise"],
                1 if t["depasse_5k"] else 0
            ))
    connexion.close()