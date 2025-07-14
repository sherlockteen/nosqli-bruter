from colorama import Fore, Style

def info(message):
    print(f"{Fore.CYAN}[i]{Style.RESET_ALL} {message}")

def success(message):
    print(f"{Fore.GREEN}[+]{Style.RESET_ALL} {message}")

def error(message):
    print(f"{Fore.RED}[-]{Style.RESET_ALL} {message}")
