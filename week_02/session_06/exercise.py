#dasgal 1 ugugdsun too eyreg surug esehiig shalgah

number = int(input("Number: "))
if number < 0 :
    print("Number is negative.")
elif number == 0:
    print("Tegtei tentsuuyum bnaa")
else: 
    print("Number is Positive")

#dasgal 2 ugugdsun jil undur jil esehiig shalgah
  # year = int(input("Number of year ?"))
  #if (year % 4 == 0 and year % 400 == 0):
    # print(str(year) + "ni undur jil ")
    # 4-т хуваагддаг Гэхдээ 100-д хуваагддаггүй, эсвэл 400-д хуваагддаг 
# Хэрэглэгчээс жил авах
year = int(input("Жил оруулна уу: "))
# Өндөр жил эсэхийг шалгах
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} он бол өндөр жил байна.")
else:
    print(f"{year} он бол жирийн жил байна.")


# DASGAL 3 Гурвалжны гурван талын урт өгөгдсөн үед тэр гурвалжин зурагдах эсэхийг шалгах програм
def can_form_triangle(a, b, c): # def гэдэг нь "define" буюу "тодорхойлох" 
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False
# Хэрэглэгчээс 3 талын уртыг авна
a = float(input("a талын урт: "))
b = float(input("b талын урт: "))
c = float(input("c талын урт: "))

if can_form_triangle(a, b, c):
    print("Эдгээр уртаар гурвалжин зурж болно.")
else:
    print("Эдгээр уртаар гурвалжин зурж болохгүй.")


# DASGAL 4 Хэрэглэгчийн оруулсан тоо 1-100 хооронд байвал "Зөв", үгүй бол "Буруу" гэж хэвлэх програм
# Хэрэглэгчээс тоо авах
num = int(input("1-100 хооронд тоо оруулна уу: "))
# Шалгах
if 1 <= num <= 100:
    print("Зөв")
else:
    print("Буруу")


# DASGAL 5 Хэрэглэгчийн оруулсан үсэг эгшиг эсвэл гийгүүлэгч эсэхийг шалгах програм 
# Монгол хэлний эгшиг үсгүүд
egshig = "аэиоуүөАОЭИОУҮӨ"

# Хэрэглэгчээс нэг үсэг авах
letter = input("Нэг үсэг оруулна уу: ")
# Үсгийн урт 1 эсэхийг шалгах
if len(letter) != 1:
    print("Зөвхөн нэг үсэг оруулна уу.")
else:
    if letter in egshig:
        print("Эгшиг үсэг байна.")
    else:
        print("Гийгүүлэгч үсэг байна.")

