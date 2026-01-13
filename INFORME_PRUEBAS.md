# Informe de Pruebas

Documento detallado de las pruebas realizadas para el Sistema de Gestion de Contactos.

---

## Descripcion del Entorno de Pruebas

Cada prueba utiliza el metodo `setUp()` que prepara el entorno inicial:
- Se crea una instancia nueva de `GestorContactos`
- Se agregan 2 contactos de prueba:
  - Juan (telefono: 12345678, email: juan@gmail.com)
  - Maria (telefono: 87654321, email: maria@outlook.com)

---

## Pruebas Unitarias Realizadas

### Prueba 1: test_agregar_contacto

**Objetivo:** Verificar que el sistema permite agregar nuevos contactos correctamente.

**Procedimiento:**
1. Se parte de 2 contactos existentes
2. Se agrega un nuevo contacto (Pedro, telefono: 11223344)
3. Se verifica que el resultado sea exitoso
4. Se verifica que el total de contactos sea 3

**Resultado esperado:** El contacto se agrega y la lista contiene 3 elementos.

**Resultado obtenido:** EXITOSO

---

### Prueba 2: test_buscar_por_telefono

**Objetivo:** Verificar que la busqueda por telefono funciona correctamente.

**Procedimiento:**
1. Buscar un telefono existente (12345678)
2. Verificar que retorna el contacto correcto (Juan)
3. Buscar un telefono inexistente (99999999)
4. Verificar que retorna None

**Resultado esperado:** Retorna el contacto si existe, None si no existe.

**Resultado obtenido:** EXITOSO

---

### Prueba 3: test_buscar_por_nombre

**Objetivo:** Verificar que la busqueda por nombre funciona correctamente.

**Procedimiento:**
1. Buscar un nombre existente (Juan)
2. Verificar que retorna una lista con 1 contacto
3. Buscar un nombre inexistente (Pedro)
4. Verificar que retorna una lista vacia

**Resultado esperado:** Retorna lista con coincidencias o lista vacia.

**Resultado obtenido:** EXITOSO

---

### Prueba 4: test_editar_contacto

**Objetivo:** Verificar que el sistema permite modificar datos de un contacto.

**Procedimiento:**
1. Obtener el nombre actual del contacto (Juan)
2. Editar el nombre a "Juanito"
3. Verificar que el resultado sea exitoso
4. Verificar que el nombre cambio correctamente

**Resultado esperado:** El contacto se actualiza con los nuevos datos.

**Resultado obtenido:** EXITOSO

---

### Prueba 5: test_eliminar_contacto

**Objetivo:** Verificar que el sistema permite eliminar contactos.

**Procedimiento:**
1. Se parte de 2 contactos existentes
2. Se elimina el contacto con telefono 12345678
3. Se verifica que el resultado sea exitoso
4. Se verifica que queda 1 contacto

**Resultado esperado:** El contacto se elimina y la lista se reduce.

**Resultado obtenido:** EXITOSO

---

## Salida de Ejecucion

```
test_agregar_contacto (pruebas unitarias.TestGestorContactos) ... ok
test_buscar_por_nombre (pruebas unitarias.TestGestorContactos) ... ok
test_buscar_por_telefono (pruebas unitarias.TestGestorContactos) ... ok
test_editar_contacto (pruebas unitarias.TestGestorContactos) ... ok
test_eliminar_contacto (pruebas unitarias.TestGestorContactos) ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
```

---

## Comando para Ejecutar las Pruebas

```bash
python -m unittest "pruebas unitarias.py" -v
```

---

## Conclusion

Todas las pruebas unitarias del sistema han sido ejecutadas satisfactoriamente. Las cinco funcionalidades principales (agregar, buscar por telefono, buscar por nombre, editar y eliminar) operan correctamente segun las especificaciones del sistema.

El sistema cumple con los requisitos funcionales establecidos y esta listo para su uso.
