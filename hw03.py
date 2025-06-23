import sys
from pathlib import Path
from colorama import init, Fore, Style
# hw03.py
init(autoreset=True)
                  
def print_directory_structure(path: Path, prefix: str = ""):
    """Функція для виведення структури директорії у вигляді дерева."""
    if not path.is_dir():
        print(Fore.RED + f"Помилка: {path} не є директорією.")
        return
    entries = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
    for i, entry in enumerate(entries):
        connector = "┗━ " if i == len(entries) - 1 else "┣━ "

        if entry.is_dir():
            print(prefix + Fore.BLUE + connector + entry.name)
            new_prefix = prefix + ("   " if i == len(entries) - 1 else "┃  ")
            print_directory_structure(entry, new_prefix)
        else:
            print(prefix + Fore.GREEN + connector + entry.name)

def main():
    """Головна функція для запуску скрипту."""
    if len(sys.argv) != 2:
        print("Використання: python hw03.py /шлях/до/директорії")
        return

    dir_path = Path(sys.argv[1])
    # Перевірка, чи існує шлях і чи є він директорією
    if not dir_path.exists(): 
        print(Fore.RED + f"Помилка: Шлях '{dir_path}' не існує.")
        return
    if not dir_path.is_dir():
        print(Fore.RED + f"Помилка: '{dir_path}' не є директорією.")
        return

    print(Fore.YELLOW + f"📦 {dir_path.name}")
    print_directory_structure(dir_path)

if __name__ == "__main__":
    main()

# Перевірка кода - python hw03.py "C:\Users\vikak\OneDrive\Робочий стіл\Інна\Neoversity\Projects\My_Repository\goit-pycore-hw-04"
