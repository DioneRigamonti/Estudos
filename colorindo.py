from colorama import Back, Fore, init
# - - Biblioteca destinada para a coloração do terminal.
init(convert=True , autoreset=True)

print(Fore.GREEN + 'Hello World')
print(Back.GREEN + 'Hello World')
print(Fore.YELLOW + 'Hello World')
print(Back.YELLOW + 'Hello World')
print(Fore.BLUE + 'Hello World')
print(Back.BLUE + 'Hello World')
print(Fore.RED + 'Hello World')
print(Back.RED + 'Hello World')
print(Back.WHITE + 'Hello World')