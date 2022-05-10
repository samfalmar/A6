from werkzeug.security import check_password_hash


# Definimos la clase con el método init que recibe id, username y password
class User():
    def __init__(self, id, username, password) -> None:
        self.id = id
        self.username = username
        self.password = password

    # @classmethod -> para no instanciar la clase 
    @classmethod
    # Verificación del hash. hashed_password -> password después del hash / password = password en texto plano
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)
