import sys
from pathlib import Path
from colorama import init, Fore

# Ініціалізація Colorama
init(autoreset=True)

def print_directory_tree(directory: Path, prefix: str = ''):
    if not directory.exists():
        print(f"{Fore.RED}Error: The path {directory} does not exist.")
        return
    if not directory.is_dir():
        print(f"{Fore.RED}Error: The path {directory} is not a directory.")
        return

    print(f"{Fore.BLUE}{prefix}{directory.name}/")
    prefix += '    '
    for item in directory.iterdir():
        if item.is_dir():
            print(f"{Fore.BLUE}{prefix}{item.name}/")
            print_directory_tree(item, prefix + '    ')
        else:
            print(f"{Fore.GREEN}{prefix}{item.name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Usage: python {sys.argv[0]} <directory_path>")
        sys.exit(1)

    directory_path = Path(sys.argv[1])
    print_directory_tree(directory_path)

#python /Users/ivalextar/Desktop/GoIT-PROJECTS/MPHomework/goit-pycore-hw-04/task_three/task_three_script.py /Users/ivalextar/Desktop/GoIT-PROJECTS/MPHomework/goit-pycore-hw-04/task_three
