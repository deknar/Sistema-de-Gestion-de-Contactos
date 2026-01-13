# Clase que representa un contacto con sus datos personales
class Contacto: 
    def __init__(self, nombre, telefono, email, direccion):
        # Guardamos los datos como privados usando guion bajo
        self._nombre = nombre
        self._telefono = telefono
        self._email = email
        self._direccion = direccion
        
    # Getter y setter para nombre - los demas (telefono, email, direccion) funcionan igual
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def telefono(self):
        return self._telefono
    
    @telefono.setter
    def telefono(self, telefono):
        self._telefono = telefono

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        self._email = email

    @property
    def direccion(self):
        return self._direccion
    
    @direccion.setter
    def direccion(self, direccion):
        self._direccion = direccion

    # Para mostrar el contacto como texto
    def __str__(self):
        return f"Nombre: {self._nombre}, Telefono: {self._telefono}, Email: {self._email}, Direccion: {self._direccion}"


# Clase que administra todos los contactos
class GestorContactos:
    def __init__(self): 
        self._contactos = []  # lista para mantener orden
        self._contactos_dict = {}  # diccionario para buscar rapido
    
    # Agrega un contacto nuevo, verifica que el telefono no exista
    def agregar_contacto(self, nombre, telefono, email, direccion):
        if telefono in self._contactos_dict:
            return False, "El número de teléfono ya está registrado."
        
        nuevo_contacto = Contacto(nombre, telefono, email, direccion)
        self._contactos.append(nuevo_contacto)
        self._contactos_dict[telefono] = nuevo_contacto
        return True, "Contacto agregado exitosamente."
    
    # Busca por telefono usando el diccionario
    def buscar_por_telefono(self, telefono):
        return self._contactos_dict.get(telefono, None)
    
    # Busca por nombre recorriendo la lista
    def buscar_por_nombre(self, nombre):
        resultados = [c for c in self._contactos if c.nombre.lower() == nombre.lower()]
        return resultados
    
    # Elimina un contacto de ambas estructuras
    def eliminar_contacto(self, telefono):
        contacto = self._contactos_dict.get(telefono, None)
        if not contacto:
            return False, "Contacto no encontrado."
        
        self._contactos.remove(contacto)
        del self._contactos_dict[telefono]
        return True, "Contacto eliminado exitosamente."
    
    # Edita los campos que se pasen, si cambia el telefono actualiza la clave
    def editar_contacto(self, telefono, nombre=None, telefono_nuevo=None, email=None, direccion=None):
        contacto = self._contactos_dict.get(telefono)
        if not contacto:
            return False, "Contacto no encontrado."

        if telefono_nuevo and telefono_nuevo != telefono:
            if telefono_nuevo in self._contactos_dict:
                return False, "El nuevo número de teléfono ya existe."
            del self._contactos_dict[telefono]
            contacto.telefono = telefono_nuevo
            self._contactos_dict[telefono_nuevo] = contacto
        
        if nombre:
            contacto.nombre = nombre
        if email:
            contacto.email = email
        if direccion:
            contacto.direccion = direccion
        return True, "Contacto actualizado exitosamente."
    
    # Devuelve todos los contactos
    def listar_contactos(self):
        return self._contactos