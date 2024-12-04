# import random
# # import my_module
#
# random_integer = random.randint(1, 10)
# print(random_integer)
#
# # print(my_module.my_favorite_number)
#
# random_numer_0_to_1 = random.random()
# print(random_numer_0_to_1)
#
# random_float = random.uniform(1 , 10)
# print(random_float)

import random

head_or_tails = random.randint(1, 2)

if head_or_tails == 1:
    print(f"HEADS - You win, the number is {head_or_tails}")
else:
    print(f"TAILS - You win, the number is {head_or_tails}")