# dasgal 1
single_quotes = 'Сайн уу, Дэлхий!'
double_quotes = "Python Програмчлал"
triple_quotes = '''Энэ бол олон мөрт
текст бөгөөд гурван ганц хашилт ашигласан.'''
triple_double = """Өөр нэг олон мөрт
текст бөгөөд гурван давхар хашилт ашигласан."""
print(single_quotes)
print(double_quotes)
print(triple_quotes)
print(triple_double)

first_name = "Болд"
last_name = "Бат"
print(f"Бүтэн нэр:"  + ' ' +   first_name + ' ' + last_name ) 

pattern = "-*-" * 5 
print(pattern)

message = "Sain uu, Python!"
print(message)

# dasgal 2 
text = "Python Програмчлал"

first_char = text[0]
sixth_char = text[5]
last_char = text[-1]
print("Эхний тэмдэгт:", first_char)
print("Зургаа дахь тэмдэгт:", sixth_char)
print("Сүүлийн тэмдэгт:", last_char)
ug = text.split()
print(f"first letter: {ug[0]}")
print(f"second letter: {ug[1]}")

# Алхамтай хэсэгчлэл 
hoyr_dahi_usegnuud = text[::2]
print("2 dahi usegnuud: " , hoyr_dahi_usegnuud)

# Текст мөрийг эсрэгээр нь эргүүлэх
ergesen_ug = text[::-1]
print("Esreg ergesen ug:", ergesen_ug)

# 'Програмчлал'-аас 'грам'-ыг гаргаж авах
text1 = "Програмчлал" 
gargasan_heseg = text1[3:7]
print("Gargasan heseg: ", gargasan_heseg)

text2 = "Python Програмчлал"
# Текстийг үгсэд хуваах
ugugdsun_ug = text2.split()
# Хоёр дахь үгийг авах
hoyr_doh_ug = ugugdsun_ug[1]
# Гурав дахь тэмдэгт бүрийг авах
third_chars = hoyr_doh_ug[::3]
print("2 dahi ugnii 3 dahi usegnuud:", third_chars)



# DASGAL 3

sample_text = " Python бол Гайхалтай Програмчлалын Хэл! "
# Жижиг үсгээр
lower_text = sample_text.lower()
print("Жижиг үсгээр:", lower_text)
# Том үсгээр
upper_text = sample_text.upper()
print("Том үсгээр:", upper_text)
# Гарчиг хэлбэрээр
title_text = sample_text.title()
print("Гарчиг хэлбэрээр:", title_text)
# Үсгийн төлөв солигдсон
swapcase_text = sample_text.swapcase()
print("Үсгийн төлөв солигдсон:", swapcase_text)


# Хоосон зай арилгах
# Бүх талын хоосон зай арилгах
stripped = sample_text.strip()
print("Хоосон зай арилгасан:", stripped)
# Зөвхөн зүүн талаас
left_stripped = sample_text.lstrip()
print("Зүүн талын хоосон зай арилгасан:", left_stripped)
# Зөвхөн баруун талаас
right_stripped = sample_text.rstrip()
print("Баруун талын хоосон зай арилгасан:", right_stripped)

# Хайлт
text = "Python бол Гайхалтай Програмчлалын Хэл!"

# 'python' агуулсан эсэх (жижиг үсгээр хайж байна)
contains_python = 'python' in text.lower()
print("'python' агуулсан эсэх:", contains_python)
# 'python' үгийн индекс (жижиг болгоод хайна)
index_of_python = text.lower().find('python')
print("'python'-ны индекс:", index_of_python)
# 'а'-ийн тоо
count_a = text.count('а')
print("'а'-ийн тоо:", count_a)

# Орлуулалт
text = "Python бол Гайхалтай Програмчлалын Хэл!"
# 'Python'-г 'JavaScript'-ээр орлуулах
replaced_text = text.replace("Python", "JavaScript")
print("Орлуулалтын дараа:", replaced_text)

# Хуваах ба нэгтгэх
text = "Python бол Гайхалтай Програмчлалын Хэл!"
# Текстийг зайгаар хуваах
words = text.split()
print("Үгсийн жагсаалт:", words)
# Үгсийг нэг мөр болгон нэгтгэх
joined_text = ' '.join(words)
print("Дахин нэгтгэсэн текст:", joined_text)


