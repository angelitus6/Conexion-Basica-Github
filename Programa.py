import random  # Importa la librería random para generar números aleatorios
import string  # Importa la librería string para obtener caracteres alfanuméricos

class PasswordGenerator:
    def __init__(self):
        # Inicializa el conjunto de caracteres utilizados previamente
        self.used_characters = set()
        # Define la longitud de la contraseña
        self.password_length = 10
        # Define los caracteres permitidos (letras mayúsculas, minúsculas y dígitos)
        self.allowed_characters = list(string.ascii_letters + string.digits)
        
        # Verifica que hay suficientes caracteres únicos para generar al menos tres contraseñas
        if len(self.allowed_characters) < 3 * self.password_length:
            raise ValueError("No hay suficientes caracteres únicos para generar tres contraseñas distintas de 10 caracteres cada una.")

    def generate_password(self):
        # Filtra los caracteres disponibles eliminando los ya usados
        available_characters = [char for char in self.allowed_characters if char not in self.used_characters]

        # Verifica que hay suficientes caracteres disponibles para generar una nueva contraseña
        if len(available_characters) < self.password_length:
            raise ValueError("No hay suficientes caracteres disponibles para generar una nueva contraseña.")

        # Genera una contraseña de 10 caracteres seleccionando aleatoriamente de los caracteres disponibles
        password = ''.join(random.sample(available_characters, self.password_length))
        # Actualiza el conjunto de caracteres utilizados
        self.used_characters.update(password)
        return password

    def generate_multiple_passwords(self, count):
        # Genera múltiples contraseñas
        passwords = []
        for _ in range(count):
            passwords.append(self.generate_password())
        return passwords

# Crear una instancia del generador de contraseñas
password_generator = PasswordGenerator()

# Generar tres contraseñas y manejarlas de forma segura
try:
    password = password_generator.generate_password()
    print(f"Contraseña generada: {password}")
except ValueError as e:
    print(e)
