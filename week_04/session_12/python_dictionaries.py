# hooson toli bcihig 
empty_dict = {}
empty_dict = dict()

# Anhnii utgatai toli bichig (key, value)
student = {
    "ner": "bat", 
    "nsd": 30,
    "hot": "ulaanbaatar",
}

# olon turliin ugugdul aguulsan toli bichig 
mixed_dict = {
    "too": 42,
    "useg": "a",
    "jagsaalt": [1, 2, 3],
    "kortej": (4, 5, 6),
    "logic": True,
    "ded_toli": {"x": 1, "y": 2},
}

# dict() functionaar toli bichig uusgeh 
person = dict(ner="Bold", nas=25, hot="darhan")

# Tulhuur-utga hosloloos toli bichig uusgeh
items = [("alim", 3), ("banana", 5), ("jurj", 2)]
fruit_count = dict(items)

# Toli bichgiin elemented handah 
student = {"нэр": "Бат", "нас": 20, "хот": "Улаанбаатар"}

# Tulhuureer handah
name = student["нэр"]  # "Бат"

# get() argiig ashiglah (tulhuur baihgui bol aldaa zaahgui)
age = student.get("nas")  # 20 
email = student.get("email")  # None (tulhuur baihgui)
email = student.get("email", "medeelel baihui") # "medeelel baihgui"

#toli bichgiin elementiig uurchluh
student = {"ner": "Bat", "nas":20, "hot":"ulaanbaatar"}

# Element uurchluh
student["nas"] = 21

# Shine element nemeh 
student["mergejil"] = "Programist"

# Olon element nemeh/uurchluh
student.update({"нас": 22, "утас": "99112233", "хот": "Дархан"})
print(student)
# {'нэр': 'Бат', 'нас': 22, 'хот': 'Дархан', 'мэргэжил':
# 'Програмист', 'утас': '99112233'}

# Толь бичгийн элементийг устгах
student = {"нэр": "Бат", "нас": 20, "хот": "Улаанбаатар", "мэргэжил": "Програмист"}

# pop() аргаар устгах - устгасан элементийн утгыг буцаана
age = student.pop("нас")  # age = 20

# popitem() аргаар сүүлийн элементийг устгах
last_item = student.popitem()  # last_item = ('мэргэжил', 'Програмист')

# del түлхүүр үгээр устгах
del student["хот"]

# buh elementiig ustgah 
student.clear() # {}




student = {
    "ner": "bat",
    "nsd": 20,
    "hot": "ulaanbatar"
}

# buh tulhuuriig avah
keys = student.keys() # dict_keys('ner', )

student = {"нэр": "Бат", "нас": 20, "хот": "Улаанбаатар"}

# Бүх түлхүүрийг авах
keys = student.keys()  # dict_keys(['нэр', 'нас', 'хот'])
# Бүх утгыг авах
values = student.values()  # dict_values(['Бат', 20, 'Улаанбаатар'])
# Бүх түлхүүр-утга хослолыг авах
items = (
    student.items()
)  # dict_items([('нэр', 'Бат'), ('нас', 20), ('хот', 'Улаанбаатар')])
# Жагсаалт болгох
keys_list = list(student.keys())  # ['нэр', 'нас', 'хот']
# Түлхүүр шалгах
student = {"нэр": "Бат", "нас": 20, "хот": "Улаанбаатар"}
# in операторыг ашиглах
has_name = "нэр" in student  # True
has_email = "имэйл" in student  # False
# Түлхүүр байхгүй бол анхны утга оноох
email = student.setdefault("имэйл", "bat@example.com")  # "bat@example.com"
print(
    student
)  # {'нэр': 'Бат', 'нас': 20, 'хот': 'Улаанбаатар', 'имэйл': 'bat@example.com'}

# toli bichgiig davhtah 
student = {
    "ner": "bat",
    "nsd": 20,
    "hot": "ulaanbatar"
}

# tulhuureer davtah 
for key in student:
    print(f"{key}: {student[key]}")

# tulhuur, utgaar davtah
for key, value in student.items():
    print(f"{key}: {value}")

# zuvhun tulhuureer davtah 
for key in student.keys():
    print(key)

