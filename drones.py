#--------------INVENTARIO DE DRONES------------------

lista_drones  = [] #lista vacia para almacenar los drones creados

class Drones: 
#creamos una funcion para el constructor
    def __init__(self, id_dron:int, marca:str, modelo:str, peso:str, precio:float):
        self.id_dron = id_dron
        self.marca = marca
        self.modelo = modelo
        self.peso = peso
        self.precio = precio

#----------METODOS DEL CRUD------------
#Crear / registrar un dispositivo, creamos la funcion

def registrar_dron(self):
    lista_drones.append(self)
    print(f"Se guardo el usuario {self.modelo} exitosamente")

#READ / VER los drones
def consultar_drones(self):
    print(f"El Dispositivo Electrico con el ID: {self.id_dron} Modelo: {self.modelo} Peso: {self.peso} Precio {self.precio}")

#UPDATE /  Actualizar datos dron

def actualizar_usuario(self, nueva_marca, nuevo_modelo, nuevo_peso, nuevo_precio):
    self.marca = nueva_marca
    self.modelo = nuevo_modelo
    self.peso = nuevo_peso
    self.precio = nuevo_precio
    print(f"El Dron {self.id_dron} se actualizo correctamente a el Modelo:{self.modelo} Marca:{self.marca} Peso:{self.peso} Precio:{self.precio}")

# DELETE / Eliminar un dispositivo del inventario

def eliminar_dron(self):
    if self in lista_drones:
        lista_drones.remove(self)
        print(f"El Dron {self.modelo} se elimino correctamente✅")
    else:
        print(f"El Dron {self.modelo} no se encuentra en el sistema ❌")

# CREAR LA INSTANCIA DE LA CLASE DRONES
dron_1 = Drones ( 1, "DJI", "Mavic 4 Pro", "1063gr", 8700.000)
dron_2 = Drones ( 2, "DJI", "Mini 5 Pro", )
    
