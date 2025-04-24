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

# Tulhuu-utga hosloloos toli bichig uusgeh
items = [("alim", 3), ("banana", 5), ("jurj", 2)]
fruit_count = dict(items)

# 
# 
#
# 




# get() argiig ashiglah (tulhuur baihgui bol aldaa zaahgui)
age = student.get("nas") 
email = student.get("email")  
email = student.get("email", "medeelel baihui")

#toli bichgiin elementiig uurchluh
student = {"ner"}

# buh elementiig ustgah 
student.clear() # {}
#
# 
# 
# 
# 
#
#
#
#


student = {
    "ner": "bat",
    "nsd": 20,
    "hot": "ulaanbatar"
}

# buh tulhuuriig avah
keys = student.keys() # dict_keys('ner', )



# 
# 
#
#
#
#
#
#


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
#
#
#
# 
# ugugdsun jagsaaltaas toli bichig uusgeh 


# suragchdiin medeelel aguulsan davhar toli bichig 
# 
# 
# 
# 
# 
# davhar toli bichgiig davhtah 


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
    #
        frequency[word] += 1 
    
        
        
    return frequency

text = "Bi Python hel surch baina. Python bol mash sonirholtoi herl. Bi Python-g sain surah heregtei."
freq = word_frequency(text)
print(freq)