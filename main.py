from math import factorial
import colorama

def progress_bar(progress, total, color=colorama.Fore.BLUE):
    percent = 100 * (progress / float(total))
    bar = '■' * int(percent) + '-' * (100 - int(percent))
    print(color + f'\r|{bar}| {percent:.2f}%', end='')
    if progress == total:
        print(colorama.Fore.GREEN + f'\r|{bar}| {percent:.2f}%', end='\r')

numbers = [x * 5 for x in range(2900, 3000)]
results = []

for i, x in enumerate(numbers):
    results.append(factorial(x))
    progress_bar(i + 1, len(numbers))

print(colorama.Fore.RESET)
