def durak():
    spisok = {'brat1': [1, 'Murad', 234], 'brat2': 'maga', 'brat3': 'Shamil'}
    for s in spisok:
        if type(spisok[s]) == list:
            print(spisok[s][1])
        else:
            print(spisok[s])

durak()