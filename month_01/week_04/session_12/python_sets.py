# python sets 
# tuple ashiglaad create_point gedeg function uusgene uu 
# enehuu function ni x , y gedeg parametruud avdag buguud 
# ene 2 parametraar tuple butsaana 

def create_point(x, y):
    return(x, y)
#calculate_distance gedeg function todorhoilood point1, point2 gedeg 
# tuple parametreer avaad kartecian product oldog bolgooroi
def calculate_distance (point1, point2):
    import math
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] + point1[1]))
   

# heregleenii jishee 
point_a = create_point(0, 0)
point_b = create_point(3, 4)
distance = calculate_distance(point_a, point_b)
print(f"hoyor tseg hoorondiin zai: {distance}") # 5.0


# Python sets
# husnegt haaltaar olonlog uusgeh 
set1 = {1, 2, 3, 4, 5}
# Давтагдсан элементүүд автоматаар арилна
set2 = {1, 2, 2, 3, 4, 4, 5}
print(set2) # {1, 2, 3, 4, 5}
# set() функцээр олонлог үүсгэх
set3 = set([1, 2, 3, 4, 5])
# Хоосон олонлог
empty_set = set() # Хоосон хүснэгт хаалт {} нь dictionary үүсгэдэг
# Тэмдэгт мөрнөөс олонлог үүсгэх
letters = set("hello")
print(letters) # {'h', 'e', 'l', 'o'}

#Olonlogiin undsen uildluud 
# Олонлог үүсгэх
fruits = {"алим", "банана", "жүрж"}
# Элемент нэмэх
fruits.add("усан үзэм")
print(fruits) # {'алим', 'банана', 'жүрж', 'усан үзэм'}
# Олон элемент нэмэх
fruits.update(["манго", "киви"])
print(fruits) # {'алим', 'банана', 'жүрж', 'усан үзэм', 'манго', 'киви'}
# Элемент хасах
fruits.remove("банана") # Элемент байхгүй бол алдаа заана
print(fruits) # {'алим', 'жүрж', 'усан үзэм', 'манго', 'киви'}
fruits.discard("лийр") # Элемент байхгүй бол алдаа заахгүй
# Сүүлийн элементийг хасах
popped = fruits.pop() # Аль элемент хасагдах нь тодорхойгүй
print(popped)
print(fruits)
# Бүх элементийг устгах
fruits.clear()
print(fruits) # set()


# olonlogiiin logical uildluud
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
# Нэгдэл (Union) - хоёр олонлогийн бүх элементүүд
print(A | B) # {1, 2, 3, 4, 5, 6, 7, 8}
print(A.union(B)) # {1, 2, 3, 4, 5, 6, 7, 8}
# Огтлолцол (Intersection) - хоёр олонлогт байгаа нийтлэг элементүүд
print(A & B) # {4, 5}
print(A.intersection(B)) # {4, 5}
# Ялгавар (Difference) - нэг олонлогт байгаа, нөгөөд байхгүй элементүүд
print(A - B) # {1, 2, 3}
print(A.difference(B)) # {1, 2, 3}
# Симметрик ялгавар (Symmetric Difference) - аль нэг олонлогт байгаа, 
# хоёуланд байхгүй элементүүд
print(A ^ B) # {1, 2, 3, 6, 7, 8}
print(A.symmetric_difference(B)) # {1, 2, 3, 6, 7, 8}


# olonlogiin shalgah uidluud 
A = {1, 2, 3, 4, 5}
B = {1, 2, 3}
C = {6, 7, 8}

# ded olonlog mun esehiig shalgah 
print(B.issubset(A)) # True - B ni A iin ded olonlog
print(A.issubset(B)) # True - A ni B-g aguuslan 

# Ogtloltsoogui esehiig shalgah 
print(A.isdisjoint(C)) # True - A, C hoyor niitleg element baihgui

# tentsuu esehiig shalgah 
D = {1, 2, 3, 4, 5}
print(A == D)  # True A D 2ni ijil elementuudtei 


# olonlogiin hereglee 
# Davahardliig arilgah: jagsaaltiin davhardsan elementuudiig arilgahad
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print(unique_numbers) # [1, 2, 3, 4, 5]

# gishuunchleliig shalgah: Element olonlogt baigaa esehiig hurdan shalgahad
fruits = {"alim", "banana", "jurj"}
print("alim" in fruits) # True - 0(1) hugatsaand shalgana

#Matematik uildluud: Negdel, ogtloltsol, ylagavar zereg uildluuded
# hoyor texted baigaa niitleg usguudiig oloh 
text1 = "hello"
text2 = "world"
common_letters = set(text1) & set(text2)
print(common_letters) # {'l', 'o'}

# ugugdliig shuuh: Davtagdashgui utguudiig olohod
# Hoyor jagsaaltiin niitleg elementuudiig oloh 
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = list(set(list1) & set(list2))
print(common_elements) # [4, 5]


# Frozen set uusgeh
frozen = frozenset([1, 2, 3, 4, 5])
# Логик үйлдлүүд хийх боломжтой
A = frozenset([1, 2, 3, 4, 5])
B = frozenset([4, 5, 6, 7, 8])
print(A | B) # frozenset({1, 2, 3, 4, 5, 6, 7, 8})
# Элемент нэмэх боломжгүй
# frozen.add(6) # AttributeError: 'frozenset' object has no attribute
'add'
# Dictionary түлхүүр болгон ашиглах боломжтой
data = {frozen: "Frozen set түлхүүр"}
print(data[frozen]) # "Frozen set түлхүүр"

# exercise 01 - enehuu function ni ugugdsun textiin ugnuudiig toolood 
# tegeed heden shirheg ugnuudiig davtagdahgui hereglegdej baigaag 
# olood butsaana

def count_unique_words(text):
    words = text.lower().split()
    unique_words = set(words)
    print(words)
    print(unique_words)
    return len(unique_words)
    

text = "Bi Python hel surch baina. Python bol mash sonirholtoi hel."
print(f"Davtagdashgui ugsiin too: {count_unique_words(text)}")
