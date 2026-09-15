from decimal import Decimal
from traitement import ajout_drapeau, iban_origine, banque_source, iban_destinataire

def test_unit():
    donnees = [
        {
            "datetime_transaction": "2024-03-01",
            "iban_origine": "FR1",
            "pays_source": "FR",
            "banque_source": "BNP",
            "iban_destinataire": "DE1",
            "pays_destinataire": "DE",
            "montant": Decimal("6000.00"),
            "devise": "EUR",
            "depasse_5k": False
        },
        {
            "datetime_transaction": "2024-03-01",
            "iban_origine": "FR1",
            "pays_source": "FR",
            "banque_source": "BNP",
            "iban_destinataire": "ES1",
            "pays_destinataire": "ES",
            "montant": Decimal("1000.00"),
            "devise": "EUR",
            "depasse_5k": False
        }
    ]

    res = ajout_drapeau(donnees)
    assert res[0]["depasse_5k"] == True
    assert res[1]["depasse_5k"] == False

    totaux_iban = iban_origine(donnees)
    assert totaux_iban["FR1"] == Decimal("7000.00")

    totaux_banque = banque_source(donnees)
    assert totaux_banque["BNP"] == Decimal("7000.00")

    totaux_dest = iban_destinataire(donnees)
    assert totaux_dest["DE1"] == Decimal("6000.00")
    assert totaux_dest["ES1"] == Decimal("1000.00")

    print("tests fonctionnel")

test_unit()