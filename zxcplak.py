import json
import csv
FilePath = "Сохранения.json"
CSV_Path = "Результаты.csv"
Info = {
    'User name': '',
    'Current place' : 'start',
    'Choice' : 0}
places = {
    'start': {
        'description': 'Комната погружена в тишину. На столе лежит пыльная книга с золотым замком на обложке. '
                       'Загадочный свет проникает сквозь щели занавесей и придает комнате волшебное настроение. '
                       'Где-то в этом мире существует девочка по имени Эвелин, которую все окружающие называли гномом '
                       'из-за ее маленького роста. Все ее детство она испытывала на себе насмешки и пренебрежение, '
                       'но в ее сердце жил огонек решимости и смелости.',
        'options': ['Да', 'Нет'],
        'places': ['Adventure', 'End']
    },
    'End': {
        'description': 'Вы растворились в волшебной пыли.',
        'options': [],
        'places': []
    },
    'Adventure': {
        'description': 'С каждым днем она все больше стремилась к приключениям и открыть для себя новый мир за пределами своей деревни. '
                       'И в один прекрасный день она приняла решение отправиться в путешествие, чтобы найти свое место в мире и показать всем, что она достойна большего, чем прозвище гнома.',
        'options': ['Пойти к мудрецу Алберту', 'Исследовать таинственный лес'],
        'places': ['Albert', 'MysteriousForest']
    },
    'Albert': {
        'description': 'Эвелин решает пойти к мудрецу Алберту, который славится своей мудростью и знаниями о внутренней силе людей. '
                       'Может быть, он поможет ей найти ответы на ее вопросы и предложит направление для ее путешествия.',
        'options': ['Выполнить советы мудреца Алберта и попытаться создать империю.', 'Попробовать найти ответы на свои вопросы в разговоре с мудрецом.'],
        'places': ['Empire', 'Questions']
    },
    'MysteriousForest': {
        'description': 'Эвелин решает отправиться в таинственный лес, который считается местом встречи с волшебством и загадками. '
                       'Может быть, эти земли откроют перед ней новые возможности и приключения.',
        'options': ['Поздороваться и попытаться подружиться', 'Быстро уклониться и пойти в другую сторону'],
        'places': ['MeetCreature', 'ContinueAlone']
    },
    'Empire': {
        'description': 'Мудрец предложил вам создать собственную империю, где будут только маленькие люди для захвата волшебного мира.',
        'options': [],
        'places': []
    },
    'Questions': {
        'description': 'Было нечто волшебное в воздухе, и девочка чувствовала, что что-то особенное должно произойти. '
                       'И вот, когда она шла по тропинке, она встретила волшебную фею, блестящую и легкую, словно частица освещенного воздуха. '
                       'Фея, по имени Ариэль, заметила, что Эвелин нуждается в помощи и решила помочь ей.',
        'options': [],
        'places': []
    },
    'MeetCreature': {
        'description': 'Эвелин решает поздороваться с таинственным созданием и попытаться подружиться с ним. '
                       'Она признается, что и сама ищет свое место в мире и надеется на его помощь и советы.',
        'options': [],
        'places': []
    },
    'ContinueAlone': {
        'description': 'Эвелин продолжала свое путешествие через таинственный лес, под ветрами шепчущих деревьев и сиянием таинственного света, '
                       'проникающего сквозь листву. Вокруг ее шептались таинственные создания, которые наблюдали за ней из тени.',
        'options': ['Поздороваться и попытаться подружиться', 'Быстро уклониться и пойти в другую сторону'],
        'places': ['MeetCreature', 'ContinueAlone']
    }
}

def load_Save():
    with open(FilePath, "r", encoding='utf-8') as save_file:
        return json.load(save_file)
def save_Pos():
    with open(FilePath, "w", encoding='utf-8') as save_file:
        json.dump(Info, save_file)
def save_toTable():
    headers = ["User name", "Current place", "Choice"]
    data = [Info]
    with open(CSV_Path, "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames = headers, delimiter = ';')
        writer.writeheader()
        writer.writerows(data)


def show_options(place):
    if 'options' in places[place]:
        options = places[place]['options']
        for i, option in enumerate(options):
            print(f"{i + 1}. {option}")

def make_choice(options):
    if options == []:
        return -1
    try:
        choice = int(input()) - 1
    except ValueError:
        exit()
    if choice < 0 or choice >= len(options):
        exit()
    return choice

def go_to_place(place, choice):
    next_place = places[place]['places'][choice]
    return next_place

def show_description(place):
    if 'description' in places[place]:
        print(places[place]['description'])

def play_game(Place):
    print("Не соизволите ли вы загрузить существующий файл")
    if input() == "да":
        Place = load_Save()
    else:
        Place['User name'] = input("Введите ваш псевдоним")
    current_place = Place['Current place']
    while current_place != '':
        show_description(current_place)
        show_options(current_place)
        choice = make_choice(places[current_place]['options'])
        Place['Choice'] = choice
        if choice == -1:
            Place['Choice'] = 0
            break
        print("Не соизволите ли вы сохраниться (да)")
        if input() == "да":
            save_Pos()
        current_place = go_to_place(current_place, choice)
    return Place
    print("Конец игры.")

Info = play_game(Info)
save_toTable()
    