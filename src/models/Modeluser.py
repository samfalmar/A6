from .entities.User import User


class ModelUser():
#Metodo login recibe self (el mismo) db para la conexión y el user para la autentificación
    @classmethod
    def login(self, db, user):
        try:
            cursor = db.connection.cursor() # Interactuar con la BBDD
            sql = """SELECT id, username, password FROM user 
                    WHERE username = '{}'""".format(user.username)
            cursor.execute(sql) # Ejecuta la sentencia sql
            row = cursor.fetchone() 
            if row != None: # Si hay algún dato resultante, si que hay usuario
                user = User(row[0], row[1], User.check_password(row[2], user.password))
                return user
            else:
                return None # En el caso de que no haya
        except Exception as ex:
            raise Exception(ex)