""""
Дан словарь (смотрите пример ниже) ключами которого являются английские слова, а занчениями - списки латинских слов. 
Необходимо развеннуть словарь. Другими словани, необходимо, на основании заданного словаря, создать новый словарь, 
у которого в качестве ключей будут взяты латинские слова, из исходного словаря, а значениями будет список, 
соответствующих им, английских слов.
"""""
from collections import defaultdict

d = {

    'apple': ['malum', 'pomum', 'popula'],

    'fruit': ['baca', 'bacca', 'popum'],

    'punishment': ['malum', 'multa']

}
new_dict = defaultdict(list)
for key, values in d.items():
    for value in values:
        new_dict[value].append(key)
print(new_dict)