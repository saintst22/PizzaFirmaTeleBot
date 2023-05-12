import json

arguments = []

with open('censorship.txt', encoding='utf-8') as file:
    for i_word in file:
        value = i_word.lower().split('\n')[0]
        if value != '':
            arguments.append(value)

with open('censorship.json', 'w', encoding='utf-8') as new_file:
    json.dump(arguments, new_file)
