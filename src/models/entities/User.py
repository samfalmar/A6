from ipaddress import ip_address
from werkzeug.security import check_password_hash, generate_password_hash
import os
from string import Template

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

    # Creamos el Hash de la pw  
    @classmethod
    def hashed_password(self, password):
        return generate_password_hash(password)


class Generate():
    def generate_vagrantfile(name, OS, Cores, Memory, Hostname, Network):
            print(name)
            print(OS)
            print(Cores)
            print(Memory)
            print(Hostname)
            print(Network)
            print("Hello from User.py")
         
            if not os.path.exists('Vagrantfiles'):
                os.makedirs('Vagrantfiles')

            path = "Vagrantfiles"
            file_name = "%s_vagrantfile.txt" %name
            vagrantfile = os.path.join(path, file_name)

            #f = open(vagrantfile,"w")
            #f.write("Host Name = " + Hostname + "\n" +"OS.vm = "+ OS + "\n"+"OS.cores = "+ Cores)
            #f.write("Host Name = " + Hostname + "\n" +"OS.vm = "+ OS + "\n"+"OS.cores = "+ Cores)
            #f.close()

            # Abrimos el archivo del cual queremos leer, supongamos que en este caso
            # el archivo se llama 'config.txt'
            template_file = open('vagrantfile.txt', 'r')

            # Este es el contexto que le pasaremos al template, toma cada uno de los
            # valores del diccionario y los reemplaza por las variables que coincidan en el
            # template
            values = {
                'name': name,
                'OS': OS,
                'Cores': Cores,
                'Memory': Memory,
                'Hostname': Hostname,
                'Network': Network,
            }
            print(values)
            # Creamos el template utilizando los contenidos del archivo, en general se le
            # puede pasar strings
            base_template = Template(template_file.read())

            # Llamamos al método substitute con el contexto y nos devolverá un string con 
            # los contenidos del template reemplazados
            result = base_template.substitute(values)

            # Guardamos el resultado en un archivo el cual llamaremos 'config.sys' (Por ejemplo)
            output_file = open(vagrantfile, 'w')
            output_file.write(result)
                    
