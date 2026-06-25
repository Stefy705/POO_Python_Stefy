#--------------INVENTARIO DE DRONES------------------

lista_drones  = [] #lista vacia para almacenar los drones creados

class Drones: 
#creamos una funcion para el constructor
    def __init__(self, id_dron:int, marca:str, modelo:str, peso:str, precio:float):
        self.id_dron = id_dron
        self.marca = marca
        self.modelo = modelo
        self.peso = peso
        self.__precio = precio  # ENCAPSULAMIENTO - atributo privado con doble guion bajo __

    #----------METODOS DEL CRUD------------
    #Crear / registrar un dispositivo, creamos la funcion
    def registrar_dron(self):
        lista_drones.append(self)
        print(f"Se guardo el dron {self.modelo} exitosamente")

    #READ / VER los drones
    def consultar_drones(self):
        print(f"El Dispositivo Electrico con el ID: {self.id_dron} Modelo: {self.modelo} Peso: {self.peso} Precio {self.__precio}")

    #UPDATE /  Actualizar datos dron
    def actualizar_dispo(self, nueva_marca, nuevo_modelo, nuevo_peso, nuevo_precio):
        self.marca = nueva_marca
        self.modelo = nuevo_modelo
        self.peso = nuevo_peso
        self.__precio = nuevo_precio  # usamos el setter para actualizar el precio encapsulado
        print(f"El Dron {self.id_dron} se actualizo correctamente a el Modelo:{self.modelo} Marca:{self.marca} Peso:{self.peso} Precio:{self.__precio}")

    # DELETE / Eliminar un dispositivo del inventario
    def eliminar_dron(self):
        if self in lista_drones:
            lista_drones.remove(self)
            print(f"El Dron {self.modelo} se elimino correctamente✅")
        else:
            print(f"El Dron {self.modelo} no se encuentra en el sistema ❌")

    # METODO que dejaremos preparado para aplicar POLIMORFISMO mas adelante 
    def vender_producto(self):
        # Cada clase hija declarara como implementar vender producto 
        print(f"El dron {self.modelo} ha sido vendido, gracias por la compra")

    #----------ENCAPSULAMIENTO GET Y SET------------
    # GET VER O CONSULTAR UN ATRIBUTO PRIVADO
    def get_precio(self):
        return self.__precio

    # SET MODIFICAR UN ATRIBUTO PRIVADO
    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0:  #indicacion para aceptar un valor especifico de precio
            self.__precio = nuevo_precio
            print(f"Precio actualizado correctamente a: {self.__precio}")
        else:
            print(f"El precio no puede ser 0 o negativo ❌")


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

    #POLIMORFISMO - sobreescribimos vender_producto del padre con el comportamiento del hijo creativo
    def vender_producto(self):
        print(f"✅ Venta CREATIVO completada: El dron {self.modelo} fue vendido como dron creativo/recreativo")
        print(f"   Incluye: Luces LED {self.colorLed} | {self.modoVuelo} | Nivel: {self.nivelHabilidad}")


# CREAR LA INSTANCIA DE LA CLASE DRON_CREATIVO

dronMavic = Dron_Creativo(1, "DJI", "Mavic 4 Pro", "1063gr", 8700.000, "verde", "Modo Sport", "Escala Beaufort 7 (Viento Fuerte)", "Avanzado", "Uso deportivo")
dronMini  = Dron_Creativo(2, "DJI", "Mini 5 Pro", "250gr", 3300.000, "azul", "Modo Cine", "Escala Beaufort 5 (Brisa Moderada)", "Principiante", "Uso creativo")
dronAir   = Dron_Creativo(3, "DJI", "Air 3S", "724gr", 4550.000, "morado", "Modo Posicion", "Escala Beaufort 6 (Brisa fuerte)", "Intermedio", "Uso creativo")
dronAva   = Dron_Creativo(4, "DJI", "Avata 2", "377gr", 4100.000, "rojo", "Modo Acro", "Escala Beaufort 5 (Brisa moderada)", "Intermedio", "Uso deportivo")


