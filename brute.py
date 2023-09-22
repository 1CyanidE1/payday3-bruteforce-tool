from itertools import product
from colorama import init, Fore
from pyfiglet import figlet_format

init(autoreset=True)


def get_combinations(digits):
    combinations = [comb for comb in product(digits, repeat=4) if all(digit in comb for digit in digits)]
    return combinations


def display_combinations(combinations):
    for combination in combinations:
        print(Fore.RED + ''.join(combination))
    print(Fore.RED + f'There are {len(combinations)} combinations in total, good luck!')


if __name__ == '__main__':
    text = figlet_format('PAYDAY 3', font='colossal')
    small_text = figlet_format('Brute Force', font='chunky')
    print(Fore.BLUE + text)
    print(Fore.RED + small_text)

    while True:
        prompt_msg = (Fore.GREEN + "|                     |                       |\n"
                      "V                     V                       V\n"
                      "===============================================\n"
                      "Enter the highlighted numbers (without spaces): ")
        digits = input(prompt_msg)
        combinations = get_combinations(digits)
        display_combinations(combinations)

        choice = input(Fore.GREEN + 'Do you want to try another set of numbers? (yes/no): ').lower()
        if choice == 'no':
            break

    input(Fore.GREEN + 'Press any button to exit...')
