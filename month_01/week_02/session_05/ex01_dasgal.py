# dasgal 1
name = input("Таны нэр хэн бэ?")  
age = input("Та хэдэн настай вэ?")  
hariu = int(age) + 1 
print(f"Сайн уу, {name} Та ирэх жил {hariu} настай болно. ")

# dasgal 2
# 3 сурагчийн нэр, оноог асуугаад форматтай хүснэгт хэвлэх програм
# 1. Гурван сурагчийн нэр, оноог цуглуулна
# 2. Өгөгдлийг хүрээтэй хүснэгт хэлбэрээр харуулна
# 3. Дундаж оноог тооцоолж харуулна

ner1 = input("Ehnii suragchiin ner: ")
onoo1 = float(input(f"{ner1}-n onoo: "))

ner2 = input("2 dahi suragchiin ner: ")
onoo2 = float(input(f"{ner2}-n onoo: "))

ner3 = input("Ehnii suragchiin ner: ")
onoo3 = float(input(f"{ner3}-n onoo: "))

dundaj_onoo = (onoo1 + onoo2 + onoo3) / 3

print("/n+" + "-"*20 + "+" + "-"*10 + "+")
print(f"| {"Name":<18} | {"Score":<8} |")
print("+" + "-"*20 + "+" + "-"*10 + "+")
print(f"| {ner1:<18} | {onoo1:<8.2f} |")
print(f"| {ner2:<18} | {onoo2:<8.2f} |")
print(f"| {ner3:<18} | {onoo3:<8.2f} |")
print("+" + "-"*20 + "+" + "-"*10 + "+")
print(f"| {'Дундаж оноо':<18} | {dundaj_onoo:<8.2f} |")
print("+" + "-"*20 + "+" + "-"*10 + "+")



#dasgal 3
# Хэрэглэгчээс хоёр тоо болон үйлдлийг авч энгийн тооны машин үүсгэх
# 1. Хэрэглэгчээс хоёр тоо болон үйлдэл (+, -, *, /) асууна
# 2. Тооцоолол хийгээд үр дүнг харуулна

too1 = float(input("Ehnii too: "))
uildel = input("Uildel songooroi (+, -, *, /): ")
too2 = float(input("Daraagiin too: "))

if uildel == "+":
    hariu = too1 + too2
elif uildel == "-":
    hariu = too1 - too2
elif uildel == "*":
    hariu = too1 * too2
elif hariu == "/":
    if too2 != 0:
        hariu = too1 / too2
    else:
        hariu = "toog 0d huvaaj bolohguiee!"
else: 
    hariu = "Iim uildel bhguiee!"

print(f"Hariu ni: {hariu}")


# DASGAL 4
#Зорилго: Хэрэглэгчийн насыг асууж шалгуур хангаж байгаа эсэхийг шалгах
# 1. Хэрэглэгчээс насыг нь асууна
# 2. Оролт нь тоо мөн эсэхийг шалгана
# 3. 0-120 хооронд байгаа эсэхийг шалгана

Nas = input("Nasaa bichne uu: ")
if Nas.isdigit():
    jinken_nas = int(Nas)
    if 0 <= 120:
        print(f"Ta nasaa {jinken_nas} gej unen heljee")
    else:
        print("Buruu shuuu! hun deed tal ni 120 naslana nasaa unen bicheerei")
else:
    print("Nas asuuj bgaa bolhoor zuvhun too bicheerei nz")


# DASGAL 5
# Хэрэглэгч олон мөр теĸст оруулах боломжтой програм үүсгэх
# 1. Хэрэглэгч шинэ мөрөнд "ДУУСАВ" гэж бичих хүртэл олон мөр теĸст оруулах боломжийг шинэ мөрөнд "ДУУСАВ" гэж бичих хүртэл олон мөр теĸст оруулах боломжийг шинэ мөрөнд "ДУУСАВ" гэж бичих хүртэл олон мөр теĸст оруулах боломжийг олгоно.
# 2. Оролт дууссаны дараа мөрийн дугаартай бүх теĸстийг харуулна
# ! Тэмдэглэлээ оруулахыг хэрэглэгчээс хүсэх
# ! Тэмдэглэлийн мөрүүдийг нэг нэгээр авах
# ! "ДУУСАВ" гэсэн оролт ирэх хүртэл үргэлжлүүлэх
# ! Цуглуулсан тэмдэглэлийг мөрийн дугаартай хамт харуулах

print("Bichmeer baigaa zuilee bicheerei. Duusgamaar baival 'DUUSLAA' gej bicheerei!")
lines = []
while True:
    line = input()
    if line.strip().upper() == "DUUSLAA":
        break
    lines.append(line)
print("\n--- Таны оруулсан тэмдэглэл ---")
for idx, text in enumerate(lines, start=1):
    print(f"{idx}: {text}")


    