import logging

from google.cloud import firestore


def authenticate(
    username: str, password: str, collection: str = "users"
) -> bool:
    """A function to authenticate with a Firestore database.
    
    Args:
        username (str): The requester's username.
        password (str): The requester's password.
        collection (str): Keyword argument. Represents the
            the name of the collection to query.

    Returns:
        bool: True if successful, False otherwise.

    :ret type: bool
    """
    db = firestore.Client()
    user_ref = (
        db.collection(collection).where("username", "==", username).stream()
    )

    user_result = [user.to_dict() for user in user_ref]

    if len(user_result) > 1:
        logging.debug("Username and password combo not found in database.")
        return False

    if user_result[0]["password"] == password:
        return True
    else:
        logging.debug("Username and password combo not found in database.")
        return False
