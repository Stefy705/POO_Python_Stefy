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

# METODO que dejaremos preparado ´para aplicar POLIMORFIRMO mas adelante 
def vender_producto(self):
    # Cada clase hija declarara como implementar vender prodcuto 
    print(f"El dron {self.modelo} ha sido vendido, gracias por la compra")

# CREAR LA INSTANCIA DE LA CLASE DRONES
dron_1 = Drones ( 1, "DJI", "Mavic 4 Pro", "1063gr", 8700.000)
dron_2 = Drones ( 2, "DJI", "Mini 5 Pro", "250gr", 3300.000 )
dron_3 = Drones (3, "DJI", "Air 3S", "724gr", 4550.000)
dron_4 = Drones (4, "DJI", "Avata 2", "377gr", 4100.000)

    #HERENCIA padre a hijos

class Dron_Creativo(Drones):
    def __init__ (self, id_dron:int, marca:str, modelo:str, peso:str, precio:float, colorLed:str, modoVuelo:str, resistenciaViento:str, nivelHabilidad:str, modoAvanzado:str, grabar4k= "Grabacion 4k"):

        # Usamos Super() para llamar al constructor de la clase de padre(Drones)
        super().__init__(id_dron, marca, modelo, peso, precio) #No lleva el self, el super viene con el self, y tampoco lleva str,int etc.

        # Atributos propios del hijo
        self.colorLed = colorLed
        self.modoVuelo = modoVuelo
        self.resistenciaViento = resistenciaViento
        # Metodos propios del hijo
        self.nivelHabilidad = nivelHabilidad
        self.modoAvanzado = modoAvanzado
        self.grabar4k = grabar4k


dronMavic= (1, "DJI", "Mavic 4 Pro", "1063gr", 8700.000, "verde", "Modo Sport", "Escala Beaufort 7 (Viento Fuerte)", "Avanzado", "Uso deportivo" )
dronMini= (2, "DJI", "Mini 5 Pro", "250gr", 3300.000, "azul", "Modo Cine", "Escala Beaufort 5 (Brisa Moderada)", "Principiante", "Uso creativo")
dronAir = (3, "DJI", "Air 3S", "724gr", 4550.000, "morado", "Modo Posicion", "Escala Beaufort 6 (Brisa fuerte)", "Intermedio", "Uso creativo")
dronAva = (4, "DJI", "Avata 2", "377gr", 4100.000, "rojo", "Modo Acro", "Escala Beaufort 5 (Brisa moderada)", "Intermedio", "Uso deportivo")

#POLIMORFISMO 

#ENCAPSULMIENTO GET PARA OBTENER SET PARA MODIFICAR
# GET VER O CONSULTAR  UN ATRIBUTO
# def get_resultados(self):
  #   return self.__resultados

# SET MODIFICAR O CONSULTAR 

# def set_resultados(self, notas):
#   self.__resultados.append(notas)
#   print(f"resultado guardado para el aprendiz {self.nombre} total notas: {len(self.resultados)}")

# print(f"imprimir privado {aprendiz_1.get_resultado}")


# CLASE DRON PROFESIONAL 
#--------------------
class Dron_Profesional(Drones):
    def __init__ (self, id_dron:int, marca:str, modelo:str, peso:str, precio:float, rangoSensor:int, almacenamientoInterno:str, resolucionCamara:int, vueloNocturno:str, mapearZona:str):

        super().__init__(id_dron, marca, modelo, peso, precio)

        self.rangoSensor = rangoSensor
        self.almacenamientoInterno = almacenamientoInterno
        self.resolucionCamara = resolucionCamara
        self.vueloNocturno = vueloNocturno
        self.mapearZona = mapearZona

dronRTK = (1,"DJI" "Matrice 350 RTK", "6.47kg", 52000.000, "Zoom 400x", "Ninguno", "45MP", "FPV + Térmica", "Mapeo 2D/3D con DJI Terra")
dronEvo = (2,"Autel" "EVO Max 4T", "1.64kg", 26000.000, "Zoom 160x", "128GB", "50MP", "Radar de ondas milimétricas", "Mapeo 3D nativo")
dronIns = (3,"DJI" "Inspire 3", "3.99kg", 75000.000, "Lentes DL Full-Frame", "1TB PROSSD", "8.1K", "Cámara FPV Starlight", "Trayectorias Waypoints Pro")
dronEnter = (4,"DJI" "Mavic 3 Enterprise", "915g", 18500.000, "Zoom 56x", "64GB", "20MP", "Infrarrojos omnidireccionales", "Obturador mecánico RTK")





#POLIMORFISMO 

#ENCAPSULMIENTO GET PARA OBTENER SET PARA MODIFICAR
# GET VER O CONSULTAR  UN ATRIBUTO
# def get_resultados(self):
  #   return self.__resultados

# SET MODIFICAR O CONSULTAR 

# def set_resultados(self, notas):
#   self.__resultados.append(notas)
#   print(f"resultado guardado para el aprendiz {self.nombre} total notas: {len(self.resultados)}")

# print(f"imprimir privado {aprendiz_1.get_resultado}")
# # SIMBOLOS DE PRIVADO __ doble guion bajo, 
