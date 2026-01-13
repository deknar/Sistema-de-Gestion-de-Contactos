# Sistema de Gestion de Contactos

Proyecto realizado para el modulo 2 del curso de especialidad en ciencia de datos.

Sistema desarrollado en Python para la gestion de contactos personales mediante una interfaz de consola.

---

## Estructura del Proyecto

```
Proyecto Modulo 2/
|-- contactos.py          # Clases principales del sistema
|-- menu.py               # Interfaz de usuario (consola)
|-- pruebas unitarias.py  # Pruebas unitarias del sistema
|-- README.md             # Documentacion del proyecto
|-- INFORME_PRUEBAS.md    # Informe de resultados de pruebas
```

---

## Modulos Utilizados

### contactos.py

Contiene las clases principales del sistema:

**Clase Contacto:**
- Representa un contacto individual con atributos privados (encapsulamiento)
- Atributos: nombre, telefono, email, direccion
- Implementa getters y setters mediante decoradores @property
- Metodo `__str__` para representacion en texto

**Clase GestorContactos:**
- Administra la coleccion de contactos
- Utiliza una lista para mantener el orden de insercion
- Utiliza un diccionario para busquedas rapidas por telefono
- Metodos: agregar, buscar, editar, eliminar y listar contactos

### menu.py

Interfaz de usuario basada en consola:

- `mostrar_menu()`: Despliega las opciones disponibles
- `main()`: Funcion principal que ejecuta el bucle del programa

Opciones del menu:
1. Agregar Contacto
2. Buscar Contacto (por nombre o telefono)
3. Editar Contacto
4. Eliminar Contacto
5. Listar Todos los Contactos
6. Salir

### pruebas unitarias.py

Pruebas automatizadas usando el modulo `unittest`:

- `test_agregar_contacto`: Verifica la creacion de contactos
- `test_buscar_por_telefono`: Verifica busqueda por telefono
- `test_buscar_por_nombre`: Verifica busqueda por nombre
- `test_editar_contacto`: Verifica la edicion de datos
- `test_eliminar_contacto`: Verifica la eliminacion de contactos

---

## Arquitectura

El sistema sigue el patron de arquitectura en capas:

```
+-------------------+
|   menu.py         |  <-- Capa de Presentacion (Interfaz de Usuario)
+-------------------+
         |
         v
+-------------------+
|  GestorContactos  |  <-- Capa de Logica de Negocio
+-------------------+
         |
         v
+-------------------+
|    Contacto       |  <-- Capa de Datos (Modelo)
+-------------------+
```

**Principios aplicados:**
- Encapsulamiento: Atributos privados con getters/setters
- Separacion de responsabilidades: Cada clase tiene una funcion especifica
- Validacion de datos: Verificacion de duplicados por telefono

---

## Instrucciones para Ejecutar en Entorno Local

### Pasos de Instalacion

1. **Clonar o descargar el repositorio:**
   ```bash
   git clone https://github.com/deknar/Sistema-de-Gestion-de-Contactos.git
   cd Sistema-de-Gestion-de-Contactos
   ```

2. **Verificar la instalacion de Python:**
   ```bash
   python --version
   ```

### Ejecucion de la Aplicacion

```bash
python menu.py
```

### Ejecucion de Pruebas Unitarias

```bash
python -m unittest "pruebas unitarias.py" -v
```

---

## Ejemplo de Uso

```
--- Sistema de Gestion de Contactos ---
1. Agregar Contacto
2. Buscar Contacto
3. Editar Contacto
4. Eliminar Contacto
5. Listar Todos los Contactos
6. Salir
Seleccione una opcion: 1

--- Agregar Contacto ---
Nombre: Juan Perez
Telefono: 12345678
Email: juan@email.com
Direccion: Calle Principal 123
Contacto agregado exitosamente.
```

---