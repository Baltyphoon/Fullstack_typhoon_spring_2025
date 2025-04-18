# Дасгал 1: Үндсэн While давталт
i = 1
while i < 11:
    print(i)
    i += 1

# Дасгал 2: Range ашиглан үндсэн For давталт
for i in range(2, 21, 2):
    print(i)

# Дасгал 3: Нэрсийн жагсаалт дахь нэр бүрийг хэвлэх
ners = ["Болд", "Сараа", "Дорж", "Нара"]
for ner in ners:
    print(ner)

# Дасгал 4: Break мэдэгдэл ашиглах
for i in range(1, 21):
    if i % 7 == 0:
        print(f"7-д хуваагддаг эхний тоо: {i}")
        break
        # break нь давталтыг шууд зогсоох команд. Тухайн нөхцөл биелмэгц давталтаас гарна.

    # 1-ээс 20 хүртэлх тооны хүрээнд 7-д хуваагддаг эхний  2 тоог олох
count = 0  # 7-д хуваагддаг тооны тоолуур
for i in range(1, 21):
    if i % 7 == 0:
        print(f"7-д хуваагддаг тоо: {i}")
        count += 1
        if count == 2:
            break  # 2 тоо олдсон тул давталтыг зогсооно

    # 1-ээс 20 хүртэлх тооны хүрээнд 7-д хуваагддаг бүх тоог олох
for i in range(1, 22):
    if i % 7 != 0:
        continue  # 7-д хуваагдахгүй бол алгасаад дараагийн тоог үргэлжлүүлнэ
    print(f"{i} нь 7-д хуваагдана")


# Дасгал 5: Continue мэдэгдэл ашиглах (1-ээс 20 хүртэлх бүх тоог хэвлэх, гэхдээ 3-т хуваагддаг тоонуудыг алгасах)
for i in range(1, 21):
    if i % 3 == 0:
        continue  # 3-т хуваагддаг тоонуудыг алгасана
    print(i)      # if i % 3 == 0: → 3-д хуваагддаг бол continue → тухайн тоог хэвлэхгүйгээр алгасна.

# Дасгал 6: Давхар давталтууд (1-ээс 5 хүртэлх тоонуудын үржүүлэх хүснэгтийг хэвлэх)
for i in range(1, 6):          # Гаднах давталт: 1-5 хүртэл
    for j in range(1, 11):     # Дотроо: 1-10 хүртэл үржүүлнэ
        print(f"{i} x {j} = {i*j}")
    print("----------------") #бүлэг тус бүрийг ялгана

# Дасгал 7: Else хэсэгтэй давталт (Тоо анхны тоо мөн эсэхийг шалгах)
# Анхны тоо: 1-ээс өөр, зөвхөн 1 ба өөрөө өөртөө хуваагддаг натурал тоо
num = int(input("Тоо оруулна уу: "))
if num < 2:
    print("Анхны тоо биш")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Анхны тоо биш")
            break
    else:
        # Давталт ямар ч 'break' хийгээгүй бол энэ хэсэг ажиллана
        print("Анхны тоо мөн")

# Дасгал 8: Жагсаалтын ойлголт (List Comprehension) (1-ээс n хүртэлх тоонуудын ĸвадратын жагсаалтыг үүсгэх)
n = int(input("n-ийн утгыг оруулна уу: "))
squares = [i**2 for i in range(1, n+1)]
print("Квадратуудын жагсаалт:", squares)

# Дасгал 9: Enumerate (Даалгавар: Жагсаалтын элемент бүрийг түүний индеĸстэй хамт хэвлэх)
# enumerate() нь жагсаалтын тус бүрийн элементийг индексийнх нь хамт авч өгдөг тусгай функц юм.
jims = ["alim", "banana", "guzeelzgene"]
for index, jim in enumerate(jims):
    print(f"{index}: {jim}")
    # 0: alim
    # 1: banana
    # 2: guzeelzgene
      # Хэрвээ 1-ээс эхлүүлмээр байвал:
for index, jim in enumerate(jims, start=1):
    print(f"{index}: {jim}")
    # 1: alim
    # 2: banana
    # 3: guzeelzgene

# Дасгал 10: Толь бичгээр давтах (Толь бичгийн түлхүүр-утга хос бүрийг хэвлэх)
 # Толь бичиг нь түлхүүр (key) – утга (value)
person = {
    "нэр": "Болд",
    "нас": 30,
    "хот": "Улаанбаатар"
}

for key, value in person.items():
    print(f"{key}: {value}")
    # Толь бичигт шинэ өгөгдөл нэмэх
person = {
    "нэр": "Болд",
    "нас": 30,
    "хот": "Улаанбаатар"
}
# Шинэ мэдээлэл нэмэх
person["мэргэжил"] = "Инженер"
for key, value in person.items():
    print(f"{key}: {value}")
    # Зөвхөн зарим түлхүүрүүдийг шүүх
person = {
    "нэр": "Болд",
    "нас": 30,
    "хот": "Улаанбаатар",
    "мэргэжил": "Инженер",
    "цалин": 2000000 #Зөвхөн зарим түлхүүрүүдийг шүүх — if ашиглан

}
selected_keys = ["нэр", "цалин"]

for key in person:
    if key in selected_keys:
        print(f"{key}: {person[key]}")