# Текст мөрийн шинж чанарыг шалгах
textt = "Python бол Гайхалтай Програмчлалын Хэл!"
print("Үсгэн тэмдэгт эсэх:", textt.isalpha()) # false
print("Үсэг тоон тэмдэгт эсэх:", textt.isalnum()) # false
print("12345 тоон тэмдэгт эсэх:", textt.isdigit()) # false

text1 = "Програмчлал"
print("Үсгэн тэмдэгт эсэх:", text1.isalpha()) # true
text2 = "Code123" 
print("Үсэг тоон тэмдэгт эсэх:", text2.isalnum()) # true
text3 = "12345"
print("12345 тоон тэмдэгт эсэх:", text3.isdigit()) # true


# # DASGAL 4

# Өөр өөр текст мөр форматлах аргуудыг дадлага хийх
# Жишээ бодолт:
name = "Болор"
age = 28
height = 1.65
programming_languages = ["Python", "JavaScript", "Java"]
# % оператор ашиглах
formatted_text = "Миний нэр %s. Би %d настай бөгөөд %.2f метр өндөр." % (name, age, height)
print(formatted_text)

# str.format() арга ашиглах
# .format() ашиглах
formatted_text = "Миний нэр {}. Би {} настай бөгөөд {:.2f} метр өндөр.".format(name, age, height)
print(formatted_text)

# format() дээр нэрлэсэн байрлуулагч ашиглах
# Нэрлэсэн байрлуулагч ашиглах
formatted_text = "Миний нэр {name}. Би {age} настай бөгөөд {height:.2f} метр өндөр.".format(name=name, age=age, height=height)
print(formatted_text)

# f-strings ашиглах
formatted_text = f"Миний нэр {name}. Би {age} настай бөгөөд {height:.2f} метр өндөр."
print(formatted_text)

# f-strings дотор илэрхийлэл ашиглах
formatted_text = f"5 жилийн дараа би {age + 5} настай болно."
print(formatted_text) # 5 жилийн дараа би 33 настай болно.

# Жагсаалтыг форматлах
programming_languages = ["Python", "JavaScript", "Java"]
# f-string ашиглан жагсаалтыг форматлах
formatted_text = f"Би {len(programming_languages)} програмчлалын хэл мэднэ: {', '.join(programming_languages)}."
print(formatted_text)
# len(programming_languages) — жагсаалтын уртыг (хичнээн програмчлалын хэл мэдэж байгааг) олж авна.
# ', '.join(programming_languages) — жагсаалтыг коммаар тусгаарлан нэг мөрөнд хөрвүүлнэ.


# Зай авах ба эгнүүлэх
programming_languages = ["Python", "JavaScript", "Java"]
# Жагсаалтыг зайгаар форматлах
for language in programming_languages:
    formatted_text = f"{language} - {len(language)} тэмдэгт"
    print(formatted_text)
# len(language) — энэ нь тухайн хэлний тэмдэгтүүдийн тоог олж авдаг.
#f-string — хэрэглэж буй {language} болон {len(language)}-ийг шууд форматлахад ашиглаж байна.

# Тоо форматлах
pi = 3.141592653589793
# f-string ашиглан тоо форматлах
formatted_text_2_decimal = f"Пи 2 орны нарийвчлалтай: {pi:.2f}"
print(formatted_text_2_decimal) # Пи 2 орны нарийвчлалтай: 3.14
formatted_text_4_decimal = f"Пи 4 орны нарийвчлалтай: {pi:.4f}"
print(formatted_text_4_decimal) # Пи 4 орны нарийвчлалтай: 3.1416
# {pi:.2f} — Пи тоог 2 арван есний оронтой (нэгжийн дараах хоёр оронтой) харуулж байна.
# {pi:.4f} — Пи тоог 4 арван есний оронтой харуулж байна.
# .f — энэ нь floating point тоо форматлахыг зааж өгдөг.

# Хувь форматлах 
score = 0.87123
print(f"Тестийн оноо: {score:.0%}") # Тестийн оноо: 87%
print(f"Тестийн оноо: {score:.1%}") # Тестийн оноо: 87.1% (1 оронтой бутархайтай хувь (87.0%))
print(f"Тестийн оноо: {score:.2%}") # Тестийн оноо: 87.12% (2 оронтой бутархайтай хувь (87.0%))
print(f"Тестийн оноо: {score:.3%}") # Тестийн оноо: 87.123% (3  оронтой бутархайтай хувь (87.0%))





