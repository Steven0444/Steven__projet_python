from decimal import Decimal
from typing import TypedDict

class Transaction(TypedDict):
    datetime_transaction: str
    iban_origine: str
    pays_source: str
    banque_source: str
    iban_destinataire: str
    pays_destinataire: str
    montant: Decimal
    devise: str
    depasse_5k: bool

def ajout_drapeau(transactions: list[Transaction]) -> list[Transaction]:
    resultat: list[Transaction] = []

    for t in transactions:
        nouvelle: Transaction = {
            "datetime_transaction": t["datetime_transaction"],
            "iban_origine": t["iban_origine"],
            "pays_source": t["pays_source"],
            "banque_source": t["banque_source"],
            "iban_destinataire": t["iban_destinataire"],
            "pays_destinataire": t["pays_destinataire"],
            "montant": t["montant"],
            "devise": t["devise"],
            "depasse_5k": False
        }

        if t["montant"] > Decimal("5000"):
            nouvelle["depasse_5k"] = True
        else:
            nouvelle["depasse_5k"] = False
        resultat.append(nouvelle)
    return resultat

def iban_origine(transactions: list[Transaction]) -> dict[str, Decimal]:
    totaux: dict[str, Decimal] = {}

    for t in transactions:
        iban = t["iban_origine"]
        if iban not in totaux:
            totaux[iban] = Decimal("0")
        totaux[iban] = totaux[iban] + t["montant"]
    return totaux

def banque_source(transactions: list[Transaction]) -> dict[str, Decimal]:
    totaux: dict[str, Decimal] = {}

    for t in transactions:
        banque = t["banque_source"]
        if banque not in totaux:
            totaux[banque] = Decimal("0")
        totaux[banque] = totaux[banque] + t["montant"]
    return totaux

def iban_destinataire(transactions: list[Transaction]) -> dict[str, Decimal]:
    totaux: dict[str, Decimal] = {}

    for t in transactions:
        iban = t["iban_destinataire"]
        if iban not in totaux:
            totaux[iban] = Decimal("0")
        totaux[iban] = totaux[iban] + t["montant"]
    return totaux

def load_fichier_csv(nom_fichier: str) -> list[Transaction]:
    transactions: list[Transaction] = []

    fichier = open(nom_fichier, "r")
    fichier.readline()

    for ligne in fichier:
        ligne = ligne.strip()
        if ligne != "":
            cols = ligne.split(",")
            if len(cols) != 8:
                raise ValueError("erreur")

            t: Transaction = {
                "datetime_transaction": cols[0],
                "iban_origine": cols[1],
                "pays_source": cols[2],
                "banque_source": cols[3],
                "iban_destinataire": cols[4],
                "pays_destinataire": cols[5],
                "montant": Decimal(cols[6]),
                "devise": cols[7],
                "depasse_5k": False
            }
            transactions.append(t)
    fichier.close()
    return transactions