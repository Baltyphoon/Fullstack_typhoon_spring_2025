# intro into python lsit

# Problem - Variables so many variables to define 
b = 7 
print(b)

# Solution - Lists 
fruits = ["алим", "банана", "гүзээлзгэнэ"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "хоёр", 3.0, True]
empty_list = []

print(type(fruits))
print(fruits)
 
# list index 
# Positive index (ehnees ni toolno) 
print(fruits[0]) # алим
print(fruits[1]) # банана
print(fruits[2]) # гүзээлзгэнэ 

# Negative index (tugsguluus ni toolno)
print(fruits[-1]) # гүзээлзгэнэ
print(fruits[-2]) # банана 
print(fruits[-3]) # алим

# change list 

# Элемент өөрчлөх
fruits[0] = "үзэм"
print(fruits) # ['үзэм', 'банана', 'гүзээлзгэнэ']

# Элемент нэмэх
fruits.append("киви")
print(fruits) # ['үзэм', 'банана', 'гүзээлзгэнэ', 'киви']

# Тодорхой байрлалд элемент оруулах
fruits.insert(1, "манго")
print(fruits) # ['үзэм', 'манго', 'банана', 'гүзээлзгэнэ', 'киви']

# Элемент устгах
fruits.remove("банана")
print(fruits) # ['үзэм', 'манго', 'гүзээлзгэнэ', 'киви']

# Индексээр элемент устгах
removed_fruit = fruits.pop(1) # манго-г устгаж, хувьсагчид хадгална
print(removed_fruit) # манго
print(fruits) # ['үзэм', 'гүзээлзгэнэ', 'киви']

# Buh elementiig ustgah 
fruits.clear
print(fruits) #[] 

# list methods 

fruits = ["алим", "банана", "гүзээлзгэнэ"]
# Жагсаалтын урт
print(len(fruits)) # 3
# Жагсаалтыг эрэмбэлэх
fruits.sort()
print(fruits) # ['алим', 'банана', 'гүзээлзгэнэ']
# Жагсаалтыг урвуу эрэмбэлэх
fruits.reverse()
print(fruits) # ['гүзээлзгэнэ', 'банана', 'алим']