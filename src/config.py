#Configuración de la clave 
class Config:
        SECRET_KEY = 'j88P8HC2Mz8!dEJ^%Y'

#Configuración para el desarrollo + heredad en Config
class DevelopmentConfig(Config):
    DEBUG = False
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'ausias38'
    MYSQL_DB = 'a6'

#Creamos el diccionario
config={
    'development': DevelopmentConfig
}

