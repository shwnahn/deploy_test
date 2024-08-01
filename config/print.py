
from pathlib import Path
import os 
import environ
env = environ.Env()

BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(BASE_DIR / './.env')
print(env('DB_HOST'))
print(env('DB_NAME'))
print(env('DB_USER'))