# 2-е испытание
def shlyapa():
print('Ты попал в комнату ,думал сразу после Пушка на Волдеморта? Выбирай- либо расслабиться,либо использовать палочку, либо попытаться выбраться?')
x = input()
if x == 'расслабиться':
    print('Ты проволился в какую-то комнату, а ещё, у тебя голюны.')
else:
    if x == 'использовать_палочку' or 'попробоват выбраться':
        print('Какие заклинания ты знаешь? Правильный ответ- ты их не знаешь, и тебя задушили.')
        exit()
    else:
        print('тебя задушили')
        exit()