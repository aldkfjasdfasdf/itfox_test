import random
import string


def generate_token() -> str:
    # Генерация случайной строки из букв и цифр
    token_length = 255
    characters = string.ascii_letters + string.digits
    token = "".join(random.choices(characters, k=token_length))
    return token
