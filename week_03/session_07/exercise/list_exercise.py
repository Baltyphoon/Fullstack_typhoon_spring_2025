# Дасгал 1: Жагсаалт үүсгэх ба хандах ()
hool = ["цуйван", "хуушуур", "будаатай хуурга", "пицца",
"тахианы шөл"]
print("Эхний хоол: " + hool[0]) # tsuiwan 
print("Сүүлийн хоол: " + hool[-1]) # тахианы шөл
print("3 дахь хоол: " + hool[2]) # будаатай хуурга

# Дасгал 2: Жагсаалтын элементүүдийг өөрчлөх
jagsaalt = [10, 20, 30, 40, 50]
print("Анхны жагсаалт:" + str(jagsaalt))
# 3dahi elementiig uurchluv 
jagsaalt[2] = 99 
print("3 дахь элементийг өөрчилсний дараа:" + str(jagsaalt))
#tugsguld ni element nemev 
jagsaalt.append(69)
print("Төгсгөлд элемент нэмсний дараа:" + str(jagsaalt))
#Эхэнд элемент оруулсны дараа:
jagsaalt.insert(0, -1)
print("Эхэнд элемент оруулсны дараа:" + str(jagsaalt))
#Элемент устгасны дараа:
jagsaalt.remove(50)
print("Элемент устгасны дараа:" + str(jagsaalt))


# Дасгал 3: Жагсаалтын аргуудыг ашиглах 
Duriin_jagsaalt = [101, 23, 12, 44, 5]
print(Duriin_jagsaalt)
# Жагсаалтыг өсөх эрэмбээр эрэмбэл 
Duriin_jagsaalt.sort()
print("Жагсаалтыг өсөх эрэмбээр эрэмбэлхэд" + str(Duriin_jagsaalt))
#Жагсаалтыг буурах эрэмбээр эрэмбэл
Duriin_jagsaalt.reverse()
print("Жагсаалтыг буурах эрэмбээр эрэмбэлхэд" + str(Duriin_jagsaalt))
#Жагсаалтын хуулбарыг үүсгэ 
Duriin_jagsaalt_copy = Duriin_jagsaalt.copy()
print("Жагсаалтын хуулбарыг үүсгэхэд" + str(Duriin_jagsaalt_copy))
#Жагсаалтын урт (элементийн тоо)-ыг хэвлэ
print(len(Duriin_jagsaalt))
print(len(Duriin_jagsaalt_copy))


# Жагсаалтын хэсэг (slicing)
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Бүтэн жагсаалт:" + str(numbers))
print("Эхний 3 элемент:" + str(numbers[0:3]))
print("Сүүлийн 3 элемент:" + str(numbers[7:]))
print("2-оос 7 хүртэлх элементүүдийг авч хэвлэхэд:" + str(numbers[2:7]))
print("1-ээс эхлэн 2 алхамаар:" + str(numbers[1:10:2]))


# Дасгал 5: Жагсаалтын давталт
ug = ['алим', 'банана', 'гүзээлзгэнэ', 'усан үзэм', 'киви']
print("Жагсаалт:" + str(ug))
#For давталт ашиглан жагсаалтын элемент бүрийг хэвлэ
for ugs in ug:
    print(ugs)
#For давталт ашиглан элемент бүрийн индеĸс болон утгыг хэвлэ (enumerate ашиглан)
for index, ugnuud in enumerate(ug):
    print(f"index {index}: {ugnuud}")


# Дасгал 6: Жагсаалтын ойлголт (List Comprehension)
numbers_01 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers_01)
print("Тэгш тоонууд:" + str(numbers_01[1:11:2]))

squares = []
for numbers in range(1,11):
    squares.append(numbers ** 2)
print("Тоонуудын квадрат:" + str(squares))

even_squares = [numbers_01 ** 2 for numbers_01 in range (1, 11) if numbers_01 > 5]
print("5-аас их тоонуудын квадрат:" + str(even_squares))









