import random
import string

for _ in range(5):
    large_font_count = [7, 8, 9]
    small_font_count = [2, 3]
    numbers_count = []

    large_c = random.choice(large_font_count)
    small_c = random.choice(small_font_count)
    numbers_count.append(12-(large_c+small_c))
    number_c = numbers_count[-1]

    larges = random.choices(string.ascii_uppercase, k=large_c)
    smalls = random.choices(string.ascii_lowercase, k=small_c)
    nums = random.choices(string.digits, k=number_c)

    mix = larges+smalls+nums
    random.shuffle(mix)
    random_code = ''.join(mix)
    if random_code[0].islower():
        pass
    else:
        print(random_code)
