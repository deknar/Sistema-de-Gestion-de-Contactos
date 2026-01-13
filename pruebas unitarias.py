import unittest
from contactos import GestorContactos, Contacto

# Clase con las pruebas del gestor de contactos
class TestGestorContactos(unittest.TestCase):
    
    # Se ejecuta antes de cada test, crea 2 contactos de prueba
    def setUp(self):
        self.gestor = GestorContactos()
        self.gestor.agregar_contacto("Juan", "12345678", "juan@gmail.com", "Calle 1")
        self.gestor.agregar_contacto("Maria", "87654321", "maria@outlook.com", "Calle 2")
        self.contacto1 = self.gestor.buscar_por_telefono("12345678")
        self.contacto2 = self.gestor.buscar_por_telefono("87654321")

    # Prueba agregar un contacto nuevo
    def test_agregar_contacto(self):
        print("\n--- Test Agregar Contacto ---")
        print(f"Contactos antes: {len(self.gestor.listar_contactos())}")
        resultado = self.gestor.agregar_contacto("Pedro", "11223344", "pedro@example.com", "Calle 3")
        print(f"Resultado de agregar Pedro: {resultado}")
        print(f"Contactos después: {len(self.gestor.listar_contactos())}")
        self.assertTrue(resultado)
        self.assertEqual(len(self.gestor.listar_contactos()), 3)

    # Los siguientes tests prueban buscar, editar y eliminar - misma estructura
    def test_buscar_por_telefono(self):
        print("\n--- Test Buscar por Teléfono ---")
        encontrado = self.gestor.buscar_por_telefono("12345678")
        print(f"Buscando teléfono '12345678': {encontrado.nombre if encontrado else 'No encontrado'}")
        no_encontrado = self.gestor.buscar_por_telefono("99999999")
        print(f"Buscando teléfono '99999999': {no_encontrado}")
        self.assertEqual(encontrado, self.contacto1)
        self.assertEqual(no_encontrado, None)

    def test_buscar_por_nombre(self):
        print("\n--- Test Buscar por Nombre ---")
        encontrados = self.gestor.buscar_por_nombre("Juan")
        print(f"Buscando nombre 'Juan': {len(encontrados)} contacto(s) encontrado(s)")
        no_encontrados = self.gestor.buscar_por_nombre("Pedro")
        print(f"Buscando nombre 'Pedro': {len(no_encontrados)} contacto(s) encontrado(s)")
        self.assertEqual(encontrados, [self.contacto1])
        self.assertEqual(no_encontrados, [])

    def test_editar_contacto(self):
        print("\n--- Test Editar Contacto ---")
        print(f"Nombre antes: {self.gestor.buscar_por_telefono('12345678').nombre}")
        resultado = self.gestor.editar_contacto("12345678", nombre="Juanito")
        print(f"Resultado de edición: {resultado}")
        print(f"Nombre después: {self.gestor.buscar_por_telefono('12345678').nombre}")
        self.assertTrue(resultado)
        self.assertEqual(self.gestor.buscar_por_telefono("12345678").nombre, "Juanito")

    def test_eliminar_contacto(self):
        print("\n--- Test Eliminar Contacto ---")
        print(f"Contactos antes: {len(self.gestor.listar_contactos())}")
        resultado = self.gestor.eliminar_contacto("12345678")
        print(f"Resultado de eliminar teléfono '12345678': {resultado}")
        print(f"Contactos después: {len(self.gestor.listar_contactos())}")
        self.assertTrue(resultado)
        self.assertEqual(len(self.gestor.listar_contactos()), 1)

if __name__ == '__main__':
    unittest.main()