# CLASE DRON PROFESIONAL 
#--------------------
class Dron_Profesional(Drones):
    def __init__ (self, id_dron:int, marca:str, modelo:str, peso:str, precio:float, rangoSensor:str, almacenamientoInterno:str, resolucionCamara:str, vueloNocturno:str, mapearZona:str):

        super().__init__(id_dron, marca, modelo, peso, precio)

        self.rangoSensor = rangoSensor
        self.almacenamientoInterno = almacenamientoInterno
        self.resolucionCamara = resolucionCamara
        self.vueloNocturno = vueloNocturno
        self.mapearZona = mapearZona

    #POLIMORFISMO - sobreescribimos vender_producto del padre con el comportamiento del hijo profesional
    def vender_producto(self):
        print(f"✅ Venta PROFESIONAL completada: El dron {self.modelo} fue vendido como dron profesional/industrial")
        print(f"   Incluye: Sensor {self.rangoSensor} | Camara {self.resolucionCamara} | {self.mapearZona}")


# CREAR LA INSTANCIA DE LA CLASE DRON_PROFESIONAL

dronRTK   = Dron_Profesional(1, "DJI", "Matrice 350 RTK", "6.47kg", 52000.000, "Zoom 400x", "Ninguno", "45MP", "FPV + Termica", "Mapeo 2D/3D con DJI Terra")
dronEvo   = Dron_Profesional(2, "Autel", "EVO Max 4T", "1.64kg", 26000.000, "Zoom 160x", "128GB", "50MP", "Radar de ondas milimetricas", "Mapeo 3D nativo")
dronIns   = Dron_Profesional(3, "DJI", "Inspire 3", "3.99kg", 75000.000, "Lentes DL Full-Frame", "1TB PROSSD", "8.1K", "Camara FPV Starlight", "Trayectorias Waypoints Pro")
dronEnter = Dron_Profesional(4, "DJI", "Mavic 3 Enterprise", "915gr", 18500.000, "Zoom 56x", "64GB", "20MP", "Infrarrojos omnidireccionales", "Obturador mecanico RTK")


#===========================================================
#................PRUEBAS DEL SISTEMA.......................
#===========================================================

print("\n========== PRUEBA 1: REGISTRAR DRONES ==========")
dronMavic.registrar_dron()
dronMini.registrar_dron()
dronAir.registrar_dron()
dronAva.registrar_dron()
dronRTK.registrar_dron()
dronEvo.registrar_dron()
dronIns.registrar_dron()
dronEnter.registrar_dron()

print("\n========== PRUEBA 2: CONSULTAR DRONES ==========")
dronMavic.consultar_drones()
dronRTK.consultar_drones()

print("\n========== PRUEBA 3: ACTUALIZAR UN DRON ==========")
dronMini.actualizar_dispo("DJI", "Mini 6 Pro", "260gr", 3800.000)

print("\n========== PRUEBA 4: ENCAPSULAMIENTO - GET Y SET ==========")
print(f"Precio actual del Mavic 4 Pro (GET): {dronMavic.get_precio()}")
dronMavic.set_precio(9200.000)

print("\n========== PRUEBA 5: POLIMORFISMO - VENDER PRODUCTO ==========")
print("    Dron Creativo     ")
dronAva.vender_producto()
print()
print("    Dron Profesional   ")
dronIns.vender_producto()

print("\n========== PRUEBA 6: ELIMINAR UN DRON ==========")
dronAir.eliminar_dron()
dronAir.eliminar_dron()  # segunda vez para probar el mensaje de error

print("\n========== ESTADO FINAL DEL INVENTARIO ==========")
print(f"Total de drones en inventario: {len(lista_drones)}")
for dron in lista_drones:
    dron.consultar_drones()