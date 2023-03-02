import random
import calendar
import requests
import pyperclip

random_pokemon_index = random.randint(0, 250)
random_verbs = ['Plays','Talks', 'Hides', 'Eats', 'Types', 'Chews', 'Shoots']
months = calendar.month_name[1:]
verb = random.choice(random_verbs)
month = random.choice(months)

req = requests.get(f'https://pokeapi.co/api/v2/pokemon/{random_pokemon_index}')
pokemon_data = req.json()
pokemon = pokemon_data['name'].capitalize()


pyperclip.copy(f'{pokemon}{verb}In{month}${random_pokemon_index}')
print('Password copied to clipboard!')
