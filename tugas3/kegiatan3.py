import math

def split_numbers(number):
    return {
        'ratusan': math.floor(number / 100),
        'puluhan': math.floor((number % 100) / 10),
        'satuan': number % 10
    }

def classify_numbers(numbers):
    floats = []
    ints = []
    strings = []

    for number in numbers:
        if isinstance(number, float):
            floats.append(number)
        elif isinstance(number, int):
            ints.append(number)
        elif isinstance(number, str):
            strings.append(number)

    return floats, ints, strings

def classify_and_split_numbers(numbers):
    floats, ints, strings = classify_numbers(numbers)
    ints_splitted = list(map(split_numbers, ints))
    return floats, ints_splitted, strings

random_list = [3.1, 2.7, 5.5, 105, 737, 412, "Hello", "Python", "world", "AI"]

floats, ints, strings = classify_and_split_numbers(random_list)

print("Data Float:")
for f in floats:
    print(f)

print("\nData Int:")
for i in ints:
    print(i)

print("\nData String:")
for s in strings:
    print(s)