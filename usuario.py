# class Usuarios: #class primera letra en mayuscula
#     id_usuario = 1
#     documento = 123456789
#     nombre = "Sofía García"
#     apellido = "García"
#     correo = "sofia.garcia@gmail.com"
#     telefono = "555-1234"
#     direccion = "Calle 183"

# #CREAR UNA INSTANCIA DE LA CLASE USUARIOS 
# usuario_1 = Usuarios() 
# usuario_2= Usuarios() #se duplica la misma información
# print(usuario_1.direccion)


lista_usuarios = []  #lista vcia para almacenar los usuarios creados

class Usuario:
    #crear una funcion para el constructor
    def __init__(self, id_usuario, documento, nombre, apellido, direccion, correo, telefono):
        self.id_usuario = id_usuario
        self.documento = documento
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.correo = correo
        self.telefono = telefono

#ejemplo de metodo para saludar al usuario
    def saludar(self):
        print(f"Mi nombre es {self.nombre} {self.apellido} ")

    # METODOS BASE DEL CRUD
    # Create 
    def crear_usuario(self):
        lista_usuarios.append(self) #append para agregar el usuario a la lista
        print(f"Se guardo el usuario {self.nombre} exitosamente")
    
    #READ 
    def mostrar_usuario(self):
        print(f"id: {self.id_usuario} nombre: {self.nombre} apellido: {self.apellido} correo: {self.correo} ")

    #ACTUALIZAR USUARIO
    def actualizar_usuario(self, nuevo_nombre, nuevo_apellido):
        self.nombre = nuevo_nombre
        self.apellido = nuevo_apellido
        print(f"El usuario {self.id_usuario} se actualizo exitosamente a {self.nombre} {self.apellido}✅")

    #ELIMINAR USUARIO
    def eliminar_usuario(self):
        if self in lista_usuarios: # si el objeto esta dentro de la lista de usuarios 
            lista_usuarios.remove(self) #remove para eliminar el usuario de la lista
            print(f"El usuario {self.nombre} se elimino exitosamente✅")
        else:
            print(f"El usuaro {self.nombre} no se encuentra en el sistema❌")


# crear una instancia de la clase usuario
usuario_1 = Usuario(1, 123456789, "Juliana", "García", "Calle 183", "ander.garcia@gmail.com", "5575-12348")
print(usuario_1.nombre)
print (usuario_1.correo) 
 
usuario_2 = Usuario(2, 98796787, "Carlos", "Lopez", "carrera 45", "carlos.lopez@gmail.com", "5575-12349")
print(usuario_2.correo) 

usuario_1.saludar()
usuario_2.saludar()

# llamar a los metodos de la clase usuario 
usuario_1.mostrar_usuario()
print(f"Lista de usuarios: {lista_usuarios}") #lista vacia
#llamar el metodo crear usuario para agregar los usuarios a la lista
usuario_1.crear_usuario() #agregar el usuario a la lista
print(f"Lista de usuarios: {lista_usuarios[0].nombre}") #con el index 0 accedemos al primer usuario de la lista y mostramos su nombre
usuario_2.crear_usuario() #agregar el usuario a la lista
print(f"Lista de usuarios: {[usuario.nombre for usuario in lista_usuarios]}") #mostrar los nombres de los usuarios en la lista
#LLamaer el metodo eliminar usuario
usuario_1.eliminar_usuario() #eliminar el usuario de la lista
#LLAMAR LOS METODOS UPDATE 
usuario_1.actualizar_usuario("Felipe", "Gomez") #actualizar el nombre y apellido del usuario
usuario_1.mostrar_usuario()