#zuvhun utgaar davtah
for value in student.values():
    print(value)

# toli bichgiig huulah 

original =  {"a": 1, "b": 2, "c": {"x": 10, "y": 20}}

# guyehen huulbar (shallow copy)
copy1 = original.copy()
copy2 = dict(original)

# gun huulbar (deepp copy)
import copy
deep_copy = copy.deepcopy(original)

# guyehn huulbarrt anhaarah zuil 
original["c"] ["x"] = 100
print(copy1["c"] ["x"]) # 100 dotood toli bichig uurchlugdsun 
print(deep_copy["c"] ["x"]) # 10 dotor toli bichug uurchlugduugui 


# toli bichgiig erembeleh 
# tulhuureer erembeleh
student = {
    "ner": "bat",
    "nsd": 20,
    "hot": "ulaanbatar"
}

sorted_keys = sorted(student.keys())
sorted_dict = {k: student[k] for k in sorted_keys}
print(sorted_dict)  ##########


# toli bichgiin oilgolt (dictionary comprehension
# Тоо болон тооны квадратыг агуулсан толь бичиг
squares = {x: x**2 for x in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

#Нөхцөлтэй толь бичгийн ойлголт
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(even_squares)  # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100
# Өгөгдсөн жагсаалтаас толь бичиг үүсгэх
names = ["Бат", "Болд", "Сараа", "Туяа"]
name_lengths = {name: len(name) for name in names}
print(name_lengths)  # {'Бат': 3, 'Болд': 4, 'Сараа': 5, 'Туяа': 4}
# Сурагчдын мэдээлэл агуулсан давхар толь бичиг
students = {
    "s001": {
        "нэр": "Бат",
        "нас": 20,
        "хичээлүүд": ["Математик", "Физик", "Програмчлал"],
    },
    "s002": {
        "нэр": "Болд",
        "нас": 21,
        "хичээлүүд": ["Англи хэл", "Програмчлал", "Дизайн"],
    },
}
 
# Давхар толь бичгийн элементэд хандах
print(students["s001"]["нэр"])  # "Бат"
print(students["s002"]["хичээлүүд"][0])  # "Англи хэл"
# Давхар толь бичгийг давтах
for student_id, info in students.items():
    print(f"Сурагчийн ID: {student_id}")
    print(f"Нэр: {info['нэр']}")
    print(f"Нас: {info['нас']}")
    print(f"Хичээлүүд: {', '.join(info['хичээлүүд'])}")
    print()



# exercise 01
# ugsiin davtamjiig tooloh

text = "bi chamd hairtai bi chamd hairtai gedgee helmeer baina"
words = text.split()
print(words)
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)
# {'bi': 2, 'chamd': 2, 'hairtai': 2, 'gedgee': 1, 'helmeer': 1, 'baina':1}


# exercise 02 
# suragchdiig nasaaar bulegleh 
students = [
    {"ner": "bat", "nas": 20},
    {"ner": "bold", "nas": 21},
    {"ner": "saraa", "nas": 20},
    {"ner": "tuya", "nas": 21},
]

students_by_age = {}
for student in students:
    age = student["nas"]
    if age in students_by_age:
        students_by_age[age].append(student["ner"])
    else:
        students_by_age[age] = [student["ner"]]

print(students_by_age)
# {20: ['bat, saraa], 21: ['bold', 'tuya']}


# exercise 03 
def word_frequency(text):
    # textiig tsewerleh 
    text = text.lower()
    # temdegtuudiig arilgah 
    for char in '.,?!;:(){}[]'""'':
        text = text.replace(char, "")
    
    # ugsiig zadlah 
    words = text.split()

    # ugsiin davtamjiig tootsooloh 
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1 
        else:
            frequency[word] = 1
    return frequency

text = "Bi Python hel surch baina. Python bol mash sonirholtoi herl. Bi Python-g sain surah heregtei."
freq = word_frequency(text)
print(freq)
# {'би': 2, 'python': 3, 'хэл': 2, 'сурч': 1, 'байна': 1, 'бол': 1,
#  'маш': 1, 'сонирхолтой': 1, 'pythonг': 1, 'сайн': 1, 'сурах': 1, 'хэрэгтэй': 1}

