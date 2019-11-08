from mockfirestore import MockFirestore

from firestore_auth import authenticate


def test_correct_login():
    client = MockFirestore()
    client.collection("users").add(
        {"username": "fatcat2", "password": "boilerup"}
    )

    assert authenticate("fatcat2", "boilerup", db=client)
