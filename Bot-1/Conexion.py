from dotenv import load_dotenv
import os

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Obtiene el valor del token
token = os.getenv('token')
