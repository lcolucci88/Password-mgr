# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
#                'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
#                'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
# nr_letters = random.randint(8, 10)
# nr_symbols = random.randint(2, 4)
# nr_numbers = random.randint(2, 4)
#
# password_letters = [random.choice(letters) for n in range(nr_letters)]
# password_numbers = [random.choice(letters) for n in range(nr_letters)]
# password_symbols = [random.choice(letters) for n in range(nr_letters)]
# print(pass_letters
#
import json

with open("readme.json", mode="r") as file:
    data = json.load(file)
    #print(data)
    print(data["Amazon"]["email"])
